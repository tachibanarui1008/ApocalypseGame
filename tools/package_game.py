#!/usr/bin/env python3
"""Build unified macOS app from this project and an explicitly retained runtime."""
from pathlib import Path
import argparse,shutil,plistlib,subprocess,tempfile,datetime,zipfile
ROOT=Path(__file__).resolve().parents[1]
p=argparse.ArgumentParser();p.add_argument("--runtime",type=Path,default=ROOT/"runtime/macos.app");p.add_argument("--output",type=Path,default=ROOT/"releases/未雨绸缪.app");a=p.parse_args()
runtime=a.runtime.resolve();output=a.output.resolve()
assert runtime.is_dir() and (runtime/"Contents/MacOS/python").is_file(),"Specify an existing Ren'Py macOS app with --runtime"
assert output!=runtime and runtime not in output.parents,"Output must not overwrite the runtime"
output.parent.mkdir(parents=True,exist_ok=True)
with tempfile.TemporaryDirectory(prefix="wyc-build-",dir="/private/tmp") as tmp:
 stage=Path(tmp)/"未雨绸缪.app"
 shutil.copytree(runtime,stage,ignore=lambda base,names:["game"] if base.endswith("/autorun") else [n for n in names if n in ("traceback.txt","log.txt","errors.txt")])
 autorun=stage/"Contents/Resources/autorun"
 shutil.copytree(ROOT/"game",autorun/"game",ignore=shutil.ignore_patterns("*.rpyc","*.pyc","__pycache__","cache","saves"))
 info=stage/"Contents/Info.plist";v=plistlib.loads(info.read_bytes());v.update(CFBundleDisplayName="未雨绸缪",CFBundleName="未雨绸缪",CFBundleIdentifier="org.tachibanarui.weiyuchoumou.unified",CFBundleShortVersionString="0.3.0",CFBundleVersion="0.3.0");info.write_bytes(plistlib.dumps(v))
 subprocess.run([str(stage/"Contents/MacOS/python"),str(autorun/"ApocalypseGame.py"),str(autorun),"compile"],check=True)
 subprocess.run(["xattr","-cr",str(stage)],check=True)
 subprocess.run(["codesign","--force","--deep","--sign","-",str(stage)],check=True)
 subprocess.run(["codesign","--verify","--deep","--strict",str(stage)],check=True)
 archive=output.with_suffix(".zip")
 if archive.exists(): archive.rename(archive.with_name(archive.name+".bak-"+datetime.datetime.now().strftime("%Y%m%d-%H%M%S")))
 with zipfile.ZipFile(archive,"w",zipfile.ZIP_DEFLATED) as z:
  for item in stage.rglob("*"):
   if item.is_file(): z.write(item,str(Path("未雨绸缪.app")/item.relative_to(stage)))
 if output.exists():
  backup=output.with_name(output.name+".bak-"+datetime.datetime.now().strftime("%Y%m%d-%H%M%S"));output.rename(backup);print("Previous build preserved:",backup)
 shutil.move(str(stage),output)
print(output)

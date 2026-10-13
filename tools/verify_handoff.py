"""Verify the checked-in portable handoff inventory; --write updates explicit baselines."""
from pathlib import Path
import argparse,hashlib,json,sys
ROOT=Path(__file__).resolve().parents[1]
MANIFEST=ROOT/'docs/handoff/RESOURCE_MANIFEST.json'
IGNORE={'cache','saves','__pycache__'}
def files():
 result=[]
 for directory in ('game','docs','tools'):
  for path in (ROOT/directory).rglob('*'):
   if not path.is_file() or any(part in IGNORE for part in path.parts):continue
   if path==MANIFEST or path.suffix in ('.rpyc','.pyc','.rpymc','.log') or path.name in ('log.txt','errors.txt','traceback.txt'):continue
   result.append(path)
 for name in ('README.md','AGENTS.md','.gitignore','.gitattributes','requirements-dev.txt'):
  result.append(ROOT/name)
 return sorted(result,key=lambda p:p.relative_to(ROOT).as_posix())
def record(path):
 return {'path':path.relative_to(ROOT).as_posix(),'bytes':path.stat().st_size,'sha256':hashlib.sha256(path.read_bytes()).hexdigest()}
p=argparse.ArgumentParser();p.add_argument('--write',action='store_true');a=p.parse_args()
if a.write:
 MANIFEST.parent.mkdir(parents=True,exist_ok=True)
 MANIFEST.write_text(json.dumps({'version':'0.3.0','files':[record(f) for f in files()]},ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
 print('Wrote',len(files()),'file checksums');sys.exit(0)
data=json.loads(MANIFEST.read_text(encoding='utf-8'));errors=[]
for item in data['files']:
 path=ROOT/item['path']
 if not path.is_file():errors.append('missing: '+item['path']);continue
 if record(path)!=item:errors.append('changed: '+item['path'])
expected={i['path'] for i in data['files']};actual={f.relative_to(ROOT).as_posix() for f in files()}
for name in sorted(actual-expected):errors.append('unlisted: '+name)
if errors:
 print('\n'.join(errors));sys.exit(1)
print('Verified',len(data['files']),'portable source/resource files')

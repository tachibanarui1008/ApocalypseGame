"""Run Ren'Py's native interaction tests against an extracted Windows package.

Uses an isolated copy and save directory; does not touch the player's saves.
"""
import argparse
import json
import os
import shutil
import subprocess
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
parser = argparse.ArgumentParser()
parser.add_argument('--package', type=Path, default=ROOT/'releases/ApocalypseGame-0.3.0-win.zip')
parser.add_argument('--output', type=Path, default=ROOT/'.runtime/windows-acceptance')
args = parser.parse_args()
output = args.output.resolve()
output.mkdir(parents=True, exist_ok=True)
project = output/'ApocalypseGame-0.3.0-win'
if project.exists():
    parser.error('Use a new output directory for each acceptance run.')
with zipfile.ZipFile(args.package) as package:
    package.extractall(output)
shutil.copyfile(ROOT/'tools/windows_acceptance.rpy', project/'game/windows_acceptance.rpy')
env = os.environ.copy()
env['WYC_TEST_OUTPUT'] = str(output/'evidence')
with (output/'test-output.txt').open('w', encoding='utf-8') as log:
    result = subprocess.run([str(project/'ApocalypseGame.exe'), '--savedir',
                             str(output/'saves'), str(project), 'test',
                             'windows_acceptance', '--report-detailed'],
                            cwd=project, env=env, stdout=log, stderr=subprocess.STDOUT,
                            timeout=600)
report = (output/'test-output.txt').read_text(encoding='utf-8')
print(report)
if result.returncode or '[rpytest] Status: PASSED' not in report:
    raise SystemExit(result.returncode or 1)
for route in 'ABCD':
    windows = json.loads((output/'evidence'/f'{route}-walk.json').read_text(encoding='utf-8'))
    mac = json.loads((ROOT/'docs/handoff/native'/f'{route}-walk.json').read_text(encoding='utf-8'))
    if windows['scenes'] != mac['scenes']:
        raise SystemExit('Route scene sequence differs from Mac: ' + route)
print('All four route scene sequences match the Mac acceptance baseline.')

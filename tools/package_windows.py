"""Build the unchanged unified game using an external Ren'Py 8.5.3 SDK.

The SDK and binaries stay outside Git. Build from a minimal staging project so
developer files, saves, logs and SDK files cannot enter the player archive.
"""
import argparse
import hashlib
import json
import shutil
import subprocess
import tempfile
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--sdk', type=Path, required=True)
    parser.add_argument('--output', type=Path, default=ROOT / 'releases')
    args = parser.parse_args()
    sdk = args.sdk.resolve()
    output = args.output.resolve()
    python = sdk / 'lib/py3-windows-x86_64/python.exe'
    if not python.is_file() or not (sdk / 'launcher').is_dir():
        parser.error('Supply an extracted Windows RenPy SDK directory.')
    output.mkdir(parents=True, exist_ok=True)
    runner = [str(python), str(sdk / 'renpy.py')]
    version = subprocess.check_output(runner + ['--version'], cwd=sdk, text=True)
    if '8.5.3.26051504' not in version:
        parser.error('Use RenPy 8.5.3.26051504 to match the Mac baseline.')
    with tempfile.TemporaryDirectory(prefix='wyc-windows-') as temporary:
        project = Path(temporary) / 'ApocalypseGame'
        shutil.copytree(ROOT / 'game', project / 'game', ignore=shutil.ignore_patterns(
            '*.rpyc', '*.pyc', '*.rpymc', '__pycache__', 'cache', 'saves',
            'log.txt', 'errors.txt', 'traceback.txt'))
        subprocess.run(runner + [str(project), 'lint', '--error-code'], cwd=sdk, check=True)
        subprocess.run(runner + [str(sdk / 'launcher'), 'distribute', str(project),
                       '--package', 'win', '--destination', str(output), '--no-update'],
                       cwd=sdk, check=True)
    archive = output / 'ApocalypseGame-0.3.0-win.zip'
    with zipfile.ZipFile(archive) as bundle:
        names = bundle.namelist()
        for required in ('ApocalypseGame.exe', 'game/ch02_model.py',
                         'game/fonts/NotoSansSC-Regular.otf', 'game/fonts/OFL.txt',
                         'game/data/ch02_routes.json', 'game/story_generated.rpy'):
            if not any(n.endswith('/' + required) for n in names):
                raise RuntimeError('Missing runtime file: ' + required)
        if any('/saves/' in n or '/tools/' in n or '/.git/' in n for n in names):
            raise RuntimeError('Developer files or saves entered the package.')
    digest = hashlib.sha256(archive.read_bytes()).hexdigest()
    archive.with_suffix('.zip.sha256').write_text(
        digest + '  ' + archive.name + '\n', encoding='utf-8', newline="\n")
    (output / 'windows-build.json').write_text(json.dumps({
        'game_version': '0.3.0', 'renpy_version': version.strip(),
        'archive': archive.name, 'bytes': archive.stat().st_size, 'sha256': digest,
        'content': 'Full chapter 1 and B-route Day6 tutorial; Day7 demo endpoint',
    }, indent=2) + '\n', encoding='utf-8', newline="\n")
    print(archive)


if __name__ == '__main__':
    main()

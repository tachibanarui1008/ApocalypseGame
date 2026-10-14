"""Run staged S05/S06 in an isolated Ren'Py SDK project and save directory."""
import argparse
import os
import shutil
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--sdk', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--tutorial-regression', action='store_true',
                        help='Run the existing chapter-one/tutorial native suite on current source.')
    args = parser.parse_args()
    sdk, output = args.sdk.resolve(), args.output.resolve()
    runtime = sdk / 'lib/py3-windows-x86_64/python.exe'
    if not runtime.is_file():
        parser.error('Supply an extracted Windows RenPy SDK.')
    if output.exists():
        parser.error('Use a new output directory to isolate saves and logs.')
    project = output / 'project'
    shutil.copytree(ROOT / 'game', project / 'game', ignore=shutil.ignore_patterns(
        '*.rpyc', '*.rpymc', '*.pyc', '__pycache__', 'cache', 'saves'))
    test_file = 'windows_acceptance.rpy' if args.tutorial_regression else 'ch02_events_acceptance.rpy'
    suite = 'windows_acceptance' if args.tutorial_regression else 'ch02_events_acceptance'
    shutil.copyfile(ROOT / 'tools' / test_file, project / 'game' / test_file)
    runner = [str(runtime), str(sdk / 'renpy.py'), '--savedir', str(output / 'saves'), str(project)]
    env = os.environ.copy()
    env['C2E_TEST_OUTPUT'] = str(output)
    env['WYC_TEST_OUTPUT'] = str(output / 'evidence')
    for name, command in [('lint', ['lint', '--error-code']),
                          ('native', ['test', suite, '--report-detailed'])]:
        with (output / (name + '.txt')).open('w', encoding='utf-8') as log:
            result = subprocess.run(runner + command, cwd=project, env=env, stdout=log,
                                    stderr=subprocess.STDOUT, timeout=300)
        report = (output / (name + '.txt')).read_text(encoding='utf-8-sig')
        print(report)
        if result.returncode or (name == 'native' and '[rpytest] Status: PASSED' not in report):
            raise SystemExit(result.returncode or 1)


if __name__ == '__main__':
    main()

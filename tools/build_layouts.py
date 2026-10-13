"""Render current plans without recreating obsolete layout or capacity drafts.

SAFEHOUSE_LAYOUT.json supplies the current room geometry. Furniture and capacity
checks must pass before replacing any generated drawings. Existing courtyard
reference artwork is retained: this entry point does not recreate that page.
"""
from pathlib import Path
import argparse
import json

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'docs/chapters/ch01/assets'


def floorplan():
    """Keep this public entry point, but use the current detailed renderer only."""
    from capacity_model import main as calculate_capacity
    from furnished_house import check_current_assets, main as render_furnished
    from pv_layout import main as render_pv

    # Check against the saved current figures before any generator writes files.
    check_current_assets()
    calculate_capacity()
    render_furnished()
    render_pv()


def townmap():
    from town_map import render_town
    render_town(OUT)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true',
                        help='Check geometry, furniture and capacities without writing images or data.')
    args = parser.parse_args()
    if args.check:
        from furnished_house import check_current_assets
        print(json.dumps(check_current_assets(), ensure_ascii=False, indent=2))
        return
    OUT.mkdir(parents=True, exist_ok=True)
    floorplan()
    townmap()
    layout = json.loads((OUT / 'SAFEHOUSE_LAYOUT.json').read_text())
    town = json.loads((OUT / 'TOWN_LAYOUT.json').read_text())
    print(f'Rendered safehouse V{layout["version"]} and town V{town["version"]}.')


if __name__ == '__main__':
    main()

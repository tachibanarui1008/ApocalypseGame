"""Restyle the existing SVG map; geometry and routing data remain unchanged."""
from pathlib import Path
import xml.etree.ElementTree as ET
import json
import cairosvg
NS='http://www.w3.org/2000/svg'
ET.register_namespace('',NS)
PALETTE={
 '#f2f1ed':'#20292a','#e9ebe7':'#263331','#dce7ce':'#334433','#afd8ec':'#293e44',
 '#e4e6e3':'#2c3537','#e5e8e4':'#2c3537','#e5ecd9':'#2c3a30','#d6ddce':'#405247',
 '#d1d4d0':'#35423e','#ffffff':'#67756d','#fbfcf7':'#65756a',
 '#d1d6d8':'#283230','#e0e4e6':'#45524c','#ccd2d5':'#57655e','#c8cfd2':'#59685f',
 '#3489db':'#789382','#cad5df':'#55655d','#e6eee3':'#354435','#eaf0e7':'#354435',
 '#eef4f9':'#45584e','#2487de':'#a0b39a','#adb6bb':'#677471','#b8bdc2':'#7a8982',
 '#899da3':'#647c7f','#d5e9f2':'#48666a','#80b0c7':'#69868a',
 '#39444b':'#bec8bd','#f4f4f0':'#20292a','#7c858b':'#8c9c92','#71816e':'#8eaa90',
 '#788187':'#9eaca3','#78856e':'#94a487','#7b858d':'#8e9c96','#7b946f':'#9cac88',
 '#4c93b7':'#89a5a9','#8e969a':'#9ba8a0','#418cd6':'#a6b9a0','#db716c':'#a0b39a',
 '#d5a65b':'#a0b39a','#558db5':'#a0b39a',
}
ICONS={
 'home':'<path d="M6 15L16 7L26 15M9 14V26H23V14M14 26V19H18V26"/>',
 'gate':'<path d="M7 6V27M25 6V27M8 11H24V24H8M12 11V24M20 11V24"/>',
 'pv_field':'<path d="M7 9H25L23 23H5ZM13 9L11 23M19 9L17 23M6 16H24M15 23V28M10 28H20"/>',
 'neighbor':'<path d="M5 15L12 9L19 15M7 14V25H17V14M19 10L26 16V25H20"/>',
 'market':'<path d="M8 12H24L26 25H6ZM12 12L14 7M20 12L18 7M12 17V22M17 17V22M22 17V22"/>',
 'farm':'<path d="M9 25C8 13 15 8 25 7C26 17 20 23 10 23M8 27L22 11M13 20L12 14M18 16L23 17"/>',
 'pharmacy':'<path d="M12 7H20V12H25V20H20V25H12V20H7V12H12Z"/>',
 'parcel':'<path d="M6 11L16 6L26 11V23L16 28L6 23ZM6 11L16 16L26 11M16 16V28M11 9L21 14"/>',
 'fuel':'<path d="M7 8H19V27H6M9 11H17V17H9ZM19 13L23 16V24Q26 27 26 22V11L23 8M6 27H21"/>',
 'hardware':'<path d="M9 9L14 6L20 10L17 14L11 10M16 13L25 25M7 25L13 19"/>',
 'workshop':'<path d="M22 7L18 11L21 14L25 10Q27 17 20 19L10 27L6 23L16 15Q13 7 22 7Z"/>',
 'station':'<rect x="9" y="5" width="14" height="21" rx="4"/><path d="M12 9H20V16H12ZM12 29L14 26M20 29L18 26M12 21H13M19 21H20"/>',
 'freight':'<path d="M5 10H15V23H5ZM15 14H26V23H15M8 26H10M21 26H23M4 29H28M20 14V9H26V14"/>',
 'port':'<circle cx="16" cy="8" r="3"/><path d="M16 11V27M10 15H22M6 21Q7 28 16 28Q25 28 26 21M6 21L6 25M26 21L26 25"/>',
}
def build_style(root=None):
    root=Path(root) if root else Path(__file__).resolve().parents[1]
    source=root/'docs/chapters/ch01/assets/TOWN_MAP.svg'
    tree=ET.fromstring(source.read_text(encoding="utf-8"))
    # Original drawing remains the reference; this is a separate game skin.
    remove_icon=False
    for node in list(tree):
        tag=node.tag.rsplit('}',1)[-1]
        if tag=='circle':remove_icon=True;tree.remove(node);continue
        if remove_icon and tag!='text':tree.remove(node);continue
        if tag=='text':remove_icon=False
        if float(node.get('y','0'))>=1300 or (tag=='path' and '1327' in node.get('d','')):
            tree.remove(node);continue
        if tag=='text' and node.text in ('安全屋','卫生服务点','便民商店'):
            tree.remove(node);continue
        if tag=='text' and node.text=='布局地图 · V0.3':node.text='城郊区域'
        for attr in ('fill','stroke'):
            value=node.get(attr)
            if value in PALETTE:node.set(attr,PALETTE[value])
            elif value=='white':node.set(attr,'#a8b8aa')
    dest=root/'game/images/ch02';(dest/'poi').mkdir(parents=True,exist_ok=True)
    svg=ET.tostring(tree,encoding='unicode')
    (dest/'town_map_game.svg').write_text(svg, encoding="utf-8", newline="\n")
    cairosvg.svg2png(bytestring=svg.encode(),write_to=str(dest/'town_map_game.png'))
    for key,icon in ICONS.items():
        for state in ('idle','hover','selected'):
            ink='#99ab9e' if state=='idle' else '#c9d98a'
            border='#566e5e' if state=='idle' else '#a5bb88'
            fill='#26322d' if state=='idle' else '#354737'
            icon_svg=f'<svg xmlns="{NS}" width="36" height="36" viewBox="0 0 36 36"><circle cx="18" cy="18" r="15" fill="{fill}" fill-opacity="0.88" stroke="{border}" stroke-width="1"/><g transform="translate(2 2)" fill="none" stroke="{ink}" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round">{icon}</g></svg>'
            (dest/'poi'/f'{key}_{state}.svg').write_text(icon_svg, encoding="utf-8", newline="\n")
            cairosvg.svg2png(bytestring=icon_svg.encode(),write_to=str(dest/'poi'/f'{key}_{state}.png'))
    route=json.loads((root/'game/data/ch02_routes.json').read_text(encoding="utf-8"))
    for mode in ('walk','suv','ev'):
        for stops in (['market'],['pharmacy'],['market','pharmacy'],['pharmacy','market']):
            parts=[];last='home'
            for stop in stops+['home']:
                path=route['path_matrices'][mode][last][stop]
                pts=' '.join(','.join(str(n) for n in route['nodes'][key]['xy']) for key in path)
                parts.append(f'<polyline points="{pts}" fill="none" stroke="#25352b" stroke-width="15" stroke-linecap="round" stroke-linejoin="round"/><polyline points="{pts}" fill="none" stroke="#c9d98a" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/>')
                last=stop
            overlay=f'<svg xmlns="{NS}" width="1800" height="1380">'+''.join(parts)+'</svg>'
            cairosvg.svg2png(bytestring=overlay.encode(),write_to=str(dest/('town_route_'+mode+'_'+'_'.join(stops)+'.png')))
    # Movement markers use the same line icon family, not oversized coloured words.
    car='<path d="M7 15L11 8H24L29 15V26H7Z M11 11H24V16H11Z M10 26V29M26 26V29"/>'
    walk='<circle cx="20" cy="8" r="3"/><path d="M18 13L17 23M17 17L11 20M18 14L24 20M17 23L11 31M17 23L24 31"/>'
    for mode in ('walk','suv','ev'):
        shape=walk if mode=='walk' else car
        marker=f'<svg xmlns="{NS}" width="40" height="40" viewBox="0 0 40 40"><circle cx="20" cy="20" r="18" fill="#1b2923" fill-opacity="0.92" stroke="#c9d98a" stroke-width="1"/><g fill="none" stroke="#d9e5b3" stroke-width="2" stroke-linejoin="round" stroke-linecap="round">{shape}</g></svg>'
        (dest/f'marker_{mode}.svg').write_text(marker, encoding="utf-8", newline="\n")
        cairosvg.svg2png(bytestring=marker.encode(),write_to=str(dest/f'marker_{mode}.png'))
    print('Game map skin: original geometry, subdued terrain, 14 line icons × 3 states.')
if __name__=='__main__':build_style()

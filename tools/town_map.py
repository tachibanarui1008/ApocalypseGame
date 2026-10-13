"""Clean map-inspired cartography with explicit, collision-checked footprints."""
from pathlib import Path
import json, html
import cairosvg
BG='#f2f1ed';BUILD='#dce0e2';EDGE='#c8ced0';TEXT='#39444b';BLUE='#2487de'
def tx(x,y,t,size=18,anchor='start',color=TEXT,halo=True):
 attrs=f'x="{x}" y="{y}" font-family="Arial Unicode MS, sans-serif" font-size="{size}" font-weight="400" text-anchor="{anchor}"'
 content=html.escape(t)
 back=f'<text {attrs} fill="none" stroke="#f4f4f0" stroke-width="4" stroke-linejoin="round">{content}</text>' if halo else ''
 return back+f'<text {attrs} fill="{color}">{content}</text>'

def box(x,y,w,h,fill,stroke='none',sw=1,rx=0):return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>'
def line(d,c,w=2,extra=''):return f'<path d="{d}" fill="none" stroke="{c}" stroke-width="{w}" stroke-linecap="round" stroke-linejoin="round" {extra}/>'
def poi(x,y,kind,color=BLUE):
 a=f'<circle cx="{x}" cy="{y}" r="15" fill="{color}" stroke="white" stroke-width="2"/>'
 if kind=='train':a+=box(x-7,y-8,14,15,'none','white',1.7,3)+line(f'M{x-4} {y+10} L{x-7} {y+13} M{x+4} {y+10} L{x+7} {y+13}','white',1.4)+box(x-4,y-5,8,5,'white')
 elif kind=='home':a+=line(f'M{x-9} {y} L{x} {y-8} L{x+9} {y} M{x-6} {y-1} V{y+8} H{x+6} V{y-1}','white',1.7)
 elif kind=='health':a+=line(f'M{x-7} {y} H{x+7} M{x} {y-7} V{y+7}','white',3)
 elif kind=='shop':a+=box(x-7,y-4,14,12,'none','white',1.6,1)+line(f'M{x-9} {y-4} H{x+9} M{x-6} {y-8} H{x+6}','white',2)
 elif kind=='port':a+=line(f'M{x} {y-9} V{y+7} M{x-7} {y+3} Q{x} {y+14} {x+7} {y+3} M{x-6} {y-3} H{x+6}','white',1.7)
 return a

def render_town(out):
 out=Path(out);previous=json.loads((out/'TOWN_LAYOUT.json').read_text(encoding="utf-8"))
 # 道路中心线：同一网络在交叉口合并绘制，建筑留在道路之间。
 roads=[([(120,610),(1330,610)],24), ([(390,290),(1200,290),(1200,910),(390,910),(390,290)],20), ([(820,160),(820,420)],16), ([(820,665),(820,1100)],16), ([(1200,290),(1330,290),(1330,1130),(1550,1130)],22), ([(1330,790),(1370,790)],18), ([(390,910),(370,930),(370,1160)],12), ([(430,270),(1330,270)],10), ([(470,1040),(1240,1040),(1240,910)],10), ([(590,290),(590,910)],10), ([(1075,290),(1075,910)],10), ([(390,565),(710,565)],10), ([(930,565),(1200,565)],10), ([(390,680),(1200,680)],10), ([(1200,910),(1330,910)],18), ([(110,870),(390,870)],10), ([(110,350),(350,350),(350,610)],10)]
 apartments=[(445,365,42,120),(525,365,42,100),(655,345,125,38),(655,420,112,35),(933,350,45,130),(1010,350,40,125),(1110,350,58,120),(432,525,116,30),(1105,525,72,28),(435,645,110,25),(1110,642,66,27),(447,740,40,112),(530,730,40,105),(650,735,120,35),(650,810,105,30),(939,735,40,110),(1010,735,40,115),(1118,735,46,108)]
 # 每一户独立布局，大小、退距与院内朝向均不同；不复制三个一组的图案。
 houses=[{'lot':(85,380,88,113),'b':(105,398,46,57),'front':(128,493),'street':(128,350)}, {'lot':(216,401,95,104),'b':(236,420,50,45),'front':(260,505),'street':(350,505)}, {'lot':(92,700,111,128),'b':(120,721,58,68),'front':(149,828),'street':(149,870)}, {'lot':(236,710,98,139),'b':(256,731,48,61),'front':(280,849),'street':(280,870)}, {'lot':(459,143,93,112),'b':(484,163,46,54),'front':(508,255),'street':(508,270)}, {'lot':(585,158,78,97),'b':(606,172,37,50),'front':(625,255),'street':(625,270)}, {'lot':(703,137,92,112),'b':(723,156,47,65),'front':(747,249),'street':(747,270)}, {'lot':(904,146,87,100),'b':(923,164,50,51),'front':(948,246),'street':(948,270)}, {'lot':(1020,157,93,94),'b':(1044,171,48,45),'front':(1068,251),'street':(1068,270)}, {'lot':(1150,143,103,112),'b':(1170,165,61,54),'front':(1201,255),'street':(1201,270)}, {'lot':(458,947,92,80),'b':(484,961,40,43),'front':(505,1027),'street':(505,1040)}, {'lot':(590,938,109,89),'b':(615,953,59,44),'front':(644,1027),'street':(644,1040)}, {'lot':(895,951,111,76),'b':(918,965,64,36),'front':(950,1027),'street':(950,1040)}, {'lot':(1050,946,78,82),'b':(1067,960,41,42),'front':(1087,1028),'street':(1087,1040)}, {'lot':(1160,945,71,76),'b':(1176,957,38,40),'front':(1195,1021),'street':(1195,1040)}, {'lot':(216,994,137,112),'b':(247,1011,64,61),'front':(290,1106),'street':(370,1120),'home':True}]
 buildings=[]
 for r in apartments:buildings.append({'type':'apartment','rect':r})
 for h in houses:buildings.append({'type':'house','rect':h['b']})
 services=[(950,495,96,54,'health'),(940,858,100,30,'shop'),(1268,348,43,104,'workshop'),(1385,710,47,153,'warehouse'),(1510,1008,69,68,'portwarehouse'),(750,470,140,62,'station')]
 for x,y,w,h,k in services:buildings.append({'type':k,'rect':(x,y,w,h)})
 # 中心线与建筑相交核对；允许道路网络自身交叉，不允许建筑占路。
 def road_hits(r,a,b,half):
  x,y,w,h=r
  if a[0]==b[0]:return x<a[0]+half and x+w>a[0]-half and y<max(a[1],b[1])+half and y+h>min(a[1],b[1])-half
  if a[1]==b[1]:return y<a[1]+half and y+h>a[1]-half and x<max(a[0],b[0])+half and x+w>min(a[0],b[0])-half
  return False
 for item in buildings:
  for points,width in roads:
   for a,b in zip(points,points[1:]):assert not road_hits(item['rect'],a,b,width/2+2),(item,a,b)
 for i,a in enumerate(buildings):
  x,y,w,h=a['rect']
  for b in buildings[i+1:]:
   xx,yy,ww,hh=b['rect'];assert not(min(x+w,xx+ww)>max(x,xx) and min(y+h,yy+hh)>max(y,yy)),(a,b)
 b=box(0,0,1800,1380,BG)
 # 地表：少量区域底色，避免繁重描边。
 b+=box(404,310,785,584,'#e9ebe7',rx=28)+box(35,940,139,235,'#dce7ce',rx=16)
 b+='<path d="M1640 145 C1600 390 1655 710 1600 950 L1600 1280 H1780 V145Z" fill="#afd8ec"/>'
 b+=box(1365,663,162,251,'#e4e6e3',rx=8)+box(1485,964,115,267,'#e5e8e4',rx=8)
 for h in houses:
  x,y,w,hh=h['lot'];b+=box(x,y,w,hh,'#e5ecd9','#d6ddce',.8,5)
 # road casings all first, fills all second, so intersections have no doubled crossbars
 for casing in [True,False]:
  for points,width in roads:
   d='M'+' L'.join(f'{x} {y}'for x,y in points)
   b+=line(d,'#d1d4d0'if casing else '#ffffff',width+3 if casing else width)
 # 家庭车道与人行路径：仅在院内空地和支路之间，避开建筑。
 for h in houses:
  x,y,w,hh=h['b'];fx,fy=h['front'];sx,sy=h['street']
  # 从房屋南侧到院内，再接街道；非车行主道路。
  d=f'M{x+w/2} {y+hh} V{fy} L{sx} {sy}'
  if sy<y:d=f'M{x+w/2} {y+hh} V{fy} H{h["lot"][0]+6} V{sy} H{sx}'
  b+=line(d,'#fbfcf7',5)
 # buildings: quiet plan footprints instead of repeating cottage icons
 for item in buildings:
  x,y,w,h=item['rect'];b+=box(x+2,y+2,w,h,'#d1d6d8',rx=2)+box(x,y,w,h,'#e0e4e6','#ccd2d5',.9,2)
 # 局部屋顶明暗形成层次，不做房屋正立面。
 for item in buildings:
  x,y,w,h=item['rect']
  if item['type']=='house':b+=line(f'M{x+5} {y+h/2} H{x+w-5}','#c8cfd2',1)
 # 地铁：沿独立预留走廊/道路旁走向，终止于站体。
 b+=line('M130 240 H820 V470','#3489db',5)
 b+=box(762,481,116,12,'#cad5df',rx=2)+box(762,509,116,12,'#cad5df',rx=2)
 b+=box(736,545,168,47,'#e6eee3','none',0,6)
 b+=poi(820,435,'train')+tx(840,451,'地铁终点站',18)+tx(820,575,'站前广场',15,'middle','#71816e')
 for x,lab in [(739,'A口'),(900,'B口')]:b+=box(x-10,536,20,18,'#eef4f9',BLUE,1,3)+tx(x,549,lab,10,'middle',BLUE,False)
 b+=box(758,635,125,21,'#eaf0e7','none',0,4)+tx(820,650,'公交 · 骑行换乘',13,'middle','#71816e')
 # 铁路线与站内股道：明确位于工业走廊，与住宅不混用。
 b+=line('M1480 160 V1100 M1480 1160 V1270','#adb6bb',4)
 for yy in range(175,1095,19):b+=line(f'M1474 {yy} H1486','#adb6bb',1.5)
 for yy in range(1170,1260,19):b+=line(f'M1474 {yy} H1486','#adb6bb',1.5)
 for xx in [1438,1456]:b+=line(f'M1480 675 L{xx} 702 V867 L1480 902','#adb6bb',2)
 b+=line('M1452 1108 H1510 M1452 1152 H1510','#b8bdc2',2)+tx(1481,1186,'道路下穿',13,'middle','#7b858d')
 # 码头岸线与船只，不用大图标压住地图。
 b+=line('M1598 998 V1218','#899da3',4)
 b+='<path d="M1662 1050 Q1683 1088 1662 1126 H1639 V1050Z" fill="#d5e9f2" stroke="#80b0c7" stroke-width="1.2"/>'
 # Labels with halos, manually kept outside road and building edges
 b+=tx(52,66,'庐州城郊城镇',32)+tx(52,100,'布局地图 · V0.3',16,color='#7c858b')+tx(1713,106,'北 ↑',20,'middle')
 b+=tx(493,334,'廉租高层公寓',20,'middle','#7c858b')+tx(1101,334,'廉租高层公寓',18,'middle','#7c858b')
 b+=tx(139,629,'独院住宅区',19)+tx(953,1191,'独院住宅与支巷',18,'middle','#78856e')
 b+=tx(109,922,'农田',16,'middle','#7b946f')
 b+=poi(305,981,'home','#418cd6')+tx(306,1168,'安全屋',21,'middle',BLUE)
 b+=poi(967,522,'health','#db716c')+tx(995,586,'卫生服务点',16,'middle')
 b+=poi(960,872,'shop','#d5a65b')+tx(992,940,'便民商店',16,'middle')
 b+=tx(1289,476,'维修作坊',16,'middle','#788187')
 b+=tx(1406,648,'货运火车站',22,'middle')+tx(1407,945,'货运站门区',14,'middle','#788187')
 b+=poi(1553,991,'port','#558db5')+tx(1544,960,'运河小型港口',22,'middle')
 b+=tx(1688,772,'运河',23,'middle','#4c93b7')
 b+=tx(119,590,'社区主路',15,color='#8e969a')+tx(1227,550,'物流道路',15,color='#8e969a')+tx(845,1113,'住宅支路',14,color='#8e969a')
 # 清爽的页脚，而不是伪装成真实苹果地图或新增应用界面。
 b+=box(38,1300,1724,53,'#ffffff','none',0,12)+poi(69,1327,'train')+tx(98,1334,'地铁站标记',14)+box(261,1320,19,13,'#e0e4e6')+tx(290,1334,'建筑轮廓',14)+line('M430 1327 H464','#3489db',4)+tx(475,1334,'地铁线路',14)+line('M619 1327 H653','#adb6bb',3)+tx(665,1334,'货运铁路',14)+tx(1734,1334,'虚构布局 · 建筑符号不按比例',14,'end','#7b858d')
 svg=f'<svg xmlns="http://www.w3.org/2000/svg" width="1800" height="1380" viewBox="0 0 1800 1380">{b}</svg>'
 (out/'TOWN_MAP.svg').write_text(svg, encoding="utf-8", newline="\n");cairosvg.svg2png(bytestring=svg.encode(),write_to=str(out/'TOWN_MAP.png'))
 previous.update({'version':'0.3','render_style':'清爽二维地图，浅色地表、白色道路、淡灰建筑、蓝色水面与交通POI，参考苹果地图视觉层次','buildings':buildings,'courtyard_lots':houses,'roads_visual':[{'points':p,'width_px':w}for p,w in roads],'station_representation':'地面站体轮廓、地铁POI、线路终点、A/B出入口、站前广场；公交骑行区另置','plot_status':'方位保持，画面重新排版；先前游戏路线预算不因画面像素变化自动换算'})
 if 'routes_budget'in previous:previous['routes_budget']['status']='上一轮游戏尺度预算继续作为参考；新排版未按像素重新测距，地图几何和数值下一轮统一'
 (out/'TOWN_LAYOUT.json').write_text(json.dumps(previous,ensure_ascii=False,indent=2), encoding="utf-8", newline="\n")
 print(f'Town map: {len(buildings)} footprints checked, no building-road or building-building overlap.')

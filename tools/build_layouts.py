"""Render the game's editable schematic plans; dimensions are design budgets."""
from pathlib import Path
import json, html
import cairosvg
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'docs/chapters/ch01/assets'
INK='#514e46';LINE='#756f65';PAPER='#f4f1e9';GREEN='#829488';PURPLE='#8b7d94'
def wrap(width,height,content):
 return f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}"><rect width="100%" height="100%" fill="{PAPER}"/><g font-family="Arial Unicode MS, PingFang SC, sans-serif" fill="{INK}">{content}</g></svg>'
def txt(x,y,t,size=18,anchor='start'):
 return f'<text x="{x}" y="{y}" font-size="{size}" text-anchor="{anchor}">{html.escape(t)}</text>'
def rect(x,y,w,h,fill='none',stroke=LINE,sw=2,rx=0):
 return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>'
def path(d,stroke=LINE,sw=2,fill='none',extra=''):
 return f'<path d="{d}" stroke="{stroke}" stroke-width="{sw}" fill="{fill}" {extra}/>'
def door(x,y,vertical=True):
 if vertical:return path(f'M{x} {y-20} V{y+20}',PAPER,7)+path(f'M{x} {y+20} l25 -25',LINE,1.4)
 return path(f'M{x-20} {y} H{x+20}',PAPER,7)+path(f'M{x-20} {y} l25 -25',LINE,1.4)
def car(x,y,color):
 return f'<g transform="translate({x},{y})">'+path('M8 0 Q0 0 0 12 V72 Q0 84 10 84 H34 Q44 84 44 72 V12 Q44 0 36 0 Z',LINE,1.5,color)+rect(6,14,32,16,PAPER,LINE,1)+rect(6,55,32,13,PAPER,LINE,1)+path('M-3 24 H0 M44 24 H47',LINE,2)+'</g>'
def render(name,svg):
 (OUT/f'{name}.svg').write_text(svg)
 cairosvg.svg2png(bytestring=svg.encode(),write_to=str(OUT/f'{name}.png'))
def floorplan():
 data=json.loads((OUT/'SAFEHOUSE_LAYOUT.json').read_text())
 data['version']='0.2'
 for f in data['floors']:
  if f['id']=='F1':
   f['rooms']=[[0,0,3,4,'楼梯'],[0,4,3,2,'卫浴'],[0,6,3,4,'临时客房'],[3,0,2,4,'楼梯厅'],[5,0,6,4,'厨房'],[3,4,8,6,'开放客餐厅 / 玄关']]
   f['note']='客厅、餐厅、玄关连通；厨房保留隔门与侧门'
  if f['id']=='F2':
   f['rooms']=[[0,0,3,4,'楼梯'],[0,4,1.5,2,'淋浴'],[1.5,4,1.5,2,'厕所'],[0,6,3,1.5,'外置洗手台'],[0,7.5,3,2.5,'洗衣 / 储物'],[3,0,2,10,'通道'],[5,0,6,3.5,'父母卧室'],[5,3.5,6,3.5,'情侣卧室'],[5,7,6,3,'书房 / 通信桌']]
   f['note']='二层干湿分开：独立厕所、淋浴与外置洗手台'
  if f['id']=='SITE':f['note']='两车集中西南一角；无车位划线，保留开敞院落'
 data['circulation']['ground_open_space']='玄关、餐厅、客厅共用开放空间，无三处分隔墙'
 data['circulation']['second_bathroom']='西侧淋浴及独立厕所，共用外置洗手台；入口来自公共通道'
 data['circulation']['yard_cars']='西南角集中停放，不画车位或停车分区'
 (OUT/'SAFEHOUSE_LAYOUT.json').write_text(json.dumps(data,ensure_ascii=False,indent=2))
 panels=[]
 for i,f in enumerate(data['floors']):
  x=25+(i%2)*690;y=115+(i//2)*650
  p=txt(55,40,f['title'],23)+txt(602,76,'北 ↑',15)+'<g transform="translate(90,87)">'
  if f['id']=='SITE':
   p+=rect(0,0,495,450)+rect(70,0,360,190,'#e8e4da')+txt(250,85,'住宅南立面',19,'middle')+txt(250,116,'正门 ↓',16,'middle')
   p+=car(45,322,'#edeae2')+car(102,322,PURPLE)+txt(35,298,'两车停于西南角',16)
   p+=txt(310,305,'开敞院落',23,'middle')+txt(310,336,'生活 / 搬物 / 通行',16,'middle')
   p+=rect(10,20,43,105)+txt(31,53,'设',15,'middle')+txt(31,77,'备',15,'middle')+txt(31,101,'位',15,'middle')
   p+=path('M225 450 H375',PAPER,7)+path('M225 450 V418 M375 450 V418')+txt(300,483,'南侧院门 / 乡村道路',16,'middle')
  else:
   doors=[]
   for xx,yy,w,h,t in sorted(f['rooms'],key=lambda r:0 if r[0]==3 else 1):
    fill='#e8e4da' if ('通道' in t or '楼梯' in t) else '#f7f5ef'
    if '光伏' in t:fill='#e1e6e3'
    p+=rect(xx*45,yy*45,w*45,h*45,fill)
    tx=(xx+w/2)*45;ty=(yy+h/2)*45
    if f['id']=='F1' and '开放' in t:continue
    if w==2 and '通道'in t:
     for k,c in enumerate(t):p+=txt(tx,ty-35+k*23,c,18,'middle')
    else:p+=txt(tx,ty+6,t,16 if w<=1.5 else 19,'middle')
    if f['id']=='F2' and t in ['淋浴','厕所']:doors.append((tx,270,False));continue
    if f['id']=='F1' and t=='厨房':doors.append((350,180,False));continue
    if xx==0 and '楼梯'not in t:
     if f['id']=='F2' and t=='外置洗手台':doors.append((135,304,True))
     elif f['id']=='F2' and t=='洗衣 / 储物':doors.append((135,382,True))
     elif f['id']!='F2':doors.append((135,(yy+min(1,h/2))*45,True))
    elif xx==5:doors.append((225,(yy+min(1,h/2))*45,True))
   for dx,dy,vert in doors:p+=door(dx,dy,vert)
   p+=path('M135 104 V147',PAPER,7)
   for k in range(7):p+=path(f'M15 {15+k*13} H103',LINE,1)
   p+=path('M0 -16 H495 M0 -22 V-10 M495 -22 V-10',LINE,1)+txt(247,-24,'11 m',15,'middle')+txt(514,f['h']*45/2,f'{f["h"]} m',15)
   if f['id']=='F1':
    p+=path('M145 180 H215',PAPER,7)+path('M155 450 H204',PAPER,7)+path('M180 486 V465 M172 475 L180 465 L188 475')+txt(180,510,'主入口',16,'middle')
    p+=path('M495 70 V112',PAPER,7)+txt(514,106,'侧门',14)
    p+=txt(350,244,'餐厅',21,'middle')+txt(350,382,'客厅',21,'middle')+txt(172,419,'玄关',16,'middle')
    p+=rect(305,264,100,38,'none','#aca69b',1.3,6)+rect(302,395,106,26,'none','#aca69b',1.3,4)
   if f['id']=='F2':
    p+=rect(408,410,69,30,'#dbe3dc',GREEN,1)+txt(442,430,'固定台',13,'middle')+path('M488 410 V70',GREEN,1.5,extra='stroke-dasharray="5 5"')+txt(477,333,'馈线上行 ↑',14,'end')
    # 两个湿区各自开门至外置洗手区；洗手区面向通道开放
    p+=path('M135 280 V327',PAPER,7)
   if f['id']=='ROOF':
    p+=f'<circle cx="450" cy="58" r="16" fill="#dae4dc" stroke="{GREEN}"/>'+path('M450 20 V90 M436 74 H464',GREEN)+txt(423,110,'X50N屋顶天线',15,'end')+path('M450 90 H488 V450',GREEN,1.5,extra='stroke-dasharray="5 5"')
    for r in range(4):
     for c in range(3):p+=rect(250+c*70,153+r*66,62,57,'none','#8b9990',1)
  p+='</g>'+txt(55,620,f['note'],15)
  panels.append(f'<g transform="translate({x},{y})">{p}</g>')
 body=txt(55,55,'安全屋户型与院落草图 · V0.2',30)+txt(55,90,'开放客餐厅｜二层卫浴分区｜两车集中院落一角',18)+''.join(panels)+txt(55,2070,'布局草案：北向上；地上约110㎡/层；院落不与楼层同比例。绿色虚线为馈线走向。',16)
 render('SAFEHOUSE_PLAN',wrap(1400,2090,body))
def townhouse(x,y,size=36,color='#e9e4da',highlight=False):
 a=rect(x-8,y-8,size+16,size+29,'none',GREEN if highlight else '#aaa295',1)
 a+=rect(x,y+8,size,size*.65,color,LINE,1.3)+path(f'M{x-4} {y+9} L{x+size/2} {y-5} L{x+size+4} {y+9}',LINE,1.3,'#d1cbc0')
 return a

def townmap():
 b=txt(55,55,'庐州城郊城镇 · 空间布局草案 V0.1',30)+txt(55,88,'地铁终点站居中，高层公寓环绕，外围独门独院住宅，东侧道路连接货运站与运河港口',18)+txt(1490,130,'北 ↑',20)
 # 运河与陆地
 b+=path('M1460 130 C1380 410 1450 690 1390 1110', '#d5e2e3',145)+path('M1460 130 C1380 410 1450 690 1390 1110','#8da5aa',2,extra='stroke-dasharray="8 10"')+txt(1492,530,'运',24,'middle')+txt(1492,568,'河',24,'middle')
 # 住宅中心片区淡色边界
 b+=rect(345,255,710,580,'#ebe7df','none',0,30)
 b+=txt(515,235,'廉租高层公寓片区',24,'middle')
 # 道路：绘制底色和中心线
 roads=['M145 525 H1130 V760 H1220','M350 265 H1050 V825 H350 Z','M705 175 V960','M350 825 H270 V960','M1130 760 V1030 H1350']
 for d in roads:b+=path(d,'#d4cec1',27)+path(d,'#f7f4ed',18)
 # 地铁线路从西北进入，在中心结束
 b+=path('M150 160 L380 350 L705 525',GREEN,6,extra='stroke-dasharray="12 7"')+txt(190,170,'地铁线路入城方向',15)
 # 高层小区组团，全部环绕中心
 towers=[]
 for bx,by in [(420,340),(560,340),(845,340),(420,625),(570,660),(875,645),(405,475),(865,470)]:
  for j in range(2):
   x=bx+j*64;y=by
   towers.append(rect(x,y,44,67,'#dce0dc',LINE,1.5)+path(f'M{x+8} {y+15} H{x+36} M{x+8} {y+31} H{x+36} M{x+8} {y+47} H{x+36}', '#999e97',1))
 b+=''.join(towers)
 b+=rect(590,465,225,125,'#f1ece1',LINE,2,14)+txt(703,512,'地铁终点站',26,'middle')+txt(703,547,'站前广场 / 换乘',16,'middle')
 # 外围低密度院落
 clusters=[(250,210),(525,130),(840,135),(1080,165),(400,920),(910,920),(180,670)]
 for x,y in clusters:
  for j in range(3):b+=townhouse(x+j*59,y)
 b+=txt(60,630,'外围独门独院住宅',21)+txt(470,1075,'外围低密度住宅与村道',21)
 # 安全屋位于外围，不作为中心
 b+=townhouse(233,893,49,'#e8e4d9',True)+txt(252,997,'主角家安全屋',19,'middle')
 # 货运铁路独立于地铁：东侧物流走廊
 b+=path('M1260 150 V1120','#787b76',7)+path('M1251 150 V1120 M1269 150 V1120','#f2efea',1.5)
 for yy in range(160,1100,21):b+=path(f'M1247 {yy} H1273','#787b76',2)
 b+=txt(1280,275,'货运铁路',18)
 b+=rect(1145,605,170,255,'#e2e4df',LINE,1.5,10)+txt(1085,589,'货运火车站',23)
 b+=path('M1260 605 V860','#787b76',7)+path('M1251 605 V860 M1269 605 V860','#f2efea',1.5)
 for yy in range(610,855,21):b+=path(f'M1247 {yy} H1273','#787b76',2)
 for xx in [1185,1210,1235]:b+=path(f'M1260 620 L{xx} 651 V806 L1260 845',LINE,1.5)
 b+=rect(1158,666,20,144,'#c8cec7',LINE,1)+txt(1228,850,'装卸场 / 货运股道',14,'middle')+txt(1157,731,'入',14)+txt(1157,756,'口',14)
 # 道路穿铁路下穿通道，不画成无控制的平交
 b+=path('M1215 1030 H1305','#d4cec1',29)+path('M1215 1030 H1305','#f7f4ed',17)+txt(1258,1080,'道路下穿铁路',14,'middle')
 # 小港位于运河西岸，与公路连接；并非铁路客运节点
 b+=rect(1304,896,74,144,'#e6dfd1',LINE,1.5)+path('M1379 891 V1050','#727970',5)+txt(1293,879,'运河小型港口',21)+txt(1338,938,'仓储',15,'middle')+txt(1338,966,'装卸',15,'middle')
 b+=path('M1441 938 Q1458 977 1441 1015 H1419 V938 Z','#799096',2,'#edf0ec')+txt(1456,1049,'货船',15,'middle')
 b+=txt(1080,965,'沿道路连接',15)+txt(1130,542,'东侧物流道路',16)
 # 图例与口径
 b+=path('M55 1135 H105',GREEN,5,extra='stroke-dasharray="12 7"')+txt(115,1141,'地铁',16)+path('M225 1135 H275','#787b76',5)+txt(285,1141,'货运铁路',16)+path('M420 1135 H470','#d4cec1',12)+txt(480,1141,'道路',16)+path('M600 1135 H650','#9ab6ba',12)+txt(660,1141,'运河',16)
 b+=txt(55,1180,'方位与设施关系示意，不按比例；户数、距离、正式地名与交通细节待定。未新增剧情事件。',16)
 render('TOWN_MAP',wrap(1600,1210,b))
 layout={'version':'0.1','north':'up','scale':'方位示意，不按比例','center':'地铁终点站与站前广场','inner_residential':'中心周边廉租高层公寓','outer_residential':'独门独院低密度住宅','safehouse':'外围西南侧低密度住宅区（方位初稿）','logistics':['东侧道路沿线货运火车站','继续沿道路通往运河西岸小型港口'],'networks':{'metro':'西北方向进入，以中心车站为终点；独立于货运铁路','freight':'东侧南北向货运铁路及站场','road':'中心道路、社区环路及东侧物流道路','canal':'东侧南北向运河；码头位于西岸','crossing':'港口道路下穿货运铁路（初稿）'}}
 (OUT/'TOWN_LAYOUT.json').write_text(json.dumps(layout,ensure_ascii=False,indent=2))
if __name__=='__main__':
 OUT.mkdir(parents=True,exist_ok=True)
 floorplan();townmap()
 print('Rendered safehouse V0.2 and town V0.1.')

"""Render the game's editable schematic plans; dimensions are design budgets."""
from pathlib import Path
import json, html, math, heapq
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
 data['version']='0.3'
 data['design_budget']={'floor_height_m':3.2,'stair':'U形双跑示意，约19～20级；尺寸待结构核算','exterior_wall_m':0.24,'partition_m':0.12,'yard_plot_m':[15,17],'house_on_plot_m':[2,1,11,10],'yard_gross_excluding_house_m2':145,'courtyard_gate_width_m':4.5,'vehicle_envelope_budget_m':[5.0,2.1],'vehicle_parking_orientation':'西南角沿院墙东西向停放；可倒车调整，不预设原地掉头','main_door_width_m':1.1,'bedroom_door_width_m':0.9,'bathroom_door_width_m':0.8}
 data['status']='空间及尺寸预算：面积非净面积，家具与门窗为布置初稿'
 data['circulation']['yard_cars']='西南角两车集中停放；前院与院门保留通道，无车位划线'
 for f in data['floors']:
  if f['id']=='F1':
   f['rooms']=[[0,0,3,4,'楼梯'],[0,4,3,2,'卫浴'],[0,6,3,4,'临时客房'],[3,0,2,4,'楼梯厅'],[5,0,6,4,'厨房'],[3,4,8,6,'开放客餐厅 / 玄关']]
   f['note']='客厅、餐厅、玄关连通；厨房保留隔门与侧门'
  if f['id']=='F2':
   f['rooms']=[[0,0,3,4,'楼梯'],[0,4,1.5,2,'淋浴'],[1.5,4,1.5,2,'厕所'],[0,6,3,1.5,'外置洗手台'],[0,7.5,3,2.5,'洗衣 / 储物'],[3,0,2,10,'通道'],[5,0,6,3.5,'父母卧室'],[5,3.5,6,3.5,'情侣卧室'],[5,7,6,3,'书房 / 通信桌']]
   f['note']='二层干湿分开：独立厕所、淋浴与外置洗手台'
  if f['id']=='SITE':f['note']='院落预算约145㎡；两车仍在西南角，无车位划线'
 data['circulation']['ground_open_space']='玄关、餐厅、客厅共用开放空间，无三处分隔墙'
 data['circulation']['second_bathroom']='西侧淋浴及独立厕所，共用外置洗手台；入口来自公共通道'
 data['circulation']['yard_cars']='西南角集中停放，不画车位或停车分区'
 (OUT/'SAFEHOUSE_LAYOUT.json').write_text(json.dumps(data,ensure_ascii=False,indent=2))
 panels=[]
 for i,f in enumerate(data['floors']):
  x=25+(i%2)*690;y=115+(i//2)*650
  p=txt(55,40,f['title'],23)+txt(602,76,'北 ↑',15)+'<g transform="translate(90,87)">'
  if f['id']=='SITE':
   u=26
   p+=rect(0,0,15*u,17*u)+rect(2*u,1*u,11*u,10*u,'#e8e4da')
   p+=txt(7.5*u,120,'三层住宅',21,'middle')+txt(7.5*u,150,'11 × 10 m',16,'middle')+txt(6*u,274,'正门 ↓',15,'middle')
   p+='<g transform="translate(20,350) rotate(-90) scale(1.24,1.548)">'+car(0,0,'#edeae2')+'</g>'
   p+='<g transform="translate(20,420) rotate(-90) scale(1.24,1.548)">'+car(0,0,PURPLE)+'</g>'
   p+=txt(245,346,'开敞前院',21,'middle')+txt(245,375,'出入 / 搬物 / 日常活动',14,'middle')
   p+=rect(8,90,30,66)+txt(23,116,'设备',12,'middle')+txt(23,137,'位置',12,'middle')
   p+=path('M234 442 H351',PAPER,7)+path('M234 442 V412 M351 442 V412')+txt(291,476,'院门约4.5 m',15,'middle')
   p+=path('M292 414 V300 L190 300 V288',GREEN,1.5,extra='stroke-dasharray="5 5"')
   p+=path('M338 73 V94',PAPER,7)+txt(346,90,'侧门',13)
   p+=txt(195,-20,'用地预算 15 m',15,'middle')+txt(407,240,'17 m',15)+txt(195,517,'南侧乡村道路',16,'middle')

  else:
   doors=[]
   for xx,yy,w,h,t in sorted(f['rooms'],key=lambda r:0 if r[0]==3 else 1):
    fill='#e8e4da' if ('通道' in t or '楼梯' in t) else '#f7f5ef'
    if '光伏' in t:fill='#e1e6e3'
    p+=rect(xx*45,yy*45,w*45,h*45,fill)
    tx=(xx+w/2)*45;ty=(yy+h/2)*45
    if f['id']=='F1' and '开放' in t:continue
    if '楼梯' in t:continue
    if f['id']=='F2' and t in ['父母卧室','情侣卧室']:continue
    if f['id']=='F3' and t=='客房':continue
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
   for k in range(10):p+=path(f'M15 {42+k*10} H58 M78 {42+k*10} H121',LINE,1)
   p+=path('M15 30 H121 M68 42 V136',LINE,1)+txt(67,166,'楼梯',18,'middle')
   p+=path('M0 -16 H495 M0 -22 V-10 M495 -22 V-10',LINE,1)+txt(247,-24,'11 m',15,'middle')+txt(514,f['h']*45/2,f'{f["h"]} m',15)
   if f['id'] in ['F1','F2','F3']:
    windows=['M305 0 H435','M495 190 V285','M280 450 H440','M0 335 V413']
    windows.append('M495 20 V55' if f['id']=='F1' else 'M495 40 V120')
    for wd in windows:
     p+=path(wd,PAPER,8)+path(wd,'#8a9d9a',3)
   if f['id']=='F1':
    p+=path('M145 180 H215',PAPER,7)+path('M155 450 H204',PAPER,7)+path('M180 486 V465 M172 475 L180 465 L188 475')+txt(180,510,'主入口',16,'middle')
    p+=path('M495 70 V112',PAPER,7)+txt(514,106,'侧门',14)
    p+=txt(350,244,'餐厅',21,'middle')+txt(350,382,'客厅',21,'middle')+txt(172,419,'玄关',16,'middle')
    p+=rect(305,264,100,38,'none','#aca69b',1.3,6)+rect(302,395,106,26,'none','#aca69b',1.3,4)
    p+=rect(430,345,45,12,'none','#aca69b',1.2)+rect(249,330,28,60,'none','#aca69b',1.2)
    p+=path('M250 20 H455 V135', '#aca69b',10)+rect(245,118,30,40,PAPER,'#aca69b',1)
    p+=txt(250,176,'隔门',13)
   if f['id'] in ['F2','F3']:
    ys=[25,183] if f['id']=='F2' else [25]
    for yy in ys:
     p+=rect(255,yy,81,90,'none','#aca69b',1.4)+rect(263,yy+8,27,14,'none','#aca69b',1)+rect(299,yy+8,27,14,'none','#aca69b',1)
    if f['id']=='F2':p+=txt(407,86,'父母卧室',19,'middle')+txt(407,245,'情侣卧室',19,'middle')
    else:p+=txt(407,96,'客房',19,'middle')
   if f['id']=='F2':
    p+=rect(18,182,31,20,'none','#aca69b',1)+rect(88,182,24,20,'none','#aca69b',1)+rect(15,320,102,12,'none','#aca69b',1)+rect(17,354,34,33,'none','#aca69b',1)
    p+=rect(260,423,115,18,'none','#aca69b',1)
    p+=rect(408,410,69,30,'#dbe3dc',GREEN,1)+txt(442,430,'固定台',13,'middle')+path('M488 410 V70',GREEN,1.5,extra='stroke-dasharray="5 5"')+txt(477,333,'馈线上行 ↑',14,'end')
    # 两个湿区各自开门至外置洗手区；洗手区面向通道开放
    p+=path('M135 280 V327',PAPER,7)
   if f['id']=='ROOF':
    p+=f'<circle cx="450" cy="58" r="16" fill="#dae4dc" stroke="{GREEN}"/>'+path('M450 20 V90 M436 74 H464',GREEN)+txt(423,110,'X50N屋顶天线',15,'end')+path('M450 90 H488 V450',GREEN,1.5,extra='stroke-dasharray="5 5"')
    for r in range(4):
     for c in range(3):p+=rect(250+c*70,153+r*66,62,57,'none','#8b9990',1)
  p+='</g>'+txt(55,620,f['note'],15)
  panels.append(f'<g transform="translate({x},{y})">{p}</g>')
 body=txt(55,55,'安全屋户型与院落细化 · V0.3',30)+txt(55,90,'门窗与家具示意｜U形楼梯｜二层卫浴分区｜院落尺寸预算',18)+''.join(panels)+txt(55,2070,'北向上；地上约110㎡/层；院落15×17m用地预算，图示比例与楼层不同。绿线为设备/出入路径。',16)
 render('SAFEHOUSE_PLAN',wrap(1400,2090,body))
def townhouse(x,y,size=36,color='#e9e4da',highlight=False):
 a=rect(x-8,y-8,size+16,size+29,'none',GREEN if highlight else '#aaa295',1)
 a+=rect(x,y+8,size,size*.65,color,LINE,1.3)+path(f'M{x-4} {y+9} L{x+size/2} {y-5} L{x+size+4} {y+9}',LINE,1.3,'#d1cbc0')
 return a

def townmap():
 b=txt(55,55,'庐州城郊城镇 · 空间布局细化 V0.2',30)+txt(55,88,'地铁终点站居中，高层公寓环绕，外围独门独院住宅，东侧道路连接货运站与运河港口',18)+txt(1490,130,'北 ↑',20)
 # 运河与陆地
 b+=path('M1460 130 C1380 410 1450 690 1390 1110', '#d5e2e3',145)+path('M1460 130 C1380 410 1450 690 1390 1110','#8da5aa',2,extra='stroke-dasharray="8 10"')+txt(1492,530,'运',24,'middle')+txt(1492,568,'河',24,'middle')
 # 住宅中心片区淡色边界
 b+=rect(345,255,710,580,'#ebe7df','none',0,30)
 b+=txt(515,235,'廉租高层公寓片区',24,'middle')
 # 道路：绘制底色和中心线
 roads=['M145 525 H1130 V760 H1220','M1050 265 H1130 V525','M1050 825 H1130','M350 265 H1050 V825 H350 Z','M705 175 V960','M350 825 H270 V960','M1130 760 V1030 H1350']
 for d in roads:b+=path(d,'#d4cec1',27)+path(d,'#f7f4ed',18)
 # 居住支路与小区内部通路：符号尺度不同于道路距离预算
 for d in ['M350 430 H1050','M350 600 H1050','M350 745 H1050','M535 265 V825','M990 265 V825','M510 208 H1130 V265','M390 990 H1100 V960 H1130','M705 960 V990','M160 746 H350','M1050 430 H1130 V350']:
  b+=path(d,'#dad5c9',10)+path(d,'#f7f4ed',6)
 # 核心周边步行提示与服务设施
 b+=rect(605,599,206,28,'#e6e8dc','none',0,5)+txt(708,620,'站前步行 / 公交 / 骑行',14,'middle')
 b+=rect(748,645,82,45,'#e4dfd3',LINE,1)+txt(789,673,'便民商店',15,'middle')
 b+=rect(753,350,80,45,'#e4dfd3',LINE,1)+txt(793,378,'卫生服务点',14,'middle')
 b+=rect(1138,330,72,70,'#e5e1d7',LINE,1)+txt(1174,371,'维修作坊',14,'middle')
 b+=rect(55,823,96,168,'#e5e9dd','#b6bfa9',1)
 for yy in range(840,985,21):b+=path(f'M65 {yy} H141','#b6bfa9',1)
 b+=txt(103,1016,'农田',16,'middle')
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
 b+=txt(55,1180,'方位与建筑符号不按比例；道路长度另有游戏设计预算，非实地测绘。公共设施为布局初稿。',16)
 render('TOWN_MAP',wrap(1600,1210,b))
 layout={'version':'0.2','north':'up','scale':'方位示意，不按比例','center':'地铁终点站与站前广场','inner_residential':'中心周边廉租高层公寓','outer_residential':'独门独院低密度住宅','safehouse':'外围西南侧低密度住宅区（方位初稿）','logistics':['东侧道路沿线货运火车站','继续沿道路通往运河西岸小型港口'],'networks':{'metro':'西北方向进入，以中心车站为终点；独立于货运铁路','freight':'东侧南北向货运铁路及站场','road':'中心道路、社区环路及东侧物流道路','canal':'东侧南北向运河；码头位于西岸','crossing':'港口道路下穿货运铁路（初稿）'}}
 layout['facilities_draft']=['站前步行与公交骑行区域','便民商店','卫生服务点','维修作坊','西侧农田']
 layout['routes_budget']=route_budget()
 (OUT/'TOWN_LAYOUT.json').write_text(json.dumps(layout,ensure_ascii=False,indent=2))
def route_budget():
 # 道路折线长度以每图示单位2m作为游戏设计预算；不为建筑符号提供比例尺。
 nodes={'home':(270,930),'lane':(270,825),'southwest':(350,825),'west':(350,525),'station_west':(590,525),'station':(705,525),'southeast':(1050,825),'east':(1050,525),'logistics_north':(1130,525),'logistics_south':(1130,825),'freight_junction':(1130,760),'freight_gate':(1145,760),'underpass_west':(1130,1030),'port_gate':(1304,1030)}
 pairs=[('home','lane'),('lane','southwest'),('southwest','west'),('west','station_west'),('station_west','station'),('southwest','southeast'),('southeast','east'),('east','station'),('east','logistics_north'),('southeast','logistics_south'),('logistics_north','freight_junction'),('freight_junction','logistics_south'),('freight_junction','freight_gate'),('logistics_south','underpass_west'),('underpass_west','port_gate')]
 edges=[];graph={k:[] for k in nodes}
 for a,b in pairs:
  length=round(math.dist(nodes[a],nodes[b])*2)
  edges.append({'from':a,'to':b,'length_m':length,'state':'正常开放假设'})
  graph[a].append((b,length));graph[b].append((a,length))
 routes=[]
 for target,title in [('station','安全屋→地铁站'),('freight_gate','安全屋→货运站入口'),('port_gate','安全屋→港口入口')]:
  queue=[(0,'home',[])];seen=set()
  while queue:
   dist,n,p=heapq.heappop(queue)
   if n in seen:continue
   seen.add(n)
   if n==target:
    routes.append({'route':title,'length_m':dist,'nodes':p+[n],'walk_minutes_at_80m_min':round(dist/80,1),'laden_minutes_at_60m_min':round(dist/60,1)})
    break
   for nxt,weight in graph[n]:heapq.heappush(queue,(dist+weight,nxt,p+[n]))
 return {'status':'虚构道路设计预算，尚未定稿；不包括等待、进出站及事件消耗','walking_speed_m_min':80,'laden_speed_m_min':60,'nodes':nodes,'edges':edges,'normal_routes':routes,'truck_route':'优先走东侧环路与物流道路，避免站前广场；下穿是独立可变状态节点'}
if __name__=='__main__':
 OUT.mkdir(parents=True,exist_ok=True)
 floorplan();townmap()
 print('Rendered safehouse V0.3 and town V0.2.')

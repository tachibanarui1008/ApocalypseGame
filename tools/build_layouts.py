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
 data['version']='0.4'
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
  if f['id']=='F3':
   f['rooms']=[[0,0,3,4,'楼梯'],[0,4,3,2,'卫浴'],[0,6,3,4,'服务器房'],[3,0,2,10,'通道'],[5,0,6,4,'客房'],[5,4,6,6,'电力储存设备间']]
   f['title']='三层 · 服务器与电力设备'
   f['note']='服务器与电力分室；30kWh储能、逆变与配电位置初稿'
  if f['id']=='SITE':f['note']='院落预算约145㎡；两车仍在西南角，无车位划线'
 data['circulation']['ground_open_space']='玄关、餐厅、客厅共用开放空间，无三处分隔墙'
 data['equipment_locations']={'server':'三层西南服务器房：Mac mini与存储、家庭网络','power':'三层东南电力储存设备间：30kWh储能、逆变器、配电及维护空间','radio':'二层书房：FTM-6000R固定台；RF线路独立布置'}
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
   p+=rect(8,90,30,66)+txt(23,116,'工具',12,'middle')+txt(23,137,'收纳',12,'middle')
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
    if f['id']=='F3' and (t=='客房' or '服务器' in t):continue
    if w==2 and '通道'in t:
     for k,c in enumerate(t):p+=txt(tx,ty-35+k*23,c,18,'middle')
    else:p+=txt(tx,ty+6,t,15 if '服务器'in t else 16 if w<=1.5 else 19,'middle')
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
   if f['id']=='F3':
    p+=rect(18,285,35,70,'#dbe1e5','#87959d',1)+txt(35,305,'服务',11,'middle')+txt(35,324,'器架',11,'middle')+txt(78,407,'服务器房',15,'middle')
    p+=rect(260,208,85,55,'#e5e9df','#9ca98f',1)+txt(302,240,'30kWh储能',13,'middle')
    p+=rect(375,208,65,55,'#e1e6ea','#94a0a7',1)+txt(407,240,'逆变/配电',12,'middle')
    p+=txt(360,389,'独立检修与通风空间',14,'middle')
   if f['id']=='ROOF':
    p+=f'<circle cx="450" cy="58" r="16" fill="#dae4dc" stroke="{GREEN}"/>'+path('M450 20 V90 M436 74 H464',GREEN)+txt(423,110,'X50N屋顶天线',15,'end')+path('M450 90 H488 V450',GREEN,1.5,extra='stroke-dasharray="5 5"')
    for r in range(4):
     for c in range(3):p+=rect(250+c*70,153+r*66,62,57,'none','#8b9990',1)
  p+='</g>'+txt(55,620,f['note'],15)
  panels.append(f'<g transform="translate({x},{y})">{p}</g>')
 body=txt(55,55,'安全屋户型与院落细化 · V0.4',30)+txt(55,90,'三层服务器房 / 电力储存设备间｜二层保留日常书房与通信桌',18)+''.join(panels)+txt(55,2070,'北向上；地上约110㎡/层；院落15×17m用地预算，图示比例与楼层不同。绿线为设备/出入路径。',16)
 render('SAFEHOUSE_PLAN',wrap(1400,2090,body))
 render('SAFEHOUSE_THIRD_FLOOR',wrap(690,650,panels[3].replace('translate(715,765)','translate(0,0)',1)))
def townmap():
 from town_map import render_town
 render_town(OUT)

if __name__=='__main__':
 OUT.mkdir(parents=True,exist_ok=True)
 floorplan();townmap()
 from furnished_house import main as render_furnished
 render_furnished()
 print('Rendered safehouse V0.4 and town V0.3.')

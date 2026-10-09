"""Detailed, editable furniture plans for ApocalypseGame; draft dimensions only."""
from pathlib import Path
import json, html, math
import cairosvg
from PIL import Image
OUT=Path(__file__).resolve().parents[1]/'docs/chapters/ch01/assets'
U=88; C={'paper':'#f7f6f2','wall':'#606865','ink':'#35403c','wood':'#e6dcc9','fabric':'#d3dfdd','metal':'#cfd9df','battery':'#dbe3d3','line':'#9ba7a2'}
def text(x,y,t,n=16,color=None,anchor='start'):
 return f'<text x="{x}" y="{y}" font-family="Arial Unicode MS, sans-serif" font-size="{n}" fill="{color or C["ink"]}" text-anchor="{anchor}">{html.escape(t)}</text>'
def rect(x,y,w,h,fill='none',stroke=None,sw=1,rx=0):return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" stroke="{stroke or C["line"]}" stroke-width="{sw}"/>'
def path(d,color=None,width=1,extra=''):return f'<path d="{d}" fill="none" stroke="{color or C["line"]}" stroke-width="{width}" stroke-linecap="round" stroke-linejoin="round" {extra}/>'
def circle(x,y,r,fill='none',stroke=None,sw=1):return f'<circle cx="{x}" cy="{y}" r="{r}" fill="{fill}" stroke="{stroke or C["line"]}" stroke-width="{sw}"/>'
def obj(kind,x,y,w,h):
 x*=U;y*=U;w*=U;h*=U
 fill=C['wood']if kind in ['shelf','wardrobe','table','desk','vdesk','console']else C['fabric']if kind in ['bed','sofa','chair']else C['metal']
 a=rect(x+2,y+3,w,h,'#e4e7e2','none',0,3)+rect(x,y,w,h,fill,sw=1.2,rx=3)
 if kind=='bed':
  a+=rect(x+5,y+5,w-10,h*.72,'#faf9f4',sw=.8,rx=3)
  for px in [x+8,x+w/2+3]:a+=rect(px,y+8,w/2-13,18,'#f4f2e9',sw=.8,rx=4)
  a+=rect(x+5,y+h*.63,w-10,h*.29,'#c9d7d2','none',0,2)+path(f'M{x+8} {y+h*.75} H{x+w-8}',width=.7)
 elif kind=='sofa':
  a+=rect(x+5,y+8,w-10,h-16,'#e7eeeb',sw=.8,rx=3)
  for yy in [y+h/3,y+2*h/3]:a+=path(f'M{x+5} {yy} H{x+w-5}',width=.8)
  a+=rect(x,y+7,8,h-14,'#bccdca',sw=.8,rx=2)
 elif kind=='table':a+=rect(x+5,y+5,w-10,h-10,'none',sw=.6,rx=3)
 elif kind=='chair':a+=circle(x+w/2,y+h/2,min(w,h)*.36,'#e5ece8',sw=.7)
 elif kind in ['desk','vdesk']:
  if kind=='desk':
   a+=rect(x+w*.30,y+5,w*.34,11,'#7d969d','none',0,2)+path(f'M{x+w*.47} {y+16} V{y+23}',width=1.4)+rect(x+w*.30,y+h*.59,w*.34,8,'#f5f5f0',sw=.6)+circle(x+w*.74,y+h*.67,3,'#7d969d',sw=.5)
  else:a+=rect(x+w-15,y+h*.25,10,h*.3,'#7d969d','none',0,2)+rect(x+8,y+h*.27,7,h*.25,'#f5f5f0',sw=.6)
 elif kind in ['rack','battery']:
  a+=rect(x+6,y+5,w-12,h-10,'#e6ecee'if kind=='rack'else '#eef2e9',sw=.8)
  for yy in [y+h*.3,y+h*.5,y+h*.7]:a+=path(f'M{x+9} {yy} H{x+w-9}',width=.8)
  a+=rect(x+w-8,y+h*.4,3,h*.17,'#829497','none',0)
 elif kind in ['shelf','wardrobe','counter','console','cabinet']:
  for xx in [x+w/3,x+2*w/3]:a+=path(f'M{xx} {y+3} V{y+h-3}',width=.7)
  if kind in ['wardrobe','cabinet']:a+=path(f'M{x+w/3+4} {y+h/2-4} V{y+h/2+4} M{x+2*w/3+4} {y+h/2-4} V{y+h/2+4}',width=1.2)
 elif kind=='double_sink':
  for bx in [x+6,x+w/2+3]:a+=rect(bx,y+7,w/2-9,h-13,'#eff4f3',sw=.8,rx=5)+circle(bx+w/4-4,y+h/2,2,'#839896',sw=.4)
 elif kind=='sink':a+=rect(x+6,y+7,w-12,h-13,'#eff4f3',sw=.8,rx=5)+circle(x+w/2,y+h/2,2,'#839896',sw=.4)
 elif kind=='wc':a+=rect(x+w*.2,y+4,w*.6,h*.25,'#f5f7f5',sw=.7,rx=2)+f'<ellipse cx="{x+w/2}" cy="{y+h*.64}" rx="{w*.3}" ry="{h*.27}" fill="#f9faf7" stroke="{C["line"]}" stroke-width=".8"/>'
 elif kind=='shower':a+=path(f'M{x+4} {y+4} L{x+w-4} {y+h-4} M{x+w-4} {y+4} L{x+4} {y+h-4}',width=.6)+circle(x+w*.75,y+h*.75,3,'#879b9a',sw=.5)
 elif kind=='washer':a+=circle(x+w/2,y+h*.58,w*.32,'#e8eef0',sw=1)+rect(x+5,y+4,w-10,9,'#f2f4f2',sw=.5)
 elif kind=='hob':
  for dx,dy in [(.28,.28),(.72,.28),(.28,.72),(.72,.72)]:a+=circle(x+w*dx,y+h*dy,min(w,h)*.15,'#65706c',sw=.6)
 elif kind in ['radio','inverter','ac','dc','ups']:
  a+=rect(x+5,y+5,max(5,w*.38),max(5,h*.34),'#607e8a','none',0,2)
  for xx in range(int(x+5),int(x+w-3),7):a+=path(f'M{xx} {y+h*.75} V{y+h-5}',width=.7)
 return a

def O(kind,x,y,w,h,name):return {'kind':kind,'rect':[x,y,w,h],'name':name}
OBJECTS={
'B1':[O('shelf',5.3,.3,5.4,.5,'食品货架：罐头与轮换清单'),O('shelf',10.2,1.3,.5,2.35,'东侧食品架'),O('shelf',7.35,1.9,.65,1.5,'低层中央储物架'),O('shelf',5.3,4.45,3,.6,'瓶装水储架'),O('cabinet',9,4.45,1.45,.6,'卫生用品封闭柜'),O('cabinet',6.1,6.5,.8,.65,'水箱/周转箱外观草案'),O('cabinet',7.5,6.5,.8,.65,'备用物资周转箱'),O('table',.3,4.3,2.35,.65,'工具检修台'),O('shelf',.3,6.55,.5,1.3,'工具与零件架')],
'F1':[O('counter',5.3,.28,5.4,.65,'北侧厨房操作台'),O('double_sink',6.5,.37,1.15,.45,'双槽水盆（操作台内）'),O('hob',9.5,.37,.6,.48,'灶具（操作台内）'),O('counter',10.05,.95,.65,1.55,'东侧备餐台'),O('cabinet',5.35,2.65,.7,.75,'冰箱'),O('table',7.2,4.95,2,.95,'六人餐桌'),O('chair',6.62,5.15,.45,.45,'餐椅左'),O('chair',9.33,5.15,.45,.45,'餐椅右'),O('chair',7.48,4.38,.45,.45,'餐椅北一'),O('chair',8.38,4.38,.45,.45,'餐椅北二'),O('chair',7.48,6.04,.45,.45,'餐椅南一'),O('chair',8.38,6.04,.45,.45,'餐椅南二'),O('sofa',6.05,7.35,.9,2.5,'三人沙发，面向东侧电视'),O('table',7.5,8.05,1.15,.65,'客厅茶几'),O('console',10.45,7.5,.3,1.4,'电视与低柜'),O('console',10.35,4.7,.4,1.35,'餐边柜'),O('cabinet',5.15,9.1,.4,.75,'玄关鞋柜'),O('bed',.4,6.55,1.4,2,'临时客房床'),O('wardrobe',.35,9.3,1.5,.5,'临时客房衣柜'),O('wc',.4,4.25,.55,.65,'一层坐便器'),O('sink',1.3,4.25,.8,.45,'一层洗手盆')],
'F2':[O('bed',6.15,.55,1.8,2.05,'父母双人床'),O('cabinet',5.62,.65,.38,.38,'父母床头柜'),O('wardrobe',8.2,2.85,2.4,.55,'父母衣柜'),O('bed',6.15,4.05,1.8,2.05,'情侣双人床'),O('cabinet',5.62,4.15,.38,.38,'情侣床头柜'),O('wardrobe',8.2,6.35,2.4,.55,'情侣衣柜'),O('shower',.25,4.22,1.0,1.3,'独立淋浴区'),O('wc',1.92,4.3,.55,.7,'独立厕所'),O('double_sink',.3,6.1,2.4,.48,'公共外置双人洗手台'),O('washer',.35,7.85,.65,.65,'洗衣机'),O('sink',1.15,7.85,.8,.6,'洗衣水盆'),O('shelf',.35,9.5,2.2,.35,'洗衣用品与布草架'),O('desk',6.2,9.2,2,.6,'日常工作桌（非服务器）'),O('chair',6.92,8.56,.5,.5,'工作椅'),O('table',9.05,7.3,1.35,.7,'无线电通信桌'),O('radio',9.35,7.37,.45,.27,'FTM-6000R（通信桌内）'),O('chair',9.45,8.25,.5,.5,'通信桌座椅'),O('shelf',5.3,9.1,.35,.7,'书籍资料架')],
'F3':[O('bed',6.05,.6,1.8,2.05,'客房双人床'),O('wardrobe',8.3,3.25,2.3,.55,'客房衣柜'),O('desk',8.85,.6,1.3,.65,'客房小书桌'),O('chair',9.25,1.48,.5,.5,'客房座椅'),O('rack',.25,7.3,.65,.8,'家用服务器机架'),O('vdesk',2.2,6.3,.55,1.35,'服务器维护桌'),O('chair',1.45,6.65,.5,.5,'维护椅'),O('shelf',.3,9.35,1.55,.4,'线缆与备件柜'),O('battery',6.15,4.3,.85,.75,'储能柜A（与B合计30kWh）'),O('battery',7.6,4.3,.85,.75,'储能柜B（模组形态草案）'),O('dc',5.7,4.12,.32,.2,'直流隔离/保护盒（壁挂）'),O('inverter',9.1,4.12,.55,.25,'储能逆变器（壁挂）'),O('ac',9.85,4.12,.35,.2,'备用负载配电箱（壁挂）'),O('ac',10.4,4.12,.4,.2,'交流配电/保护箱（壁挂）'),O('table',6.2,9.2,1.65,.55,'金属检修台'),O('cabinet',10.0,7.6,.65,1.3,'专用工具金属柜'),O('wc',.4,4.25,.55,.65,'三层坐便器'),O('sink',1.3,4.25,.8,.45,'三层洗手盆')]
}
NESTED={'双槽水盆（操作台内）','灶具（操作台内）','FTM-6000R（通信桌内）'}
CAPTIONS={'B1':[(1.5,3.8,'楼梯'),(1.5,7.98,'工具区'),(8.7,3.77,'食品储藏'),(8.8,7.98,'饮水 / 用品')],'F1':[(1.5,3.8,'楼梯'),(1.5,5.8,'卫浴'),(1.5,9.03,'临时客房'),(8.2,3.1,'厨房'),(6.4,6.85,'餐厅'),(9.3,9.7,'客厅'),(4.0,7.5,'玄关')],'F2':[(1.5,3.8,'楼梯'),(9.3,2.25,'父母卧室'),(9.3,5.75,'情侣卧室'),(.75,5.75,'淋浴'),(2.25,5.75,'厕所'),(1.5,6.95,'洗手区'),(1.5,9.05,'洗衣 / 储物'),(8.0,8.55,'书房 / 通信')],'F3':[(1.5,3.8,'楼梯'),(9.3,2.6,'客房'),(1.5,5.8,'卫浴'),(1.5,8.8,'服务器房'),(8.3,7.6,'电力储存设备间')]}
DOORS={'B1':[(3,2.7,'E',.9),(3,6.3,'W',.9),(5,1.3,'E',.9),(5,6.1,'E',.9)],'F1':[(3,2.7,'E',.9),(3,5.2,'W',.9),(3,7.4,'W',.9),(4,10,'N',1.1),(11,3.15,'W',.9)],'F2':[(3,2.7,'E',.9),(3,8.8,'W',.9),(5,1.7,'E',.9),(5,5.2,'E',.9),(5,8.1,'E',.9),(.75,6,'SLIDE',.8),(2.25,6,'N',.8)],'F3':[(3,2.7,'E',.9),(3,5.2,'W',.9),(3,8.55,'W',.9),(5,1.7,'E',.9),(5,5.2,'E',.9)]}
WINDOWS={'B1':[(0,4.5,0,5.8)],'F1':[(6.8,0,9.6,0),(11,.45,11,1.2),(11,4.7,11,6.2),(6.9,10,9.5,10),(0,7.3,0,9.05)],'F2':[(6.8,0,9.6,0),(11,.65,11,2.55),(11,4.15,11,6.1),(6.9,10,9.5,10),(0,7.9,0,9.4)],'F3':[(6.8,0,9.6,0),(11,.65,11,2.55),(11,6.6,11,7.2),(0,6.5,0,7.0)]}

def render(name,body,w=1530,h=1260):
 svg=f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}"><rect width="100%" height="100%" fill="{C["paper"]}"/>{body}</svg>'
 (OUT/f'{name}.svg').write_text(svg);cairosvg.svg2png(bytestring=svg.encode(),write_to=str(OUT/f'{name}.png'))
def merge_walls(rooms):
 horizontal={};vertical={}
 for x,y,w,h,_ in rooms:
  for yy in [y,y+h]:horizontal.setdefault(round(yy,4),[]).append((x,x+w))
  for xx in [x,x+w]:vertical.setdefault(round(xx,4),[]).append((y,y+h))
 def merged(d):
  result=[]
  for key,intervals in d.items():
   ends=[]
   for a,b in sorted(intervals):
    if ends and a<=ends[-1][1]+.001:ends[-1]=(ends[-1][0],max(b,ends[-1][1]))
    else:ends.append((a,b))
   result.extend((key,a,b)for a,b in ends)
  return result
 return merged(horizontal),merged(vertical)
def door_draw(x,y,d,width):
 x*=U;y*=U;q=width*U
 if d=='SLIDE':return path(f'M{x-q/2} {y} H{x+q/2}',C['paper'],11)+path(f'M{x-q/2} {y-3} H{x+q*.12} M{x-q*.12} {y+3} H{x+q/2}',C['line'],1.3)
 if d in ['E','W']:
  sign=1 if d=='E'else -1
  a=path(f'M{x} {y-q/2} V{y+q/2}',C['paper'],11)
  a+=path(f'M{x} {y-q/2} h{sign*q}',C['wall'],1.8)+path(f'M{x+sign*q} {y-q/2} A{q} {q} 0 0 {1 if sign<0 else 0} {x} {y+q/2}',C['line'],1)
 else:
  a=path(f'M{x-q/2} {y} H{x+q/2}',C['paper'],11)+path(f'M{x-q/2} {y} v{-q}',C['wall'],1.8)+path(f'M{x-q/2} {y-q} A{q} {q} 0 0 1 {x+q/2} {y}',C['line'],1)
 return a

def floor_sheet(f):
 fid=f['id'];obs=OBJECTS[fid];height=f['h'];rooms=f['rooms'];title={'B1':'地下室｜储物与维护','F1':'一层｜开放起居与厨房','F2':'二层｜家庭卧室与通信','F3':'三层｜服务器房与储电配电'}[fid]
 b=text(60,55,'安全屋 · 家具与设备陈列',30)+text(60,89,title+'  /  精细草案 V0.5',20,color='#73837b')+text(1080,89,'北 ↑',17,anchor='end')
 plan=''
 for x,y,w,h,t in rooms:plan+=rect(x*U,y*U,w*U,h*U,'#f3f4ee'if '通道'in t else '#fafaf6','none',0)
 if fid=='F3':plan+=rect(6.0*U,5.2*U,2.7*U,1.2*U,'#edf2e6','none',0,6)+text(7.35*U,6.16*U,'储能柜前检修留空',14,'#81906f','middle')
 hs,vs=merge_walls(rooms)
 for y,x1,x2 in hs:plan+=path(f'M{x1*U} {y*U} H{x2*U}',C['wall'],7 if y in [0,height]else 5)
 for x,y1,y2 in vs:plan+=path(f'M{x*U} {y1*U} V{y2*U}',C['wall'],7 if x in [0,11]else 5)
 for x1,y1,x2,y2 in WINDOWS[fid]:plan+=path(f'M{x1*U} {y1*U} L{x2*U} {y2*U}',C['paper'],10)+path(f'M{x1*U} {y1*U} L{x2*U} {y2*U}','#83a6a3',3)
 for x,y,d,w in DOORS[fid]:plan+=door_draw(x,y,d,w)
 # 开口和滑门，保持公共区开放
 if fid=='F1':plan+=path(f'M{3.1*U} {4*U} H{4.9*U}',C['paper'],10)+path(f'M{7.2*U} {4*U} H{8.8*U}',C['paper'],10)+path(f'M{7.2*U} {4*U-4} H{8.1*U} M{7.9*U} {4*U+4} H{8.8*U}',C['line'],1.4)
 if fid=='F2':plan+=path(f'M{3*U} {6.15*U} V{7.3*U}',C['paper'],10)
 # U形楼梯，两跑踏步、休息平台、方向箭头
 plan+=rect(.22*U,.28*U,2.5*U,.52*U,'#e3e8e1',sw=.7)
 for k in range(10):
  yy=(.92+k*.25)*U;plan+=path(f'M{.3*U} {yy} H{1.24*U} M{1.72*U} {yy} H{2.65*U}',width=.8)
 plan+=path(f'M{1.46*U} {.9*U} V{3.45*U}',width=.7)+path(f'M{.78*U} {3.1*U} V{1.1*U} l-5 8 M{.78*U} {1.1*U} l5 8',C['wall'],1.2)
 for i,o in enumerate(obs,1):
  x,y,w,h=o['rect'];plan+=obj(o['kind'],x,y,w,h)
  plan+=circle((x+w)*U-5,y*U+6,10,'#fafaf7','#9cacaa',.8)+text((x+w)*U-5,y*U+10,str(i),10,anchor='middle')
 for x,y,t in CAPTIONS[fid]:plan+=text(x*U,y*U,t,18,color='#55645b',anchor='middle')
 plan+=path(f'M0 -25 H{11*U} M0 -30 V-20 M{11*U} -30 V-20',width=.8)+text(5.5*U,-35,'11 m 外包预算',14,anchor='middle')+text(11*U+18,height*U/2,f'{height} m',14)
 b+=f'<g transform="translate(72,152)">{plan}</g>'
 # 侧栏不把长文字挤进房间内
 b+=rect(1120,140,360,1060,'#ffffff','#e2e6df',1,12)+text(1143,179,'陈列索引',21)
 yy=216
 for i,o in enumerate(obs,1):
  b+=circle(1157,yy-5,10,'#f6f8f2','#9cacaa',.8)+text(1157,yy-1,str(i),10,anchor='middle')+text(1176,yy,o['name'],13)
  x,y,w,h=o['rect'];b+=text(1176,yy+20,f'{w:g} × {h:g} m 位置包络草案',11,color='#8b9690');yy+=42
 note={'B1':['食品、饮水与工具分区','图中容器不锁定初始数量','货架之间留通行与搬运位置'],'F1':['客厅 / 餐厅 / 玄关仍连通','厨房隔门与侧门避免柜体遮挡','玄关到楼梯不穿越家具'],'F2':['厕所与淋浴独立，洗手外置','工作桌与无线电桌分开','服务器已迁至三层'],'F3':['房名按用户要求：服务器房','两个储能柜合计仍为30kWh','壁挂逆变、保护与配电分开画','淡绿色为柜前检修留空示意']}[fid]
 yy=max(yy+18,1010)
 for t in note:b+=text(1143,yy,t,13,color='#71806f');yy+=23
 b+=text(65,1198,'浅色平面图为游戏空间与美术陈列草案；门窗、家具和设备尺寸可修改，不作为施工接线图。',14,color='#7d8981')+text(65,1228,'设备外观参考现实形态，品牌型号、承重、净面积、供电参数与安装间距待具体选型复核。',13,color='#8a958e')
 render('SAFEHOUSE_'+fid+'_DETAIL',b)
 return obs

def elevation_sheet():
 b=text(55,55,'三层设备 · 正面外观与功能分工',29)+text(55,89,'将上一版位置方框拆成具体设备；以下为外观初稿，不是接线施工图。',17,color='#77857e')
 b+=rect(45,122,1400,510,'#ffffff','#e0e5df',1,12)+text(75,160,'电力储存设备间 · 北侧设备墙',22)
 # 储能柜为两组模块化柜体，合计容量来自世界设定，不把某真实型号改成30。
 for x,label in [(100,'储能柜 A'),(340,'储能柜 B')]:
  b+=rect(x,218,175,310,'#d5dfd2','#8b9a86',1.5,6)+rect(x+12,230,151,281,'#edf2e9','#95a190',1,3)
  for j in range(4):
   yy=246+j*57;b+=rect(x+23,yy,129,43,'#dce6d7','#9fab99',.8,3)
   b+=rect(x+32,yy+10,44,11,'#748879','none',0,2)+circle(x+132,yy+17,3,'#69a17d','none',0)
   b+=path(f'M{x+95} {yy+30} H{x+139}',width=.7)
  b+=text(x+87,563,label,18,anchor='middle')
 b+=text(306,600,'A＋B合计：标称30kWh；模组数量与单体容量尚未定型',14,anchor='middle')
 # 不把所有电气功能塞进一个大柜
 for x,y,w,h,label,k in [(590,248,74,95,'直流保护','dc'),(715,218,158,204,'储能逆变器','inverter'),(960,235,157,156,'备用负载配电','ac'),(1202,240,153,146,'交流配电','ac')]:
  b+=rect(x,y,w,h,'#e2e8ea','#91a0a6',1.2,6)+rect(x+14,y+17,w-28,30,'#657f89','none',0,3)
  if k=='inverter':
   for j in range(7):b+=path(f'M{x+18} {y+110+j*9} H{x+w-18}','#a5b1b7',1)
  elif k=='dc':
   b+=circle(x+w/2,y+72,12,'#dca68c','#9f897a',.8)+path(f'M{x+w/2} {y+61} V{y+75}','#796b64',2)
  else:
   for j in range(3):b+=rect(x+18+j*(w-30)/3,y+67,(w-42)/3,27,'#f3f5f4','#91a0a6',.7,2)
  b+=text(x+w/2,y+h+35,label,16,anchor='middle')
 b+=text(989,559,'壁挂设备下方保留操作与检修空间',16,anchor='middle')+text(989,590,'电缆走向在独立线槽内表达，不绘裸露跨门电线',13,color='#849087',anchor='middle')
 # 服务器矮柜与维护桌
 b+=rect(45,658,1400,485,'#ffffff','#e0e5df',1,12)+text(75,700,'服务器房 · 家用机架与维护桌',22)
 b+=rect(115,760,225,282,'#cbd7de','#8c9da6',1.4,5)+rect(129,773,197,253,'#edf2f3','#9caab0',.8,3)
 for yy in [819,882,949]:b+=path(f'M130 {yy} H325','#8c9da6',2)
 b+=rect(178,793,44,17,'#bfcbd1','#8c9da6',1,4)+rect(236,792,17,20,'#d2dbdf','#8c9da6',.8,3)+text(410,810,'上层：Mac mini M4＋外接2TB存储',17)
 b+=rect(151,838,137,22,'#8d9ca4','#7c8a90',.7,2)+text(410,862,'中层：路由器、交换机与整理后的网线',17)
 b+=rect(154,910,103,33,'#d3dce0','#8c9da6',.7,3)+text(410,926,'下层：小型UPS与供电保护外观方案',17)
 b+=text(410,983,'不增加未确认的大型算力服务器或设备性能。',14,color='#829086')
 b+=rect(963,874,362,24,'#e5dccb','#b8ac96',1,3)+path('M985 899 V1055 M1304 899 V1055','#aaa994',5)
 b+=rect(1092,760,120,84,'#637d89','#637d89',1,5)+rect(1100,768,104,65,'#c5dce2','none',0,3)+path('M1152 844 V870','#637d89',4)+rect(1086,882,138,8,'#dfe7e4','#96a79f',.8,2)+rect(1097,941,93,18,'#c6d4ce','#96a79f',1,4)+rect(1097,968,93,33,'#dfe7e4','#96a79f',1,5)+path('M1108 1001 V1064 M1180 1001 V1064','#96a79f',3)
 b+=text(1144,1096,'维护桌：显示器、键盘与座椅',16,anchor='middle')
 b+=text(55,1185,'模块柜形态参考现实储能产品；厂商资料并未确认本游戏的30kWh整套组合。',14,color='#7d8981')
 b+=text(55,1216,'本页强调外观与功能分工；楼板承重、通风、防火分隔和电气设计仍为待核项目。',14,color='#7d8981')
 render('SAFEHOUSE_EQUIPMENT_ELEVATIONS',b,1490,1250)

def audit_objects(data):
 results=[]
 for f in data['floors']:
  fid=f['id']
  if fid not in OBJECTS:continue
  obs=OBJECTS[fid]
  for o in obs:
   x,y,w,h=o['rect'];assert x>=.1 and y>=.1 and x+w<=10.9 and y+h<=f['h']-.1+1e-6,(fid,o)
   assert any(x>=a-.001 and y>=b-.001 and x+w<=a+ww+.001 and y+h<=b+hh+.001 for a,b,ww,hh,_ in f['rooms']),('跨墙',fid,o)
  for i,a in enumerate(obs):
   if a['name']in NESTED:continue
   x,y,w,h=a['rect']
   for o in obs[i+1:]:
    if o['name']in NESTED:continue
    xx,yy,ww,hh=o['rect'];assert not(min(x+w,xx+ww)>max(x,xx)+.001 and min(y+h,yy+hh)>max(y,yy)+.001),('家具重叠',fid,a,o)
  # 实体家具不能侵入门扇的矩形运动包络；嵌在台面上的物件不单独算占地。
  for dx,dy,side,width in DOORS[fid]:
   if side=='SLIDE':continue
   if side=='W':swing=(dx-width,dy-width/2,width,width)
   elif side=='E':swing=(dx,dy-width/2,width,width)
   else:swing=(dx-width/2,dy-width,width,width)
   a,b,ww,hh=swing
   for o in obs:
    if o['name']in NESTED:continue
    x,y,w,h=o['rect'];assert not(min(a+ww,x+w)>max(a,x)+.01 and min(b+hh,y+h)>max(b,y)+.01),('门扇碰家具',fid,o,swing)
  results.append({'floor':fid,'objects':len(obs),'status':'边界、房间归属、实体家具重叠、门扇包络检查通过'})
 return results

def main():
 data=json.loads((OUT/'SAFEHOUSE_LAYOUT.json').read_text());data['version']='0.5'
 f3=next(f for f in data['floors']if f['id']=='F3')
 for r in f3['rooms']:
  if '服务器'in r[4]:r[4]='服务器房'
 data['equipment_locations']['server']='三层西南服务器房：Mac mini、外接存储、网络设备与维护桌'
 checks=audit_objects(data)
 (OUT/'SAFEHOUSE_LAYOUT.json').write_text(json.dumps(data,ensure_ascii=False,indent=2))
 inventory={'version':'0.5','status':'用户授权先画细节，外观与尺寸待审看','equipment_total_storage_kwh':30,'furniture':OBJECTS,'doors':DOORS,'windows':WINDOWS,'qa_pass_1':checks}
 (OUT/'SAFEHOUSE_FURNITURE.json').write_text(json.dumps(inventory,ensure_ascii=False,indent=2))
 for f in data['floors']:
  if f['id']in OBJECTS:floor_sheet(f)
 elevation_sheet()
 # 精细四层总览，保留单层大图，兼容已有主图链接。
 overview=text(45,45,'安全屋 · 精细陈列总览 V0.5',30)
 for i,fid in enumerate(['B1','F1','F2','F3']):
  source=(OUT/f'SAFEHOUSE_{fid}_DETAIL.svg').read_text()
  inner=source[source.index('>')+1:source.rindex('</svg>')]
  overview+=f'<svg x="{40+i%2*1080}" y="{85+i//2*1080}" width="1060" height="1060" viewBox="0 0 1100 1100">{inner}</svg>'
 render('SAFEHOUSE_PLAN',overview,2200,2260)
 for ext in ['svg','png']:(OUT/f'SAFEHOUSE_THIRD_FLOOR.{ext}').write_bytes((OUT/f'SAFEHOUSE_F3_DETAIL.{ext}').read_bytes())
 print(checks)
if __name__=='__main__':main()

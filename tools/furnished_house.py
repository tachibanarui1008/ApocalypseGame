"""Detailed, editable furniture plans for ApocalypseGame; draft dimensions only."""
from pathlib import Path
import json, html, math, re
from capacity_model import audit_capacity, calculate_capacity
OUT=Path(__file__).resolve().parents[1]/'docs/chapters/ch01/assets'
U=88; C={'paper':'#f7f6f2','wall':'#606865','ink':'#35403c','wood':'#e6dcc9','fabric':'#d3dfdd','metal':'#cfd9df','battery':'#dbe3d3','line':'#9ba7a2'}
def text(x,y,t,n=16,color=None,anchor='start'):
 return f'<text x="{x}" y="{y}" font-family="Arial Unicode MS, sans-serif" font-size="{n}" fill="{color or C["ink"]}" text-anchor="{anchor}">{html.escape(t)}</text>'
def rect(x,y,w,h,fill='none',stroke=None,sw=1,rx=0):return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" stroke="{stroke or C["line"]}" stroke-width="{sw}"/>'
def path(d,color=None,width=1,extra=''):return f'<path d="{d}" fill="none" stroke="{color or C["line"]}" stroke-width="{width}" stroke-linecap="round" stroke-linejoin="round" {extra}/>'
def circle(x,y,r,fill='none',stroke=None,sw=1):return f'<circle cx="{x}" cy="{y}" r="{r}" fill="{fill}" stroke="{stroke or C["line"]}" stroke-width="{sw}"/>'
def obj(kind,x,y,w,h,style=None,orientation='N',units=None,front=None):
 x*=U;y*=U;w*=U;h*=U
 fill=C['wood']if kind in ['shelf','wardrobe','table','desk','vdesk','console']else C['fabric']if kind in ['bed','sofa','chair']else C['metal']
 palettes={'parents':{'wood':'#cdbb9f','fabric':'#bfcdd7'},'couple':{'wood':'#e8ddc8','fabric':'#cadbce'},'guest':{'wood':'#e9e3d5','fabric':'#ddd8ca'},'office':{'wood':'#ddd2bf','fabric':'#c9d0d4'},'storage':{'wood':'#cbd6d0','fabric':'#dde5db'}}
 if style in palettes:fill=palettes[style]['wood' if kind in ['shelf','wardrobe','table','desk','vdesk','console','vanity'] else 'fabric']
 a=rect(x+2,y+3,w,h,'#e4e7e2','none',0,3)+rect(x,y,w,h,fill,sw=1.2,rx=3)
 if kind=='waterbarrel':a=''
 if kind=='bed':
  a+=rect(x+5,y+5,w-10,h-10,'#faf9f4',sw=.8,rx=3)
  throw={'parents':'#aabfce','couple':'#c6bcd8','guest':'#d2c9b9'}.get(style,'#c9d7d2')
  if orientation=='E':
   a+=rect(x+w-22,y+14,15,h-28,'#f4f2e9',sw=.8,rx=4)+rect(x+5,y+5,w*.32,h-10,throw,'none',0,2)
   a+=rect(x+2,y+h-14,w-4,12,'#b8aa93','none',0,3)+path(f'M{x+w*.18} {y+10} H{x+w*.34} M{x+w*.63} {y+10} H{x+w*.79}','#a4957d',2)
  else:
   py=y+8 if orientation=='N'else y+h-26
   for px in [x+8,x+w/2+3]:a+=rect(px,py,w/2-13,18,'#f4f2e9',sw=.8,rx=4)
   ty=y+h*.64 if orientation=='N'else y+5
   a+=rect(x+5,ty,w-10,h*.29,throw,'none',0,2)
 elif kind=='armchair':
  a+=rect(x+7,y+9,w-14,h-18,'#eff2ed',sw=.7,rx=5)
  if orientation=='E':a+=rect(x+3,y+4,9,h-8,'#b8c7be',sw=.5,rx=2)
  elif orientation=='W':a+=rect(x+w-12,y+4,9,h-8,'#b8c7be',sw=.5,rx=2)
  else:a+=rect(x+3,y+4,w-6,9,'#b8c7be',sw=.5,rx=2)
 elif kind=='vanity':
  a+=f'<ellipse cx="{x+w*.63}" cy="{y+8}" rx="{w*.22}" ry="5" fill="#dae7e8" stroke="#8d9da0" stroke-width="1"/>'+rect(x+9,y+h*.55,w*.3,h*.25,'#f5f0e6',sw=.6)
 elif kind=='waterbarrel':
  a+=circle(x+w/2,y+h/2,min(w,h)*.43,'#c4dbe0','#789ca6',1.4)+circle(x+w*.66,y+h*.33,4,'#eaf5f5','#789ca6',.6)
 elif kind=='boxbank':
  for j in range(max(1,round(w/32))):a+=rect(x+4+j*32,y+4,min(28,w-8-j*32),h-8,'#e4e2d7',sw=.6,rx=2)
 elif kind=='dehumidifier':
  a+=rect(x+5,y+5,w-10,10,'#f2f5f3',sw=.6)
  for yy in range(int(y+20),int(y+h-3),6):a+=path(f'M{x+5} {yy} H{x+w-5}',width=.6)
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
  for xx in ([x+w*j/units for j in range(1,units)] if units else [x+w/3,x+2*w/3]):a+=path(f'M{xx} {y+3} V{y+h-3}',width=.7)
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
 if kind=='battery'and front:
  yy=y+h+5 if front=='S'else y-5
  delta=6 if front=='S'else -6
  a+=f'<path d="M{x+w/2-5} {yy} L{x+w/2} {yy+delta} L{x+w/2+5} {yy} Z" fill="#7e9288"/>'
 return a

def O(kind,x,y,w,h,name,**props):return {'kind':kind,'rect':[x,y,w,h],'name':name,**props}
# Current V0.6 furniture only; old V0.5/30kWh objects remain in Git history.
OBJECTS = {
 'B1': [
  O('shelf', 5.3, 0.3, 5.1, 0.55, '北排食品架：6组四层架', units=6, style='storage'),
  O('shelf', 6.4, 1.8, 3.4, 0.55, '中央食品架：4组四层架', units=4, style='storage'),
  O('shelf', 5.3, 3.3, 5.1, 0.55, '南排食品架：6组四层架', units=6, style='storage'),
  O('shelf', 5.3, 4.3, 5.1, 0.55, '饮水罐/瓶水低架：6组', units=6, style='storage'),
  O('table', 0.3, 4.3, 2.35, 0.65, '工具检修台'),
  O('shelf', 0.3, 6.55, 0.5, 1.3, '工具零件架', style='storage'),
  O('dehumidifier', 2.25, 7.6, 0.45, 0.4, '移动除湿机备位，控湿效果待核'),
  O('waterbarrel', 6.05, 5.75, 0.6, 0.6, '饮烹水桶1：220L'),
  O('waterbarrel', 6.83, 5.75, 0.6, 0.6, '饮烹水桶2：220L'),
  O('waterbarrel', 7.61, 5.75, 0.6, 0.6, '饮烹水桶3：220L'),
  O('waterbarrel', 8.39, 5.75, 0.6, 0.6, '饮烹水桶4：220L'),
  O('waterbarrel', 9.17, 5.75, 0.6, 0.6, '饮烹水桶5：220L'),
  O('waterbarrel', 9.95, 5.75, 0.6, 0.6, '饮烹水桶6：220L'),
  O('waterbarrel', 6.05, 7.15, 0.6, 0.6, '生活水桶1：220L'),
  O('waterbarrel', 6.83, 7.15, 0.6, 0.6, '生活水桶2：220L'),
  O('waterbarrel', 7.61, 7.15, 0.6, 0.6, '生活水桶3：220L'),
  O('waterbarrel', 8.39, 7.15, 0.6, 0.6, '生活水桶4：220L'),
  O('waterbarrel', 9.17, 7.15, 0.6, 0.6, '生活水桶5：220L'),
  O('waterbarrel', 9.95, 7.15, 0.6, 0.6, '生活水桶6：220L'),
 ],
 'F1': [
  O('counter', 5.3, 0.28, 5.4, 0.65, '北侧厨房操作台'),
  O('double_sink', 6.5, 0.37, 1.15, 0.45, '双槽水盆（操作台内）'),
  O('hob', 9.5, 0.37, 0.6, 0.48, '灶具（操作台内）'),
  O('counter', 10.05, 0.95, 0.65, 1.55, '东侧备餐台'),
  O('cabinet', 5.35, 2.65, 0.7, 0.75, '冰箱'),
  O('table', 7.2, 4.95, 2, 0.95, '六人餐桌'),
  O('chair', 6.62, 5.15, 0.45, 0.45, '餐椅左'),
  O('chair', 9.33, 5.15, 0.45, 0.45, '餐椅右'),
  O('chair', 7.48, 4.38, 0.45, 0.45, '餐椅北一'),
  O('chair', 8.38, 4.38, 0.45, 0.45, '餐椅北二'),
  O('chair', 7.48, 6.04, 0.45, 0.45, '餐椅南一'),
  O('chair', 8.38, 6.04, 0.45, 0.45, '餐椅南二'),
  O('sofa', 6.05, 7.35, 0.9, 2.5, '三人沙发，面向东侧电视'),
  O('table', 7.5, 8.05, 1.15, 0.65, '客厅茶几'),
  O('console', 10.45, 7.5, 0.3, 1.4, '电视与低柜'),
  O('console', 10.35, 4.7, 0.4, 1.35, '餐边柜'),
  O('cabinet', 5.15, 9.1, 0.4, 0.75, '玄关鞋柜'),
  O('bed', 0.4, 6.55, 1.4, 2, '临时客房床'),
  O('wardrobe', 0.35, 9.3, 1.5, 0.5, '临时客房衣柜'),
  O('wc', 0.4, 4.25, 0.55, 0.65, '一层坐便器'),
  O('sink', 1.3, 4.25, 0.8, 0.45, '一层洗手盆'),
  O('boxbank', 10.35, 6.2, 0.4, 0.95, '客厅应急箱：6×60L，双列三层'),
  O('boxbank', 2.05, 8.85, 0.6, 0.9, '客房轻箱：4×60L，双列两层'),
  O('cabinet', 0.35, 6.2, 1.25, 0.25, '干燥医疗耗材柜：100L额度'),
 ],
 'F2': [
  O('bed', 7.4, 0.45, 1.8, 2.05, '父母北向双人床', style='parents'),
  O('cabinet', 6.85, 0.58, 0.42, 0.42, '父母左床头柜'),
  O('cabinet', 9.33, 0.58, 0.42, 0.42, '父母右床头柜'),
  O('wardrobe', 5.3, 2.8, 1.85, 0.55, '父母低调衣柜', style='parents', emergency_box_capacity_l=80),
  O('armchair', 10.0, 1.65, 0.6, 0.75, '父母窗边阅读椅', style='parents', orientation='W'),
  O('cabinet', 9.55, 2.85, 1.1, 0.4, '父母家庭药箱/日常低柜'),
  O('bed', 8.35, 4.4, 1.7, 2.05, '情侣南向双人床', style='couple', orientation='S'),
  O('cabinet', 7.8, 5.95, 0.4, 0.4, '情侣左床头柜'),
  O('cabinet', 10.2, 5.95, 0.4, 0.4, '情侣右床头柜'),
  O('wardrobe', 5.3, 3.8, 2.3, 0.55, '情侣浅木衣柜', style='couple', emergency_box_capacity_l=80),
  O('vanity', 6.05, 6.2, 1.5, 0.5, '梳妆兼阅读桌', style='couple'),
  O('chair', 6.55, 5.55, 0.5, 0.5, '梳妆阅读椅', style='couple'),
  O('shower', 0.25, 4.22, 1.0, 1.3, '独立淋浴区'),
  O('wc', 1.92, 4.3, 0.55, 0.7, '独立厕所'),
  O('double_sink', 0.3, 6.1, 2.4, 0.48, '公共外置双人洗手台'),
  O('washer', 0.35, 7.85, 0.65, 0.65, '洗衣机'),
  O('sink', 1.15, 7.85, 0.8, 0.6, '洗衣水盆'),
  O('shelf', 0.35, 9.5, 2.2, 0.35, '洗衣用品与布草架'),
  O('desk', 6.2, 9.2, 2, 0.6, '日常工作桌（非服务器）'),
  O('chair', 6.92, 8.56, 0.5, 0.5, '工作椅'),
  O('table', 9.05, 7.3, 1.35, 0.7, '无线电通信桌'),
  O('radio', 9.35, 7.37, 0.45, 0.27, 'FTM-6000R（通信桌内）'),
  O('chair', 9.45, 8.25, 0.5, 0.5, '通信桌座椅'),
  O('shelf', 5.3, 9.1, 0.35, 0.7, '书籍资料架'),
 ],
 'F3': [
  O('bed', 8.45, 2.3, 2.05, 1.35, '抽屉日床：东西向', style='guest', orientation='E', emergency_box_capacity_l=80),
  O('desk', 9.15, 0.4, 1.45, 0.6, '客房小书桌', style='guest'),
  O('chair', 9.65, 1.2, 0.5, 0.5, '客房座椅', style='guest'),
  O('wardrobe', 5.3, 3.15, 1.7, 0.5, '客房行李/衣柜', style='guest'),
  O('armchair', 6.55, 0.55, 0.65, 0.75, '客房阅读椅', style='guest'),
  O('table', 7.35, 0.8, 0.4, 0.4, '客房边几', style='guest'),
  O('desk', 0.35, 6.3, 1.85, 0.7, '服务器房正式办公桌', style='office'),
  O('chair', 0.95, 7.25, 0.55, 0.55, '办公椅', style='office'),
  O('rack', 0.28, 7.95, 0.65, 0.8, '家用机架：Mac mini/网络/UPS'),
  O('shelf', 2.42, 7.05, 0.32, 1.0, '办公室书架与备件'),
  O('armchair', 0.28, 9.02, 0.7, 0.55, '服务器房阅读椅', style='office', orientation='E'),
  O('table', 1.15, 9.08, 0.4, 0.4, '阅读边几', style='office'),
  O('wc', 0.4, 4.25, 0.55, 0.65, '三层坐便器'),
  O('sink', 1.3, 4.25, 0.8, 0.45, '三层洗手盆'),
  O('battery', 6.05, 4.55, 0.6, 0.8, '储能柜1：5×5.12kWh', front='S'),
  O('battery', 7.2, 4.55, 0.6, 0.8, '储能柜2：5×5.12kWh', front='S'),
  O('battery', 8.35, 4.55, 0.6, 0.8, '储能柜3：5×5.12kWh', front='S'),
  O('battery', 9.5, 4.55, 0.6, 0.8, '储能柜4：5×5.12kWh', front='S'),
  O('battery', 6.05, 6.75, 0.6, 0.8, '储能柜5：5×5.12kWh', front='N'),
  O('battery', 7.2, 6.75, 0.6, 0.8, '储能柜6：5×5.12kWh', front='N'),
  O('battery', 8.35, 6.75, 0.6, 0.8, '储能柜7：5×5.12kWh', front='N'),
  O('battery', 9.5, 6.75, 0.6, 0.8, '储能柜8：5×5.12kWh', front='N'),
  O('battery', 6.05, 8.95, 0.6, 0.8, '储能柜9：5×5.12kWh', front='N'),
  O('battery', 7.2, 8.95, 0.6, 0.8, '储能柜10：5×5.12kWh', front='N'),
  O('battery', 8.35, 8.95, 0.6, 0.8, '储能柜11：5×5.12kWh', front='N'),
  O('battery', 9.5, 8.95, 0.6, 0.8, '储能柜12：5×5.12kWh', front='N'),
  O('dc', 5.7, 4.12, 0.32, 0.2, '直流隔离/保护盒（壁挂）'),
  O('inverter', 9.1, 4.12, 0.422, 0.254, '12kW三相储能逆变器'),
  O('ac', 9.85, 4.12, 0.35, 0.2, '备用负载配电箱（壁挂）'),
  O('ac', 10.4, 4.12, 0.4, 0.2, '交流配电/保护箱（壁挂）'),
 ],
}
NESTED={'双槽水盆（操作台内）','灶具（操作台内）','FTM-6000R（通信桌内）'}
CAPTIONS={'B1':[(1.5,3.8,'楼梯'),(1.5,7.98,'工具区'),(8.7,3.77,'食品储藏'),(8.8,7.98,'饮水 / 用品')],'F1':[(1.5,3.8,'楼梯'),(1.5,5.8,'卫浴'),(1.5,9.03,'临时客房'),(8.2,3.1,'厨房'),(6.4,6.85,'餐厅'),(9.3,9.7,'客厅'),(4.0,7.5,'玄关')],'F2':[(1.5,3.8,'楼梯'),(9.3,2.25,'父母卧室'),(9.3,5.75,'情侣卧室'),(.75,5.75,'淋浴'),(2.25,5.75,'厕所'),(1.5,6.95,'洗手区'),(1.5,9.05,'洗衣 / 储物'),(8.0,8.55,'书房 / 通信')],'F3':[(1.5,3.8,'楼梯'),(9.3,2.6,'客房'),(1.5,5.8,'卫浴'),(1.5,8.8,'服务器房'),(8.3,7.6,'电力储存设备间')]}
DOORS={'B1':[(3,2.7,'E',.9),(3,6.3,'W',.9),(5,1.3,'E',.9),(5,6.1,'E',.9)],'F1':[(3,2.7,'E',.9),(3,5.2,'W',.9),(3,7.4,'W',.9),(4,10,'N',1.1),(11,3.15,'W',.9)],'F2':[(3,2.7,'E',.9),(3,8.8,'W',.9),(5,1.7,'E',.9),(5,5.2,'E',.9),(5,8.1,'E',.9),(.75,6,'SLIDE',.8),(2.25,6,'N',.8)],'F3':[(3,2.7,'E',.9),(3,5.2,'W',.9),(3,8.55,'W',.9),(5,1.7,'E',.9),(5,5.2,'E',.9)]}
WINDOWS={'B1':[(0,4.5,0,5.8)],'F1':[(6.8,0,9.6,0),(11,.45,11,1.2),(11,4.7,11,6.2),(6.9,10,9.5,10),(0,7.3,0,9.05)],'F2':[(6.8,0,9.6,0),(11,.65,11,2.55),(11,4.15,11,6.1),(6.9,10,9.5,10),(0,7.9,0,9.4)],'F3':[(6.8,0,9.6,0),(11,.65,11,2.55),(11,6.6,11,7.2),(0,6.5,0,7.0)]}

CAPTIONS['B1']=[(1.5,3.8,'楼梯'),(1.5,7.98,'工具与除湿'),(8.7,2.93,'食品区'),(5.6,7.9,'储水区')]
CAPTIONS['F2']=[(1.5,3.8,'楼梯'),(8.15,3.0,'父母卧室'),(8.8,3.73,'情侣卧室'),(.75,5.75,'淋浴'),(2.25,5.75,'厕所'),(1.5,6.95,'洗手区'),(1.5,9.05,'洗衣 / 储物'),(8.0,8.55,'书房 / 通信')]
CAPTIONS['F3']=[(1.5,3.8,'楼梯'),(8.1,1.95,'客房 · 日床'),(1.5,5.8,'卫浴'),(1.5,9.88,'服务器房 · 办公/阅读'),(5.56,9.75,'储电配电')]
def render(name,body,w=1530,h=1260):
 import cairosvg
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
 fid=f['id'];obs=OBJECTS[fid];height=f['h'];rooms=f['rooms'];step=34 if len(obs)>23 else 42;page_h=max(1260,216+len(obs)*step+100);title={'B1':'地下室｜储物与维护','F1':'一层｜开放起居与厨房','F2':'二层｜家庭卧室与通信','F3':'三层｜服务器房与储电配电'}[fid]
 b=text(60,55,'安全屋 · 家具与设备陈列',30)+text(60,89,title+'  /  扩容与差异设计 V0.6',20,color='#73837b')+text(1080,89,'北 ↑',17,anchor='end')
 plan=''
 for x,y,w,h,t in rooms:plan+=rect(x*U,y*U,w*U,h*U,'#f3f4ee'if '通道'in t else '#fafaf6','none',0)
 if fid=='F3':
  for yy in [5.4,7.6]:plan+=rect(6*U,yy*U,4.2*U,1.2*U,'#edf2e6','none',0,6)+text(8.1*U,(yy+.72)*U,'排间操作 / 检修通道',13,'#81906f','middle')
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
  x,y,w,h=o['rect'];plan+=obj(o['kind'],x,y,w,h,o.get('style'),o.get('orientation','N'),o.get('units'),o.get('front'))
  plan+=circle((x+w)*U-5,y*U+6,10,'#fafaf7','#9cacaa',.8)+text((x+w)*U-5,y*U+10,str(i),10,anchor='middle')
 for x,y,t in CAPTIONS[fid]:plan+=text(x*U,y*U,t,18,color='#55645b',anchor='middle')
 plan+=path(f'M0 -25 H{11*U} M0 -30 V-20 M{11*U} -30 V-20',width=.8)+text(5.5*U,-35,'11 m 外包预算',14,anchor='middle')+text(11*U+18,height*U/2,f'{height} m',14)
 b+=f'<g transform="translate(72,152)">{plan}</g>'
 # 侧栏不把长文字挤进房间内
 b+=rect(1120,140,360,page_h-180,'#ffffff','#e2e6df',1,12)+text(1143,179,'陈列索引',21)
 yy=216
 step=34 if len(obs)>23 else 42
 for i,o in enumerate(obs,1):
  b+=circle(1157,yy-5,10,'#f6f8f2','#9cacaa',.8)+text(1157,yy-1,str(i),10,anchor='middle')+text(1176,yy,o['name'],13)
  x,y,w,h=o['rect'];b+=text(1176,yy+20,f'{w:g} × {h:g} m 位置包络草案',11,color='#8b9690');yy+=step
 note={'B1':['食品、饮水与工具分区','图中容器不锁定初始数量','货架之间留通行与搬运位置'],'F1':['客厅 / 餐厅 / 玄关仍连通','厨房隔门与侧门避免柜体遮挡','玄关到楼梯不穿越家具'],'F2':['厕所与淋浴独立，洗手外置','工作桌与无线电桌分开','服务器已迁至三层'],'F3':['服务器房兼办公和阅读，机架维护留空','12柜×5模块：307.2kWh目标，承重待核','壁挂逆变、保护与配电分开画','△标柜门朝向；淡绿色为检修通道']}[fid]
 yy=1090
 for t in note:b+=text(70,yy,t,13,color='#71806f');yy+=23
 b+=text(65,page_h-62,'浅色平面图为游戏空间与美术陈列草案；门窗、家具和设备尺寸可修改，不作为施工接线图。',14,color='#7d8981')+text(65,page_h-32,'设备外观参考现实形态，品牌型号、承重、净面积、供电参数与安装间距待具体选型复核。',13,color='#8a958e')
 render('SAFEHOUSE_'+fid+'_DETAIL',b,1530,page_h)
 return obs

def elevation_sheet():
 b=text(55,55,'高密度储能与日常办公 · V0.6',29)+text(55,88,'容量307.2kWh目标｜额定逆变输出12kW｜工程与满载库存仍待核',18,color='#77857e')
 b+=rect(45,122,1400,752,'#ffffff','#e0e5df',1,12)+text(75,160,'12柜 × 每柜5模块 × 5.12kWh',23)
 for i in range(12):
  xx=85+i%4*155;yy=193+i//4*205
  b+=rect(xx,yy,120,164,'#d5dfd2','#8b9a86',1,4)+rect(xx+8,yy+8,104,145,'#edf2e9','#95a190',.8,2)
  for j in range(5):
   my=yy+15+j*26;b+=rect(xx+14,my,92,21,'#dce6d7','#9fab99',.7,2)+rect(xx+22,my+4,25,6,'#718778','none',0,1)+circle(xx+98,my+8,2,'#69a17d','none',0)
  b+=text(xx+60,yy+188,f'柜{i+1} · 25.6kWh',13,anchor='middle')
 b+=text(420,851,'合计60模块；电池2700kg，整套约3.2～3.5t，三层承重未验证',14,anchor='middle')
 for x,y,w,h,label,k in [(810,218,130,175,'12kW混合逆变器','inverter'),(1050,235,100,110,'直流保护','dc'),(810,490,140,150,'备用负载配电','ac'),(1080,490,140,150,'交流配电','ac')]:
  b+=rect(x,y,w,h,'#e2e8ea','#91a0a6',1.2,5)+rect(x+12,y+15,w-24,26,'#657f89','none',0,3)
  if k=='dc':b+=circle(x+w/2,y+72,12,'#dca68c','#9f897a',.8)
  elif k=='inverter':
   for j in range(7):b+=path(f'M{x+14} {y+80+j*8} H{x+w-14}','#a5b1b7',1)
  else:
   for j in range(3):b+=rect(x+14+j*(w-25)/3,y+58,(w-38)/3,25,'#f3f5f4','#91a0a6',.7,2)
  b+=text(x+w/2,y+h+32,label,16,anchor='middle')
 b+=text(1020,766,'排间保留操作与维护路径',17,anchor='middle')+text(1020,797,'增加容量不增加逆变器额定输出',14,color='#849087',anchor='middle')
 b+=rect(45,900,1400,385,'#ffffff','#e0e5df',1,12)+text(75,940,'服务器房 · 工作 / 阅读 / 设备',23)
 b+=rect(100,982,185,220,'#cbd7de','#8c9da6',1.3,4)
 for yy in [1040,1110,1174]:b+=path(f'M112 {yy} H273','#8c9da6',1.5)
 b+=rect(164,1009,38,14,'#bfcbd1','#8c9da6',.8,3)+rect(218,1007,16,20,'#d2dbdf','#8c9da6',.8,2)
 b+=rect(129,1066,126,22,'#8d9ca4','#7c8a90',.7,2)+rect(135,1130,83,31,'#d3dce0','#8c9da6',.7,3)
 b+=text(95,1239,'M4 / 外接盘 / 网络 / 小UPS',14)
 b+=rect(365,1085,455,25,'#ddd2bf','#afa28d',1,3)+path('M393 1110 V1228 M795 1110 V1228','#aaa994',4)
 b+=rect(515,984,130,83,'#637d89','#637d89',1,5)+rect(523,992,114,66,'#c5dce2','none',0,3)+path('M580 1067 V1080','#637d89',3)+rect(509,1091,145,9,'#dfe7e4','#96a79f',.8,2)
 b+=text(594,1253,'正式办公桌，不只是维护台',15,anchor='middle')
 b+=rect(927,976,150,241,'#e0d5c0','#b3a68f',1,3)
 for yy in [1028,1090,1152]:b+=path(f'M937 {yy} H1067','#a99b84',1)
 for j in range(8):b+=rect(940+j*14,990,9,35,'#b7c7bf','#9caea1',.5)
 b+=rect(1150,1054,140,116,'#c6d0cf','#98aaa4',1,10)+rect(1164,1068,112,80,'#e4ece6','#98aaa4',.6,8)
 b+=text(1110,1253,'书架与阅读角',15,anchor='middle')
 b+=text(55,1324,'扩容目标可调整；柜体、并联分组、三相接入、楼板集中荷载与散热分隔均需进一步核验。',14,color='#7d8981')
 render('SAFEHOUSE_EQUIPMENT_ELEVATIONS',b,1490,1360)

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

def sync_layout_notes(data,capacity):
 """Update descriptions only; never reconstruct saved room coordinates."""
 battery=capacity['battery']
 f3=next(f for f in data['floors']if f['id']=='F3')
 for r in f3['rooms']:
  if '服务器'in r[4]:r[4]='服务器房'
 f3['note']=f"服务器与电力分室；{battery['cabinets']}柜{battery['modules']}模块、{battery['nominal_kwh']:g}kWh储能目标与{battery['rated_inverter_output_kw']:g}kW逆变输出，结构及组配待核"
 data['equipment_locations']['server']='三层西南服务器房：办公桌、阅读角、书架与Mac mini家用机架'
 data['equipment_locations']['power']=f"三层储电配电密排目标：{battery['cabinets']}柜{battery['modules']}模块{battery['nominal_kwh']:g}kWh、{battery['rated_inverter_output_kw']:g}kW逆变器；结构与组配仍待核"
 data['capacity_reference']='SAFEHOUSE_CAPACITY.json'

def capacity_inventory_check(capacity):
 """Check drawn quantities against the scenario, not only numeric totals."""
 audit_capacity(capacity)
 battery,water,food=(capacity[k]for k in ['battery','water','food'])
 total=sum(len(objects)for objects in OBJECTS.values())
 cabinets=[o for o in OBJECTS['F3']if o['kind']=='battery']
 barrels=[o for o in OBJECTS['B1']if o['kind']=='waterbarrel']
 racks=sum(o.get('units',1)for o in OBJECTS['B1']if '食品架'in o['name'])
 assert len(cabinets)==battery['cabinets'],('储能柜数量与容量数据不一致',len(cabinets),battery['cabinets'])
 for o in cabinets:
  assert o['rect'][2:]==battery['cabinet_envelope_m'][:2],('储能柜包络不一致',o)
  assert f"{battery['modules_per_cabinet']}×{battery['module_kwh']:g}kWh"in o['name'],('储能模块标注不一致',o)
 assert racks==food['basement_racks'],('食品架数量不一致',racks,food['basement_racks'])
 assert len(barrels)==water['drinking_cooking_barrels']+water['nonpotable_living_barrels']
 assert sum('饮烹水'in o['name']for o in barrels)==water['drinking_cooking_barrels']
 assert sum('生活水'in o['name']for o in barrels)==water['nonpotable_living_barrels']
 assert all(f"{water['barrel_l']}L"in o['name']for o in barrels)
 boxed_l=sum(int(a)*int(b)for o in OBJECTS['F1']for a,b in re.findall(r'(\d+)×(\d+)L',o['name']))
 furniture_l=sum(o.get('emergency_box_capacity_l',0)for objects in OBJECTS.values()for o in objects)
 assert boxed_l+furniture_l==capacity['upper_storage']['upper_nominal_box_l']
 return {'version':capacity['version'],'status':f'{total}项陈列；{racks}食品架、{len(barrels)}水桶、{len(cabinets)}储能柜与数据对应；容量/质量/光伏投影/分类储水/热量复算通过','structural_approval':False,'initial_inventory_fixed':False}

def check_current_assets():
 """Read-only preflight: a newer saved scenario must not be silently reset."""
 data=json.loads((OUT/'SAFEHOUSE_LAYOUT.json').read_text())
 capacity=json.loads((OUT/'SAFEHOUSE_CAPACITY.json').read_text())
 expected=calculate_capacity()
 for key,value in expected.items():
  assert capacity.get(key)==value,('容量脚本与保存数据不一致；先同步配置再生成',key)
 previous=json.loads((OUT/'SAFEHOUSE_FURNITURE.json').read_text())
 assert previous['furniture']==OBJECTS,'当前家具数据与生成脚本不一致；先同步配置再生成'
 assert previous['doors']==json.loads(json.dumps(DOORS)),'当前门位与生成脚本不一致'
 assert previous['windows']==json.loads(json.dumps(WINDOWS)),'当前窗位与生成脚本不一致'
 return {'floors':audit_objects(data),'capacity':capacity_inventory_check(capacity)}

def build_inventory(data,capacity,previous=None):
 # Retain additional review notes, while recalculating every generated QA field.
 inventory=dict(previous or {})
 inventory.update({'version':data['version'],'status':'用户授权先画细节，外观与尺寸待审看','equipment_total_storage_kwh':capacity['battery']['nominal_kwh'],'furniture':OBJECTS,'doors':DOORS,'windows':WINDOWS,'qa_pass_1':audit_objects(data),'qa_capacity':capacity_inventory_check(capacity)})
 return inventory

def main():
 check_current_assets()
 data=json.loads((OUT/'SAFEHOUSE_LAYOUT.json').read_text())
 capacity=json.loads((OUT/'SAFEHOUSE_CAPACITY.json').read_text())
 previous=json.loads((OUT/'SAFEHOUSE_FURNITURE.json').read_text())
 sync_layout_notes(data,capacity)
 checks=audit_objects(data)
 (OUT/'SAFEHOUSE_LAYOUT.json').write_text(json.dumps(data,ensure_ascii=False,indent=2))
 inventory=build_inventory(data,capacity,previous)
 (OUT/'SAFEHOUSE_FURNITURE.json').write_text(json.dumps(inventory,ensure_ascii=False,indent=2))
 for f in data['floors']:
  if f['id']in OBJECTS:floor_sheet(f)
 elevation_sheet()
 # 精细四层总览，保留单层大图，兼容已有主图链接。
 overview=text(45,45,'安全屋 · 精细陈列总览 V0.6',30)
 for i,fid in enumerate(['B1','F1','F2','F3']):
  source=(OUT/f'SAFEHOUSE_{fid}_DETAIL.svg').read_text()
  inner=source[source.index('>')+1:source.rindex('</svg>')]
  overview+=f'<svg x="{40+i%2*1080}" y="{85+i//2*1080}" width="1060" height="1060" viewBox="0 0 1100 1100">{inner}</svg>'
 render('SAFEHOUSE_PLAN',overview,2200,2260)
 for ext in ['svg','png']:(OUT/f'SAFEHOUSE_THIRD_FLOOR.{ext}').write_bytes((OUT/f'SAFEHOUSE_F3_DETAIL.{ext}').read_bytes())
 print(checks)
if __name__=='__main__':main()

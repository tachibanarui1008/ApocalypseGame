from pathlib import Path
import json,math
from furnished_house import OUT,text,rect,path,circle,render

def main():
 m=json.loads((OUT/'SAFEHOUSE_CAPACITY.json').read_text());p=m['pv'];u=105;body=text(60,55,'光伏功率与屋面布置 · V0.6',29)+text(60,89,'屋顶18块455W = 8.19kWp｜院内9块扩展目标 = 4.095kWp',18,color='#6e8278')
 plan=rect(0,0,6*u,7*u,'#e9ede8','#8fa098',2)
 width,height=p['roof_projected_array_m'];sx=(6-width)/2;sy=(7-height)/2;panel_h=1.134*math.cos(math.radians(30))
 for r in range(6):
  for c in range(3):
   x=(sx+c*(1.722+.02))*u;y=(sy+r*(panel_h+.02))*u;w=1.722*u;h=panel_h*u
   plan+=rect(x,y,w,h,'#c0d0dc','#6e8798',1,2)
   for k in range(1,7):plan+=path(f'M{x+k*w/7} {y+4} V{y+h-4}','#91a7b6',.7)
   for k in range(1,4):plan+=path(f'M{x+4} {y+k*h/4} H{x+w-4}','#91a7b6',.7)
   plan+=text(x+12,y+24,str(r*3+c+1),13,color='#556e80')
 plan+=text(3*u,-25,'坡面投影宽 6 m',15,anchor='middle')+text(6*u+15,3.5*u,'7 m',15)+text(3*u,7*u+35,'30°坡度草案；阵列投影约5.206 × 5.992 m',14,anchor='middle')
 body+=f'<g transform="translate(72,160)">{plan}</g>'
 body+=rect(800,145,640,965,'#ffffff','#e0e5df',1,12)+text(825,186,'屋顶阵列核算',24)
 for i,t in enumerate(['组件参考：隆基 LR5-54HTH-455M','单片1.722 × 1.134m，20.8kg','横放3列 × 6排，20mm缝隙','组件面积合计约35.15㎡','仅组件重量约374.4kg','8.19kWp不是每天固定发电量']):body+=text(827,228+i*37,t,17)
 body+=text(827,492,'有效日照情景（80%综合系数）',20)
 for i,(h,e)in enumerate(p['roof_generation_kwh_scenarios'].items()):body+=text(845,531+i*36,f'{h}小时 → 约{e:.2f}kWh/日',18)
 body+=text(827,674,'院内扩展棚 · 另计',22)+text(827,712,'9片 × 455W = 4.095kWp',18)+text(827,749,'扩展后总目标12.285kWp',18)+text(827,786,'需约18㎡组件面积及支撑/维护空间',17)+text(827,823,'位置拟在院落东南侧开放棚上',17)+text(827,860,'不占围墙外土地，不能与屋顶面积混算',17)
 body+=text(827,969,'安装完成状态、支架承载、抗风与遮挡',16,color='#7b8981')+text(827,1001,'均待后续确定，不画成已经验证的施工图。',16,color='#7b8981')
 body+=text(60,1190,'307.2kWh是储能目标，12kW是逆变输出，8.19kWp是屋顶装机；三者分别控制续航、瞬时负载与补能。',15,color='#738179')
 render('SAFEHOUSE_ROOF_DETAIL',body,1490,1240)
if __name__=='__main__':main()

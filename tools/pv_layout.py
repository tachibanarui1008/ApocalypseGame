"""Render the current PV scenario using saved capacity and roof dimensions."""
from pathlib import Path
import json,math
from capacity_model import audit_capacity
from furnished_house import OUT,text,rect,path,render

# Mass belongs to this specific reference module, not to every 455 W panel.
MODULE_MASS_REFERENCE_KG = {'LONGi LR5-54HTH-455M': 20.8}


def roof_details_body(model,layout):
 audit_capacity(model)
 pv=model['pv'];battery=model['battery'];u=105
 roof=next(f for f in layout['floors']if f['id']=='ROOF')
 _,_,roof_w,roof_h,_=next(r for r in roof['rooms']if r[4]=='南向光伏坡面')
 columns,rows=pv['roof_columns'],pv['roof_rows']
 module_w,module_h=pv['module_size_m'];gap=pv['gap_m']
 panel_h=module_h*math.cos(math.radians(pv['pitch_deg_draft']))
 width,height=pv['roof_projected_array_m'];sx=(roof_w-width)/2;sy=(roof_h-height)/2
 assert sx>=0 and sy>=0,'当前光伏阵列超出保存的屋面预算'
 body=text(60,55,f'光伏功率与屋面布置 · V{model["version"]}',29)+text(60,89,f'屋顶{pv["roof_count"]}块{pv["module_w"]}W = {pv["roof_kwp"]:g}kWp｜院内{pv["extension_count"]}块扩展目标 = {pv["extension_kwp"]:g}kWp',18,color='#6e8278')
 plan=rect(0,0,roof_w*u,roof_h*u,'#e9ede8','#8fa098',2)
 for row in range(rows):
  for col in range(columns):
   x=(sx+col*(module_w+gap))*u;y=(sy+row*(panel_h+gap))*u;w=module_w*u;h=panel_h*u
   plan+=rect(x,y,w,h,'#c0d0dc','#6e8798',1,2)
   for k in range(1,7):plan+=path(f'M{x+k*w/7} {y+4} V{y+h-4}','#91a7b6',.7)
   for k in range(1,4):plan+=path(f'M{x+4} {y+k*h/4} H{x+w-4}','#91a7b6',.7)
   plan+=text(x+12,y+24,str(row*columns+col+1),13,color='#556e80')
 plan+=text(roof_w*u/2,-25,f'坡面投影宽 {roof_w:g} m',15,anchor='middle')+text(roof_w*u+15,roof_h*u/2,f'{roof_h:g} m',15)+text(roof_w*u/2,roof_h*u+35,f'{pv["pitch_deg_draft"]:g}°坡度草案；阵列投影约{width:.3f} × {height:.3f} m',14,anchor='middle')
 body+=f'<g transform="translate(72,160)">{plan}</g>'
 body+=rect(800,145,640,965,'#ffffff','#e0e5df',1,12)+text(825,186,'屋顶阵列核算',24)
 mass=MODULE_MASS_REFERENCE_KG.get(pv['module_reference'])
 single_mass=f'，{mass:g}kg'if mass is not None else '，质量待核'
 total_mass=f'仅组件重量约{pv["roof_count"]*mass:g}kg'if mass is not None else '组件总重量待具体型号核算'
 notes=[f'组件参考：{pv["module_reference"]}',f'单片{module_w:g} × {module_h:g}m{single_mass}',f'横放{columns}列 × {rows}排，{gap*1000:g}mm缝隙',f'组件面积合计约{pv["roof_count"]*module_w*module_h:.2f}㎡',total_mass,f'{pv["roof_kwp"]:g}kWp不是每天固定发电量']
 for i,note in enumerate(notes):body+=text(827,228+i*37,note,17)
 body+=text(827,492,f'有效日照情景（{pv["system_factor_assumption"]:.0%}综合系数）',20)
 for i,(hours,energy)in enumerate(pv['roof_generation_kwh_scenarios'].items()):body+=text(845,531+i*36,f'{hours}小时 → 约{energy:.2f}kWh/日',18)
 body+=text(827,674,'院内扩展棚 · 另计',22)+text(827,712,f'{pv["extension_count"]}片 × {pv["module_w"]}W = {pv["extension_kwp"]:g}kWp',18)+text(827,749,f'扩展后总目标{pv["total_target_kwp"]:g}kWp',18)+text(827,786,f'约{pv["extension_count"]*module_w*module_h:.2f}㎡组件面积，支撑/维护另计',17)+text(827,823,'位置拟在院落东南侧开放棚上',17)+text(827,860,'不占围墙外土地，不能与屋顶面积混算',17)
 body+=text(827,969,'安装完成状态、支架承载、抗风与遮挡',16,color='#7b8981')+text(827,1001,'均待后续确定，不画成已经验证的施工图。',16,color='#7b8981')
 body+=text(60,1190,f'{battery["nominal_kwh"]:g}kWh是储能目标，{battery["rated_inverter_output_kw"]:g}kW是逆变输出，{pv["roof_kwp"]:g}kWp是屋顶装机；三者分别控制续航、瞬时负载与补能。',15,color='#738179')
 return body


def main():
 model=json.loads((OUT/'SAFEHOUSE_CAPACITY.json').read_text(encoding="utf-8"))
 layout=json.loads((OUT/'SAFEHOUSE_LAYOUT.json').read_text(encoding="utf-8"))
 render('SAFEHOUSE_ROOF_DETAIL',roof_details_body(model,layout),1490,1240)


if __name__=='__main__':main()

"""Scenario calculations: proposed limits are not initial inventory or engineering approval."""
from pathlib import Path
import json,math
OUT=Path(__file__).resolve().parents[1]/'docs/chapters/ch01/assets'
def calculate_capacity():
 """Return the current V0.6 scenario without writing or rendering anything."""
 battery={'module':'Deye SE-G5.1 Pro-B','module_kwh':5.12,'module_mass_kg':45,'cabinets':12,'modules_per_cabinet':5,'cabinet_mass_budget_kg':30,'cabinet_envelope_m':[.6,.8,1.2],'rated_inverter_output_kw':12,'usable_fraction_assumption':.9,'conversion_fraction_assumption':.92}
 battery['modules']=battery['cabinets']*battery['modules_per_cabinet'];battery['nominal_kwh']=battery['modules']*battery['module_kwh'];battery['ac_energy_scenario_kwh']=round(battery['nominal_kwh']*.9*.92,4);battery['battery_mass_kg']=battery['modules']*45;battery['battery_cabinet_mass_budget_kg']=battery['battery_mass_kg']+battery['cabinets']*30
 battery['no_generation_days_scenarios']={str(x):round(battery['ac_energy_scenario_kwh']/x,2)for x in [6,10,16]};battery['not_verified']=['三层结构集中荷载','超过32块后的厂商外部配置','并联分组与固件兼容','住宅三相接入','安装间距与通风分隔']
 pv={'module_reference':'LONGi LR5-54HTH-455M','module_w':455,'module_size_m':[1.722,1.134],'pitch_deg_draft':30,'roof_rows':6,'roof_columns':3,'gap_m':.02,'extension_count':9,'system_factor_assumption':.8}
 pv['roof_count']=pv['roof_rows']*pv['roof_columns'];pv['roof_kwp']=pv['roof_count']*(pv['module_w']/1000);pv['extension_kwp']=pv['extension_count']*(pv['module_w']/1000);pv['total_target_kwp']=(pv['roof_count']+pv['extension_count'])*(pv['module_w']/1000);pv['roof_projected_array_m']=[pv['roof_columns']*pv['module_size_m'][0]+(pv['roof_columns']-1)*pv['gap_m'],pv['roof_rows']*pv['module_size_m'][1]*math.cos(math.radians(pv['pitch_deg_draft']))+(pv['roof_rows']-1)*pv['gap_m']]
 pv['roof_generation_kwh_scenarios']={str(h):round(pv['roof_kwp']*h*.8,3)for h in [1.5,3,5]};pv['recharge_90pct_days_ideal_no_charging_loss_at_3sunhours_daily6kwh']=round(battery['nominal_kwh']*.9/(pv['roof_kwp']*3*.8-6),2)
 food={'basement_racks':16,'rack_m':[.85,.55,1.90],'shelves_per_rack':4,'effective_storage_height_m_assumption':1.6,'packing_fraction_assumption':.7,'basement_mass_cap_draft_kg':2000,'upper_house_light_food_cap_draft_kg':100}
 food['rack_footprint_m2']=food['basement_racks']*food['rack_m'][0]*food['rack_m'][1];food['shelf_surface_m2']=food['rack_footprint_m2']*food['shelves_per_rack'];food['packaged_volume_cap_m3']=round(food['rack_footprint_m2']*food['effective_storage_height_m_assumption']*food['packing_fraction_assumption'],4);food['whole_house_mass_cap_draft_kg']=food['basement_mass_cap_draft_kg']+food['upper_house_light_food_cap_draft_kg']
 water={'drinking_cooking_barrels':6,'nonpotable_living_barrels':6,'barrel_l':220,'drinking_jerrycans':24,'jerrycan_l':20,'bottled_cases':20,'case_l':12,'upper_floor_bottled_l':120}
 water['potable_container_cap_l']=water['drinking_cooking_barrels']*water['barrel_l']+water['drinking_jerrycans']*water['jerrycan_l']+water['bottled_cases']*water['case_l']+water['upper_floor_bottled_l'];water['living_container_cap_l']=water['nonpotable_living_barrels']*water['barrel_l'];water['all_container_cap_l']=water['potable_container_cap_l']+water['living_container_cap_l'];water['scenario_persons']=4
 potable_days=water['potable_container_cap_l']/(water['scenario_persons']*4);living_days=water['living_container_cap_l']/(water['scenario_persons']*8)
 water['days_at_4potable_8living']={'potable':potable_days,'living':living_days,'both':min(potable_days,living_days)}
 inventory=[('米面',150,3600),('豆类',20,3300),('油',10,8800),('混合罐头',80,1000),('饼干',20,4500),('奶粉',10,5000),('坚果',10,5800),('糖',5,4000)]
 example={'items':[{'name':n,'kg':m,'kcal_per_kg_assumption':c}for n,m,c in inventory],'total_mass_kg':sum(x[1]for x in inventory),'raw_kcal':sum(m*c for n,m,c in inventory),'loss_fraction_assumption':.1,'people':4,'kcal_person_day_assumption':2000}
 example['usable_kcal']=example['raw_kcal']*(1-example['loss_fraction_assumption']);example['caloric_equivalent_days']=example['usable_kcal']/(example['people']*example['kcal_person_day_assumption'])
 extra={'upper_nominal_box_l':6*60+4*60+6*40,'packing_fraction_assumption':.75,'upper_management_volume_cap_l':600,'light_food_allocation_l':300,'medical_consumables_allocation_l':160,'hygiene_and_misc_allocation_l':140,'medical_not_medicine_days':True}
 extra['box_usable_l']=extra['upper_nominal_box_l']*.75
 data={'version':'0.6','status':'授权扩容的设定目标与满载上限草案，不等于初始库存或结构安装证明','battery':battery,'pv':pv,'food':food,'water':water,'upper_storage':extra,'food_example':example}
 audit_capacity(data)
 return data

def audit_capacity(data):
 """Reject stale or mismatched derived values; this is not engineering approval."""
 b,p,f,w,e,x=(data[k]for k in ['battery','pv','food','water','food_example','upper_storage'])
 def equal(actual,expected):
  assert math.isclose(actual,expected,rel_tol=1e-9,abs_tol=1e-9),(actual,expected)
 equal(b['modules'],b['cabinets']*b['modules_per_cabinet'])
 assert b['modules']<=64
 equal(b['nominal_kwh'],b['modules']*b['module_kwh'])
 equal(b['ac_energy_scenario_kwh'],b['nominal_kwh']*b['usable_fraction_assumption']*b['conversion_fraction_assumption'])
 equal(b['battery_mass_kg'],b['modules']*b['module_mass_kg'])
 equal(b['battery_cabinet_mass_budget_kg'],b['battery_mass_kg']+b['cabinets']*b['cabinet_mass_budget_kg'])
 equal(p['roof_count'],p['roof_rows']*p['roof_columns'])
 equal(p['roof_kwp'],p['roof_count']*p['module_w']/1000)
 equal(p['extension_kwp'],p['extension_count']*p['module_w']/1000)
 equal(p['total_target_kwp'],p['roof_kwp']+p['extension_kwp'])
 for a,z in zip(p['roof_projected_array_m'],[p['roof_columns']*p['module_size_m'][0]+(p['roof_columns']-1)*p['gap_m'],p['roof_rows']*p['module_size_m'][1]*math.cos(math.radians(p['pitch_deg_draft']))+(p['roof_rows']-1)*p['gap_m']]):equal(a,z)
 assert p['roof_projected_array_m'][0]<5.4 and p['roof_projected_array_m'][1]<6.4
 for h,energy in p['roof_generation_kwh_scenarios'].items():equal(energy,p['roof_kwp']*float(h)*p['system_factor_assumption'])
 equal(f['rack_footprint_m2'],f['basement_racks']*f['rack_m'][0]*f['rack_m'][1])
 equal(f['shelf_surface_m2'],f['rack_footprint_m2']*f['shelves_per_rack'])
 equal(f['packaged_volume_cap_m3'],round(f['rack_footprint_m2']*f['effective_storage_height_m_assumption']*f['packing_fraction_assumption'],4))
 equal(f['whole_house_mass_cap_draft_kg'],f['basement_mass_cap_draft_kg']+f['upper_house_light_food_cap_draft_kg'])
 equal(w['potable_container_cap_l'],w['drinking_cooking_barrels']*w['barrel_l']+w['drinking_jerrycans']*w['jerrycan_l']+w['bottled_cases']*w['case_l']+w['upper_floor_bottled_l'])
 equal(w['living_container_cap_l'],w['nonpotable_living_barrels']*w['barrel_l'])
 equal(w['all_container_cap_l'],w['potable_container_cap_l']+w['living_container_cap_l'])
 equal(e['total_mass_kg'],sum(o['kg']for o in e['items']))
 equal(e['raw_kcal'],sum(o['kg']*o['kcal_per_kg_assumption']for o in e['items']))
 equal(e['usable_kcal'],e['raw_kcal']*(1-e['loss_fraction_assumption']))
 equal(e['caloric_equivalent_days'],e['usable_kcal']/(e['people']*e['kcal_person_day_assumption']))
 equal(x['box_usable_l'],x['upper_nominal_box_l']*x['packing_fraction_assumption'])
 equal(x['light_food_allocation_l']+x['medical_consumables_allocation_l']+x['hygiene_and_misc_allocation_l'],x['upper_management_volume_cap_l'])
 assert x['upper_management_volume_cap_l']<=x['box_usable_l']

def main():
 data=calculate_capacity();battery,pv,food,water,example=(data[k]for k in ['battery','pv','food','water','food_example'])
 (OUT/'SAFEHOUSE_CAPACITY.json').write_text(json.dumps(data,ensure_ascii=False,indent=2), encoding="utf-8", newline="\n");print(json.dumps({'capacity_kwh':battery['nominal_kwh'],'output_kw':battery['rated_inverter_output_kw'],'roof_kwp':pv['roof_kwp'],'pv_projected_array_m':pv['roof_projected_array_m'],'food_cap_kg':food['whole_house_mass_cap_draft_kg'],'water_container_l':water['all_container_cap_l'],'food_example_days':round(example['caloric_equivalent_days'],1)},ensure_ascii=False))
if __name__=='__main__':main()

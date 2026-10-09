"""Scenario calculations: proposed limits are not initial inventory or engineering approval."""
from pathlib import Path
import json,math
OUT=Path(__file__).resolve().parents[1]/'docs/chapters/ch01/assets'
def main():
 battery={'module':'Deye SE-G5.1 Pro-B','module_kwh':5.12,'module_mass_kg':45,'cabinets':12,'modules_per_cabinet':5,'cabinet_mass_budget_kg':30,'cabinet_envelope_m':[.6,.8,1.2],'rated_inverter_output_kw':12,'usable_fraction_assumption':.9,'conversion_fraction_assumption':.92}
 battery['modules']=battery['cabinets']*battery['modules_per_cabinet'];battery['nominal_kwh']=battery['modules']*battery['module_kwh'];battery['ac_energy_scenario_kwh']=round(battery['nominal_kwh']*.9*.92,4);battery['battery_mass_kg']=battery['modules']*45;battery['battery_cabinet_mass_budget_kg']=battery['battery_mass_kg']+battery['cabinets']*30
 battery['no_generation_days_scenarios']={str(x):round(battery['ac_energy_scenario_kwh']/x,2)for x in [6,10,16]};battery['not_verified']=['三层结构集中荷载','超过32块后的厂商外部配置','并联分组与固件兼容','住宅三相接入','安装间距与通风分隔']
 pv={'module_reference':'LONGi LR5-54HTH-455M','module_w':455,'module_size_m':[1.722,1.134],'pitch_deg_draft':30,'roof_rows':6,'roof_columns':3,'gap_m':.02,'extension_count':9,'system_factor_assumption':.8}
 pv['roof_count']=18;pv['roof_kwp']=18*.455;pv['extension_kwp']=9*.455;pv['total_target_kwp']=27*.455;pv['roof_projected_array_m']=[3*1.722+2*.02,6*1.134*math.cos(math.radians(30))+5*.02]
 pv['roof_generation_kwh_scenarios']={str(h):round(pv['roof_kwp']*h*.8,3)for h in [1.5,3,5]};pv['recharge_90pct_days_ideal_no_charging_loss_at_3sunhours_daily6kwh']=round(battery['nominal_kwh']*.9/(pv['roof_kwp']*3*.8-6),2)
 food={'basement_racks':16,'rack_m':[.85,.55,1.90],'shelves_per_rack':4,'effective_storage_height_m_assumption':1.6,'packing_fraction_assumption':.7,'basement_mass_cap_draft_kg':2000,'upper_house_light_food_cap_draft_kg':100}
 food['rack_footprint_m2']=16*.85*.55;food['shelf_surface_m2']=food['rack_footprint_m2']*4;food['packaged_volume_cap_m3']=round(food['rack_footprint_m2']*1.6*.7,4);food['whole_house_mass_cap_draft_kg']=2100
 water={'drinking_cooking_barrels':6,'nonpotable_living_barrels':6,'barrel_l':220,'drinking_jerrycans':24,'jerrycan_l':20,'bottled_cases':20,'case_l':12,'upper_floor_bottled_l':120}
 water['potable_container_cap_l']=6*220+24*20+20*12+120;water['living_container_cap_l']=6*220;water['all_container_cap_l']=water['potable_container_cap_l']+water['living_container_cap_l'];water['scenario_persons']=4
 water['days_at_4potable_8living']={'potable':2160/(4*4),'living':1320/(4*8),'both':min(2160/(4*4),1320/(4*8))}
 inventory=[('米面',150,3600),('豆类',20,3300),('油',10,8800),('混合罐头',80,1000),('饼干',20,4500),('奶粉',10,5000),('坚果',10,5800),('糖',5,4000)]
 example={'items':[{'name':n,'kg':m,'kcal_per_kg_assumption':c}for n,m,c in inventory],'total_mass_kg':sum(x[1]for x in inventory),'raw_kcal':sum(m*c for n,m,c in inventory),'loss_fraction_assumption':.1,'people':4,'kcal_person_day_assumption':2000}
 example['usable_kcal']=example['raw_kcal']*.9;example['caloric_equivalent_days']=example['usable_kcal']/8000
 extra={'upper_nominal_box_l':6*60+4*60+6*40,'packing_fraction_assumption':.75,'upper_management_volume_cap_l':600,'light_food_allocation_l':300,'medical_consumables_allocation_l':160,'hygiene_and_misc_allocation_l':140,'medical_not_medicine_days':True}
 extra['box_usable_l']=extra['upper_nominal_box_l']*.75
 data={'version':'0.6','status':'授权扩容的设定目标与满载上限草案，不等于初始库存或结构安装证明','battery':battery,'pv':pv,'food':food,'water':water,'upper_storage':extra,'food_example':example}
 assert battery['modules']==60<=64 and battery['nominal_kwh']==307.2
 assert pv['roof_projected_array_m'][0]<5.4 and pv['roof_projected_array_m'][1]<6.4
 assert water['all_container_cap_l']==3480 and water['potable_container_cap_l']==2160
 assert example['raw_kcal']==992000 and round(example['caloric_equivalent_days'],1)==111.6
 assert extra['light_food_allocation_l']+extra['medical_consumables_allocation_l']+extra['hygiene_and_misc_allocation_l']==600
 (OUT/'SAFEHOUSE_CAPACITY.json').write_text(json.dumps(data,ensure_ascii=False,indent=2));print(json.dumps({'capacity_kwh':battery['nominal_kwh'],'output_kw':12,'roof_kwp':pv['roof_kwp'],'pv_projected_array_m':pv['roof_projected_array_m'],'food_cap_kg':2100,'water_container_l':3480,'food_example_days':111.6},ensure_ascii=False))
if __name__=='__main__':main()

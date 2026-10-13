import unittest, runpy, json, copy
from pathlib import Path
r=Path(__file__).resolve().parents[1]
m=runpy.run_path(str(r/'game/ch02_model.py'));cfg=m['c2_attach_routes'](json.loads((r/'game/ch02_demo.json').read_text(encoding="utf-8")),json.loads((r/'game/data/ch02_routes.json').read_text(encoding="utf-8")))
class TutorialState(unittest.TestCase):
 def new(self,transport='walk'):
  s=m['c2_new_state'](cfg);s['tutorial']=2;s['plan']['home']['mother']='清点';s['plan']['transport']=transport;return s
 def finish(self,s):
  s=m['c2_begin'](s,cfg)
  for stop in s['pending']['preview']['stops']: s=m['c2_buy'](s,cfg,stop,1)
  return m['c2_finish'](s,cfg)
 def test_three_transports_and_immutable_snapshots(self):
  for transport in cfg['transport']:
   with self.subTest(transport=transport):
    s=self.new(transport);old=copy.deepcopy(s);morning=self.finish(s)
    self.assertEqual(s,old);self.assertEqual(morning['resources']['food'],92)
    self.assertEqual(morning['resources']['cash'],5820);self.assertIn('库存清点',morning['completed'])
    if transport=='suv': self.assertLess(morning['resources']['fuel'],40)
    if transport=='ev': self.assertLess(morning['resources']['ev'],100)
    evening=self.finish(morning);settled=m['c2_settle'](evening,cfg)
    self.assertEqual(settled['resources']['food'],88);self.assertEqual(settled['resources']['water'],240)
    self.assertEqual(settled['resources']['ev'],100)
    self.assertEqual(m['c2_settle'](settled,cfg),settled)
    self.assertEqual(m['c2_next_day'](settled)['day'],7)
 def test_pending_and_complete_roundtrip(self):
  s=m['c2_begin'](self.new(),cfg);s=json.loads(json.dumps(s))
  s=m['c2_buy'](s,cfg,'market',1)
  self.assertEqual(s['resources']['food'],80) # onboard, not at-home stock
  with self.assertRaises(ValueError): m['c2_buy'](s,cfg,'market',1)
  s=m['c2_finish'](s,cfg);self.assertEqual(m['c2_finish'](s,cfg),s)
 def test_invalid_plans(self):
  for change,expected in [(('cash',0),'资金'),(('fuel',0),'燃油'),(('ev',0),'电量')]:
   s=self.new('suv' if change[0]=='fuel' else 'ev');s['resources'][change[0]]=change[1]
   self.assertTrue(any(expected in e for e in m['c2_errors'](s,cfg)))
  s=self.new();s['plan']['quantity']=3;self.assertTrue(any('载货' in e for e in m['c2_errors'](s,cfg)))
  s=self.new();s['plan']['companion']=True;s['plan']['home']['partner']='清点'
  self.assertTrue(any('同时' in e for e in m['c2_errors'](s,cfg)))
  s=self.new();tiny=copy.deepcopy(cfg);tiny['slot_minutes']=1
  self.assertTrue(any('时间' in e for e in m['c2_errors'](s,tiny)))
 def test_multistop_and_home_tasks(self):
  s=self.finish(self.new('suv'));s['plan'].update(destination='pharmacy',transport='ev',extra=True)
  v=m['c2_preview'](s,cfg);self.assertEqual(v['stops'],['pharmacy','market'])
  s=self.finish(s);self.assertEqual(s['resources']['care'],5);self.assertEqual(s['resources']['food'],104)
  self.assertEqual(s['resources']['cash'],5550)
  s=self.finish(self.new());s['plan']['home']['father']='院门检查';s=self.finish(s)
  self.assertIn('院门检查',s['completed']);self.assertIn('地下室检查',s['completed'])
 def test_cannot_settle_or_duplicate_day(self):
  with self.assertRaises(ValueError): m['c2_settle'](self.new(),cfg)
  s=m['c2_settle'](self.finish(self.finish(self.new())),cfg);s=json.loads(json.dumps(s))
  self.assertEqual(m['c2_settle'](s,cfg),s)
  with self.assertRaises(ValueError): m['c2_next_day'](m['c2_next_day'](s))
 def test_needs_action_once_and_save(self):
  s=self.new();before=copy.deepcopy(s);s=self.finish(s)
  self.assertLess(s['people']['hero']['satiety'],s['people']['father']['satiety'])
  self.assertLess(s['people']['hero']['hydration'],s['people']['father']['hydration'])
  self.assertEqual(before['people']['hero']['satiety'],90)
  s=json.loads(json.dumps(s));self.assertEqual(m['c2_finish'](s,cfg),s)
  s=self.finish(s);old=copy.deepcopy(s);settled=m['c2_settle'](s,cfg)
  self.assertGreater(settled['people']['hero']['satiety'],old['people']['hero']['satiety'])
  self.assertEqual(settled['resources']['water'],240)
  self.assertEqual(settled['mains_water_used'],8)
  self.assertEqual(m['c2_settle'](json.loads(json.dumps(settled)),cfg),settled)
 def test_washing_and_water_shortage(self):
  s=self.finish(self.new());s['plan']['destination']='wash';s['plan']['home']['mother']='洗漱'
  s['people']['hero']['hygiene']=20;s['people']['mother']['hygiene']=20
  s=self.finish(s)
  self.assertEqual(s['people']['hero']['hygiene'],52)
  self.assertEqual(s['mains_water_used'],12);self.assertEqual(s['resources']['water'],240)
  s['supply']['water']=False;s['resources']['water']=2;s['resources']['food']=0
  old=copy.deepcopy(s);n=m['c2_settle'](s,cfg)
  self.assertEqual(n['resources']['water'],0);self.assertEqual(n['water_shortage'],6)
  self.assertEqual(n['people']['hero']['satiety'],old['people']['hero']['satiety'])
  self.assertEqual(n['people']['hero']['hydration'],min(100,old['people']['hero']['hydration']+20))
 def test_old_save_upgrade_does_not_replay(self):
  s=self.finish(self.new());s.pop('people');s.pop('supply');s.pop('water_used');s.pop('mains_water_used')
  old=copy.deepcopy(s);n=m['c2_upgrade'](s,cfg)
  self.assertEqual(n['resources'],old['resources']);self.assertEqual(n['reports'],old['reports'])
  self.assertEqual(m['c2_upgrade'](n,cfg),n)
 def test_skip_does_not_give_resources(self):
  s=self.new();s['hints']=False;s['tutorial']=0
  self.assertEqual(s['resources'],cfg['initial']);self.assertEqual(m['c2_errors'](s,cfg),[])
if __name__=='__main__': unittest.main(verbosity=2)

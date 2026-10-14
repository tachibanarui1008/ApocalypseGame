import copy
import json
import runpy
import unittest
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
M=runpy.run_path(str(ROOT/'game/ch02_model.py'))
CFG=M['c2_attach_routes'](json.loads((ROOT/'game/ch02_demo.json').read_text(encoding='utf-8')),
                        json.loads((ROOT/'game/data/ch02_routes.json').read_text(encoding='utf-8')))

class Stress(unittest.TestCase):
    def new(self):
        s=M['c2_new_state'](CFG);s['hints']=False
        return s
    def finish(self,s,destination='rest'):
        s=copy.deepcopy(s);s['plan']['destination']=destination
        s=M['c2_begin'](s,CFG)
        for stop in s['pending']['preview']['stops']: s=M['c2_buy'](s,CFG,stop,1)
        return M['c2_finish'](s,CFG)
    def test_work_rest_and_reading_are_per_person_once(self):
        s=self.new();old=copy.deepcopy(s)
        s['plan']['home']['father']='阅读放松'
        n=self.finish(s,'basement')
        self.assertEqual(n['people']['hero']['stress'],26)
        self.assertEqual(n['people']['father']['stress'],11)
        self.assertEqual(n['people']['mother']['stress'],15)
        self.assertEqual(old['people']['hero']['stress'],20)
        self.assertEqual(M['c2_finish'](n,CFG),n)
    def test_sleep_after_meal_per_person_not_on_opening_summary(self):
        s=M['c2_settle'](self.finish(self.finish(self.new())),CFG)
        s=M['c2_upgrade'](s,CFG);s['sleep_on_time']['mother']=False
        old=copy.deepcopy(s);n=M['c2_sleep'](s,CFG)
        self.assertEqual(s,old)
        self.assertEqual(n['people']['hero']['stress'],4)
        self.assertEqual(n['people']['mother']['stress'],10)
        self.assertEqual(M['c2_sleep'](json.loads(json.dumps(n)),CFG),n)
        n['sleep_on_time']['mother']=True
        self.assertEqual(M['c2_sleep'](n,CFG)['people']['mother']['stress'],10)
        with self.assertRaises(ValueError): M['c2_sleep'](self.new(),CFG)
    def test_migration_and_event_clamps_and_deduplication(self):
        s=self.new();s['people']['hero']['stress']=97
        self.assertEqual(M['c2_upgrade'](s,CFG),s)
        del s['people']['partner']['stress']
        n=M['c2_upgrade'](s,CFG)
        self.assertEqual(n['people']['hero']['stress'],97)
        self.assertEqual(n['people']['partner']['stress'],20)
        n=M['c2_stress_event'](n,CFG,'news-1',{'hero':10,'partner':-100})
        self.assertEqual(n['people']['hero']['stress'],100)
        self.assertEqual(n['people']['partner']['stress'],0)
        self.assertEqual(M['c2_stress_event'](n,CFG,'news-1',{'hero':10}),n)
        with self.assertRaises(ValueError): M['c2_stress_event'](n,CFG,'bad',{'hero':float('nan')})
    def test_shortage_once_and_next_day_sleep_choices_reset(self):
        s=self.finish(self.finish(self.new()));s['resources']['food']=0;s['resources']['water']=0;s['supply']['water']=False
        n=M['c2_settle'](s,CFG)
        self.assertEqual(n['people']['hero']['stress'],18)
        self.assertEqual(M['c2_settle'](n,CFG),n)
        n=M['c2_sleep'](n,CFG);next_day=M['c2_next_day'](n)
        self.assertTrue(all(next_day['sleep_on_time'].values()))
        self.assertEqual(next_day['people']['hero']['stress'],12)

if __name__=='__main__': unittest.main()

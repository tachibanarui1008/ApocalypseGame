"""Verify narrative branch continuity without pretending to test Ren'Py UI."""
import copy
import json
import runpy
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
M = runpy.run_path(str(ROOT / "game/ch02_events.py"))


class NarrativeContinuity(unittest.TestCase):
    def ending(self, route, outcome):
        s = M['c2e_new'](route)
        if outcome == 'safe':
            s = M['c2e_day'](s, 9 if route == 'B' else 4)
            s = M['c2e_parents'](s, 'aboard')
            s = M['c2e_parents'](s, 'safe')
            return M['c2e_day'](s, 12)
        s = M['c2e_day'](s, 12)
        s = M['c2e_parents'](s, 'en_route')
        return M['c2e_parents'](s, outcome)

    def test_calendar_and_fixed_disaster(self):
        for route, arrival, tutorial in [('B', 5, 6), ('C', 2, 3)]:
            s = M['c2e_new'](route)
            self.assertEqual((s['arrival_day'], s['tutorial_day']), (arrival, tutorial))
            self.assertEqual(s['disaster_day'] - tutorial, 6 if route == 'B' else 9)
            old = copy.deepcopy(s)
            self.assertEqual(M['c2e_day'](s, 8)['logistics'], 'detour')
            self.assertEqual(M['c2e_day'](s, 12)['logistics'], 'halted')
            self.assertEqual(s, old)
        for route in 'AD':
            with self.assertRaises(ValueError): M['c2e_new'](route)

    def test_abort_retry_and_arrival_are_distinct(self):
        s = M['c2e_day'](M['c2e_new']('B'), 9)
        s = M['c2e_parents'](s, 'delayed')
        self.assertEqual(s['household_size'], 4)
        s = M['c2e_parents'](s, 'aboard')
        self.assertEqual(s['household_size'], 4)
        s = M['c2e_parents'](s, 'safe')
        self.assertEqual(s['household_size'], 6)
        self.assertEqual(M['c2e_parents'](s, 'safe'), s)
        with self.assertRaises(ValueError): M['c2e_parents'](s, 'en_route')

    def test_no_death_from_delay_or_missing_contact(self):
        s = M['c2e_new']('C')
        for outcome in ('deceased', 'unknown', 'en_route'):
            with self.assertRaises(ValueError): M['c2e_parents'](s, outcome)
        s = self.ending('C', 'unknown')
        self.assertFalse(s['grief'])
        self.assertFalse(s['gate_opened'])
        with self.assertRaises(ValueError): M['c2e_gate_open'](s)

    def test_every_death_path_opens_gate_and_preserves_snapshot(self):
        for route in 'BC':
            for choice in ('stay', 'close'):
                for repaired in (False, True):
                    for watch in (False, True):
                        s = self.ending(route, 'deceased')
                        with self.assertRaises(ValueError): M['c2e_handoff'](s)
                        s = M['c2e_gate_open'](s)
                        old = copy.deepcopy(s)
                        s = M['c2e_gate_resolve'](s, choice, repaired, watch)
                        secured = repaired and (choice == 'stay' or watch)
                        self.assertTrue(s['gate_opened'])
                        self.assertEqual(s['intrusion'], not secured)
                        self.assertEqual(old['gate_status'], 'open')
                        self.assertNotIn('CH02-S05-resolved', old['seen_events'])
                        self.assertEqual(M['c2e_gate_resolve'](s, choice, repaired, watch), s)
                        # Loading a serialized mid-event snapshot can continue normally.
                        saved = json.loads(json.dumps(old))
                        self.assertEqual(M['c2e_gate_resolve'](saved, choice, repaired, watch), s)
                        self.assertEqual(M['c2e_handoff'](s)['day'], 13)

    def test_safe_and_unknown_chapter_three_handoff(self):
        for route in 'BC':
            for outcome in ('safe', 'unknown'):
                s = self.ending(route, outcome)
                end = M['c2e_handoff'](s)
                self.assertEqual(end['parents_status'], outcome)
                self.assertEqual(end['household_size'], 6 if outcome == 'safe' else 4)
                self.assertFalse(end['gate_opened'])
                self.assertEqual(s['day'], 12)

    def test_reject_unresolved_or_late_transitions(self):
        s = M['c2e_new']('B')
        with self.assertRaises(ValueError): M['c2e_day'](s, 5)
        with self.assertRaises(ValueError): M['c2e_day'](s, True)
        s = M['c2e_day'](s, 12)
        with self.assertRaises(ValueError): M['c2e_parents'](s, 'aboard')
        with self.assertRaises(ValueError): M['c2e_handoff'](s)
        with self.assertRaises(ValueError): M['c2e_gate_resolve'](s, 'stay')


if __name__ == '__main__':
    unittest.main()

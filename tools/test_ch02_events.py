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
        s = M['c2e_choose_rescue'](M['c2e_new'](route), 'pickup' if outcome == 'safe' else 'self_arrival')
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
        s = M['c2e_choose_rescue'](M['c2e_new']('B'), 'pickup')
        s = M['c2e_day'](s, 9)
        s = M['c2e_parents'](s, 'delayed')
        self.assertEqual(s['household_size'], 4)
        s = M['c2e_parents'](s, 'aboard')
        self.assertEqual(s['household_size'], 4)
        s = M['c2e_parents'](s, 'safe')
        self.assertEqual(s['household_size'], 6)
        self.assertEqual(M['c2e_parents'](s, 'safe'), s)
        with self.assertRaises(ValueError): M['c2e_parents'](s, 'en_route')

    def test_choice_once_and_plan_guards(self):
        s = M['c2e_new']('C')
        old = copy.deepcopy(s)
        with self.assertRaises(ValueError): M['c2e_parents'](s, 'aboard')
        pickup = M['c2e_choose_rescue'](s, 'pickup')
        self.assertEqual(s, old)
        self.assertEqual(M['c2e_choose_rescue'](pickup, 'pickup'), pickup)
        with self.assertRaises(ValueError): M['c2e_choose_rescue'](pickup, 'self_arrival')
        self_arrival = M['c2e_choose_rescue'](s, 'self_arrival')
        with self.assertRaises(ValueError): M['c2e_parents'](self_arrival, 'aboard')
        with self.assertRaises(ValueError): M['c2e_parents'](pickup, 'en_route')
        with self.assertRaises(ValueError): M['c2e_parents'](self_arrival, 'unknown')
        # An old snapshot remains a valid place to make the other choice.
        self.assertEqual(M['c2e_choose_rescue'](old, 'self_arrival')['rescue_plan'], 'self_arrival')

    def test_room_inspection_unlocks_work_not_completion(self):
        s = M['c2e_new']('B')
        for room in ('basement', 'radio', 'server', 'power'):
            prior = copy.deepcopy(s)
            updated = M['c2e_inspect_room'](s, room)
            self.assertEqual(s, prior)
            self.assertEqual(M['c2e_inspect_room'](updated, room), updated)
            s = updated
        self.assertEqual(len(s['unlocked_tasks']), 5)
        self.assertNotIn('completed_tasks', s)
        self.assertNotIn('resources', s)

    def test_hidden_online_delivery_cutoff(self):
        for route in 'BC':
            s = M['c2e_new'](route)
            self.assertTrue(M['c2e_day'](s, 7)['online_delivery_open'])
            closed = M['c2e_day'](s, 8)
            self.assertFalse(closed['online_delivery_open'])
            self.assertEqual(closed['logistics'], 'detour')
            self.assertFalse(M['c2e_day'](closed, 11)['online_delivery_open'])
            self.assertTrue(s['online_delivery_open'])

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
                        end = M['c2e_handoff'](s)
                        self.assertEqual(end['day'], 12)
                        self.assertEqual(end['chapter_outcome'], 'bad')
                        self.assertEqual(M['c2e_handoff'](end), end)
                        with self.assertRaises(ValueError): M['c2e_day'](end, 13)

    def test_only_pickup_good_end_reaches_chapter_three(self):
        for route in 'BC':
            s = self.ending(route, 'safe')
            end = M['c2e_handoff'](s)
            self.assertEqual(end['day'], 13)
            self.assertEqual(end['chapter_outcome'], 'good')
            self.assertEqual(end['household_size'], 6)
            self.assertFalse(end['gate_opened'])
            self.assertEqual(s['day'], 12)
            self.assertEqual(M['c2e_handoff'](end), end)

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

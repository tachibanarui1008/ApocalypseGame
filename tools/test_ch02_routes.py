"""Validate the original-map route data, cached matrices and runtime consumption."""
import unittest, json, runpy, copy, hashlib
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
M=runpy.run_path(str(ROOT/"game/ch02_model.py"))
DATA=json.loads((ROOT/"game/data/ch02_routes.json").read_text())
CFG=M["c2_attach_routes"](json.loads((ROOT/"game/ch02_demo.json").read_text()),DATA)
class TownRoutes(unittest.TestCase):
    def test_original_image_is_byte_identical(self):
        original=(ROOT/DATA["source_image"]).read_bytes()
        self.assertEqual(original,(ROOT/"game/images/ch02/town_map.png").read_bytes())
        self.assertEqual(hashlib.sha256(original).hexdigest(),DATA["source_image_sha256"])
    def test_all_pairs_match_runtime_recalculation(self):
        fresh=copy.deepcopy(CFG);fresh["closed_edges"]=["sentinel-force-recalculate"]
        for mode in ("walk","suv","ev"):
            for a in DATA["matrix_order"]:
                for b in DATA["matrix_order"]:
                    expected=DATA["distance_matrices"][mode][a][b]
                    distance,path=M["c2_path"](fresh,a,b,mode)
                    self.assertAlmostEqual(distance*1000,expected)
                    self.assertEqual(path[0],DATA["places"][a]["endpoints"][mode])
                    self.assertEqual(path[-1],DATA["places"][b]["endpoints"][mode])
    def test_matrix_metric_and_corridor_budgets(self):
        for matrix in DATA["distance_matrices"].values():
            for a in matrix:
                self.assertEqual(matrix[a][a],0)
                for b in matrix:
                    self.assertEqual(matrix[a][b],matrix[b][a])
                    for c in matrix:self.assertLessEqual(matrix[a][c],matrix[a][b]+matrix[b][c])
        for corridor in DATA["corridor_budgets"]:
            self.assertEqual(corridor["length_m"],sum(e["length_m"] for e in DATA["edges"] if e["source_corridor"]==corridor["id"]))
    def test_car_never_uses_pedestrian_access(self):
        allowed={(e["from"],e["to"]) for e in DATA["edges"] if "suv" in e["modes"]}
        allowed|={(b,a) for a,b in allowed}
        for rows in DATA["path_matrices"]["suv"].values():
            for path in rows.values():
                for a,b in zip(path,path[1:]):self.assertIn((a,b),allowed)
        self.assertNotEqual(DATA["places"]["station"]["endpoints"]["walk"],DATA["places"]["station"]["endpoints"]["suv"])
    def test_underpass_closure_disconnects_port(self):
        blocked=copy.deepcopy(CFG);blocked["closed_edges"]=[e["id"] for e in DATA["edges"] if e["underpass"]]
        for mode in ("walk","suv","ev"):
            with self.assertRaises(ValueError):M["c2_path"](blocked,"home","port",mode)
            self.assertGreater(M["c2_path"](blocked,"home","station",mode)[0],0)
    def test_blocked_entrance_rejects_action_instead_of_crash(self):
        cfg=copy.deepcopy(CFG)
        node=DATA["places"]["market"]["endpoints"]["walk"]
        cfg["closed_edges"]=[e["id"] for e in DATA["edges"] if node in (e["from"],e["to"])]
        state=M["c2_new_state"](cfg);state["hints"]=False
        self.assertTrue(any("道路不通" in e for e in M["c2_errors"](state,cfg)))
    def test_trip_consumption_uses_mode_matrix(self):
        for mode in ("walk","suv","ev"):
            s=M["c2_new_state"](CFG);s["plan"]["transport"]=mode;s["hints"]=False
            p=M["c2_preview"](s,CFG)
            km=2*DATA["distance_matrices"][mode]["home"]["market"]/1000
            self.assertAlmostEqual(p["km"],round(km,2))
            self.assertEqual(p["fuel"],round(km*CFG["transport"][mode]["fuel_per_km"],2))
            self.assertEqual(p["ev"],round(km*CFG["transport"][mode]["ev_per_km"],2))
if __name__=="__main__":unittest.main(verbosity=2)

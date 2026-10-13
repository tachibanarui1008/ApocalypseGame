import json,hashlib,runpy,re,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
class UnifiedResources(unittest.TestCase):
 def test_first_chapter_all_assets_preserved(self):
  records=json.loads((ROOT/"docs/chapters/ch01/INTEGRATED_ASSETS.json").read_text(encoding="utf-8"))
  self.assertEqual(len(records),42)
  for item in records:
   self.assertEqual(hashlib.sha256((ROOT/"game"/item["path"]).read_bytes()).hexdigest(),item["sha256"],item["path"])
 def test_scene_cues_match_current_manuscript(self):
  generator=runpy.run_path(str(ROOT/"tools/export_renpy.py"));story=generator["load_story"](ROOT/"docs/chapters/ch01/SCRIPT.md")
  cues=json.loads((ROOT/"game/data/ch01_presentation.json").read_text(encoding="utf-8"));assets=json.loads((ROOT/"game/data/ch01_assets.json").read_text(encoding="utf-8"))
  self.assertEqual(set(cues),{s["id"] for s in story["scenes"]})
  for scene in story["scenes"]:
   cue=cues[scene["id"]];count=sum(b["type"]!="direction" for b in scene["blocks"])
   self.assertEqual(cue["dialogue_count"],count)
   self.assertIn(cue["initial"],set(assets)|{"black"})
   for index,pictures in cue["cues"].items():
    self.assertLessEqual(int(index),count)
    self.assertTrue(set(pictures)<=set(assets)|{"black"})
 def test_export_keeps_all_dialogue_and_hooks(self):
  generator=runpy.run_path(str(ROOT/"tools/export_renpy.py"));story=generator["load_story"](ROOT/"docs/chapters/ch01/SCRIPT.md")
  generated=generator["render"](story);self.assertEqual(generated,(ROOT/"game/story_generated.rpy").read_text(encoding="utf-8"))
  self.assertEqual(generated.count("$ c1_before("),1216)
  self.assertEqual(generated.count("$ c1_scene("),30)
  labels=[]
  for path in (ROOT/"game").glob("*.rpy"):labels+=re.findall(r"^label (\w+)",path.read_text(encoding="utf-8"),re.M)
  self.assertEqual(len(labels),len(set(labels)))
if __name__=="__main__": unittest.main(verbosity=2)

# 第二章详细稿与局部事件验证 · 2026-10-14

基线：main `491183c`（Windows v0.3.0），工作分支`codex/ch02-storm-script`。当前改动是六幕正式详细创作稿V0.1与S05/S06局部事件接入基础，不是完整第二章发行版。

## 正文与连续性核对

- SCRIPT共26节点：H4/E4/L4/P5/D3/S6；正文含分支对白、场景事件、演出说明、日历、状态合同及第三章交接。
- B Day5晚归家、Day6教程；C Day2晚归家、Day3父母从市区到安全屋并开始教程。C与B相差三天，Day12灾难固定。
- Day7漫游、Day8楼区封锁、Day9—10接应（C可Day4提前）、Day11晚宴、Day12枢纽失守/紧急广播/院门事故为本版创作安排。
- 父母接回成功才记六人；登车仍与入住分开；折返保留重试，不直接死亡；失联不当死亡。途中遇害确认后实际打开院门，后续维修/预警与现场选择影响重封或入院。
- 楼区传播链仅作体液暴露调查方向，未增加空气传播、同楼必感染或短时转化；主角不获知实验室与免疫秘密。恐怖通过遮挡、信息断裂与秩序变化表达。
- 此核对是创作连续性检查，不是感染规则的现实医学证明，也不认定未定初始库存/工程能力已完成。

## 程序测试

| 检查 | 结果 | 范围 |
|---|---|---|
| `test_ch02_events.py` | 6项通过 | B/C日历、折返重试、登车/入住区分、失联/死亡区分、16种院门组合、快照序列化、重复调用与非法转换 |
| 原`test_ch02_model.py` | 9项通过 | 原教程资源、采购、需求、洗漱、结算与防重复 |
| 原`test_ch02_routes.py` | 7项通过 | 现有路网、通行限制、距离与资源预算 |
| 原`test_unified_resources.py` | 3项通过 | 第一章导出、42项资源与逐行画面映射 |
| Ren’Py 8.5.3.26051504 lint | 通过 | 新事件脚本与原工程可解析；新增测试脚本也已解析 |
| 新局部事件原生测试 | 20用例/148断言通过 | B/C×16院门条件组合及4成功/失联尾声；16处菜单存读档恢复；Day13状态交接，教程`c2`未被写入 |
| 原Windows原生回归脚本 | 8用例/46断言通过 | 当前源码运行A/B/C/D、B接教程、三种交通、采购/洗漱/日结/Day7、原存读档位置及界面框架 |

原生测试使用Windows SDK与隔离复制的当前`game/`，隔离存档，不使用或覆盖玩家档案；不是仅跑历史发行包。重现入口：

```powershell
python tools/test_ch02_events.py
python tools/test_ch02_model.py
python tools/test_ch02_routes.py
python tools/test_unified_resources.py
python tools/test_ch02_events_native.py --sdk <SDK目录> --output .runtime/events-new
python tools/test_ch02_events_native.py --sdk <SDK目录> --output .runtime/tutorial-new --tutorial-regression
python tools/verify_handoff.py
```

每次原生测试需使用新的输出目录，运行日志与存档留在`.runtime/`而不入Git。通过的报告摘存[事件原生报告](validation/events-native.txt)、[原教程回归报告](validation/tutorial-native.txt)和[lint报告](validation/lint.txt)。

首次测试发现测试参数不能引用尚未执行的init变量，改为解析期可求值列表；随后测试快照变量不能用于存档后的可靠比对，改为隔离目录中的检查点。修复的是测试工具；最终20用例通过后才记录上述通过结果，早期失败报告未冒充验收。

## 保留的边界与后续

- `game/ch02_story.rpy`、`game/ch02_model.py`、`game/script.rpy`、第一章正文/生成文件、地图与美术在本轮未改。B教程和Day7演示页保持可玩。
- S05/S06仅是可调用Ren’Py标签，没有正式模式入口；局部测试使用独立测试驱动。日程调度尚未接入，不宣称完整26节点可玩。
- C线正式资源初始化、可玩Day3教程、六人需求与结算、接应地址路网/成本、多队伍、正式准备工程和第三章正文仍未实现。
- 新脚本尚无正式背景/人物/音效制作；原生测试证明执行、选择与状态保存，不是新场景视觉验收。没有更新版本号、重打发行包或替换v0.3.0下载。
- 前次聊天最后两段长稿只返回引用占位；本稿未声称逐字恢复不可读正文。可读讨论与本次用户要求已作为创作边界。
- 同步README、CANON、WORLD_BIBLE、PLANNING与教程说明，世界观里旧B Day3日期更正为当前main的Day5，不改第一章内容。
- 完成合法改动后重建交接文件清单并再次核验；新增文件不借更新清单掩盖缺失旧素材。

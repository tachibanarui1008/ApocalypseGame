# 未雨绸缪 / ApocalypseGame

当前交接版本：**0.3.0（第一章完整＋第二章B线Day6可玩教程）**。第一章30场景、1216段正文及42项美术已接入；第二章保留城镇地图、14地点距离矩阵、三种交通、采购、家庭排班、人物需求条、洗漱和晚间结算。

**Windows玩家先读 [下载与运行说明](docs/WINDOWS.md)；开发接手参考 [原始交接文档](docs/HANDOFF_WINDOWS.md)。**

```powershell
git clone https://github.com/tachibanarui1008/ApocalypseGame.git
cd ApocalypseGame
```

使用有该私有仓库权限的GitHub账号。仓库已直接包含源码、字体、背景、人物、CG、地图图片/SVG及数据，克隆无需Git LFS。玩家下载Windows ZIP并完整解压，双击ApocalypseGame.exe；开发者使用官方Ren'Py 8.5.3 SDK打开根目录工程。Windows与Mac使用同一套0.3.0游戏内容，平台验收见[记录](docs/handoff/WINDOWS_VALIDATION.md)。

- [GitHub发布页：试玩、完整工程、历史资源归档](https://github.com/tachibanarui1008/ApocalypseGame/releases/tag/v0.3.0)
- [确定设定与时间线](docs/CANON.md)
- [第一章资料](docs/chapters/ch01/README.md) / [主剧本](docs/chapters/ch01/SCRIPT.md)
- [第一章美术规范](docs/BACKGROUND_STYLE.md)
- [第二章教程](docs/chapters/ch02/TUTORIAL_B_V0.1.md)
- [第二章正式剧本V0.1](docs/chapters/ch02/SCRIPT.md) / [剧情索引与接入规划](docs/chapters/ch02/PLANNING.md) / [本轮验证](docs/chapters/ch02/VALIDATION.md)：六幕正文已落盘，S05/S06局部Ren’Py接口与叙事状态已开始；正式日程未接，Day6教程和Day7演示终点保持。
- [路网与距离](docs/chapters/ch02/TOWN_ROUTES_V0.4.md) / [地图风格](docs/chapters/ch02/MAP_STYLE_V0.5.md)
- [人物与物资条](docs/chapters/ch02/NEEDS_V0.6.md) / [后续剧情待办](docs/chapters/ch02/PLANNING.md)
- [资源校验清单](docs/handoff/RESOURCE_MANIFEST.json)

最低检查（Python标准库即可）：

```powershell
py -3 tools/verify_handoff.py
py -3 tools/test_unified_resources.py
py -3 tools/test_ch02_model.py
py -3 tools/test_ch02_routes.py
```

第一章正文更新后运行 `py -3 tools/export_story.py` 与 `py -3 tools/export_renpy.py`。地图PNG已随仓库保存，正常运行无需安装CairoSVG；需要重绘时再参考交接文档。Mac打包工具为 `tools/package_game.py`；Windows打包使用 `tools/package_windows.py --sdk <SDK目录>`，原生验收使用 `tools/test_windows.py`。

开始工作前 `git pull --ff-only`，切换设备前提交并推送。不要同时在Mac和Windows修改同一份文件。

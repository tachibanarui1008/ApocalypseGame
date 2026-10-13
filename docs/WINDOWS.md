# Windows版 · 未雨绸缪0.3.0

Windows版沿用Mac版0.3.0的同一份`game/`，使用Ren'Py 8.5.3.26051504。没有另起剧情分支：第一章30场景、1216段正文、四条路线、42项美术完整保留；第二章为B线Day6教程，到Day7演示完成页结束。C线第二章和Day7以后的剧情仍待开发。

## 直接游玩

从[0.3.0发布页](https://github.com/tachibanarui1008/ApocalypseGame/releases/tag/v0.3.0)下载`ApocalypseGame-0.3.0-win.zip`，将整个ZIP解压到普通文件夹，双击其中的`ApocalypseGame.exe`。无需安装Python或Ren'Py SDK。不要只取出EXE，旁边的`game`、`lib`和`renpy`目录是运行必需文件。

本机交付位于`F:\weiyuchoumou\releases\ApocalypseGame-0.3.0-win\ApocalypseGame.exe`。主菜单“开始阅读”进入第一章；“第二章 · B线教程（演示）”可直接试玩经营教程。

鼠标点击或空格继续阅读，Esc打开菜单，滚轮向上回退；地图可拖动、缩放和点击地点。存档仍使用`%APPDATA%\RenPy\Weiyuchoumou-Unified-V03`。Windows新存档已纳入验收，旧Mac存档迁移兼容没有验证。

## 重新打包

下载并解压[官方Ren'Py 8.5.3 SDK](https://www.renpy.org/release/8.5.3)，SDK保存在Git忽略的`.runtime/`或仓库外。命令中按实际位置填写SDK路径：

```powershell
python tools/package_windows.py --sdk .runtime/renpy-8.5.3-sdk
```

工具从`game/`建立临时工程，运行lint，再调用官方Windows发行包构建器。输出ZIP、SHA256和`windows-build.json`到`releases/`，校验必需脚本、地图、字体、许可和EXE，排除存档与开发工具。默认输出文件名随当前游戏版本0.3.0固定；升级版本时同步更新工具和文档。

## 验收与维护

```powershell
python tools/test_unified_resources.py
python tools/test_ch02_model.py
python tools/test_ch02_routes.py
python tools/test_windows.py --output .runtime/windows-acceptance-new
python tools/verify_handoff.py
```

原生验收从发行ZIP解压一份独立测试工程，再注入`tools/windows_acceptance.rpy`。测试通过Windows运行时执行剧情与屏幕操作，覆盖A/B/C/D、B衔接第二章、步行/SUV/电车、食品采购、清点、洗漱、晚间结算、Day7，以及安排/结果/晚间三个位置的存读档。测试存档和截图隔离于指定输出目录，不覆盖玩家档案。每次使用一个新的输出目录。

测试脚本不包含在玩家ZIP。具体验收结果见[Windows验收记录](handoff/WINDOWS_VALIDATION.md)。源码、文档和工具通过Git同步，SDK、缓存、存档、发行ZIP不入Git；发行包放GitHub Release。

# Windows开发交接 · 未雨绸缪0.3.0

交接日期：2026-10-13。仓库：https://github.com/tachibanarui1008/ApocalypseGame 。基线发布标签：v0.3.0。本轮上传当前内容与交接资料，未开发Windows或iPad发行包。

## 1. 在Windows接手

1. 登录有此私有仓库权限的GitHub账号，安装Git；在本地普通工作目录克隆，建议 `D:\Projects\ApocalypseGame`，先避免云盘自动卸载文件。
2. 执行 `git clone https://github.com/tachibanarui1008/ApocalypseGame.git`，进入目录。素材直接在Git中，没有LFS步骤。
3. 从[官方8.5.3发布页](https://www.renpy.org/release/8.5.3)安装Ren'Py SDK。本轮Mac实际验证版本为8.5.3.26051504。[启动器官方说明](https://www.renpy.org/doc/html/quickstart.html)。
4. 启动 `renpy.exe`，在启动器设置中把项目目录设为 `D:\Projects`，选择ApocalypseGame，点击启动项目。`game/`是唯一游戏入口，不要把另一套旧Demo的game目录覆盖进来。
5. 从主菜单开始阅读可走第一章；第二章B线教程也有直接入口。首次到Windows须自行确认中文字体、鼠标操作、存读档和三种交通流程，本轮没有Windows实机验证。

```powershell
cd D:\Projects
git clone https://github.com/tachibanarui1008/ApocalypseGame.git
cd ApocalypseGame
py -3 tools/verify_handoff.py
py -3 tools/test_unified_resources.py
py -3 tools/test_ch02_model.py
py -3 tools/test_ch02_routes.py
```

模型、寻路、资源检查只用Python标准库；建议Python3.12或3.13，Mac已用3.13通过。Ren'Py运行使用SDK自带Python，不依赖上面安装的Python。

## 2. 已完成的游戏内容

- 第一章：30场景、1216段正文；A/D坏结局，B/C抵达安全屋。26背景、4人物、3CG、2额外画面、7变体共42项全部保留，并有美术浏览入口。
- 已定时间：危机正式爆发Day12；B线Day5抵家，Day6开始倒计时6天；C线Day2抵家，Day3开始倒计时9天。两线相差3天。
- 第二章：只实现B线Day6。早餐说明、上午采购、地图道路移动、步行/燃油SUV/电车、可选同行者、家人排班、下午检查/采购/洗漱、晚间结算、进入Day7演示终点。
- 地图：沿用原城镇几何，游戏采用深灰绿工业风与细线图标；14地点，按道路入口建立步行、SUV、电车距离与路径矩阵。
- 四个人各有饱腹/饮水/卫生（0—100），不设体力。工作额外消耗人物饱腹和饮水；每日口粮仍统一扣4人日。正常供水时每日8L饮水及每次6L洗漱用自来水，不扣应急储水。人物低于30变警示色，暂未做疾病惩罚。
- 晚间食物、饮水恢复人物状态；洗漱恢复卫生；市电正常时电车充满，燃油不自动补回。购买、行动、晚间结算均有防重复记账。
- 当前演示初始资源：资金6000、食品80人日、应急水240L、燃油40L、电车100%、储能100%、护理4单位、建材6单位。不是正式物资平衡，不是房屋容量。

## 3. 文件职责

| 文件 | 用途 |
|---|---|
| `docs/CANON.md` | 当前确定事实与时间线，优先于历史草稿 |
| `docs/chapters/ch01/SCRIPT.md` | 第一章正文唯一维护来源 |
| `tools/export_story.py`、`tools/export_renpy.py` | 导出章节数据和原生剧情；不要直接长期维护生成文件 |
| `game/ch01_visuals.rpy` | 第一章画面、人物与美术浏览 |
| `game/data/ch01_presentation.json` | 30场景画面与逐行提示映射，正文增删时同步更新 |
| `game/data/ch01_assets.json`、`ch01_asset_names.json` | 第一章资源路径及中文名称 |
| `game/screens.rpy`、`script.rpy`、`options.rpy` | 通用工业风UI、第一章入口/结局衔接、画布/字体/版本 |
| `game/ch02_model.py` | 独立状态运算、路径查询、采购和结算；返回新字典以支持存档回退 |
| `game/ch02_screens.rpy` | 地图、行动计划、人物/资源条与各交互窗口 |
| `game/ch02_story.rpy` | Day6剧情与行动流程 |
| `game/ch02_demo.json` | 演示库存、需求、载货与交通成本配置 |
| `game/data/ch02_routes.json` | 当前运行时路网、距离/路径矩阵 |
| `tools/build_town_routes.py`、`style_town_map.py` | 重建路网数据与游戏地图皮肤 |
| `game/images/`、`game/fonts/` | 实际运行资源；中文字体及许可已保存 |
| `docs/chapters/ch01/assets/` | 房屋/容量/地图设计、原始美术参考与生产素材 |
| `docs/chapters/ch02/` | 教程、路网、需求、地图风格与后续待办 |
| `docs/handoff/` | 本次完整性清单、测试证据与发布附件说明 |
| `tools/package_game.py` | macOS签名/打包工具；不能在Windows直接作为打包入口 |

第一章再生成：

```powershell
py -3 tools/export_story.py
py -3 tools/export_renpy.py
py -3 tools/test_unified_resources.py
```

## 4. 资源、归档与存档

Git主分支完整保存当前有效game源码/美术/地图/字体以及docs/tools。`docs/handoff/RESOURCE_MANIFEST.json`记录当前资源校验值；`py -3 tools/verify_handoff.py`检查克隆后文件是否缺失或改变。改动合法资源后，先验证功能，再执行 `py -3 tools/verify_handoff.py --write` 更新清单；不要用更新清单来掩盖缺文件。

发布页附件保留：Mac试玩ZIP、完整交接工程ZIP、文件校验清单。完整工程附带Mac运行时和172种历史game文件内容的去重归档。旧稿/旧图在恢复索引中可找回，不混入当前剧情或默认地图。原始旧程序和旧存档仍在Mac本地保留，私人存档不上传到代码仓库。

当前存档目录为 `Weiyuchoumou-Unified-V03`。Windows通常在 `%APPDATA%\RenPy\Weiyuchoumou-Unified-V03`；旧Demo各有独立目录。不要把旧目录混拷覆盖新目录，跨架构旧档兼容没有承诺。第二章旧状态有字段补充逻辑，但不能代替跨版本迁移验证。

云盘占位文件指名称可见但内容可能只在云端，需下载后才能校验。此次Git中上传的有效资源已核验可读；未核验的旧ZIP保持原位，未声称其内容已全部吸收，也未删除它们。

## 5. 已做验证及边界

- 模型9项、路网7项、集成资源3项，共19项通过；资源42项逐个校验，历史归档172项逐个校验。
- Mac原生Ren'Py：第一章A/B/C/D，B接Day6并到Day7；步行/SUV/电车；规划、行动结果、晚间结算三个位置存读档通过。测试结果保存于 `docs/handoff/native/`。
- Mac原生界面已检查第一章背景、资源浏览及第二章人物/家庭物资条；打包签名与Ren'Py lint通过。
- Windows、iPad安装包、触屏完整交互本轮均未制作或实机验证。当前Mac `.app`不能直接装到iPad；此前提出的有线平板试玩尚未完成，需以后另做iPad或浏览器发布方案。

## 6. 未完成与建议下一步

1. 先在Windows SDK打开当前原样工程，完成一轮平台验收；不要先换引擎或覆盖已有界面。
2. 扩写B线真正的支线：地下室防潮、院门加固、医疗采购、邻居/快递/墙外光伏等。现检查只记录进度，不等于维修已完成。任务需同时支持日期触发与到达地点触发；隐藏截止日按世界日期，成功/失败分支后仍能继续。
3. Day7—Day11准备日、危机广播/紧急状态章末尚待写；不要把Day7演示终点误认为后续章节已实现。
4. C线第二章尚未接入；不同路线初始资源差异仍待正式配置。
5. 接林晚宁父母的支线保留在PLANNING，尚未写定人名、接应时点或入住；当前家中仍4人。
6. 多队伍独立行动、网购截止日、完整工程施工/随机事件、正式物资平衡均未实现。

## 7. 开发环境与风险点

普通启动不需渲染依赖，PNG全部已提供。只在重绘地图/房屋时使用 `py -3 -m pip install -r requirements-dev.txt`；CairoSVG还需要系统Cairo库，Windows可能需另外安装，不把安装成功当现有功能已验收。旧地图/房屋SVG使用过Mac字体名，重绘时需确认中文字体。修改地图几何/入口后须重建矩阵与路线叠图并运行路网测试。

人物/物资状态由屏幕函数修改时需保留 `renpy.retain_after_load()`；不要改成原地修改字典。距离矩阵的汽车入口不同于步行入口，不能简单用地点像素直线距离替代。车辆不是全地图所有路段都可通行。旧资源清单中的Mac绝对路径是来源记录，不是运行依赖。

开发开始前 `git pull --ff-only`；结束时 `git status`，有选择地提交源码/素材/文档再 `git push`。不提交SDK、runtime、缓存、`.rpyc`、存档、密钥。发行包通过Release附件保存，仓库素材文件目前都小于GitHub普通Git单文件上限，未引入LFS。

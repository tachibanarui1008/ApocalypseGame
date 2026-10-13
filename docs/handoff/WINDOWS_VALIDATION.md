# Windows 0.3.0验收 · 2026-10-13

## 交付与一致性

- 基于Git提交`312491d`的Mac整合版0.3.0，在Windows打包同一份`game/`；未新增剧情或改变演出、地图、人物、库存配置。
- Ren'Py **8.5.3.26051504**，与Mac交接记录相同。官方SDK ZIP SHA256：`ff57648f9c04f27e381c48af6d8e3ee3cdec296bed4d3831f47f09b0a71b505e`，下载文件与官方清单一致。
- Windows发行包`ApocalypseGame-0.3.0-win.zip`，134257780字节（约128 MiB）。SHA256：`2ff06370a8f04f1d48913c8910933314022ca733a2b8644646da8af69ccffc8e`。
- ZIP内169项游戏源码/资源与当前`game/`逐文件字节一致。游戏层唯一修改为显式保留第二章运行时读取的`ch02_model.py`；其余平台适配是工具UTF-8编码、Git LF换行与新的构建/验收脚本。

## 实际Windows运行

测试环境为Windows 11（build 26200）、NVIDIA GeForce RTX 4070 Laptop GPU、OpenGL 4.6。使用从发行ZIP解压的Windows EXE，注入独立测试脚本，以Ren'Py官方测试框架执行原生屏幕与存档操作；独立存档目录，不使用或覆盖玩家存档。

- 原有19项测试通过：模型9、路网7、集成资源3；Ren'Py lint通过。
- 原生验收8项测试、46个断言全部通过，约41秒。原始结果见[日志](windows/test-output.txt)。
- A/B/C/D从开头走到章末，正确解锁对应成就。四条路线的完整场景序列与`docs/handoff/native/`中的Mac记录相同。
- B从第一章进入Day6；主菜单教程入口分别使用步行、燃油SUV、电车，走完采购、回家、下午洗漱、晚间结算，到Day7结束页。
- 确认80初始食品＋12采购−4消耗＝88人日；应急水仍240L；洗漱6L＋日饮水8L来自自来水；电车夜间充满；燃油SUV保留扣减后的油量。
- B与三种交通教程各在安排、行动结果、晚间结算三个位置保存并加载，状态逐字段一致；安排阶段额外修改购买数量后读回原值。
- 资源浏览入口可打开，42项资源完整。已实际查看主菜单、第一章开场、地图、人物/储备条和晚间结算截图，中文字体与主要布局正常。截图见[主菜单](windows/screenshots/main-menu.png)、[地图](windows/screenshots/B-walk-map.png)、[结算](windows/screenshots/T-ev-settlement.png)。

## 验证边界

测试属于Windows本机原生运行的自动交互验收，未声称在所有Windows机型、缩放设置、显卡或触屏上完成手工测试。旧Mac存档跨设备迁移、安装签名、iPad包、后续章节仍未验证或未实现。Mac没有在这台Windows机器上重新运行；内容一致性依据共享源码、资源校验与既有Mac场景序列记录。

演示库存与正式初始物资平衡保持原有边界，Day7是教程结束页，C线第二章尚未接入。发行包与SDK不进入Git，Windows包附加到现有v0.3.0 Release，不覆盖Mac包和历史交接附件。

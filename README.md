# ApocalypseGame

一个用于长期开发的跨平台末日生存文字冒险 / Galgame 项目。

计划使用 **Ren’Py**，以每日行动、地点探索、资源管理与剧情选择为核心，玩家的选择将影响各项状态并导向不同结局。

## 目标平台

- Windows
- macOS
- iOS / iPadOS
- Android

## 当前阶段

已建立项目仓库骨架、世界观设定集 V0.4，以及第一章《晦暗阴云》V1.0 的完整文本归档。第一章保持纯视觉小说；背景图与CG已整理文本提示词，图像、立绘及Ren’Py原型尚待制作，音乐留到最后统一生成。

## 文档索引

- [第一章《晦暗阴云》V1.0](docs/chapters/ch01/README.md)：完整主剧本、共通线与A/B/C/D分册、30个节点索引、26个背景与3个CG提示词、3个成就、修订摘录、变更日志、待定问题及校验记录。A/D为BAD END，B/C共通《长路归乡》；第二章《风暴前夜》未扩写。
- [《末日游戏》世界观设定集 V0.4](docs/WORLD_BIBLE.md)：整合 V0.3 世界观与 V0.4 家庭防灾历史，包含四口之家、住宅与能源、感染规则、社会失序、社区群像和序章第1—6天。

设定集为开发内部资料，含后期剧情剧透。编写剧情和程序时，请遵守文档中的「已确定 / 暂定 / 待讨论」标记及玩家信息揭示规则；暂定参数不能直接作为定稿。

## 跨设备协作

Mac 和 Windows 共用同一套源代码，通过这个私有 GitHub 仓库同步。

首次在另一台电脑上获取项目：

```sh
git clone https://github.com/tachibanarui1008/ApocalypseGame.git
cd ApocalypseGame
```

每次开始工作前运行 `git pull --ff-only`。完成修改后提交并推送：

```sh
git add .
git commit -m "Describe the changes"
git push
```

切换电脑前先提交并推送，避免同时在两台电脑上修改同一份文件。克隆私有仓库需要有访问权限的 GitHub 账号。

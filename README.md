# ApocalypseGame

一个用于长期开发的跨平台末日生存文字冒险 / Galgame 项目。

计划使用 **Ren’Py**，以每日行动、地点探索、资源管理与剧情选择为核心，玩家的选择将影响各项状态并导向不同结局。

## 目标平台

- Windows
- macOS
- iOS / iPadOS
- Android

## 当前阶段

目前仅建立项目仓库骨架，包含项目说明和 Git 忽略规则。后续逐步整理世界观、游戏机制、人物与剧情，再开发可玩的原型。

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

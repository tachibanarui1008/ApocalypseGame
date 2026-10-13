# GENERATED FILE — edit docs/chapters/ch01/SCRIPT.md, then regenerate.
# Generator: python3 tools/export_renpy.py
# Source: docs/chapters/ch01/SCRIPT.md
# SHA-256: e53219f00f6097e0565de0dc3f9b40b1eae78ef4c674b660b992dde9cfc1df72
# Visual cues: game/data/ch01_presentation.json; chapter dialogue is unchanged.
# Requires n, char_protagonist, char_partner, char_father, char_mother, route_end.

define story_choice_descriptions = {"查阅官方消息": "与其相信网络视频，不如看看官方究竟怎么说。", "联系庐州市的父母": "不管消息是真是假，先让家里检查一下应急物资。", "先与伴侣商量": "这件事或许值得认真对待。至少应该两个人一起决定。", "暂时不予理会": "现在还没有任何可靠结论。先把今天的工作做好。"}

label ch01_001:
    $ current_scene_id = "CH01-001"
    $ current_scene_title = "清晨"
    $ current_scene_time = "Day 1，07:15"
    $ current_scene_location = "沪海市，主角租住的公寓"
    $ phone_mode = False
    $ c1_scene("CH01-001")
    $ c1_before("CH01-001", 0, "")
    n "窗帘没有完全拉紧。"
    $ c1_before("CH01-001", 1, "")
    n "从缝隙透进来的阳光落在地板上，将房间分成明暗两半。"
    $ c1_before("CH01-001", 2, "")
    n "床头柜上的手机震动了几下。"
    $ c1_before("CH01-001", 3, "")
    n "你伸出手，在桌面上摸索了一阵，终于按掉闹钟。"
    $ c1_before("CH01-001", 4, "")
    n "房间恢复了安静。"
    $ c1_before("CH01-001", 5, "林晚宁")
    char_partner "“……几点了？”"
    $ c1_before("CH01-001", 6, "陈知远")
    char_protagonist "“七点一刻。”"
    $ c1_before("CH01-001", 7, "林晚宁")
    char_partner "“再睡五分钟。”"
    $ c1_before("CH01-001", 8, "陈知远")
    char_protagonist "“昨天也是这么说的。”"
    $ c1_before("CH01-001", 9, "林晚宁")
    char_partner "“昨天不是起来了吗。”"
    $ c1_before("CH01-001", 10, "")
    n "你看了她一眼。"
    $ c1_before("CH01-001", 11, "")
    n "她已经重新把脸埋进枕头里。"
    $ c1_before("CH01-001", 12, "")
    n "你没有继续争辩。"
    $ c1_before("CH01-001", 13, "")
    n "拿起手机，锁屏上堆着十几条通知。"
    $ c1_before("CH01-001", 14, "")
    n "工作群。"
    $ c1_before("CH01-001", 15, "")
    n "购物软件。"
    $ c1_before("CH01-001", 16, "")
    n "天气预报。"
    $ c1_before("CH01-001", 17, "")
    n "还有几条凌晨推送的新闻。"
    $ c1_before("CH01-001", 18, "")
    n "你漫不经心地向上划动。"
    $ c1_before("CH01-001", 19, "")
    n "其中一条消息引起了你的注意。"
    $ c1_before("CH01-001", 20, "")
    $ phone_mode = True
    $ phone_speaker = "新闻"
    $ phone_text = "《东部某市一医院发生突发事件，警方已介入调查》"
    n "《东部某市一医院发生突发事件，警方已介入调查》"
    $ phone_mode = False
    $ c1_before("CH01-001", 21, "")
    n "新闻发布于凌晨03:41。"
    $ c1_before("CH01-001", 22, "")
    n "正文只有寥寥几行。"
    $ c1_before("CH01-001", 23, "")
    $ phone_mode = True
    $ phone_speaker = "新闻"
    $ phone_text = "昨日晚间，东部某市一医疗机构发生突发事件，造成多人受伤。有关部门已介入调查，具体情况正在核实。"
    n "昨日晚间，东部某市一医疗机构发生突发事件，造成多人受伤。有关部门已介入调查，具体情况正在核实。"
    $ phone_mode = False
    $ c1_before("CH01-001", 24, "")
    n "评论区里有人贴出一张模糊的照片。"
    $ c1_before("CH01-001", 25, "")
    n "似乎是一家医院的急诊入口。"
    $ c1_before("CH01-001", 26, "")
    n "警灯将建筑外墙照成红蓝两色。"
    $ c1_before("CH01-001", 27, "")
    n "但照片中看不到具体发生了什么。"
    $ c1_before("CH01-001", 28, "")
    n "你又翻了几条评论。"
    $ c1_before("CH01-001", 29, "")
    n "“听说医院都封了。”"
    $ c1_before("CH01-001", 30, "")
    n "“别乱传，具体情况还没出来。”"
    $ c1_before("CH01-001", 31, "")
    n "“有人说是医患冲突。”"
    $ c1_before("CH01-001", 32, "")
    n "“半夜三点发这种新闻，真够吓人的。”"
    $ c1_before("CH01-001", 33, "")
    n "你退出新闻页面。"
    $ c1_before("CH01-001", 34, "")
    n "又有一条工作消息弹了出来。"
    $ c1_before("CH01-001", 35, "")
    $ phone_mode = True
    $ phone_speaker = "讯息"
    $ phone_text = "“今天九点半例会，大家记得提前准备材料。”"
    n "“今天九点半例会，大家记得提前准备材料。”"
    $ phone_mode = False
    $ c1_before("CH01-001", 36, "")
    n "你看了一眼时间。"
    $ c1_before("CH01-001", 37, "")
    n "07:23。"
    $ c1_before("CH01-001", 38, "林晚宁")
    char_partner "“你还不起床？”"
    $ c1_before("CH01-001", 39, "陈知远")
    char_protagonist "“起来了。”"
    $ c1_before("CH01-001", 40, "林晚宁")
    char_partner "“那帮我把咖啡弄一下。”"
    $ c1_before("CH01-001", 41, "陈知远")
    char_protagonist "“好。”"
    jump ch01_002

label ch01_002:
    $ current_scene_id = "CH01-002"
    $ current_scene_title = "早餐"
    $ current_scene_time = "07:38"
    $ current_scene_location = "公寓厨房及餐厅"
    $ phone_mode = False
    $ c1_scene("CH01-002")
    $ c1_before("CH01-002", 0, "")
    n "水壶发出轻微的响声。"
    $ c1_before("CH01-002", 1, "")
    n "你把两杯咖啡放到桌上。"
    $ c1_before("CH01-002", 2, "")
    n "早餐是面包、煎蛋和冰箱里剩下的半盒牛奶。"
    $ c1_before("CH01-002", 3, "")
    n "伴侣坐在对面，一边吃东西，一边检查手机上的日程。"
    $ c1_before("CH01-002", 4, "林晚宁")
    char_partner "“今天晚上要不要在外面吃？”"
    $ c1_before("CH01-002", 5, "陈知远")
    char_protagonist "“怎么突然想在外面吃？”"
    $ c1_before("CH01-002", 6, "林晚宁")
    char_partner "“冰箱没什么菜了。”"
    $ c1_before("CH01-002", 7, "陈知远")
    char_protagonist "“那下班去超市？”"
    $ c1_before("CH01-002", 8, "林晚宁")
    char_partner "“也行。”"
    $ c1_before("CH01-002", 9, "")
    n "她放下手机。"
    $ c1_before("CH01-002", 10, "林晚宁")
    char_partner "“对了，叔叔阿姨最近怎么样？”"
    $ c1_before("CH01-002", 11, "陈知远")
    char_protagonist "“挺好的。我爸昨天还给我发照片。”"
    $ c1_before("CH01-002", 12, "林晚宁")
    char_partner "“什么照片？”"
    $ c1_before("CH01-002", 13, "陈知远")
    char_protagonist "“乡下那套房子。他又去整理地下室了。”"
    $ c1_before("CH01-002", 14, "林晚宁")
    char_partner "“那地方不是上个月刚整理过？”"
    $ c1_before("CH01-002", 15, "陈知远")
    char_protagonist "“他说把储物架重新固定了一遍。”"
    $ c1_before("CH01-002", 16, "林晚宁")
    char_partner "“叔叔还挺有精力。”"
    $ c1_before("CH01-002", 17, "")
    n "你笑了笑。"
    $ c1_before("CH01-002", 18, "")
    n "那栋房子购置于几年前。"
    $ c1_before("CH01-002", 19, "")
    n "当时庐州市周边接连发生小规模地震。"
    $ c1_before("CH01-002", 20, "")
    n "虽然没有造成严重损失，但父母还是认真考虑起了家庭应急避险的问题。"
    $ c1_before("CH01-002", 21, "")
    n "后来，他们在城郊置办了一套三层独栋住宅。"
    $ c1_before("CH01-002", 22, "")
    n "经过修缮，地下室被改成储物空间，屋顶安装了光伏，院子里还配备了备用能源设施。"
    $ c1_before("CH01-002", 23, "")
    n "父母平时仍住在庐州市区。"
    $ c1_before("CH01-002", 24, "")
    n "那栋房子更多时候只是一个备用住所。"
    $ c1_before("CH01-002", 25, "林晚宁")
    char_partner "“其实有备无患也挺好的。”"
    $ c1_before("CH01-002", 26, "陈知远")
    char_protagonist "“我爸就是这个想法。”"
    $ c1_before("CH01-002", 27, "林晚宁")
    char_partner "“地下室的罐头还没过期吧？”"
    $ c1_before("CH01-002", 28, "陈知远")
    char_protagonist "“我妈管着呢。她比谁都清楚。”"
    $ c1_before("CH01-002", 29, "林晚宁")
    char_partner "“也是，阿姨做护士，肯定比我们细心。”"
    $ c1_before("CH01-002", 30, "")
    n "你喝了一口咖啡。"
    $ c1_before("CH01-002", 31, "陈知远")
    char_protagonist "“我爸倒是更关心那些米面粮油。”"
    $ c1_before("CH01-002", 32, "林晚宁")
    char_partner "“开餐厅的职业习惯？”"
    $ c1_before("CH01-002", 33, "陈知远")
    char_protagonist "“差不多。”"
    $ c1_before("CH01-002", 34, "林晚宁")
    char_partner "“你也没好到哪里去。不是还弄了台 Mac mini，当你的‘末日服务器’？”"
    $ c1_before("CH01-002", 35, "陈知远")
    char_protagonist "“平时也用得上。”"
    $ c1_before("CH01-002", 36, "林晚宁")
    char_partner "“叔叔肯定也这么说。”"
    $ c1_before("CH01-002", 37, "")
    n "你笑了笑。"
    $ c1_before("CH01-002", 38, "陈知远")
    char_protagonist "“那会儿你不也弄了一套无线电？说手机没信号的时候，总得留个办法。”"
    $ c1_before("CH01-002", 39, "林晚宁")
    char_partner "“有备无患嘛。”"
    $ c1_before("CH01-002", 40, "陈知远")
    char_protagonist "“那就别光笑我爸了。”"
    $ c1_before("CH01-002", 41, "")
    n "她端起咖啡，嘴角还带着笑。"
    $ c1_before("CH01-002", 42, "")
    n "两人继续吃早餐。"
    $ c1_before("CH01-002", 43, "")
    n "窗外的道路已经堵了起来。"
    $ c1_before("CH01-002", 44, "")
    n "一辆公交车停在路口，后面排着长长的车队。"
    $ c1_before("CH01-002", 45, "")
    n "远处传来汽车喇叭声。"
    $ c1_before("CH01-002", 46, "")
    n "又一个再普通不过的工作日。"
    jump ch01_003

label ch01_003:
    $ current_scene_id = "CH01-003"
    $ current_scene_title = "风声"
    $ current_scene_time = "08:12"
    $ current_scene_location = "沪海市，通勤途中"
    $ phone_mode = False
    $ c1_scene("CH01-003")
    $ c1_before("CH01-003", 0, "")
    n "你和伴侣一起离开公寓。"
    $ c1_before("CH01-003", 1, "")
    n "街边停着共享单车。"
    $ c1_before("CH01-003", 2, "")
    n "早餐店门口排着队。"
    $ c1_before("CH01-003", 3, "")
    n "几个学生一边吃包子，一边匆匆向路口跑去。"
    $ c1_before("CH01-003", 4, "林晚宁")
    char_partner "“我从这边走了。”"
    $ c1_before("CH01-003", 5, "陈知远")
    char_protagonist "“晚上见。”"
    $ c1_before("CH01-003", 6, "林晚宁")
    char_partner "“别忘了买菜。”"
    $ c1_before("CH01-003", 7, "陈知远")
    char_protagonist "“知道了。”"
    $ c1_before("CH01-003", 8, "")
    n "她挥了挥手，走向另一侧的地铁入口。"
    $ c1_before("CH01-003", 9, "")
    n "你沿着人行道继续往前走。"
    $ c1_before("CH01-003", 10, "")
    n "手机震动了一下。"
    $ c1_before("CH01-003", 11, "普通朋友")
    $ phone_mode = True
    $ phone_speaker = "普通朋友"
    $ phone_text = "“看今天那个医院的视频了吗？”"
    n "“看今天那个医院的视频了吗？”"
    $ phone_mode = False
    $ c1_before("CH01-003", 12, "")
    n "对方发来一段十五秒左右的录像。"
    $ c1_before("CH01-003", 13, "")
    n "画面来自一条医院走廊。"
    $ c1_before("CH01-003", 14, "")
    n "拍摄者站得很远。"
    $ c1_before("CH01-003", 15, "")
    n "几名工作人员正在试图控制一个不断挣扎的人。"
    $ c1_before("CH01-003", 16, "")
    n "有人喊着让其他人退后。"
    $ c1_before("CH01-003", 17, "")
    n "镜头猛烈晃动了一下。"
    $ c1_before("CH01-003", 18, "")
    n "一阵尖叫声之后，录像突然结束。"
    $ c1_before("CH01-003", 19, "普通朋友")
    n "普通朋友：“听说有人在医院咬伤了好几个医护。”"
    $ c1_before("CH01-003", 20, "陈知远")
    char_protagonist "“真的假的？”"
    $ c1_before("CH01-003", 21, "普通朋友")
    n "普通朋友：“不知道。几个群里都在传。”"
    $ c1_before("CH01-003", 22, "普通朋友")
    n "普通朋友：“有人说吸毒，有人说精神疾病。”"
    $ c1_before("CH01-003", 23, "")
    n "你重新看了一遍。"
    $ c1_before("CH01-003", 24, "")
    n "视频太模糊。"
    $ c1_before("CH01-003", 25, "")
    n "无法确定拍摄时间，也看不清参与者的面孔。"
    $ c1_before("CH01-003", 26, "")
    n "你想起早晨看到的那条新闻。"
    $ c1_before("CH01-003", 27, "")
    n "随后打开另一个聊天窗口。"
    $ c1_before("CH01-003", 28, "")
    n "联系人是一位在沪海市医院系统工作的老朋友。"
    $ c1_before("CH01-003", 29, "陈知远")
    $ phone_mode = True
    $ phone_speaker = "陈知远"
    $ phone_text = "“在吗？问你个事。”"
    n "“在吗？问你个事。”"
    $ phone_mode = False
    $ c1_before("CH01-003", 30, "")
    n "过了一会儿。"
    $ c1_before("CH01-003", 31, "医院朋友")
    $ phone_mode = True
    $ phone_speaker = "医院朋友"
    $ phone_text = "“咋了？”"
    n "“咋了？”"
    $ phone_mode = False
    $ c1_before("CH01-003", 32, "陈知远")
    $ phone_mode = True
    $ phone_speaker = "陈知远"
    $ phone_text = "“今天网上那个医院视频你看过没？”"
    n "“今天网上那个医院视频你看过没？”"
    $ phone_mode = False
    $ c1_before("CH01-003", 33, "")
    n "几分钟后。"
    $ c1_before("CH01-003", 34, "医院朋友")
    $ phone_mode = True
    $ phone_speaker = "医院朋友"
    $ phone_text = "“看过。”"
    n "“看过。”"
    $ phone_mode = False
    $ c1_before("CH01-003", 35, "陈知远")
    $ phone_mode = True
    $ phone_speaker = "陈知远"
    $ phone_text = "“真的假的？”"
    n "“真的假的？”"
    $ phone_mode = False
    $ c1_before("CH01-003", 36, "医院朋友")
    $ phone_mode = True
    $ phone_speaker = "医院朋友"
    $ phone_text = "“视频本身我不知道真假，也不是我们医院。”"
    n "“视频本身我不知道真假，也不是我们医院。”"
    $ phone_mode = False
    $ c1_before("CH01-003", 37, "陈知远")
    $ phone_mode = True
    $ phone_speaker = "陈知远"
    $ phone_text = "“最近医院有什么不对劲的吗？”"
    n "“最近医院有什么不对劲的吗？”"
    $ phone_mode = False
    $ c1_before("CH01-003", 38, "医院朋友")
    $ phone_mode = True
    $ phone_speaker = "医院朋友"
    $ phone_text = "“最近发热门诊的事比较多。”"
    n "“最近发热门诊的事比较多。”"
    $ phone_mode = False
    $ c1_before("CH01-003", 39, "医院朋友")
    $ phone_mode = True
    $ phone_speaker = "医院朋友"
    $ phone_text = "“院里这两天在重新检查防护物资，异常病例的上报也抓得比较紧。”"
    n "“院里这两天在重新检查防护物资，异常病例的上报也抓得比较紧。”"
    $ phone_mode = False
    $ c1_before("CH01-003", 40, "陈知远")
    $ phone_mode = True
    $ phone_speaker = "陈知远"
    $ phone_text = "“又是什么传染病？”"
    n "“又是什么传染病？”"
    $ phone_mode = False
    $ c1_before("CH01-003", 41, "医院朋友")
    $ phone_mode = True
    $ phone_speaker = "医院朋友"
    $ phone_text = "“现在没有明确说法。”"
    n "“现在没有明确说法。”"
    $ phone_mode = False
    $ c1_before("CH01-003", 42, "医院朋友")
    $ phone_mode = True
    $ phone_speaker = "医院朋友"
    $ phone_text = "“有些地方发现了不明原因肺炎病例，调查还在做。”"
    n "“有些地方发现了不明原因肺炎病例，调查还在做。”"
    $ phone_mode = False
    $ c1_before("CH01-003", 43, "陈知远")
    $ phone_mode = True
    $ phone_speaker = "陈知远"
    $ phone_text = "“跟那个咬人的事有关？”"
    n "“跟那个咬人的事有关？”"
    $ phone_mode = False
    $ c1_before("CH01-003", 44, "医院朋友")
    $ phone_mode = True
    $ phone_speaker = "医院朋友"
    $ phone_text = "“不知道。”"
    n "“不知道。”"
    $ phone_mode = False
    $ c1_before("CH01-003", 45, "医院朋友")
    $ phone_mode = True
    $ phone_speaker = "医院朋友"
    $ phone_text = "“你别把网上传的东西全串起来。”"
    n "“你别把网上传的东西全串起来。”"
    $ phone_mode = False
    $ c1_before("CH01-003", 46, "医院朋友")
    $ phone_mode = True
    $ phone_speaker = "医院朋友"
    $ phone_text = "“不过家里常用的药、口罩这些，可以先检查一下。缺的补一点，别等真要用的时候再找。”"
    n "“不过家里常用的药、口罩这些，可以先检查一下。缺的补一点，别等真要用的时候再找。”"
    $ phone_mode = False
    $ c1_before("CH01-003", 47, "陈知远")
    $ phone_mode = True
    $ phone_speaker = "陈知远"
    $ phone_text = "“行。”"
    n "“行。”"
    $ phone_mode = False
    $ c1_before("CH01-003", 48, "医院朋友")
    $ phone_mode = True
    $ phone_speaker = "医院朋友"
    $ phone_text = "“不过最近没必要的话，确实少往医院跑。”"
    n "“不过最近没必要的话，确实少往医院跑。”"
    $ phone_mode = False
    $ c1_before("CH01-003", 49, "陈知远")
    $ phone_mode = True
    $ phone_speaker = "陈知远"
    $ phone_text = "“你自己也注意点。”"
    n "“你自己也注意点。”"
    $ phone_mode = False
    $ c1_before("CH01-003", 50, "医院朋友")
    $ phone_mode = True
    $ phone_speaker = "医院朋友"
    $ phone_text = "“放心吧。”"
    n "“放心吧。”"
    $ phone_mode = False
    $ c1_before("CH01-003", 51, "")
    n "你收起手机。"
    $ c1_before("CH01-003", 52, "")
    n "红灯转绿。"
    $ c1_before("CH01-003", 53, "")
    n "人群开始穿过路口。"
    $ c1_before("CH01-003", 54, "")
    n "一个骑电动车的外卖员停在人行横道边，低头看着导航。"
    $ c1_before("CH01-003", 55, "")
    n "身后的车流没有停过。"
    $ c1_before("CH01-003", 56, "")
    n "你突然意识到，自己已经站在原地很久了。"
    $ c1_before("CH01-003", 57, "")
    n "08:28"
    $ c1_before("CH01-003", 58, "")
    n "距离上班还有一段时间。"
    $ c1_before("CH01-003", 59, "")
    n "你决定……"
    jump ch01_004

label ch01_004:
    $ current_scene_id = "CH01-004"
    $ current_scene_title = "第一次选择"
    $ current_scene_time = ""
    $ current_scene_location = ""
    $ phone_mode = False
    $ c1_scene("CH01-004")
    menu:
        "查阅官方消息":
            $ chapter_route = "A"
            jump ch01_a01
        "联系庐州市的父母":
            $ chapter_route = "B"
            jump ch01_b01
        "先与伴侣商量":
            $ chapter_route = "C"
            jump ch01_c01
        "暂时不予理会":
            $ chapter_route = "D"
            jump ch01_d01

label ch01_a01:
    $ current_scene_id = "CH01-A01"
    $ current_scene_title = "新型肺炎"
    $ current_scene_time = "Day 1，08:30"
    $ current_scene_location = ""
    $ phone_mode = False
    $ c1_scene("CH01-A01")
    $ c1_before("CH01-A01", 0, "")
    n "你打开新闻软件。"
    $ c1_before("CH01-A01", 1, "")
    n "搜索栏里输入了“不明原因肺炎”。"
    $ c1_before("CH01-A01", 2, "")
    n "搜索结果很快出现。"
    $ c1_before("CH01-A01", 3, "")
    n "最新的一条来自龙国卫生主管部门。"
    $ c1_before("CH01-A01", 4, "")
    $ phone_mode = True
    $ phone_speaker = "新闻"
    $ phone_text = "《关于近期部分地区不明原因肺炎病例的情况通报》"
    n "《关于近期部分地区不明原因肺炎病例的情况通报》"
    $ phone_mode = False
    $ c1_before("CH01-A01", 5, "")
    $ phone_mode = True
    $ phone_speaker = "新闻"
    $ phone_text = "近期，部分地区报告了由新型病原体引起的肺炎病例。有关部门正组织开展流行病学调查、病例救治及病原学研究。\n\n目前，相关病例的临床表现及传播特征尚在进一步调查中。建议公众保持良好卫生习惯，及时关注官方发布的信息。"
    n "近期，部分地区报告了由新型病原体引起的肺炎病例。有关部门正组织开展流行病学调查、病例救治及病原学研究。\n\n目前，相关病例的临床表现及传播特征尚在进一步调查中。建议公众保持良好卫生习惯，及时关注官方发布的信息。"
    $ phone_mode = False
    $ c1_before("CH01-A01", 6, "")
    n "你看完通报，又往下翻了几条新闻。"
    $ c1_before("CH01-A01", 7, "")
    n "大部分媒体都采用了相似的标题。"
    $ c1_before("CH01-A01", 8, "")
    n "“新型肺炎”。"
    $ c1_before("CH01-A01", 9, "")
    n "“加强个人防护”。"
    $ c1_before("CH01-A01", 10, "")
    n "“相关部门正在调查”。"
    $ c1_before("CH01-A01", 11, "")
    n "你对这些词并不陌生。"
    $ c1_before("CH01-A01", 12, "")
    n "几年前，人们曾经反复听到过类似的提醒。"
    $ c1_before("CH01-A01", 13, "")
    n "当时许多人的生活被改变了很长一段时间。"
    $ c1_before("CH01-A01", 14, "")
    n "想到这里，你决定先买些口罩。"
    $ c1_before("CH01-A01", 15, "")
    $ phone_mode = True
    $ phone_speaker = "讯息"
    $ phone_text = "搜索：医用外科口罩。"
    n "搜索：医用外科口罩。"
    $ phone_mode = False
    $ c1_before("CH01-A01", 16, "")
    n "商品页面加载出来。"
    $ c1_before("CH01-A01", 17, "")
    n "你愣了一下。"
    $ c1_before("CH01-A01", 18, "")
    n "一盒平时二十多元的口罩，现在标价已经超过一百元。"
    $ c1_before("CH01-A01", 19, "")
    n "有几家店铺甚至显示售罄。"
    $ c1_before("CH01-A01", 20, "陈知远")
    char_protagonist "“操，怎么又涨成这样了。”"
    $ c1_before("CH01-A01", 21, "")
    n "你又翻了几家。"
    $ c1_before("CH01-A01", 22, "")
    n "价格都差不多。"
    $ c1_before("CH01-A01", 23, "")
    n "犹豫片刻，你还是买下了几盒口罩，又添了些消毒用品。"
    $ c1_before("CH01-A01", 24, "")
    $ phone_mode = True
    $ phone_speaker = "讯息"
    $ phone_text = "订单已提交。"
    n "订单已提交。"
    $ phone_mode = False
    $ c1_before("CH01-A01", 25, "")
    $ phone_mode = True
    $ phone_speaker = "讯息"
    $ phone_text = "预计后日送达。"
    n "预计后日送达。"
    $ phone_mode = False
    $ c1_before("CH01-A01", 26, "")
    n "地铁进站的提示音响起。"
    $ c1_before("CH01-A01", 27, "")
    n "你跟着人群向前移动。"
    $ c1_before("CH01-A01", 28, "")
    n "车厢里有不少乘客已经戴上口罩。"
    $ c1_before("CH01-A01", 29, "")
    n "一个年轻人正在和朋友聊天。"
    $ c1_before("CH01-A01", 30, "乘客甲")
    n "乘客甲：“不会又要开始吧？”"
    $ c1_before("CH01-A01", 31, "乘客乙")
    n "乘客乙：“谁知道。反正口罩先备着。”"
    $ c1_before("CH01-A01", 32, "乘客甲")
    n "乘客甲：“我妈刚才还让我少坐地铁。”"
    $ c1_before("CH01-A01", 33, "")
    n "你站在门边，看着窗玻璃上映出的自己。"
    $ c1_before("CH01-A01", 34, "")
    n "手机信号短暂地消失了。"
    jump ch01_a02

label ch01_a02:
    $ current_scene_id = "CH01-A02"
    $ current_scene_title = "正常生活的代价"
    $ current_scene_time = "Day 2，20:16"
    $ current_scene_location = "沪海市公寓"
    $ phone_mode = False
    $ c1_scene("CH01-A02")
    $ c1_before("CH01-A02", 0, "")
    n "餐桌上堆着几盒刚刚送来的口罩。"
    $ c1_before("CH01-A02", 1, "")
    n "伴侣正在拆开快递。"
    $ c1_before("CH01-A02", 2, "林晚宁")
    char_partner "“你怎么一下买了这么多？”"
    $ c1_before("CH01-A02", 3, "陈知远")
    char_protagonist "“最近情况不太对，先备点。”"
    $ c1_before("CH01-A02", 4, "林晚宁")
    char_partner "“还买了酒精？”"
    $ c1_before("CH01-A02", 5, "陈知远")
    char_protagonist "“嗯。”"
    $ c1_before("CH01-A02", 6, "林晚宁")
    char_partner "“你觉得这次会像上一次那样吗？”"
    $ c1_before("CH01-A02", 7, "")
    n "你没有马上回答。"
    $ c1_before("CH01-A02", 8, "")
    n "电视里正播放当天的晚间新闻。"
    $ c1_before("CH01-A02", 9, "")
    n "主持人介绍着有关部门开展公共卫生调查的最新进展。"
    $ c1_before("CH01-A02", 10, "")
    n "画面中，一名工作人员站在医院门口接受采访。"
    $ c1_before("CH01-A02", 11, "")
    n "身后是整齐停放的救护车。"
    $ c1_before("CH01-A02", 12, "")
    n "你看了一会儿。"
    $ c1_before("CH01-A02", 13, "陈知远")
    char_protagonist "“不知道。”"
    $ c1_before("CH01-A02", 14, "陈知远")
    char_protagonist "“但感觉不像什么小事。”"
    $ c1_before("CH01-A02", 15, "林晚宁")
    char_partner "“那我们要不要回庐州？”"
    $ c1_before("CH01-A02", 16, "")
    n "你拿起手机，打开地图。"
    $ c1_before("CH01-A02", 17, "")
    n "沪海市到庐州市。"
    $ c1_before("CH01-A02", 18, "")
    n "导航显示高速路况基本正常。"
    $ c1_before("CH01-A02", 19, "陈知远")
    char_protagonist "“可以考虑。”"
    $ c1_before("CH01-A02", 20, "林晚宁")
    char_partner "“明天走？”"
    $ c1_before("CH01-A02", 21, "")
    n "你想起公司里还没处理完的工作。"
    $ c1_before("CH01-A02", 22, "")
    n "还有一些东西没有收拾。"
    $ c1_before("CH01-A02", 23, "陈知远")
    char_protagonist "“先把东西备齐吧。总不能什么都不带。”"
    $ c1_before("CH01-A02", 24, "林晚宁")
    char_partner "“也是。”"
    $ c1_before("CH01-A02", 25, "")
    n "她把口罩放进柜子。"
    $ c1_before("CH01-A02", 26, "林晚宁")
    char_partner "“那我们明天下班去趟超市？”"
    $ c1_before("CH01-A02", 27, "陈知远")
    char_protagonist "“好。”"
    $ c1_before("CH01-A02", 28, "")
    n "电视里的新闻结束了。"
    $ c1_before("CH01-A02", 29, "")
    n "接下来是一档娱乐节目。"
    $ c1_before("CH01-A02", 30, "")
    n "屏幕上响起欢快的掌声。"
    $ c1_before("CH01-A02", 31, "")
    n "你把音量调低了一点。"
    jump ch01_a03

label ch01_a03:
    $ current_scene_id = "CH01-A03"
    $ current_scene_title = "准备"
    $ current_scene_time = "Day 3—Day 4"
    $ current_scene_location = ""
    $ phone_mode = False
    $ c1_scene("CH01-A03")
    $ c1_before("CH01-A03", 0, "")
    n "你推着购物车，从一排排货架间经过。"
    $ c1_before("CH01-A03", 1, "")
    n "罐头、方便食品、瓶装水、卫生用品。"
    $ c1_before("CH01-A03", 2, "")
    n "购物车很快装满了。"
    $ c1_before("CH01-A03", 3, "")
    n "旁边的货架前站着几名顾客。"
    $ c1_before("CH01-A03", 4, "")
    n "他们低声讨论着最近的新闻。"
    $ c1_before("CH01-A03", 5, "顾客甲")
    n "顾客甲：“昨天我们小区有人发烧，居委会都上门了。”"
    $ c1_before("CH01-A03", 6, "顾客乙")
    n "顾客乙：“现在发烧不是挺正常的吗？”"
    $ c1_before("CH01-A03", 7, "顾客甲")
    n "顾客甲：“谁知道。”"
    $ c1_before("CH01-A03", 8, "")
    n "结账时，收银员告诉你，一部分商品已经开始限购。"
    $ c1_before("CH01-A03", 9, "")
    n "你没有争论。"
    $ c1_before("CH01-A03", 10, "")
    n "把买到的东西搬上车，随后返回公寓。"
    $ c1_before("CH01-A03", 11, "")
    n "地板上摆着几箱饮用水。"
    $ c1_before("CH01-A03", 12, "")
    n "餐桌下面塞满了罐头和饼干。"
    $ c1_before("CH01-A03", 13, "")
    n "伴侣正蹲在行李箱旁整理衣物。"
    $ c1_before("CH01-A03", 14, "林晚宁")
    char_partner "“你看这些够不够？”"
    $ c1_before("CH01-A03", 15, "陈知远")
    char_protagonist "“应该差不多。”"
    $ c1_before("CH01-A03", 16, "林晚宁")
    char_partner "“我们到底什么时候走？”"
    $ c1_before("CH01-A03", 17, "")
    n "你看了一眼手机。"
    $ c1_before("CH01-A03", 18, "")
    n "白天，公司临时通知下周部分岗位可以居家办公。"
    $ c1_before("CH01-A03", 19, "")
    n "新闻里也开始出现更多城市实施交通限制的消息。"
    $ c1_before("CH01-A03", 20, "陈知远")
    char_protagonist "“再等一天吧。”"
    $ c1_before("CH01-A03", 21, "林晚宁")
    char_partner "“为什么？”"
    $ c1_before("CH01-A03", 22, "陈知远")
    char_protagonist "“还有两个快递没到。”"
    $ c1_before("CH01-A03", 23, "林晚宁")
    char_partner "“那些东西也不是必须的。”"
    $ c1_before("CH01-A03", 24, "陈知远")
    char_protagonist "“主要是我想再看看外面的情况。”"
    $ c1_before("CH01-A03", 25, "")
    n "她没有继续追问。"
    $ c1_before("CH01-A03", 26, "")
    n "只是把行李箱拉链拉好。"
    $ c1_before("CH01-A03", 27, "")
    n "过了一会儿，她忽然说道："
    $ c1_before("CH01-A03", 28, "林晚宁")
    char_partner "“你要是真想回去，我们可以不要那些快递。”"
    $ c1_before("CH01-A03", 29, "")
    n "你看着地上的物资。"
    $ c1_before("CH01-A03", 30, "陈知远")
    char_protagonist "“嗯。明天再决定。”"
    $ c1_before("CH01-A03", 31, "")
    n "手机上的新闻推送越来越频繁。"
    $ c1_before("CH01-A03", 32, "")
    n "有些道路开始设置临时检查点。"
    $ c1_before("CH01-A03", 33, "")
    n "几处大型交通枢纽调整了运营安排。"
    $ c1_before("CH01-A03", 34, "")
    n "你终于给父母打去电话。"
    $ c1_before("CH01-A03", 35, "陈建川")
    char_father "“最近你们那边是不是挺乱的？”"
    $ c1_before("CH01-A03", 36, "陈知远")
    char_protagonist "“有点。我准备回去。”"
    $ c1_before("CH01-A03", 37, "陈建川")
    char_father "“那就早点走。”"
    $ c1_before("CH01-A03", 38, "陈知远")
    char_protagonist "“嗯。东西已经收拾得差不多了。”"
    $ c1_before("CH01-A03", 39, "陈建川")
    char_father "“乡下房子前段时间刚检查过。你们回来有地方住。”"
    $ c1_before("CH01-A03", 40, "陈知远")
    char_protagonist "“知道。”"
    $ c1_before("CH01-A03", 41, "陈建川")
    char_father "“路上注意安全。”"
    $ c1_before("CH01-A03", 42, "")
    n "你挂断电话。"
    $ c1_before("CH01-A03", 43, "")
    n "又一次打开地图。"
    $ c1_before("CH01-A03", 44, "")
    n "几条原本通畅的道路已经变成了红色。"
    $ c1_before("CH01-A03", 45, "")
    n "你盯着屏幕看了一会儿。"
    $ c1_before("CH01-A03", 46, "")
    n "然后把手机扣在桌上。"
    $ c1_before("CH01-A03", 47, "陈知远")
    char_protagonist "“明天一早走。”"
    jump ch01_a04

label ch01_a04:
    $ current_scene_id = "CH01-A04"
    $ current_scene_title = "出城"
    $ current_scene_time = "Day 5，06:40"
    $ current_scene_location = "沪海市外围道路"
    $ phone_mode = False
    $ c1_scene("CH01-A04")
    $ c1_before("CH01-A04", 0, "")
    n "天刚亮。"
    $ c1_before("CH01-A04", 1, "")
    n "你们把最后一箱物资放进后备厢。"
    $ c1_before("CH01-A04", 2, "")
    n "新能源轿车的电量显示为97%%。"
    $ c1_before("CH01-A04", 3, "")
    n "伴侣坐进副驾驶。"
    $ c1_before("CH01-A04", 4, "林晚宁")
    char_partner "“爸妈知道我们今天走吗？”"
    $ c1_before("CH01-A04", 5, "陈知远")
    char_protagonist "“说了。”"
    $ c1_before("CH01-A04", 6, "林晚宁")
    char_partner "“那就好。”"
    $ c1_before("CH01-A04", 7, "")
    n "你启动汽车。"
    $ c1_before("CH01-A04", 8, "")
    n "导航开始规划路线。"
    $ c1_before("CH01-A04", 9, "")
    $ phone_mode = True
    $ phone_speaker = "讯息"
    $ phone_text = "目的地：庐州市城郊住宅。"
    n "目的地：庐州市城郊住宅。"
    $ phone_mode = False
    $ c1_before("CH01-A04", 10, "")
    $ phone_mode = True
    $ phone_speaker = "讯息"
    $ phone_text = "预计行驶距离：约500公里。"
    n "预计行驶距离：约500公里。"
    $ phone_mode = False
    $ c1_before("CH01-A04", 11, "")
    n "你驶出小区。"
    $ c1_before("CH01-A04", 12, "")
    n "平时这个时间，路上的汽车并不算多。"
    $ c1_before("CH01-A04", 13, "")
    n "今天却已经排起了长队。"
    $ c1_before("CH01-A04", 14, "")
    n "车辆缓缓向前挪动。"
    $ c1_before("CH01-A04", 15, "")
    n "前方有人正在核验通行信息。"
    $ c1_before("CH01-A04", 16, "")
    n "一名交警走到车窗旁。"
    $ c1_before("CH01-A04", 17, "交警")
    n "交警：“去哪儿？”"
    $ c1_before("CH01-A04", 18, "陈知远")
    char_protagonist "“庐州市，回老家。”"
    $ c1_before("CH01-A04", 19, "交警")
    n "交警：“车上几个人？”"
    $ c1_before("CH01-A04", 20, "陈知远")
    char_protagonist "“两个。”"
    $ c1_before("CH01-A04", 21, "")
    n "对方检查了你们的证件和通行信息。"
    $ c1_before("CH01-A04", 22, "交警")
    n "交警：“最近部分路段临时管制，按导航不一定能走通。”"
    $ c1_before("CH01-A04", 23, "陈知远")
    char_protagonist "“明白。”"
    $ c1_before("CH01-A04", 24, "交警")
    n "交警：“路上注意安全，有情况服从现场指挥。”"
    $ c1_before("CH01-A04", 25, "")
    n "车辆终于被放行。"
    $ c1_before("CH01-A04", 26, "林晚宁")
    char_partner "“还好出来了。”"
    $ c1_before("CH01-A04", 27, "陈知远")
    char_protagonist "“嗯。”"
    $ c1_before("CH01-A04", 28, "")
    n "你松了一口气。"
    $ c1_before("CH01-A04", 29, "")
    n "可是离开检查点不久，前方再次出现拥堵。"
    $ c1_before("CH01-A04", 30, "")
    n "车载导航反复重新规划路线。"
    $ c1_before("CH01-A04", 31, "")
    n "预计到达时间从下午三点，变成五点，又变成七点。"
    $ c1_before("CH01-A04", 32, "")
    n "你们在路上耗费了数个小时。"
    $ c1_before("CH01-A04", 33, "")
    n "午后，电量逐渐接近需要补充的范围。"
    $ c1_before("CH01-A04", 34, "")
    n "你不得不将目的地暂时改为前方的一处高速服务区。"
    $ c1_before("CH01-A04", 35, "林晚宁")
    char_partner "“还剩多少电？”"
    $ c1_before("CH01-A04", 36, "陈知远")
    char_protagonist "“够到服务区。”"
    $ c1_before("CH01-A04", 37, "林晚宁")
    char_partner "“那先充电吧。”"
    $ c1_before("CH01-A04", 38, "")
    n "你点了点头。"
    $ c1_before("CH01-A04", 39, "")
    n "远处，服务区入口的指示牌渐渐出现在道路尽头。"
    jump ch01_a05

label ch01_a05:
    $ current_scene_id = "CH01-A05"
    $ current_scene_title = "最后一站"
    $ current_scene_time = "Day 5，17:26"
    $ current_scene_location = "沪庐高速某服务区"
    $ phone_mode = False
    $ c1_scene("CH01-A05")
    $ c1_before("CH01-A05", 0, "")
    n "服务区里停满了汽车。"
    $ c1_before("CH01-A05", 1, "")
    n "原本宽敞的停车场被临时停放的车辆挤得十分狭窄。"
    $ c1_before("CH01-A05", 2, "")
    n "几辆大货车停在广场另一侧。"
    $ c1_before("CH01-A05", 3, "")
    n "有司机站在车旁抽烟。"
    $ c1_before("CH01-A05", 4, "")
    n "便利店门口排着长队。"
    $ c1_before("CH01-A05", 5, "")
    n "不远处，有工作人员正在反复提醒旅客不要聚集。"
    $ c1_before("CH01-A05", 6, "")
    n "你把车驶向充电区。"
    $ c1_before("CH01-A05", 7, "")
    n "幸运的是，终于轮到了一个空闲的充电车位。"
    $ c1_before("CH01-A05", 8, "")
    n "你下车接好充电枪。"
    $ c1_before("CH01-A05", 9, "")
    n "看着充电桩屏幕上缓慢增加的数字，长长地舒了一口气。"
    $ c1_before("CH01-A05", 10, "林晚宁")
    char_partner "“还要充多久？”"
    $ c1_before("CH01-A05", 11, "陈知远")
    char_protagonist "“二十分钟左右，充到够跑下一段就行。”"
    $ c1_before("CH01-A05", 12, "林晚宁")
    char_partner "“今天能回去吗？”"
    $ c1_before("CH01-A05", 13, "")
    n "你打开手机导航。"
    $ c1_before("CH01-A05", 14, "")
    $ phone_mode = True
    $ phone_speaker = "讯息"
    $ phone_text = "目的地：庐州市城郊住宅"
    n "目的地：庐州市城郊住宅"
    $ phone_mode = False
    $ c1_before("CH01-A05", 15, "")
    $ phone_mode = True
    $ phone_speaker = "讯息"
    $ phone_text = "剩余距离：217公里"
    n "剩余距离：217公里"
    $ phone_mode = False
    $ c1_before("CH01-A05", 16, "")
    $ phone_mode = True
    $ phone_speaker = "讯息"
    $ phone_text = "预计到达时间：因道路管制，暂无法准确估算"
    n "预计到达时间：因道路管制，暂无法准确估算"
    $ phone_mode = False
    $ c1_before("CH01-A05", 17, "陈知远")
    $ phone_mode = True
    $ phone_speaker = "陈知远"
    $ phone_text = "“应该能。”"
    n "“应该能。”"
    $ phone_mode = False
    $ c1_before("CH01-A05", 18, "林晚宁")
    $ phone_mode = True
    $ phone_speaker = "林晚宁"
    $ phone_text = "“那我给叔叔阿姨发个消息。”"
    n "“那我给叔叔阿姨发个消息。”"
    $ phone_mode = False
    $ c1_before("CH01-A05", 19, "陈知远")
    $ phone_mode = True
    $ phone_speaker = "陈知远"
    $ phone_text = "“嗯。”"
    n "“嗯。”"
    $ phone_mode = False
    $ c1_before("CH01-A05", 20, "")
    n "你看了一眼便利店。"
    $ c1_before("CH01-A05", 21, "陈知远")
    char_protagonist "“我去买两瓶水。”"
    $ c1_before("CH01-A05", 22, "林晚宁")
    char_partner "“车上不是还有吗？”"
    $ c1_before("CH01-A05", 23, "陈知远")
    char_protagonist "“顺便看看有没有热的东西吃。”"
    $ c1_before("CH01-A05", 24, "林晚宁")
    char_partner "“那你快点。”"
    $ c1_before("CH01-A05", 25, "")
    n "你关上车门，朝服务区广场走去。"
    $ c1_before("CH01-A05", 26, "")
    n "玻璃门上贴着一张手写告示："
    $ c1_before("CH01-A05", 27, "")
    n "“部分商品暂时缺货，敬请谅解。”"
    $ c1_before("CH01-A05", 28, "")
    n "店里有些闷热。"
    $ c1_before("CH01-A05", 29, "")
    n "冰柜仍然发出低沉的运转声。"
    $ c1_before("CH01-A05", 30, "")
    n "你拿了两瓶水，又在货架上找到几袋饼干。"
    $ c1_before("CH01-A05", 31, "")
    n "排队结账时，远处传来一阵争吵。"
    $ c1_before("CH01-A05", 32, "")
    n "最初，你没有在意。"
    $ c1_before("CH01-A05", 33, "")
    n "这样的争执今天已经见过很多次了。"
    $ c1_before("CH01-A05", 34, "")
    n "有人抱怨充电太慢。"
    $ c1_before("CH01-A05", 35, "")
    n "有人抱怨交通检查。"
    $ c1_before("CH01-A05", 36, "")
    n "有人说前面的高速已经封了。"
    $ c1_before("CH01-A05", 37, "")
    n "你低头看了一眼手机。"
    $ c1_before("CH01-A05", 38, "")
    n "17:43。"
    $ c1_before("CH01-A05", 39, "")
    n "伴侣发来消息。"
    $ c1_before("CH01-A05", 40, "林晚宁")
    char_partner "“爸说家里已经准备好了，让我们慢慢开。”"
    $ c1_before("CH01-A05", 41, "")
    n "你笑了一下。"
    $ c1_before("CH01-A05", 42, "")
    n "回复："
    $ c1_before("CH01-A05", 43, "陈知远")
    char_protagonist "“马上回来。”"
    $ c1_before("CH01-A05", 44, "")
    n "就在这时，服务区入口处传来一阵尖叫。"
    $ c1_before("CH01-A05", 45, "")
    n "你抬起头。"
    $ c1_before("CH01-A05", 46, "")
    n "几个人正从停车场另一侧跑过来。"
    $ c1_before("CH01-A05", 47, "")
    n "其中一个人不断回头。"
    $ c1_before("CH01-A05", 48, "远处旅客")
    n "远处旅客：“别过去！”"
    $ c1_before("CH01-A05", 49, "另一个声音")
    n "另一个声音：“车上有人发疯了！”"
    $ c1_before("CH01-A05", 50, "")
    n "你透过便利店的玻璃窗望去。"
    $ c1_before("CH01-A05", 51, "")
    n "一辆大客车停在服务区入口附近。"
    $ c1_before("CH01-A05", 52, "")
    n "车身周围聚集着不少人。"
    $ c1_before("CH01-A05", 53, "")
    n "客车前门敞开着。"
    $ c1_before("CH01-A05", 54, "")
    n "有人正在从车里往外跑。"
    $ c1_before("CH01-A05", 55, "")
    n "一名乘客摔倒在台阶上。"
    $ c1_before("CH01-A05", 56, "")
    n "紧接着，另一个身影从车厢里冲了出来。"
    $ c1_before("CH01-A05", 57, "")
    n "他扑向附近试图搀扶乘客的工作人员。"
    $ c1_before("CH01-A05", 58, "")
    n "两人一起跌倒。"
    $ c1_before("CH01-A05", 59, "")
    n "周围的人群开始后退。"
    $ c1_before("CH01-A05", 60, "")
    n "紧接着，又有几名神情异常的乘客从车内冲出。"
    $ c1_before("CH01-A05", 61, "")
    n "他们的动作迅速而凌乱。"
    $ c1_before("CH01-A05", 62, "")
    n "有人试图阻拦。"
    $ c1_before("CH01-A05", 63, "")
    n "有人惊叫着跑开。"
    $ c1_before("CH01-A05", 64, "")
    n "车厢里仍然传出撞击声。"
    $ c1_before("CH01-A05", 65, "")
    n "你也许再也不会知道：那辆客车上已经有数名旅客在出发前感染。漫长而各不相同的潜伏期，让他们直到这段旅程中才陆续出现严重症状。"
    $ c1_before("CH01-A05", 66, "")
    n "而此刻，你所能看见的，只是人群忽然失去了秩序。"
    $ c1_before("CH01-A05", 67, "")
    n "几名临时驻守的武警迅速赶向客车。"
    $ c1_before("CH01-A05", 68, "")
    n "有人通过扩音器要求旅客后退。"
    $ c1_before("CH01-A05", 69, "现场喊话")
    n "现场喊话：“所有人员不要靠近客车！”"
    $ c1_before("CH01-A05", 70, "现场喊话")
    n "现场喊话：“保持距离！向后撤离！”"
    $ c1_before("CH01-A05", 71, "")
    n "但服务区里的人实在太多。"
    $ c1_before("CH01-A05", 72, "")
    n "客车附近的旅客四散奔逃，后方的人却还不知道发生了什么。"
    $ c1_before("CH01-A05", 73, "")
    n "拥挤的人群不断推搡。"
    $ c1_before("CH01-A05", 74, "")
    n "几名武警正在不断射击冲向另一侧的感染者，却被同时涌来的旅客撞得失去平衡。"
    $ c1_before("CH01-A05", 75, "")
    n "警戒线随即被冲破。"
    $ c1_before("CH01-A05", 76, "")
    n "临时防线出现了缺口。"
    $ c1_before("CH01-A05", 77, "")
    n "随后，更多感染者混在人群中冲向停车场。"
    $ c1_before("CH01-A05", 78, "")
    n "执勤人员仍在组织疏散，但已经无法控制整个广场。"
    $ c1_before("CH01-A05", 79, "")
    n "你终于意识到事情远比普通的伤人事件严重。"
    $ c1_before("CH01-A05", 80, "")
    n "手机突然响起。"
    $ c1_before("CH01-A05", 81, "陈知远")
    char_protagonist "“喂？”"
    $ c1_before("CH01-A05", 82, "林晚宁")
    char_partner "“外面怎么回事？”"
    $ c1_before("CH01-A05", 83, "陈知远")
    char_protagonist "“不知道。好像有人在打架。”"
    $ c1_before("CH01-A05", 84, "")
    n "电话那头沉默了一瞬。"
    $ c1_before("CH01-A05", 85, "林晚宁")
    char_partner "“我看见有人在跑。”"
    $ c1_before("CH01-A05", 86, "陈知远")
    char_protagonist "“你别下车。”"
    $ c1_before("CH01-A05", 87, "")
    n "一声沉闷的撞击突然从不远处传来。"
    $ c1_before("CH01-A05", 88, "")
    n "便利店的玻璃门被逃跑的人群撞开。"
    $ c1_before("CH01-A05", 89, "")
    n "有人跌倒在你身旁。"
    $ c1_before("CH01-A05", 90, "")
    n "你看见他的手臂上有一大片血迹。"
    $ c1_before("CH01-A05", 91, "")
    n "紧接着，一个神情异常的男子从门外扑向了倒地的人。"
    $ c1_before("CH01-A05", 92, "")
    n "你后退一步。"
    $ c1_before("CH01-A05", 93, "")
    n "购物袋掉在地上。"
    $ c1_before("CH01-A05", 94, "")
    n "两瓶水滚向货架下面。"
    $ c1_before("CH01-A05", 95, "陈知远")
    char_protagonist "“……操。”"
    $ c1_before("CH01-A05", 96, "")
    n "电话里传来伴侣急促的声音。"
    $ c1_before("CH01-A05", 97, "林晚宁")
    char_partner "“你快回来！”"
    $ c1_before("CH01-A05", 98, "陈知远")
    char_protagonist "“把车门锁好！”"
    $ c1_before("CH01-A05", 99, "林晚宁")
    char_partner "“你在哪儿？”"
    $ c1_before("CH01-A05", 100, "陈知远")
    char_protagonist "“我马上过去！”"
    $ c1_before("CH01-A05", 101, "")
    n "你转身冲出便利店。"
    jump ch01_a06

label ch01_a06:
    $ current_scene_id = "CH01-A06"
    $ current_scene_title = "217公里"
    $ current_scene_time = "17:47"
    $ current_scene_location = "服务区停车场"
    $ phone_mode = False
    $ c1_scene("CH01-A06")
    $ c1_before("CH01-A06", 0, "")
    n "停车场里到处是奔跑的人。"
    $ c1_before("CH01-A06", 1, "")
    n "汽车喇叭接连响起。"
    $ c1_before("CH01-A06", 2, "")
    n "有人试图倒车，却被后面的车辆堵住。"
    $ c1_before("CH01-A06", 3, "")
    n "一辆轿车撞上了路边的护栏。"
    $ c1_before("CH01-A06", 4, "")
    n "你远远看见充电区。"
    $ c1_before("CH01-A06", 5, "")
    n "自己的车还停在那里。"
    $ c1_before("CH01-A06", 6, "")
    n "充电枪没有拔下。"
    $ c1_before("CH01-A06", 7, "")
    n "隔着车窗，似乎能够看见伴侣正向这边张望。"
    $ c1_before("CH01-A06", 8, "")
    n "你努力朝那个方向跑去。"
    $ c1_before("CH01-A06", 9, "林晚宁")
    char_partner "“我看见你了！”"
    $ c1_before("CH01-A06", 10, "陈知远")
    char_protagonist "“别出来！”"
    $ c1_before("CH01-A06", 11, "")
    n "一群逃跑的旅客迎面冲过来。"
    $ c1_before("CH01-A06", 12, "")
    n "你被撞得踉跄了一下。"
    $ c1_before("CH01-A06", 13, "")
    n "等重新站稳时，前方的道路已经挤满了人。"
    $ c1_before("CH01-A06", 14, "")
    n "你试图绕过一辆面包车。"
    $ c1_before("CH01-A06", 15, "")
    n "身后传来急促的脚步声。"
    $ c1_before("CH01-A06", 16, "")
    n "有人撞倒了旁边的行李箱。"
    $ c1_before("CH01-A06", 17, "")
    n "你回头。"
    $ c1_before("CH01-A06", 18, "")
    n "一名感染者已经越过混乱的人群，朝你所在的方向奔来。"
    $ c1_before("CH01-A06", 19, "")
    n "你下意识加快脚步。"
    $ c1_before("CH01-A06", 20, "林晚宁")
    char_partner "“你快点！”"
    $ c1_before("CH01-A06", 21, "陈知远")
    char_protagonist "“我——”"
    $ c1_before("CH01-A06", 22, "")
    n "话音未落，你的肩膀突然被重重撞了一下。"
    $ c1_before("CH01-A06", 23, "")
    n "身体失去平衡。"
    $ c1_before("CH01-A06", 24, "")
    n "手机从手中滑落。"
    $ c1_before("CH01-A06", 25, "")
    n "你伸手去抓。"
    $ c1_before("CH01-A06", 26, "")
    n "却什么也没有抓到。"
    $ c1_before("CH01-A06", 27, "")
    n "眼前是混乱的车灯、奔跑的双腿，还有越来越近的脚步声。"
    $ c1_before("CH01-A06", 28, "")
    n "电话里仍然传来伴侣的声音。"
    $ c1_before("CH01-A06", 29, "林晚宁")
    char_partner "“喂？”"
    $ c1_before("CH01-A06", 30, "林晚宁")
    char_partner "“你说话啊！”"
    $ c1_before("CH01-A06", 31, "林晚宁")
    char_partner "“你在哪儿？！”"
    $ c1_before("CH01-A06", 32, "")
    n "远处传来一声尖叫。"
    $ c1_before("CH01-A06", 33, "")
    n "随后是金属撞击的声音。"
    $ c1_before("CH01-A06", 34, "")
    n "……"
    $ c1_before("CH01-A06", 35, "")
    n "手机掉在停车场的地面上。"
    $ c1_before("CH01-A06", 36, "")
    n "屏幕出现了一道裂纹。"
    $ c1_before("CH01-A06", 37, "")
    n "通话已经中断。"
    $ c1_before("CH01-A06", 38, "")
    n "导航界面仍然停留在屏幕上。"
    $ c1_before("CH01-A06", 39, "")
    n "目的地：庐州市"
    $ c1_before("CH01-A06", 40, "")
    n "剩余距离：217公里"
    $ c1_before("CH01-A06", 41, "")
    n "镜头停留数秒。"
    $ c1_before("CH01-A06", 42, "")
    n "那一天，你们最终都没能离开那座服务区。"
    $ c1_before("CH01-A06", 43, "")
    n "……"
    $ c1_before("CH01-A06", 44, "")
    n "你曾以为，自己还有足够的时间。"
    $ chapter_route = "A"
    call route_end("A")
    return

label ch01_b01:
    $ current_scene_id = "CH01-B01"
    $ current_scene_title = "母亲的电话"
    $ current_scene_time = "Day 1，08:30"
    $ current_scene_location = ""
    $ phone_mode = False
    $ c1_scene("CH01-B01")
    $ c1_before("CH01-B01", 0, "")
    n "你没有继续看新闻。"
    $ c1_before("CH01-B01", 1, "")
    n "而是拨通了母亲的电话。"
    $ c1_before("CH01-B01", 2, "")
    n "电话响了几声。"
    $ c1_before("CH01-B01", 3, "周慧敏")
    char_mother "“喂？怎么这么早打电话？”"
    $ c1_before("CH01-B01", 4, "")
    n "你隐约听见电话另一边有人交谈。"
    $ c1_before("CH01-B01", 5, "")
    n "还有推车经过走廊的声音。"
    $ c1_before("CH01-B01", 6, "陈知远")
    char_protagonist "“妈，你在医院？”"
    $ c1_before("CH01-B01", 7, "周慧敏")
    char_mother "“在呢。刚交完班。”"
    $ c1_before("CH01-B01", 8, "陈知远")
    char_protagonist "“问你个事，最近是不是又有什么传染病？”"
    $ c1_before("CH01-B01", 9, "")
    n "电话那头安静了片刻。"
    $ c1_before("CH01-B01", 10, "周慧敏")
    char_mother "“你也看新闻了？”"
    $ c1_before("CH01-B01", 11, "陈知远")
    char_protagonist "“嗯。我有个朋友在沪海的医院工作，说最近他们在加强防护。”"
    $ c1_before("CH01-B01", 12, "周慧敏")
    char_mother "“我们这边也差不多。”"
    $ c1_before("CH01-B01", 13, "周慧敏")
    char_mother "“这两天发热门诊挺忙的，院里反复强调防护和异常情况上报。”"
    $ c1_before("CH01-B01", 14, "陈知远")
    char_protagonist "“严重吗？”"
    $ c1_before("CH01-B01", 15, "周慧敏")
    char_mother "“现在还不好说。我们也没有那么多确定的消息。”"
    $ c1_before("CH01-B01", 16, "陈知远")
    char_protagonist "“不是说新型肺炎吗？”"
    $ c1_before("CH01-B01", 17, "周慧敏")
    char_mother "“通报是这么说的。不过具体是什么、怎么传播，还得等调查。”"
    $ c1_before("CH01-B01", 18, "")
    n "她停顿了一下。"
    $ c1_before("CH01-B01", 19, "周慧敏")
    char_mother "“你是不是担心了？”"
    $ c1_before("CH01-B01", 20, "陈知远")
    char_protagonist "“有一点。”"
    $ c1_before("CH01-B01", 21, "周慧敏")
    char_mother "“担心也正常。做好防护，别听见什么都往自己身上套。”"
    $ c1_before("CH01-B01", 22, "陈知远")
    char_protagonist "“我知道。”"
    $ c1_before("CH01-B01", 23, "")
    n "你看了一眼路口排起的车流。"
    $ c1_before("CH01-B01", 24, "陈知远")
    char_protagonist "“妈，我想让你跟爸商量一下，先往乡下那套房子备点东西。”"
    $ c1_before("CH01-B01", 25, "周慧敏")
    char_mother "“我也有这个想法。”"
    $ c1_before("CH01-B01", 26, "陈知远")
    char_protagonist "“反正那地方本来就是为了应急准备的。”"
    $ c1_before("CH01-B01", 27, "陈知远")
    char_protagonist "“你们检查一下保质期。水和罐头可以再买点。”"
    $ c1_before("CH01-B01", 28, "周慧敏")
    char_mother "“行。”"
    $ c1_before("CH01-B01", 29, "陈知远")
    char_protagonist "“让我爸问问他那些供货商。别等超市开始抢了再买。”"
    $ c1_before("CH01-B01", 30, "周慧敏")
    char_mother "“好，我跟他说。”"
    $ c1_before("CH01-B01", 31, "")
    n "电话另一边有人叫了她一声。"
    $ c1_before("CH01-B01", 32, "周慧敏")
    char_mother "“我这边还有事，先不说了。”"
    $ c1_before("CH01-B01", 33, "陈知远")
    char_protagonist "“你自己也注意安全。”"
    $ c1_before("CH01-B01", 34, "周慧敏")
    char_mother "“知道。你们两个也是。”"
    $ c1_before("CH01-B01", 35, "周慧敏")
    char_mother "“晚上记得给家里打电话。”"
    $ c1_before("CH01-B01", 36, "")
    n "你站在人行道边，低头看着手机。"
    $ c1_before("CH01-B01", 37, "")
    n "路上仍然是熟悉的车流。"
    $ c1_before("CH01-B01", 38, "")
    n "片刻之后，一条消息弹了出来。"
    $ c1_before("CH01-B01", 39, "周慧敏")
    $ phone_mode = True
    $ phone_speaker = "周慧敏"
    $ phone_text = "“已经跟你爸说了。他一会儿去问供应商，尽量按一年的量准备。”"
    n "“已经跟你爸说了。他一会儿去问供应商，尽量按一年的量准备。”"
    $ phone_mode = False
    $ c1_before("CH01-B01", 40, "")
    n "你回复了一个“好”。"
    $ c1_before("CH01-B01", 41, "")
    n "随后把医院朋友发来的消息转给伴侣。"
    $ c1_before("CH01-B01", 42, "陈知远")
    char_protagonist "“我刚给妈打电话了。”"
    $ c1_before("CH01-B01", 43, "林晚宁")
    char_partner "“怎么了？”"
    $ c1_before("CH01-B01", 44, "陈知远")
    char_protagonist "“让他们检查一下乡下的储备。”"
    $ c1_before("CH01-B01", 45, "林晚宁")
    char_partner "“你觉得真会严重起来？”"
    $ c1_before("CH01-B01", 46, "陈知远")
    char_protagonist "“说不好。晚上回来再商量吧。”"
    $ c1_before("CH01-B01", 47, "林晚宁")
    char_partner "“好。”"
    jump ch01_b02

label ch01_b02:
    $ current_scene_id = "CH01-B02"
    $ current_scene_title = "餐厅后厨"
    $ current_scene_time = "Day 1，12:20"
    $ current_scene_location = "庐州市区，父亲经营的餐厅"
    $ phone_mode = False
    $ c1_scene("CH01-B02")
    $ c1_before("CH01-B02", 0, "")
    n "餐厅刚过了午间最忙的时候。"
    $ c1_before("CH01-B02", 1, "")
    n "后厨还留着炒菜的热气。"
    $ c1_before("CH01-B02", 2, "")
    n "一名员工正在清洗餐具。"
    $ c1_before("CH01-B02", 3, "")
    n "父亲坐在后面的办公室里，翻看手机上的进货记录。"
    $ c1_before("CH01-B02", 4, "")
    n "电话响了。"
    $ c1_before("CH01-B02", 5, "供货商")
    n "供货商：“喂，哥，怎么了？”"
    $ c1_before("CH01-B02", 6, "陈建川")
    char_father "“最近米面和油还有现货吧？”"
    $ c1_before("CH01-B02", 7, "供货商")
    n "供货商：“有啊。你店里不够了？”"
    $ c1_before("CH01-B02", 8, "陈建川")
    char_father "“不是店里。我家里想备一些。”"
    $ c1_before("CH01-B02", 9, "供货商")
    n "供货商：“最近确实有不少人问。”"
    $ c1_before("CH01-B02", 10, "陈建川")
    char_father "“那我先订一批，按市场价走。”"
    $ c1_before("CH01-B02", 11, "供货商")
    n "供货商：“行。你把数量发我。”"
    $ c1_before("CH01-B02", 12, "")
    n "父亲挂断电话。"
    $ c1_before("CH01-B02", 13, "")
    n "他看着手机上的采购清单，想了一会儿，又拨通另一个号码。"
    $ c1_before("CH01-B02", 14, "")
    n "窗外，一辆送货面包车正在倒车。"
    $ c1_before("CH01-B02", 15, "")
    n "隔着玻璃，能够看见街边小店的招牌。"
    $ c1_before("CH01-B02", 16, "")
    n "一切都和平时没什么两样。"
    $ c1_before("CH01-B02", 17, "")
    n "只有手机上的订单，比往常多了几行。"
    $ c1_before("CH01-B02", 18, "")
    n "傍晚，父母在家中整理采购清单。"
    $ c1_before("CH01-B02", 19, "陈建川")
    char_father "“米面油基本能拿到，罐头还得去超市看看。”"
    $ c1_before("CH01-B02", 20, "周慧敏")
    char_mother "“水也多买一点。”"
    $ c1_before("CH01-B02", 21, "陈建川")
    char_father "“我明天去。”"
    $ c1_before("CH01-B02", 22, "周慧敏")
    char_mother "“地下室的东西得再检查一遍。”"
    $ c1_before("CH01-B02", 23, "陈建川")
    char_father "“嗯。”"
    $ c1_before("CH01-B02", 24, "")
    n "母亲看着手机。"
    $ c1_before("CH01-B02", 25, "周慧敏")
    char_mother "“孩子今天还说，可能想提前回来。”"
    $ c1_before("CH01-B02", 26, "陈建川")
    char_father "“那就回来吧。”"
    $ c1_before("CH01-B02", 27, "周慧敏")
    char_mother "“工作怎么办？”"
    $ c1_before("CH01-B02", 28, "陈建川")
    char_father "“不是还有年假吗？要是像上次那样被封在里面，才真是得不偿失。”"
    $ c1_before("CH01-B02", 29, "")
    n "他说得很随意。"
    $ c1_before("CH01-B02", 30, "")
    n "随后又低下头，继续核对清单。"
    jump ch01_b03

label ch01_b03:
    $ current_scene_id = "CH01-B03"
    $ current_scene_title = "决定"
    $ current_scene_time = "Day 1，20:37"
    $ current_scene_location = "沪海市公寓"
    $ phone_mode = False
    $ c1_scene("CH01-B03")
    $ c1_before("CH01-B03", 0, "")
    n "你回到家时，伴侣已经在厨房里忙了一会儿。"
    $ c1_before("CH01-B03", 1, "")
    n "桌上放着两碗刚做好的面。"
    $ c1_before("CH01-B03", 2, "林晚宁")
    char_partner "“今天怎么回来这么晚？”"
    $ c1_before("CH01-B03", 3, "陈知远")
    char_protagonist "“临时开了个会。”"
    $ c1_before("CH01-B03", 4, "林晚宁")
    char_partner "“你们公司也开始讨论那个事了？”"
    $ c1_before("CH01-B03", 5, "陈知远")
    char_protagonist "“嗯。有人建议减少线下会议。”"
    $ c1_before("CH01-B03", 6, "")
    n "你洗了洗手，在桌边坐下。"
    $ c1_before("CH01-B03", 7, "")
    n "两人吃了一会儿。"
    $ c1_before("CH01-B03", 8, "")
    n "伴侣先开口。"
    $ c1_before("CH01-B03", 9, "林晚宁")
    char_partner "“所以，你现在还是想回庐州？”"
    $ c1_before("CH01-B03", 10, "陈知远")
    char_protagonist "“想。”"
    $ c1_before("CH01-B03", 11, "林晚宁")
    char_partner "“那就回去。”"
    $ c1_before("CH01-B03", 12, "")
    n "你抬起头。"
    $ c1_before("CH01-B03", 13, "陈知远")
    char_protagonist "“这么干脆？”"
    $ c1_before("CH01-B03", 14, "林晚宁")
    char_partner "“不是你早上让我一起商量的吗？”"
    $ c1_before("CH01-B03", 15, "")
    n "她拿起杯子喝了口水。"
    $ c1_before("CH01-B03", 16, "林晚宁")
    char_partner "“我下午也想了很久。”"
    $ c1_before("CH01-B03", 17, "林晚宁")
    char_partner "“说实话，我不觉得现在就会出什么大事。”"
    $ c1_before("CH01-B03", 18, "林晚宁")
    char_partner "“但是我们留在沪海，好像也没什么一定要留下来的理由。”"
    $ c1_before("CH01-B03", 19, "陈知远")
    char_protagonist "“工作呢？”"
    $ c1_before("CH01-B03", 20, "林晚宁")
    char_partner "“请年假啊。”"
    $ c1_before("CH01-B03", 21, "陈知远")
    char_protagonist "“你年假还有几天？”"
    $ c1_before("CH01-B03", 22, "林晚宁")
    char_partner "“够用。”"
    $ c1_before("CH01-B03", 23, "")
    n "你笑了。"
    $ c1_before("CH01-B03", 24, "陈知远")
    char_protagonist "“我也还有几天。”"
    $ c1_before("CH01-B03", 25, "")
    n "她继续说道："
    $ c1_before("CH01-B03", 26, "林晚宁")
    char_partner "“其实我更担心家里人。叔叔阿姨在庐州，我爸妈也在那边，万一真有什么事，我们隔这么远也帮不上忙。”"
    $ c1_before("CH01-B03", 27, "")
    n "你想起早晨母亲的电话。"
    $ c1_before("CH01-B03", 28, "陈知远")
    char_protagonist "“我爸已经开始买东西了。”"
    $ c1_before("CH01-B03", 29, "林晚宁")
    char_partner "“那我们也别拖太久。”"
    $ c1_before("CH01-B03", 30, "陈知远")
    char_protagonist "“行。明天把工作处理一下，后天走。”"
    $ c1_before("CH01-B03", 31, "林晚宁")
    char_partner "“好。”"
    $ c1_before("CH01-B03", 32, "")
    n "她把碗端起来。"
    $ c1_before("CH01-B03", 33, "林晚宁")
    char_partner "“不过今天还是先把面吃完吧，都快凉了。”"
    $ c1_before("CH01-B03", 34, "")
    n "窗外，城市的灯光一盏接着一盏亮起。"
    $ c1_before("CH01-B03", 35, "")
    n "远处高架桥上的车流连成一道缓慢移动的光带。"
    $ c1_before("CH01-B03", 36, "")
    n "你忽然觉得，这个夜晚比平时安静了一些。"
    jump ch01_b04

label ch01_b04:
    $ current_scene_id = "CH01-B04"
    $ current_scene_title = "年假"
    $ current_scene_time = "Day 2，09:14"
    $ current_scene_location = "公司办公室"
    $ phone_mode = False
    $ c1_scene("CH01-B04")
    $ c1_before("CH01-B04", 0, "")
    n "你坐在工位前，打开与上级的聊天窗口。"
    $ c1_before("CH01-B04", 1, "")
    n "反复斟酌了一下措辞。"
    $ c1_before("CH01-B04", 2, "陈知远")
    $ phone_mode = True
    $ phone_speaker = "陈知远"
    $ phone_text = "“领导，我这两天身体状态不太好，想把剩下的年假休一下，回老家调整几天。”"
    n "“领导，我这两天身体状态不太好，想把剩下的年假休一下，回老家调整几天。”"
    $ phone_mode = False
    $ c1_before("CH01-B04", 3, "")
    n "对方很快回复。"
    $ c1_before("CH01-B04", 4, "上级")
    n "上级：“哪里不舒服？”"
    $ c1_before("CH01-B04", 5, "陈知远")
    char_protagonist "“最近有些疲惫，想休息一下。”"
    $ c1_before("CH01-B04", 6, "上级")
    n "上级：“最近这个情况，你要是不舒服就别勉强来公司了。”"
    $ c1_before("CH01-B04", 7, "上级")
    n "上级：“手头的工作交接好就行。”"
    $ c1_before("CH01-B04", 8, "陈知远")
    char_protagonist "“谢谢领导。”"
    $ c1_before("CH01-B04", 9, "上级")
    n "上级：“注意身体。有需要线上沟通。”"
    $ c1_before("CH01-B04", 10, "")
    n "你关闭聊天窗口。"
    $ c1_before("CH01-B04", 11, "")
    n "又给伴侣发消息。"
    $ c1_before("CH01-B04", 12, "陈知远")
    char_protagonist "“我这边批了。”"
    $ c1_before("CH01-B04", 13, "林晚宁")
    char_partner "“我也是。”"
    $ c1_before("CH01-B04", 14, "陈知远")
    char_protagonist "“那按计划走。”"
    $ c1_before("CH01-B04", 15, "林晚宁")
    char_partner "“嗯，晚上收拾东西。”"
    $ c1_before("CH01-B04", 16, "")
    n "你看着办公桌上的文件。"
    $ c1_before("CH01-B04", 17, "")
    n "突然有些恍惚。"
    $ c1_before("CH01-B04", 18, "")
    n "你并没有辞职。"
    $ c1_before("CH01-B04", 19, "")
    n "只是请了几天年假。"
    $ c1_before("CH01-B04", 20, "")
    n "下周也许还会回来。"
    $ c1_before("CH01-B04", 21, "")
    n "桌上的杯子、抽屉里的零食、电脑里没写完的报告，都还在这里。"
    $ c1_before("CH01-B04", 22, "")
    n "你甚至没有认真地向同事告别。"
    $ c1_before("CH01-B04", 23, "")
    n "接下来的两天，你们没有再讨论是否回去。"
    $ c1_before("CH01-B04", 24, "")
    n "工作需要交接，订好的东西也陆续送到。"
    $ c1_before("CH01-B04", 25, "")
    n "你把文件发给同事，伴侣在地板上分开要带走和留在这里的用品。纸箱拆了一只，又多了一只。"
    $ c1_before("CH01-B04", 26, "")
    n "父亲在电话里说，买到的东西已经搬进乡下，家里还热着饭，不用再绕路。"
    $ c1_before("CH01-B04", 27, "")
    n "你们将出发时间定在第五天清晨。"
    $ c1_before("CH01-B04", 28, "")
    n "那时，你仍然觉得，晚两天不过是多收拾几件东西。"
    jump ch01_b05

label ch01_b05:
    $ current_scene_id = "CH01-B05"
    $ current_scene_title = "出发之前"
    $ current_scene_time = "Day 5，07:10"
    $ current_scene_location = "沪海市公寓地下停车场"
    $ phone_mode = False
    $ c1_scene("CH01-B05")
    $ c1_before("CH01-B05", 0, "")
    n "你把最后一个行李箱放进后备厢。"
    $ c1_before("CH01-B05", 1, "")
    n "伴侣清点了一遍随身物品。"
    $ c1_before("CH01-B05", 2, "林晚宁")
    char_partner "“证件？”"
    $ c1_before("CH01-B05", 3, "陈知远")
    char_protagonist "“带了。”"
    $ c1_before("CH01-B05", 4, "林晚宁")
    char_partner "“充电线？”"
    $ c1_before("CH01-B05", 5, "陈知远")
    char_protagonist "“带了。”"
    $ c1_before("CH01-B05", 6, "林晚宁")
    char_partner "“钥匙？”"
    $ c1_before("CH01-B05", 7, "")
    n "你从口袋里掏出来晃了晃。"
    $ c1_before("CH01-B05", 8, "林晚宁")
    char_partner "“好。”"
    $ c1_before("CH01-B05", 9, "")
    n "她关上车门。"
    $ c1_before("CH01-B05", 10, "")
    n "你看着车库里整齐排列的汽车。"
    $ c1_before("CH01-B05", 11, "")
    n "平时这个时间，已经有不少人开车出门。"
    $ c1_before("CH01-B05", 12, "")
    n "今天却有些安静。"
    $ c1_before("CH01-B05", 13, "陈建川")
    char_father "“出发了没？”"
    $ c1_before("CH01-B05", 14, "陈知远")
    char_protagonist "“刚准备走。”"
    $ c1_before("CH01-B05", 15, "陈建川")
    char_father "“昨天买的东西基本都到齐了。”"
    $ c1_before("CH01-B05", 16, "陈知远")
    char_protagonist "“水呢？”"
    $ c1_before("CH01-B05", 17, "陈建川")
    char_father "“买了。车里的油也加好了。”"
    $ c1_before("CH01-B05", 18, "陈建川")
    char_father "“我还去了一趟老同学承包的加油站，买了好几桶汽油备着。”"
    $ c1_before("CH01-B05", 19, "陈知远")
    char_protagonist "“餐厅怎么办？”"
    $ c1_before("CH01-B05", 20, "陈建川")
    char_father "“这两天生意本来就少，先让他们休息几天。”"
    $ c1_before("CH01-B05", 21, "陈知远")
    char_protagonist "“妈呢？”"
    $ c1_before("CH01-B05", 22, "陈建川")
    char_father "“昨天上完班，今天轮休。我们准备去乡下整理东西。”"
    $ c1_before("CH01-B05", 23, "陈知远")
    char_protagonist "“行，那我们晚上见。”"
    $ c1_before("CH01-B05", 24, "陈建川")
    char_father "“路上别急。”"
    $ c1_before("CH01-B05", 25, "")
    n "你坐进驾驶座。"
    $ c1_before("CH01-B05", 26, "")
    n "检查电量。"
    $ c1_before("CH01-B05", 27, "")
    n "96%%。"
    $ c1_before("CH01-B05", 28, "")
    $ phone_mode = True
    $ phone_speaker = "讯息"
    $ phone_text = "目的地：庐州市。"
    n "目的地：庐州市。"
    $ phone_mode = False
    $ c1_before("CH01-B05", 29, "")
    $ phone_mode = True
    $ phone_speaker = "讯息"
    $ phone_text = "推荐路线已生成。"
    n "推荐路线已生成。"
    $ phone_mode = False
    $ c1_before("CH01-B05", 30, "")
    n "你按下开始导航。"
    $ c1_before("CH01-B05", 31, "")
    n "地下停车场出口的卷帘门缓缓升起。"
    $ c1_before("CH01-B05", 32, "")
    n "清晨的阳光照进车内。"
    jump ch01_b06

label ch01_b06:
    $ current_scene_id = "CH01-B06"
    $ current_scene_title = "长路"
    $ current_scene_time = "Day 5，上午至傍晚"
    $ current_scene_location = ""
    $ phone_mode = False
    $ c1_scene("CH01-B06")
    $ c1_before("CH01-B06", 0, "")
    n "汽车驶离沪海市。"
    $ c1_before("CH01-B06", 1, "")
    n "道路两旁的高楼逐渐稀疏。"
    $ c1_before("CH01-B06", 2, "")
    n "再往前，是物流园、厂房和不断延伸的高速公路。"
    $ c1_before("CH01-B06", 3, "")
    n "伴侣坐在副驾驶，一边看导航，一边与母亲聊天。"
    $ c1_before("CH01-B06", 4, "林晚宁")
    char_partner "“阿姨说冰箱里还给我们留了吃的。”"
    $ c1_before("CH01-B06", 5, "陈知远")
    char_protagonist "“什么？”"
    $ c1_before("CH01-B06", 6, "林晚宁")
    char_partner "“她说等到了就知道。”"
    $ c1_before("CH01-B06", 7, "陈知远")
    char_protagonist "“还搞神秘。”"
    $ c1_before("CH01-B06", 8, "")
    n "你笑了笑。"
    $ c1_before("CH01-B06", 9, "")
    n "车里安静了一会儿。"
    $ c1_before("CH01-B06", 10, "")
    n "广播正在播放交通信息。"
    $ c1_before("CH01-B06", 11, "")
    n "部分城市周边新增了临时检查措施。"
    $ c1_before("CH01-B06", 12, "")
    n "有几条路段提示车辆提前规划行程。"
    $ c1_before("CH01-B06", 13, "")
    n "你们经过一处服务区。"
    $ c1_before("CH01-B06", 14, "")
    n "停车休息、补充电量。"
    $ c1_before("CH01-B06", 15, "")
    n "周围人不少，但秩序基本正常。"
    $ c1_before("CH01-B06", 16, "")
    n "便利店里还能买到热食。"
    $ c1_before("CH01-B06", 17, "")
    n "你拿着两杯咖啡走回车旁。"
    $ c1_before("CH01-B06", 18, "")
    n "伴侣站在车边，望着远处的道路。"
    $ c1_before("CH01-B06", 19, "陈知远")
    char_protagonist "“看什么呢？”"
    $ c1_before("CH01-B06", 20, "林晚宁")
    char_partner "“没什么。”"
    $ c1_before("CH01-B06", 21, "")
    n "她接过咖啡。"
    $ c1_before("CH01-B06", 22, "林晚宁")
    char_partner "“就是觉得有点奇怪。”"
    $ c1_before("CH01-B06", 23, "陈知远")
    char_protagonist "“什么？”"
    $ c1_before("CH01-B06", 24, "林晚宁")
    char_partner "“昨天还在上班，今天就已经在回家的路上了。”"
    $ c1_before("CH01-B06", 25, "")
    n "你没有说话。"
    $ c1_before("CH01-B06", 26, "")
    n "远处，一辆货车从高速上驶过。"
    $ c1_before("CH01-B06", 27, "林晚宁")
    char_partner "“你觉得我们是不是有点小题大做？”"
    $ c1_before("CH01-B06", 28, "陈知远")
    char_protagonist "“可能吧。”"
    $ c1_before("CH01-B06", 29, "林晚宁")
    char_partner "“那你后悔吗？”"
    $ c1_before("CH01-B06", 30, "陈知远")
    char_protagonist "“不后悔。”"
    $ c1_before("CH01-B06", 31, "")
    n "她笑了。"
    $ c1_before("CH01-B06", 32, "林晚宁")
    char_partner "“我也是。”"
    $ c1_before("CH01-B06", 33, "")
    n "你们喝完咖啡，重新上车。"
    $ c1_before("CH01-B06", 34, "")
    n "窗外的城市越来越远。"
    $ c1_before("CH01-B06", 35, "")
    n "前方的道路仍然漫长。"
    $ c1_before("CH01-B06", 36, "")
    n "但至少此刻，你们正在朝家的方向行驶。"
    jump ch01_b07

label ch01_b07:
    $ current_scene_id = "CH01-B07"
    $ current_scene_title = "故乡"
    $ current_scene_time = "Day 5，19:06"
    $ current_scene_location = "庐州市城郊"
    $ phone_mode = False
    $ c1_scene("CH01-B07")
    $ c1_before("CH01-B07", 0, "")
    n "天色已经暗了下来。"
    $ c1_before("CH01-B07", 1, "")
    n "导航引导你驶出城市主干道。"
    $ c1_before("CH01-B07", 2, "")
    n "道路逐渐变窄。"
    $ c1_before("CH01-B07", 3, "")
    n "两旁出现成片的农田和零散的住宅。"
    $ c1_before("CH01-B07", 4, "")
    n "远处，一列货车缓慢驶过铁路桥。"
    $ c1_before("CH01-B07", 5, "")
    n "车轮与铁轨的摩擦声顺着晚风传过来。"
    $ c1_before("CH01-B07", 6, "")
    n "伴侣望向窗外。"
    $ c1_before("CH01-B07", 7, "林晚宁")
    char_partner "“这边好像比上次来又多了几栋楼。”"
    $ c1_before("CH01-B07", 8, "陈知远")
    char_protagonist "“附近新修的。”"
    $ c1_before("CH01-B07", 9, "林晚宁")
    char_partner "“那边是什么？”"
    $ c1_before("CH01-B07", 10, "陈知远")
    char_protagonist "“物流园。再往前还有货运站。”"
    $ c1_before("CH01-B07", 11, "林晚宁")
    char_partner "“以前好像没这么多车。”"
    $ c1_before("CH01-B07", 12, "")
    n "你看了一眼路边。"
    $ c1_before("CH01-B07", 13, "")
    n "几辆货车正停在仓库门口。"
    $ c1_before("CH01-B07", 14, "")
    n "远处高层住宅的窗户里亮着灯。"
    $ c1_before("CH01-B07", 15, "")
    n "有人推着自行车从路口经过。"
    $ c1_before("CH01-B07", 16, "")
    n "一个骑电动车的年轻人停在便利店门前，低头翻看手机。"
    $ c1_before("CH01-B07", 17, "")
    n "除了不断出现的疫情新闻，这里仍然和任何一个普通的城郊社区没有太大区别。"
    $ c1_before("CH01-B07", 18, "")
    n "导航提示你在前方路口右转。"
    $ c1_before("CH01-B07", 19, "")
    n "不久，熟悉的院墙出现在道路一侧。"
    $ c1_before("CH01-B07", 20, "")
    n "院门外停着父亲的老款SUV。"
    $ c1_before("CH01-B07", 21, "")
    n "院子里亮着灯。"
    $ c1_before("CH01-B07", 22, "")
    n "父亲听见汽车驶来的声音，从屋里走出来。"
    $ c1_before("CH01-B07", 23, "陈建川")
    char_father "“到了？”"
    $ c1_before("CH01-B07", 24, "")
    n "你停好车。"
    $ c1_before("CH01-B07", 25, "陈知远")
    char_protagonist "“到了。”"
    $ c1_before("CH01-B07", 26, "陈建川")
    char_father "“路上堵不堵？”"
    $ c1_before("CH01-B07", 27, "陈知远")
    char_protagonist "“还行，检查耽误了一会儿。”"
    $ c1_before("CH01-B07", 28, "陈建川")
    char_father "“那就好。”"
    $ c1_before("CH01-B07", 29, "")
    n "他接过一个行李箱。"
    $ c1_before("CH01-B07", 30, "陈建川")
    char_father "“先进去吃饭，东西明天再收拾。”"
    $ c1_before("CH01-B07", 31, "")
    n "你走进院子。"
    $ c1_before("CH01-B07", 32, "")
    n "母亲从屋里出来，手里还拿着一条围裙。"
    $ c1_before("CH01-B07", 33, "周慧敏")
    char_mother "“怎么这么晚？”"
    $ c1_before("CH01-B07", 34, "陈知远")
    char_protagonist "“路上充了次电。”"
    $ c1_before("CH01-B07", 35, "周慧敏")
    char_mother "“饭还热着，洗手吃饭。”"
    $ c1_before("CH01-B07", 36, "")
    n "伴侣笑着叫了一声阿姨。"
    $ c1_before("CH01-B07", 37, "")
    n "母亲拉着她往屋里走。"
    $ c1_before("CH01-B07", 38, "")
    n "父亲还在后面慢慢搬行李。"
    $ c1_before("CH01-B07", 39, "")
    n "你站在院门口，回头望了一眼来时的道路。"
    $ c1_before("CH01-B07", 40, "")
    n "远处的天已经完全黑了。"
    $ c1_before("CH01-B07", 41, "")
    n "只有路灯把树影投在地上。"
    $ c1_before("CH01-B07", 42, "")
    n "屋里传来母亲的声音。"
    $ c1_before("CH01-B07", 43, "周慧敏")
    char_mother "“别在外面站着了，快进来。”"
    $ c1_before("CH01-B07", 44, "")
    n "你收回视线。"
    $ c1_before("CH01-B07", 45, "陈知远")
    char_protagonist "“来了。”"
    $ c1_before("CH01-B07", 46, "")
    n "……"
    $ c1_before("CH01-B07", 47, "")
    n "这一程虽不容易，但幸好，家还在。"
    $ chapter_route = "B"
    call route_end("B")
    return

label ch01_c01:
    $ current_scene_id = "CH01-C01"
    $ current_scene_title = "两个人的决定"
    $ current_scene_time = "Day 1，08:30"
    $ current_scene_location = ""
    $ phone_mode = False
    $ c1_scene("CH01-C01")
    $ c1_before("CH01-C01", 0, "")
    n "你把手机里的新闻和医院朋友的聊天记录转发给伴侣。"
    $ c1_before("CH01-C01", 1, "")
    n "随后拨通电话。"
    $ c1_before("CH01-C01", 2, "林晚宁")
    char_partner "“怎么了？不是刚分开吗？”"
    $ c1_before("CH01-C01", 3, "陈知远")
    char_protagonist "“你看一下我发的消息。”"
    $ c1_before("CH01-C01", 4, "")
    n "电话那头安静了片刻。"
    $ c1_before("CH01-C01", 5, "林晚宁")
    char_partner "“看到了。”"
    $ c1_before("CH01-C01", 6, "陈知远")
    char_protagonist "“你觉得怎么样？”"
    $ c1_before("CH01-C01", 7, "林晚宁")
    char_partner "“好像有点不太对。”"
    $ c1_before("CH01-C01", 8, "陈知远")
    char_protagonist "“我也是这么想的。”"
    $ c1_before("CH01-C01", 9, "")
    n "你停在人行道边。"
    $ c1_before("CH01-C01", 10, "陈知远")
    char_protagonist "“要不我们提前回庐州？”"
    $ c1_before("CH01-C01", 11, "林晚宁")
    char_partner "“现在？”"
    $ c1_before("CH01-C01", 12, "陈知远")
    char_protagonist "“对。”"
    $ c1_before("CH01-C01", 13, "林晚宁")
    char_partner "“你认真的？”"
    $ c1_before("CH01-C01", 14, "陈知远")
    char_protagonist "“嗯。”"
    $ c1_before("CH01-C01", 15, "林晚宁")
    char_partner "“工作怎么办？”"
    $ c1_before("CH01-C01", 16, "陈知远")
    char_protagonist "“请年假。先回去住几天。”"
    $ c1_before("CH01-C01", 17, "林晚宁")
    char_partner "“那边房子能住吗？”"
    $ c1_before("CH01-C01", 18, "陈知远")
    char_protagonist "“能。我爸他们一直在维护。”"
    $ c1_before("CH01-C01", 19, "林晚宁")
    char_partner "“也是。”"
    $ c1_before("CH01-C01", 20, "")
    n "她沉默了一会儿。"
    $ c1_before("CH01-C01", 21, "林晚宁")
    char_partner "“其实我也觉得可以回去。”"
    $ c1_before("CH01-C01", 22, "陈知远")
    char_protagonist "“真的？”"
    $ c1_before("CH01-C01", 23, "林晚宁")
    char_partner "“反正最近也挺累的。就算什么事都没有，我们也能休息一下。”"
    $ c1_before("CH01-C01", 24, "陈知远")
    char_protagonist "“那就这么定？”"
    $ c1_before("CH01-C01", 25, "林晚宁")
    char_partner "“等等。”"
    $ c1_before("CH01-C01", 26, "陈知远")
    char_protagonist "“怎么了？”"
    $ c1_before("CH01-C01", 27, "林晚宁")
    char_partner "“我们是不是应该先查一下路况？”"
    $ c1_before("CH01-C01", 28, "")
    n "你忍不住笑了。"
    $ c1_before("CH01-C01", 29, "陈知远")
    char_protagonist "“行。”"
    $ c1_before("CH01-C01", 30, "林晚宁")
    char_partner "“还有车，昨天充满电了吗？”"
    $ c1_before("CH01-C01", 31, "陈知远")
    char_protagonist "“充了。”"
    $ c1_before("CH01-C01", 32, "林晚宁")
    char_partner "“那你先问问能不能休假。”"
    $ c1_before("CH01-C01", 33, "陈知远")
    char_protagonist "“好。”"
    $ c1_before("CH01-C01", 34, "")
    n "挂断电话后，你忽然感觉轻松了一些。"
    $ c1_before("CH01-C01", 35, "")
    n "虽然还没有确认究竟发生了什么，但至少不用再一个人反复考虑这件事了。"
    jump ch01_c02

label ch01_c02:
    $ current_scene_id = "CH01-C02"
    $ current_scene_title = "离开办公室"
    $ current_scene_time = "Day 1，下午"
    $ current_scene_location = "沪海市，公司办公室"
    $ phone_mode = False
    $ c1_scene("CH01-C02")
    $ c1_before("CH01-C02", 0, "")
    n "上午的工作照常进行。"
    $ c1_before("CH01-C02", 1, "")
    n "你参加了一场会议。"
    $ c1_before("CH01-C02", 2, "")
    n "同事讨论着项目进度和下周的安排。"
    $ c1_before("CH01-C02", 3, "")
    n "偶尔有人提到最近的新闻。"
    $ c1_before("CH01-C02", 4, "")
    n "但话题很快又回到工作上。"
    $ c1_before("CH01-C02", 5, "")
    n "午后，你向上级提出休年假的申请。"
    $ c1_before("CH01-C02", 6, "陈知远")
    char_protagonist "“领导，最近身体状态有些不太好，想请几天年假回家休息。”"
    $ c1_before("CH01-C02", 7, "上级")
    n "上级：“哪里不舒服？”"
    $ c1_before("CH01-C02", 8, "陈知远")
    char_protagonist "“有些疲惫，想调整一下。”"
    $ c1_before("CH01-C02", 9, "上级")
    n "上级：“最近外面这个情况，你要是不舒服就先休息吧。”"
    $ c1_before("CH01-C02", 10, "上级")
    n "上级：“工作交接一下，别把身体拖坏了。”"
    $ c1_before("CH01-C02", 11, "陈知远")
    char_protagonist "“好，谢谢。”"
    $ c1_before("CH01-C02", 12, "")
    n "你关闭工作聊天窗口。"
    $ c1_before("CH01-C02", 13, "")
    n "伴侣几乎同时发来消息。"
    $ c1_before("CH01-C02", 14, "林晚宁")
    char_partner "“我这边也批了。”"
    $ c1_before("CH01-C02", 15, "陈知远")
    char_protagonist "“那明天走？”"
    $ c1_before("CH01-C02", 16, "林晚宁")
    char_partner "“可以。”"
    $ c1_before("CH01-C02", 17, "陈知远")
    char_protagonist "“晚上早点回来收拾东西。”"
    $ c1_before("CH01-C02", 18, "林晚宁")
    char_partner "“好。你别忘了买点吃的。”"
    $ c1_before("CH01-C02", 19, "")
    n "你看着电脑屏幕。"
    $ c1_before("CH01-C02", 20, "")
    n "打开文件夹，把需要交接的材料整理好。"
    $ c1_before("CH01-C02", 21, "")
    n "临走时，你顺手把桌上的咖啡杯洗干净。"
    $ c1_before("CH01-C02", 22, "")
    n "又把没吃完的零食放进抽屉。"
    $ c1_before("CH01-C02", 23, "")
    n "这些都是再平常不过的小事。"
    $ c1_before("CH01-C02", 24, "")
    n "你并没有意识到，自己将有很长一段时间不会再回到这里。"
    jump ch01_c03

label ch01_c03:
    $ current_scene_id = "CH01-C03"
    $ current_scene_title = "行李"
    $ current_scene_time = "Day 1，21:10"
    $ current_scene_location = "沪海市公寓"
    $ phone_mode = False
    $ c1_scene("CH01-C03")
    $ c1_before("CH01-C03", 0, "")
    n "客厅地上摆着两个行李箱。"
    $ c1_before("CH01-C03", 1, "")
    n "伴侣坐在沙发上，认真核对手机上的清单。"
    $ c1_before("CH01-C03", 2, "林晚宁")
    char_partner "“衣服不用带太多吧？”"
    $ c1_before("CH01-C03", 3, "陈知远")
    char_protagonist "“够换就行。反正那边有洗衣机。”"
    $ c1_before("CH01-C03", 4, "林晚宁")
    char_partner "“电脑肯定得带。”"
    $ c1_before("CH01-C03", 5, "陈知远")
    char_protagonist "“嗯。”"
    $ c1_before("CH01-C03", 6, "林晚宁")
    char_partner "“药箱呢？”"
    $ c1_before("CH01-C03", 7, "陈知远")
    char_protagonist "“装上。”"
    $ c1_before("CH01-C03", 8, "")
    n "她抬头看着你。"
    $ c1_before("CH01-C03", 9, "林晚宁")
    char_partner "“怎么感觉我们像是在搬家。”"
    $ c1_before("CH01-C03", 10, "陈知远")
    char_protagonist "“哪有搬家只带这点东西的。”"
    $ c1_before("CH01-C03", 11, "林晚宁")
    char_partner "“也是。”"
    $ c1_before("CH01-C03", 12, "")
    n "你们把行李放在门口。"
    $ c1_before("CH01-C03", 13, "")
    n "随后给父亲打去电话。"
    $ c1_before("CH01-C03", 14, "陈建川")
    char_father "“怎么了？”"
    $ c1_before("CH01-C03", 15, "陈知远")
    char_protagonist "“爸，我和她明天回去。”"
    $ c1_before("CH01-C03", 16, "陈建川")
    char_father "“这么突然？”"
    $ c1_before("CH01-C03", 17, "陈知远")
    char_protagonist "“最近想休息一下。”"
    $ c1_before("CH01-C03", 18, "陈建川")
    char_father "“沪海那边是不是出什么事了？”"
    $ c1_before("CH01-C03", 19, "陈知远")
    char_protagonist "“现在还说不好。就是感觉不太对。”"
    $ c1_before("CH01-C03", 20, "陈建川")
    char_father "“行。那你们回来。”"
    $ c1_before("CH01-C03", 21, "陈知远")
    char_protagonist "“乡下那套房子还能住吧？”"
    $ c1_before("CH01-C03", 22, "陈建川")
    char_father "“当然能。上周还过去了。”"
    $ c1_before("CH01-C03", 23, "陈知远")
    char_protagonist "“我们想先住那边。”"
    $ c1_before("CH01-C03", 24, "陈建川")
    char_father "“可以。钥匙你不是有吗？”"
    $ c1_before("CH01-C03", 25, "陈知远")
    char_protagonist "“有。”"
    $ c1_before("CH01-C03", 26, "陈建川")
    char_father "“我明天跟你妈说一声。”"
    $ c1_before("CH01-C03", 27, "陈知远")
    char_protagonist "“她还在上班？”"
    $ c1_before("CH01-C03", 28, "陈建川")
    char_father "“明天白班。”"
    $ c1_before("CH01-C03", 29, "陈知远")
    char_protagonist "“那你们不用急着过去。我们自己能弄。”"
    $ c1_before("CH01-C03", 30, "陈建川")
    char_father "“好，路上注意安全。”"
    $ c1_before("CH01-C03", 31, "")
    n "挂断电话。"
    $ c1_before("CH01-C03", 32, "")
    n "伴侣已经把客厅收拾得差不多了。"
    $ c1_before("CH01-C03", 33, "")
    n "她站在窗边。"
    $ c1_before("CH01-C03", 34, "")
    n "沪海市的夜景依然明亮。"
    $ c1_before("CH01-C03", 35, "林晚宁")
    char_partner "“有点舍不得。”"
    $ c1_before("CH01-C03", 36, "陈知远")
    char_protagonist "“怎么？”"
    $ c1_before("CH01-C03", 37, "林晚宁")
    char_partner "“也没什么。就是突然要走了。”"
    $ c1_before("CH01-C03", 38, "")
    n "你走到她身边。"
    $ c1_before("CH01-C03", 39, "")
    n "远处高楼的灯光在夜色中闪烁。"
    $ c1_before("CH01-C03", 40, "陈知远")
    char_protagonist "“又不是不回来了。”"
    $ c1_before("CH01-C03", 41, "")
    n "她轻轻点了点头。"
    $ c1_before("CH01-C03", 42, "林晚宁")
    char_partner "“嗯。”"
    $ c1_before("CH01-C03", 43, "")
    n "两个人没有再说话。"
    jump ch01_c04

label ch01_c04:
    $ current_scene_id = "CH01-C04"
    $ current_scene_title = "清晨出发"
    $ current_scene_time = "Day 2，06:20"
    $ current_scene_location = "沪海市"
    $ phone_mode = False
    $ c1_scene("CH01-C04")
    $ c1_before("CH01-C04", 0, "")
    n "天还没有完全亮。"
    $ c1_before("CH01-C04", 1, "")
    n "你们将行李放进车里。"
    $ c1_before("CH01-C04", 2, "")
    n "车载电量显示98%%。"
    $ c1_before("CH01-C04", 3, "")
    n "道路比平日通畅许多。"
    $ c1_before("CH01-C04", 4, "")
    n "导航很快规划出一条返回庐州市的路线。"
    $ c1_before("CH01-C04", 5, "")
    $ phone_mode = True
    $ phone_speaker = "讯息"
    $ phone_text = "预计行驶距离：约500公里。"
    n "预计行驶距离：约500公里。"
    $ phone_mode = False
    $ c1_before("CH01-C04", 6, "")
    $ phone_mode = True
    $ phone_speaker = "讯息"
    $ phone_text = "预计行驶时间：视补能及道路状况而定。"
    n "预计行驶时间：视补能及道路状况而定。"
    $ phone_mode = False
    $ c1_before("CH01-C04", 7, "")
    n "伴侣把手机固定在支架上。"
    $ c1_before("CH01-C04", 8, "林晚宁")
    char_partner "“早餐怎么办？”"
    $ c1_before("CH01-C04", 9, "陈知远")
    char_protagonist "“路上买。”"
    $ c1_before("CH01-C04", 10, "林晚宁")
    char_partner "“我想吃热的。”"
    $ c1_before("CH01-C04", 11, "陈知远")
    char_protagonist "“那到服务区看看。”"
    $ c1_before("CH01-C04", 12, "林晚宁")
    char_partner "“好。”"
    $ c1_before("CH01-C04", 13, "")
    n "汽车驶出停车场。"
    $ c1_before("CH01-C04", 14, "")
    n "你们经过平时上班的路口。"
    $ c1_before("CH01-C04", 15, "")
    n "红灯亮起。"
    $ c1_before("CH01-C04", 16, "")
    n "车停了下来。"
    $ c1_before("CH01-C04", 17, "")
    n "不远处的早餐店刚刚开门。"
    $ c1_before("CH01-C04", 18, "")
    n "一个穿着围裙的男人正在搬桌子。"
    $ c1_before("CH01-C04", 19, "")
    n "有人骑着电动车经过。"
    $ c1_before("CH01-C04", 20, "")
    n "还有几名学生站在公交站台上。"
    $ c1_before("CH01-C04", 21, "")
    n "伴侣忽然说道："
    $ c1_before("CH01-C04", 22, "林晚宁")
    char_partner "“你说，如果最后什么事都没发生，我们是不是挺傻的？”"
    $ c1_before("CH01-C04", 23, "陈知远")
    char_protagonist "“那不是更好吗？”"
    $ c1_before("CH01-C04", 24, "")
    n "她想了一会儿。"
    $ c1_before("CH01-C04", 25, "林晚宁")
    char_partner "“也是。”"
    $ c1_before("CH01-C04", 26, "")
    n "红灯变绿。"
    $ c1_before("CH01-C04", 27, "")
    n "你踩下加速踏板。"
    $ c1_before("CH01-C04", 28, "")
    n "汽车缓缓驶过路口。"
    jump ch01_c05

label ch01_c05:
    $ current_scene_id = "CH01-C05"
    $ current_scene_title = "公路"
    $ current_scene_time = "Day 2，上午至下午"
    $ current_scene_location = ""
    $ phone_mode = False
    $ c1_scene("CH01-C05")
    $ c1_before("CH01-C05", 0, "")
    n "高速公路两侧的景色不断变化。"
    $ c1_before("CH01-C05", 1, "")
    n "城市。"
    $ c1_before("CH01-C05", 2, "")
    n "工厂。"
    $ c1_before("CH01-C05", 3, "")
    n "桥梁。"
    $ c1_before("CH01-C05", 4, "")
    n "田野。"
    $ c1_before("CH01-C05", 5, "")
    n "长长的隔音墙在窗外掠过。"
    $ c1_before("CH01-C05", 6, "")
    n "车载广播里正在播放新闻。"
    $ c1_before("CH01-C05", 7, "")
    n "主持人提到部分地区出现了新的公共卫生事件。"
    $ c1_before("CH01-C05", 8, "")
    n "有关部门正在开展调查。"
    $ c1_before("CH01-C05", 9, "")
    n "广播提醒公众关注正式信息，合理安排出行。"
    $ c1_before("CH01-C05", 10, "")
    n "伴侣低头看着手机。"
    $ c1_before("CH01-C05", 11, "林晚宁")
    char_partner "“我妈刚给我发消息了。”"
    $ c1_before("CH01-C05", 12, "陈知远")
    char_protagonist "“说什么？”"
    $ c1_before("CH01-C05", 13, "林晚宁")
    char_partner "“问我们怎么突然回去。”"
    $ c1_before("CH01-C05", 14, "陈知远")
    char_protagonist "“你怎么说的？”"
    $ c1_before("CH01-C05", 15, "林晚宁")
    char_partner "“说最近想休息。”"
    $ c1_before("CH01-C05", 16, "陈知远")
    char_protagonist "“她信吗？”"
    $ c1_before("CH01-C05", 17, "林晚宁")
    char_partner "“好像不太信。”"
    $ c1_before("CH01-C05", 18, "")
    n "你笑了笑。"
    $ c1_before("CH01-C05", 19, "")
    n "午后，你们在一处服务区停车。"
    $ c1_before("CH01-C05", 20, "")
    n "充电桩还有空位。"
    $ c1_before("CH01-C05", 21, "")
    n "旁边的餐厅正在营业。"
    $ c1_before("CH01-C05", 22, "")
    n "有人端着面条从餐厅里走出来。"
    $ c1_before("CH01-C05", 23, "")
    n "远处的休息区坐着几个带孩子的家庭。"
    $ c1_before("CH01-C05", 24, "")
    n "伴侣站在自动售货机前。"
    $ c1_before("CH01-C05", 25, "林晚宁")
    char_partner "“你喝什么？”"
    $ c1_before("CH01-C05", 26, "陈知远")
    char_protagonist "“水就行。”"
    $ c1_before("CH01-C05", 27, "林晚宁")
    char_partner "“不喝咖啡了？”"
    $ c1_before("CH01-C05", 28, "陈知远")
    char_protagonist "“今天已经喝过了。”"
    $ c1_before("CH01-C05", 29, "")
    n "她给你递来一瓶水。"
    $ c1_before("CH01-C05", 30, "")
    n "两个人坐在长椅上，等车辆补能。"
    $ c1_before("CH01-C05", 31, "")
    n "远处的停车场里，一名工作人员正在提醒旅客佩戴口罩。"
    $ c1_before("CH01-C05", 32, "")
    n "另一个人则在打电话，抱怨前面有些道路开始检查。"
    $ c1_before("CH01-C05", 33, "")
    n "你们听见了，却没有参与讨论。"
    $ c1_before("CH01-C05", 34, "林晚宁")
    char_partner "“我忽然有点期待回去了。”"
    $ c1_before("CH01-C05", 35, "陈知远")
    char_protagonist "“期待什么？”"
    $ c1_before("CH01-C05", 36, "林晚宁")
    char_partner "“睡觉。”"
    $ c1_before("CH01-C05", 37, "")
    n "你笑出了声。"
    $ c1_before("CH01-C05", 38, "林晚宁")
    char_partner "“真的。什么都不用想，先睡个够。”"
    $ c1_before("CH01-C05", 39, "陈知远")
    char_protagonist "“那恐怕要让你失望了。”"
    $ c1_before("CH01-C05", 40, "林晚宁")
    char_partner "“为什么？”"
    $ c1_before("CH01-C05", 41, "陈知远")
    char_protagonist "“我爸知道我们回来，估计明天就要拉着我们整理房子。”"
    $ c1_before("CH01-C05", 42, "")
    n "她无奈地笑了。"
    $ c1_before("CH01-C05", 43, "林晚宁")
    char_partner "“那我现在反悔还来得及吗？”"
    $ c1_before("CH01-C05", 44, "陈知远")
    char_protagonist "“来不及了。”"
    $ c1_before("CH01-C05", 45, "")
    n "汽车再次驶上高速。"
    jump ch01_c06

label ch01_c06:
    $ current_scene_id = "CH01-C06"
    $ current_scene_title = "早归"
    $ current_scene_time = "Day 2，18:10"
    $ current_scene_location = "庐州市城郊"
    $ phone_mode = False
    $ c1_scene("CH01-C06")
    $ c1_before("CH01-C06", 0, "")
    n "夕阳已经落到了远处建筑的后面。"
    $ c1_before("CH01-C06", 1, "")
    n "道路两侧出现低矮的房屋。"
    $ c1_before("CH01-C06", 2, "")
    n "远处高层公寓的轮廓在暮色中显得格外清楚。"
    $ c1_before("CH01-C06", 3, "")
    n "还有几座仓库，静静地坐落在道路另一侧。"
    $ c1_before("CH01-C06", 4, "")
    n "伴侣打开车窗。"
    $ c1_before("CH01-C06", 5, "")
    n "一阵微凉的风吹进来。"
    $ c1_before("CH01-C06", 6, "林晚宁")
    char_partner "“快到了？”"
    $ c1_before("CH01-C06", 7, "陈知远")
    char_protagonist "“嗯。前面再转两个路口。”"
    $ c1_before("CH01-C06", 8, "林晚宁")
    char_partner "“这地方还挺安静。”"
    $ c1_before("CH01-C06", 9, "陈知远")
    char_protagonist "“晚上是挺安静的。”"
    $ c1_before("CH01-C06", 10, "")
    n "远处传来火车经过的声音。"
    $ c1_before("CH01-C06", 11, "")
    n "你们沿着乡村道路继续向前。"
    $ c1_before("CH01-C06", 12, "")
    n "不久，一栋三层独栋住宅出现在视线中。"
    $ c1_before("CH01-C06", 13, "")
    n "灰白色的外墙。"
    $ c1_before("CH01-C06", 14, "")
    n "普通的砖砌院墙。"
    $ c1_before("CH01-C06", 15, "")
    n "一扇有些旧的金属院门。"
    $ c1_before("CH01-C06", 16, "")
    n "房屋没有什么特别显眼的地方。"
    $ c1_before("CH01-C06", 17, "")
    n "只是屋顶上的光伏组件在暮色中反射着最后一点光。"
    $ c1_before("CH01-C06", 18, "")
    n "你把车停在院门前。"
    $ c1_before("CH01-C06", 19, "林晚宁")
    char_partner "“到了？”"
    $ c1_before("CH01-C06", 20, "陈知远")
    char_protagonist "“到了。”"
    $ c1_before("CH01-C06", 21, "")
    n "你下车打开院门。"
    $ c1_before("CH01-C06", 22, "")
    n "院子里很安静。"
    $ c1_before("CH01-C06", 23, "")
    n "屋子里没有开灯。"
    $ c1_before("CH01-C06", 24, "")
    n "伴侣从车上取下一个行李箱。"
    $ c1_before("CH01-C06", 25, "林晚宁")
    char_partner "“钥匙呢？”"
    $ c1_before("CH01-C06", 26, "")
    n "你从背包里翻出钥匙。"
    $ c1_before("CH01-C06", 27, "")
    n "锁芯有些发涩。"
    $ c1_before("CH01-C06", 28, "")
    n "转动两下之后，门终于打开。"
    $ c1_before("CH01-C06", 29, "")
    n "屋里带着一点久未居住的气味。"
    $ c1_before("CH01-C06", 30, "")
    n "你伸手按下开关。"
    $ c1_before("CH01-C06", 31, "")
    n "灯亮了。"
    $ c1_before("CH01-C06", 32, "")
    n "客厅里整整齐齐地摆着家具。"
    $ c1_before("CH01-C06", 33, "")
    n "窗边的柜子上放着一个旧相框。"
    $ c1_before("CH01-C06", 34, "")
    n "伴侣把行李箱放在门旁。"
    $ c1_before("CH01-C06", 35, "林晚宁")
    char_partner "“还不错嘛。”"
    $ c1_before("CH01-C06", 36, "陈知远")
    char_protagonist "“我爸他们经常过来打扫。”"
    $ c1_before("CH01-C06", 37, "")
    n "她走到窗边，拉开窗帘。"
    $ c1_before("CH01-C06", 38, "")
    n "院子外面是一条安静的乡村道路。"
    $ c1_before("CH01-C06", 39, "")
    n "不远处，几户人家的厨房已经亮起灯。"
    $ c1_before("CH01-C06", 40, "林晚宁")
    char_partner "“我们现在做什么？”"
    $ c1_before("CH01-C06", 41, "")
    n "你看着客厅。"
    $ c1_before("CH01-C06", 42, "")
    n "又看了一眼行李箱。"
    $ c1_before("CH01-C06", 43, "陈知远")
    char_protagonist "“先收拾一下。”"
    $ c1_before("CH01-C06", 44, "林晚宁")
    char_partner "“然后呢？”"
    $ c1_before("CH01-C06", 45, "陈知远")
    char_protagonist "“然后吃饭。”"
    $ c1_before("CH01-C06", 46, "林晚宁")
    char_partner "“好。”"
    $ c1_before("CH01-C06", 47, "")
    n "她笑了。"
    $ c1_before("CH01-C06", 48, "")
    n "你拿起手机，给父母发去消息。"
    $ c1_before("CH01-C06", 49, "陈知远")
    $ phone_mode = True
    $ phone_speaker = "陈知远"
    $ phone_text = "“我们到了。”"
    n "“我们到了。”"
    $ phone_mode = False
    $ c1_before("CH01-C06", 50, "陈建川")
    $ phone_mode = True
    $ phone_speaker = "陈建川"
    $ phone_text = "“这么早？路上还顺利吧？”"
    n "“这么早？路上还顺利吧？”"
    $ phone_mode = False
    $ c1_before("CH01-C06", 51, "陈知远")
    $ phone_mode = True
    $ phone_speaker = "陈知远"
    $ phone_text = "“挺顺利的。”"
    n "“挺顺利的。”"
    $ phone_mode = False
    $ c1_before("CH01-C06", 52, "周慧敏")
    $ phone_mode = True
    $ phone_speaker = "周慧敏"
    $ phone_text = "“饭吃了没有？”"
    n "“饭吃了没有？”"
    $ phone_mode = False
    $ c1_before("CH01-C06", 53, "林晚宁")
    $ phone_mode = True
    $ phone_speaker = "林晚宁"
    $ phone_text = "“还没呢，准备找点吃的。”"
    n "“还没呢，准备找点吃的。”"
    $ phone_mode = False
    $ c1_before("CH01-C06", 54, "周慧敏")
    $ phone_mode = True
    $ phone_speaker = "周慧敏"
    $ phone_text = "“厨房柜子里有面，冰箱里还有东西。明天我们过去。”"
    n "“厨房柜子里有面，冰箱里还有东西。明天我们过去。”"
    $ phone_mode = False
    $ c1_before("CH01-C06", 55, "")
    n "你看着手机上的消息，忽然有些安心。"
    $ c1_before("CH01-C06", 56, "")
    n "窗外，一辆电动车慢慢驶过。"
    $ c1_before("CH01-C06", 57, "")
    n "远处传来几声犬吠。"
    $ c1_before("CH01-C06", 58, "")
    n "屋里的灯光温暖而明亮。"
    $ c1_before("CH01-C06", 59, "")
    n "这栋曾经因为地震而购置的房子，终于迎来了新的住客。"
    $ c1_before("CH01-C06", 60, "")
    n "……"
    $ c1_before("CH01-C06", 61, "")
    n "离开熟悉的城市后，家乡的灯光依然为你亮着。"
    $ chapter_route = "C"
    call route_end("C")
    return

label ch01_d01:
    $ current_scene_id = "CH01-D01"
    $ current_scene_title = "工作日"
    $ current_scene_time = "Day 1，08:30—21:00"
    $ current_scene_location = "沪海市"
    $ phone_mode = False
    $ c1_scene("CH01-D01")
    $ c1_before("CH01-D01", 0, "")
    n "你收起手机。"
    $ c1_before("CH01-D01", 1, "")
    n "无论发生了什么，眼下都还没有可靠的结论。"
    $ c1_before("CH01-D01", 2, "")
    n "况且，再过不久就要上班了。"
    $ c1_before("CH01-D01", 3, "")
    n "你走进地铁站。"
    $ c1_before("CH01-D01", 4, "")
    n "刷卡。"
    $ c1_before("CH01-D01", 5, "")
    n "安检。"
    $ c1_before("CH01-D01", 6, "")
    n "候车。"
    $ c1_before("CH01-D01", 7, "")
    n "列车进站。"
    $ c1_before("CH01-D01", 8, "")
    n "所有步骤都熟悉得不需要思考。"
    $ c1_before("CH01-D01", 9, "")
    n "上午的会议照常进行。"
    $ c1_before("CH01-D01", 10, "")
    n "午间，有同事提起医院的视频。"
    $ c1_before("CH01-D01", 11, "同事甲")
    n "同事甲：“你们看见今天那个新闻了吗？”"
    $ c1_before("CH01-D01", 12, "同事乙")
    n "同事乙：“看了，好像是什么传染病。”"
    $ c1_before("CH01-D01", 13, "同事甲")
    n "同事甲：“网上说得可吓人了。”"
    $ c1_before("CH01-D01", 14, "同事乙")
    n "同事乙：“过两天应该就清楚了吧。”"
    $ c1_before("CH01-D01", 15, "")
    n "有人笑了笑。"
    $ c1_before("CH01-D01", 16, "")
    n "话题很快转向了下午的工作。"
    $ c1_before("CH01-D01", 17, "")
    n "晚上，伴侣买了菜。"
    $ c1_before("CH01-D01", 18, "")
    n "两人在厨房里忙了一会儿。"
    $ c1_before("CH01-D01", 19, "林晚宁")
    char_partner "“今天外面好多人戴口罩。”"
    $ c1_before("CH01-D01", 20, "陈知远")
    char_protagonist "“嗯，我也看见了。”"
    $ c1_before("CH01-D01", 21, "林晚宁")
    char_partner "“我们要不要买几盒？”"
    $ c1_before("CH01-D01", 22, "陈知远")
    char_protagonist "“家里不是还有吗？”"
    $ c1_before("CH01-D01", 23, "林晚宁")
    char_partner "“好像剩得不多了。”"
    $ c1_before("CH01-D01", 24, "陈知远")
    char_protagonist "“那周末去超市买点吧。”"
    $ c1_before("CH01-D01", 25, "林晚宁")
    char_partner "“行。”"
    $ c1_before("CH01-D01", 26, "")
    n "吃完饭，你们看了一部电影。"
    $ c1_before("CH01-D01", 27, "")
    n "十一点多，伴侣先去睡觉。"
    $ c1_before("CH01-D01", 28, "")
    n "你坐在沙发上，刷了一会儿手机。"
    $ c1_before("CH01-D01", 29, "")
    n "新闻软件推送了一条新的疫情消息。"
    $ c1_before("CH01-D01", 30, "")
    n "你看了一眼标题。"
    $ c1_before("CH01-D01", 31, "")
    n "然后划了过去。"
    $ c1_before("CH01-D01", 32, "")
    n "第二天还要上班。"
    jump ch01_d02

label ch01_d02:
    $ current_scene_id = "CH01-D02"
    $ current_scene_title = "下周再说"
    $ current_scene_time = "Day 2—Day 4"
    $ current_scene_location = ""
    $ phone_mode = False
    $ c1_scene("CH01-D02")
    $ c1_before("CH01-D02", 0, "")
    n "几天过去。"
    $ c1_before("CH01-D02", 1, "")
    n "网上关于异常病例的消息越来越多。"
    $ c1_before("CH01-D02", 2, "")
    n "有人发布了医院门口排队的照片。"
    $ c1_before("CH01-D02", 3, "")
    n "有人声称某个居民区已经实施封闭管理。"
    $ c1_before("CH01-D02", 4, "")
    n "还有人不断转发模糊不清的视频。"
    $ c1_before("CH01-D02", 5, "")
    n "但沪海市大部分地区仍然保持着正常生活。"
    $ c1_before("CH01-D02", 6, "")
    n "你依旧能够坐地铁上班。"
    $ c1_before("CH01-D02", 7, "")
    n "楼下的便利店仍然营业。"
    $ c1_before("CH01-D02", 8, "")
    n "快递也没有完全中断。"
    $ c1_before("CH01-D02", 9, "")
    n "某天下午，公司召开了一次临时会议。"
    $ c1_before("CH01-D02", 10, "")
    n "负责人宣布，考虑到近期公共卫生风险，部分员工将逐渐转为远程办公。"
    $ c1_before("CH01-D02", 11, "")
    n "办公室里响起一些低声议论。"
    $ c1_before("CH01-D02", 12, "同事甲")
    n "同事甲：“那下周是不是不用来了？”"
    $ c1_before("CH01-D02", 13, "同事乙")
    n "同事乙：“看安排吧。”"
    $ c1_before("CH01-D02", 14, "同事甲")
    n "同事甲：“早该这样了。”"
    $ c1_before("CH01-D02", 15, "")
    n "你也觉得这个安排不错。"
    $ c1_before("CH01-D02", 16, "")
    n "至少可以省下通勤的时间。"
    $ c1_before("CH01-D02", 17, "")
    n "晚上，伴侣向你提起返乡的事情。"
    $ c1_before("CH01-D02", 18, "林晚宁")
    char_partner "“我们要不要也回庐州？”"
    $ c1_before("CH01-D02", 19, "陈知远")
    char_protagonist "“现在回去干什么？”"
    $ c1_before("CH01-D02", 20, "林晚宁")
    char_partner "“就是觉得最近有点乱。”"
    $ c1_before("CH01-D02", 21, "陈知远")
    char_protagonist "“再看看吧。”"
    $ c1_before("CH01-D02", 22, "林晚宁")
    char_partner "“万一后面交通限制更多呢？”"
    $ c1_before("CH01-D02", 23, "陈知远")
    char_protagonist "“现在也还没到那个程度。”"
    $ c1_before("CH01-D02", 24, "")
    n "她没有再说话。"
    $ c1_before("CH01-D02", 25, "")
    n "你打开电视。"
    $ c1_before("CH01-D02", 26, "")
    n "新闻里正在播放一场发布会。"
    $ c1_before("CH01-D02", 27, "")
    n "有关部门宣布将根据疫情调查结果，对部分区域采取临时交通及人员管理措施。"
    $ c1_before("CH01-D02", 28, "")
    n "你看了一会儿。"
    $ c1_before("CH01-D02", 29, "陈知远")
    char_protagonist "“等周末吧。”"
    $ c1_before("CH01-D02", 30, "林晚宁")
    char_partner "“嗯。”"
    $ c1_before("CH01-D02", 31, "")
    n "那天晚上，你们照常睡觉。"
    $ c1_before("CH01-D02", 32, "")
    n "没有任何特别的事情发生。"
    jump ch01_d03

label ch01_d03:
    $ current_scene_id = "CH01-D03"
    $ current_scene_title = "关门"
    $ current_scene_time = "Day 6，16:34"
    $ current_scene_location = "沪海市，社区附近"
    $ phone_mode = False
    $ c1_scene("CH01-D03")
    $ c1_before("CH01-D03", 0, "")
    n "你终于决定去超市买点东西。"
    $ c1_before("CH01-D03", 1, "")
    n "但当你走到门口时，才发现货架已经空了一大片。"
    $ c1_before("CH01-D03", 2, "")
    n "方便食品、饮用水和常用药品都比平时难买。"
    $ c1_before("CH01-D03", 3, "")
    n "部分商品贴着限购通知。"
    $ c1_before("CH01-D03", 4, "")
    n "收银台前排着很长的队。"
    $ c1_before("CH01-D03", 5, "")
    n "一个中年男人正在和店员争论。"
    $ c1_before("CH01-D03", 6, "顾客")
    n "顾客：“我昨天来的时候还有，怎么今天就没有了？”"
    $ c1_before("CH01-D03", 7, "店员")
    n "店员：“今天的货没送到，我们也没办法。”"
    $ c1_before("CH01-D03", 8, "")
    n "你买到了一些饼干、面包和瓶装水。"
    $ c1_before("CH01-D03", 9, "")
    n "结账时，身后的顾客不断看手机。"
    $ c1_before("CH01-D03", 10, "后面的顾客")
    n "后面的顾客：“听说出城的路都开始查了。”"
    $ c1_before("CH01-D03", 11, "另一人")
    n "另一人：“真的假的？”"
    $ c1_before("CH01-D03", 12, "后面的顾客")
    n "后面的顾客：“我亲戚今天开车回老家，走了几个小时还没出去。”"
    $ c1_before("CH01-D03", 13, "")
    n "你听见这句话，心里突然一沉。"
    $ c1_before("CH01-D03", 14, "")
    n "回到公寓后，你打开导航。"
    $ c1_before("CH01-D03", 15, "")
    n "几条主要出城道路显示异常拥堵。"
    $ c1_before("CH01-D03", 16, "")
    n "部分高速入口已经实施临时管制。"
    $ c1_before("CH01-D03", 17, "")
    n "你给父亲打去电话。"
    $ c1_before("CH01-D03", 18, "陈建川")
    char_father "“喂？”"
    $ c1_before("CH01-D03", 19, "陈知远")
    char_protagonist "“爸，我们可能想回去。”"
    $ c1_before("CH01-D03", 20, "陈建川")
    char_father "“那就早点回来。”"
    $ c1_before("CH01-D03", 21, "陈知远")
    char_protagonist "“我刚看了，外面好像很多路不让走了。”"
    $ c1_before("CH01-D03", 22, "")
    n "电话另一边沉默了几秒。"
    $ c1_before("CH01-D03", 23, "陈建川")
    char_father "“你先看看有没有正常的通行办法。”"
    $ c1_before("CH01-D03", 24, "陈知远")
    char_protagonist "“嗯。”"
    $ c1_before("CH01-D03", 25, "陈建川")
    char_father "“你们别乱跑，安全最重要。”"
    $ c1_before("CH01-D03", 26, "陈知远")
    char_protagonist "“知道。”"
    $ c1_before("CH01-D03", 27, "")
    n "挂断电话。"
    $ c1_before("CH01-D03", 28, "")
    n "你打开各类出行平台。"
    $ c1_before("CH01-D03", 29, "")
    n "高铁车次大幅减少。"
    $ c1_before("CH01-D03", 30, "")
    n "跨城客运基本停止。"
    $ c1_before("CH01-D03", 31, "")
    n "道路通行信息反复变化。"
    $ c1_before("CH01-D03", 32, "")
    n "部分检查点只允许符合临时通行条件的车辆通过。"
    $ c1_before("CH01-D03", 33, "")
    n "你想了许多办法。"
    $ c1_before("CH01-D03", 34, "")
    n "但没有一个能够让你确定地离开沪海市。"
    $ c1_before("CH01-D03", 35, "")
    n "伴侣站在身后。"
    $ c1_before("CH01-D03", 36, "林晚宁")
    char_partner "“怎么样？”"
    $ c1_before("CH01-D03", 37, "")
    n "你沉默了一会儿。"
    $ c1_before("CH01-D03", 38, "陈知远")
    char_protagonist "“暂时走不了。”"
    $ c1_before("CH01-D03", 39, "")
    n "她看着手机上的路线图。"
    $ c1_before("CH01-D03", 40, "林晚宁")
    char_partner "“那我们怎么办？”"
    $ c1_before("CH01-D03", 41, "陈知远")
    char_protagonist "“先在家待几天。”"
    $ c1_before("CH01-D03", 42, "")
    n "窗外，一辆救护车从道路上驶过。"
    $ c1_before("CH01-D03", 43, "")
    n "警笛声渐渐远去。"
    jump ch01_d04

label ch01_d04:
    $ current_scene_id = "CH01-D04"
    $ current_scene_title = "公寓"
    $ current_scene_time = "Day 10"
    $ current_scene_location = "沪海市公寓"
    $ phone_mode = False
    $ c1_scene("CH01-D04")
    $ c1_before("CH01-D04", 0, "")
    n "外面的城市仍然存在。"
    $ c1_before("CH01-D04", 1, "")
    n "只是你能够接触到的部分越来越少。"
    $ c1_before("CH01-D04", 2, "")
    n "楼下的餐厅已经停止营业。"
    $ c1_before("CH01-D04", 3, "")
    n "快递配送变得不稳定。"
    $ c1_before("CH01-D04", 4, "")
    n "小区开始实行更严格的出入管理。"
    $ c1_before("CH01-D04", 5, "")
    n "住宅楼里仍然有人生活。"
    $ c1_before("CH01-D04", 6, "")
    n "楼道里偶尔传来开门声。"
    $ c1_before("CH01-D04", 7, "")
    n "有人在电梯口放下垃圾袋。"
    $ c1_before("CH01-D04", 8, "")
    n "也有人从门缝里探出头，询问社区物资发放的时间。"
    $ c1_before("CH01-D04", 9, "")
    n "你和伴侣开始认真清点家里的食品。"
    $ c1_before("CH01-D04", 10, "")
    n "几袋方便面。"
    $ c1_before("CH01-D04", 11, "")
    n "一些罐头。"
    $ c1_before("CH01-D04", 12, "")
    n "两箱饮用水。"
    $ c1_before("CH01-D04", 13, "")
    n "还有冰箱里剩下的食材。"
    $ c1_before("CH01-D04", 14, "林晚宁")
    char_partner "“这些还能吃多久？”"
    $ c1_before("CH01-D04", 15, "陈知远")
    char_protagonist "“省着点吃，应该够一阵子。”"
    $ c1_before("CH01-D04", 16, "林晚宁")
    char_partner "“社区不是说有物资配送吗？”"
    $ c1_before("CH01-D04", 17, "陈知远")
    char_protagonist "“说是会安排。”"
    $ c1_before("CH01-D04", 18, "")
    n "她点了点头。"
    $ c1_before("CH01-D04", 19, "")
    n "你打开手机。"
    $ c1_before("CH01-D04", 20, "")
    n "父母发来消息。"
    $ c1_before("CH01-D04", 21, "周慧敏")
    char_mother "“你们那边现在怎么样？”"
    $ c1_before("CH01-D04", 22, "陈知远")
    char_protagonist "“还行，就是暂时出不去。”"
    $ c1_before("CH01-D04", 23, "周慧敏")
    char_mother "“吃的够不够？”"
    $ c1_before("CH01-D04", 24, "陈知远")
    char_protagonist "“够，别担心。”"
    $ c1_before("CH01-D04", 25, "")
    n "你看着自己刚刚发出去的两个字。"
    $ c1_before("CH01-D04", 26, "")
    n "又看了一眼桌上的食物。"
    $ c1_before("CH01-D04", 27, "")
    n "没有再说什么。"
    $ c1_before("CH01-D04", 28, "")
    n "窗外偶尔能听见警笛声。"
    $ c1_before("CH01-D04", 29, "")
    n "不知道从什么时候起，你已经习惯了这种声音。"
    $ c1_before("CH01-D04", 30, "")
    n "反而是警笛停止的时候，更容易感到不安。"
    jump ch01_d05

label ch01_d05:
    $ current_scene_id = "CH01-D05"
    $ current_scene_title = "日子"
    $ current_scene_time = "Day 17—Day 24"
    $ current_scene_location = ""
    $ phone_mode = False
    $ c1_scene("CH01-D05")
    $ c1_before("CH01-D05", 0, "")
    n "手机日历翻过一页。"
    $ c1_before("CH01-D05", 1, "")
    n "接着又翻过一页。"
    $ c1_before("CH01-D05", 2, "")
    n "餐桌上的食品逐渐减少。"
    $ c1_before("CH01-D05", 3, "")
    n "冰箱里的新鲜食材早已吃完。"
    $ c1_before("CH01-D05", 4, "")
    n "墙上的时钟依旧在走。"
    $ c1_before("CH01-D05", 5, "")
    n "某天早晨，楼里突然停了电。"
    $ c1_before("CH01-D05", 6, "")
    n "但几小时后又恢复了。"
    $ c1_before("CH01-D05", 7, "")
    n "另一天，水龙头里的水流变得很小。"
    $ c1_before("CH01-D05", 8, "")
    n "物业群里有人解释，楼宇供水设备出了问题，正在联系维修。"
    $ c1_before("CH01-D05", 9, "")
    n "你在群里看到有人发出求助消息。"
    $ c1_before("CH01-D05", 10, "")
    n "一户居民家中有人发烧，希望能够得到帮助。"
    $ c1_before("CH01-D05", 11, "")
    n "另一个人回复说，社区医疗人员暂时无法及时赶来。"
    $ c1_before("CH01-D05", 12, "")
    n "群里争论了很久。"
    $ c1_before("CH01-D05", 13, "")
    n "最后没有人再说话。"
    $ c1_before("CH01-D05", 14, "")
    n "伴侣坐在窗边。"
    $ c1_before("CH01-D05", 15, "")
    n "她已经很久没有出门。"
    $ c1_before("CH01-D05", 16, "林晚宁")
    char_partner "“今天几号了？”"
    $ c1_before("CH01-D05", 17, "")
    n "你看了一眼手机。"
    $ c1_before("CH01-D05", 18, "")
    n "告诉了她。"
    $ c1_before("CH01-D05", 19, "林晚宁")
    char_partner "“已经这么久了。”"
    $ c1_before("CH01-D05", 20, "陈知远")
    char_protagonist "“嗯。”"
    $ c1_before("CH01-D05", 21, "林晚宁")
    char_partner "“你说外面什么时候能恢复？”"
    $ c1_before("CH01-D05", 22, "陈知远")
    char_protagonist "“不知道。”"
    $ c1_before("CH01-D05", 23, "")
    n "她望着窗外。"
    $ c1_before("CH01-D05", 24, "")
    n "远处仍然有些楼房亮着灯。"
    $ c1_before("CH01-D05", 25, "")
    n "有一条主干道上，偶尔还能看见执行任务的车辆。"
    $ c1_before("CH01-D05", 26, "")
    n "城市并没有完全死去。"
    $ c1_before("CH01-D05", 27, "")
    n "只是你们已经无法像过去那样自由地生活。"
    $ c1_before("CH01-D05", 28, "林晚宁")
    char_partner "“我想回家。”"
    $ c1_before("CH01-D05", 29, "")
    n "你转过头。"
    $ c1_before("CH01-D05", 30, "陈知远")
    char_protagonist "“我知道。”"
    $ c1_before("CH01-D05", 31, "林晚宁")
    char_partner "“我是说，真的很想回去。”"
    $ c1_before("CH01-D05", 32, "")
    n "你没有回答。"
    $ c1_before("CH01-D05", 33, "")
    n "手机里还保存着庐州市那栋房子的照片。"
    $ c1_before("CH01-D05", 34, "")
    n "照片上，院子里阳光明亮。"
    $ c1_before("CH01-D05", 35, "")
    n "父亲站在楼梯旁边。"
    $ c1_before("CH01-D05", 36, "")
    n "母亲正在整理花盆。"
    $ c1_before("CH01-D05", 37, "")
    n "你忽然不敢再看。"
    jump ch01_d06

label ch01_d06:
    $ current_scene_id = "CH01-D06"
    $ current_scene_title = "楼道"
    $ current_scene_time = "Day 25，深夜"
    $ current_scene_location = "沪海市公寓"
    $ phone_mode = False
    $ c1_scene("CH01-D06")
    $ c1_before("CH01-D06", 0, "")
    n "你被一阵刺耳的声音惊醒。"
    $ c1_before("CH01-D06", 1, "")
    n "起初，你以为是手机闹钟。"
    $ c1_before("CH01-D06", 2, "")
    n "随后才意识到，是楼里的火灾报警器。"
    $ c1_before("CH01-D06", 3, "")
    n "伴侣也醒了。"
    $ c1_before("CH01-D06", 4, "林晚宁")
    char_partner "“怎么了？”"
    $ c1_before("CH01-D06", 5, "陈知远")
    char_protagonist "“不知道，可能是报警器。”"
    $ c1_before("CH01-D06", 6, "")
    n "你下床，走到门边。"
    $ c1_before("CH01-D06", 7, "")
    n "楼道里传来急促的脚步声。"
    $ c1_before("CH01-D06", 8, "")
    n "有人在喊叫。"
    $ c1_before("CH01-D06", 9, "")
    n "还夹杂着门板被用力敲打的声音。"
    $ c1_before("CH01-D06", 10, "")
    n "你透过猫眼望出去。"
    $ c1_before("CH01-D06", 11, "")
    n "走廊上的应急灯正在闪烁。"
    $ c1_before("CH01-D06", 12, "")
    n "几个人从远处跑过。"
    $ c1_before("CH01-D06", 13, "")
    n "其中一人不小心撞到墙上。"
    $ c1_before("CH01-D06", 14, "")
    n "他似乎在躲避什么。"
    $ c1_before("CH01-D06", 15, "")
    n "随后，一个动作异常的人影从拐角处冲了出来。"
    $ c1_before("CH01-D06", 16, "")
    n "那人没有停下。"
    $ c1_before("CH01-D06", 17, "")
    n "径直扑向走廊另一端。"
    $ c1_before("CH01-D06", 18, "")
    n "你猛地离开猫眼。"
    $ c1_before("CH01-D06", 19, "林晚宁")
    char_partner "“外面怎么了？”"
    $ c1_before("CH01-D06", 20, "陈知远")
    char_protagonist "“别出声。”"
    $ c1_before("CH01-D06", 21, "")
    n "你转身检查门锁。"
    $ c1_before("CH01-D06", 22, "")
    n "刚刚走到客厅，一股淡淡的焦糊味飘了进来。"
    $ c1_before("CH01-D06", 23, "")
    n "烟雾开始从门缝和通风口渗入。"
    $ c1_before("CH01-D06", 24, "")
    n "你打开手机，拨打物业电话。"
    $ c1_before("CH01-D06", 25, "")
    n "无人接听。"
    $ c1_before("CH01-D06", 26, "")
    n "你又尝试拨打紧急求助电话。"
    $ c1_before("CH01-D06", 27, "")
    n "线路一直繁忙。"
    $ c1_before("CH01-D06", 28, "")
    n "伴侣拿来湿毛巾。"
    $ c1_before("CH01-D06", 29, "林晚宁")
    char_partner "“是不是着火了？”"
    $ c1_before("CH01-D06", 30, "陈知远")
    char_protagonist "“不知道。但楼道里有人出事了。”"
    $ c1_before("CH01-D06", 31, "")
    n "你走到窗边。"
    $ c1_before("CH01-D06", 32, "")
    n "楼下聚集着一些人。"
    $ c1_before("CH01-D06", 33, "")
    n "有人正仰头望向楼上。"
    $ c1_before("CH01-D06", 34, "")
    n "远处能听见消防车辆的警笛声。"
    $ c1_before("CH01-D06", 35, "")
    n "但住宅楼外的道路已经被临时停放的车辆堵住了一部分。"
    $ c1_before("CH01-D06", 36, "")
    n "楼道里的声音越来越近。"
    $ c1_before("CH01-D06", 37, "")
    n "你猛地转过身。"
    $ c1_before("CH01-D06", 38, "")
    n "有人正在敲门。"
    $ c1_before("CH01-D06", 39, "门外的声音")
    n "门外的声音：“开门！”"
    $ c1_before("CH01-D06", 40, "")
    n "又是一阵撞击。"
    $ c1_before("CH01-D06", 41, "门外的声音")
    n "门外的声音：“快！里面有人吗？！”"
    $ c1_before("CH01-D06", 42, "")
    n "你看向伴侣。"
    $ c1_before("CH01-D06", 43, "")
    n "她的脸色很苍白。"
    $ c1_before("CH01-D06", 44, "")
    n "门外突然传来一声尖叫。"
    $ c1_before("CH01-D06", 45, "")
    n "紧接着，是混乱的脚步声。"
    $ c1_before("CH01-D06", 46, "")
    n "又过了一会儿。"
    $ c1_before("CH01-D06", 47, "")
    n "敲门声停止了。"
    $ c1_before("CH01-D06", 48, "")
    n "只剩下持续不断的火灾警报。"
    $ c1_before("CH01-D06", 49, "")
    n "空气中的烟味越来越浓。"
    $ c1_before("CH01-D06", 50, "")
    n "你知道，继续留在房间里也可能会有危险。"
    $ c1_before("CH01-D06", 51, "")
    n "但走廊里究竟发生了什么，你同样不知道。"
    $ c1_before("CH01-D06", 52, "")
    n "你们收拾起仅剩的随身物品，准备寻找能够安全撤离的路线。"
    $ c1_before("CH01-D06", 53, "")
    n "就在你靠近房门、准备再次观察外面的时候，一声沉重的撞击突然响起。"
    $ c1_before("CH01-D06", 54, "")
    n "门锁剧烈晃动。"
    $ c1_before("CH01-D06", 55, "")
    n "第二下。"
    $ c1_before("CH01-D06", 56, "")
    n "第三下。"
    $ c1_before("CH01-D06", 57, "")
    n "伴侣退到了你身后。"
    $ c1_before("CH01-D06", 58, "林晚宁")
    char_partner "“怎么办？”"
    $ c1_before("CH01-D06", 59, "")
    n "你紧紧盯着门。"
    $ c1_before("CH01-D06", 60, "")
    n "没有回答。"
    $ c1_before("CH01-D06", 61, "")
    n "门外的撞击声与火警声混在一起。"
    $ c1_before("CH01-D06", 62, "")
    n "你听见门框发出了不堪重负的声音。"
    $ c1_before("CH01-D06", 63, "林晚宁")
    char_partner "“我们是不是……回不去了？”"
    $ c1_before("CH01-D06", 64, "")
    n "你想开口。"
    $ c1_before("CH01-D06", 65, "")
    n "却不知道该说什么。"
    $ c1_before("CH01-D06", 66, "")
    n "……"
    $ c1_before("CH01-D06", 67, "")
    n "这座公寓没有成为你们最后的避难所。"
    $ c1_before("CH01-D06", 68, "")
    n "它只是你们再也没能离开的地方。"
    jump ch01_d07

label ch01_d07:
    $ current_scene_id = "CH01-D07"
    $ current_scene_title = "围城"
    $ current_scene_time = ""
    $ current_scene_location = ""
    $ phone_mode = False
    $ c1_scene("CH01-D07")
    $ c1_before("CH01-D07", 0, "")
    n "早晨的光线从窗帘缝隙照进房间。"
    $ c1_before("CH01-D07", 1, "")
    n "餐桌上放着两只空杯子。"
    $ c1_before("CH01-D07", 2, "")
    n "墙上的时钟仍然在走。"
    $ c1_before("CH01-D07", 3, "")
    n "手机屏幕亮了起来。"
    $ c1_before("CH01-D07", 4, "周慧敏（母亲）· 未读消息")
    $ phone_mode = True
    $ phone_speaker = "周慧敏（母亲）· 未读消息"
    $ phone_text = "“今天好点了吗？”"
    n "“今天好点了吗？”"
    $ phone_mode = False
    $ c1_before("CH01-D07", 5, "周慧敏（母亲）· 未读消息")
    $ phone_mode = True
    $ phone_speaker = "周慧敏（母亲）· 未读消息"
    $ phone_text = "“看到消息回个电话。”"
    n "“看到消息回个电话。”"
    $ phone_mode = False
    $ c1_before("CH01-D07", 6, "周慧敏（母亲）· 未读消息")
    $ phone_mode = True
    $ phone_speaker = "周慧敏（母亲）· 未读消息"
    $ phone_text = "“乡下的房子已经收拾好了。”"
    n "“乡下的房子已经收拾好了。”"
    $ phone_mode = False
    $ c1_before("CH01-D07", 7, "周慧敏（母亲）· 未读消息")
    $ phone_mode = True
    $ phone_speaker = "周慧敏（母亲）· 未读消息"
    $ phone_text = "“你们什么时候回来？”"
    n "“你们什么时候回来？”"
    $ phone_mode = False
    $ c1_before("CH01-D07", 8, "")
    n "屏幕缓缓暗下去。"
    $ c1_before("CH01-D07", 9, "")
    n "没有人回复。"
    $ c1_before("CH01-D07", 10, "")
    n "……"
    $ c1_before("CH01-D07", 11, "")
    n "你以为自己只是暂时没有离开。"
    $ chapter_route = "D"
    call route_end("D")
    return

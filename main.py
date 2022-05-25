# encoding: UTF-8

import time # 实现程序暂停功能
import Hero # 导入 Hero 类对象

# 设置超参数
TIME_DELAY = 0.75    # 程序暂停时间，单位为 秒

# 欢迎界面
print("     ----------                   ---------       ----------     ----------              ")
print("      \      /  -----\   \        |        \       \      /       \      /  -----\   \   ")
print("       |    |   ------\   \       |    |\   \       |    |         |    |   ------\   \  ")
print("       |    |          \   \      |    | \   \      |    |         |    |          \   \ ")
print("       |    |           |   |     |    |  \   \     |    |         |    |           |   |")
print("       |    |           |   |     |    |   \   \    |    |         |    |           |   |")
print("       |    |           |   |     |    |    \   \   |    |         |    |           |   |")
print("       |    |           |   |     |    |     \   \  |    |         |    |           |   |")
print("       |    |          /   /      |    |      \   \ |    |         |    |          /   / ")
print("       |    |   ------/   /       |    |       \   \|    |         |    |   ------/   /  ")
print("      /      \  -----/   /       /      \       \   \     \       /      \  -----/  /    ")
print("     ----------                 ----------       ----------      ----------              ")
print("                                                                                         ")
print("                                                                                         ")
print("                           ------------------------------------                          ")
print("                          |       欢迎来到游戏《来自另一端》     |                         ")
print("                          |              1.进入游戏             |                         ")
print("                          |              2.退出游戏             |                         ")
print("                           ------------------------------------                          ")

# 选择是否进入游戏
while True:
    choice = input("您的选择是：\n")
    if choice is "1":
        print("------------------")
        print("欢迎来到游戏！")
        break
    elif choice is "2":
        print("------------------")
        print("您已退出游戏！")
        break
    else:
        print("------------------")
        print("请选择正确选项！")

# 背景介绍
game_flag = True
while game_flag:
    print("-------背景-------"),time.sleep(TIME_DELAY)
    print("五百年前，矮人氏族和侏儒氏族签订了著名的凡戴尔协定，这纸合约让他们共同"),time.sleep(TIME_DELAY)   
    print("分享在回浪洞穴下的富矿资源，同时该矿藏也因富含强大的魔法力量而知名。一"),time.sleep(TIME_DELAY)
    print("些和矮人以及侏儒结盟的人类施法者们将这股魔法力量链接转化成为一个强大的"),time.sleep(TIME_DELAY)
    print("魔法物品工厂，在这里，魔法物品能够轻易地制造出来。在矿坑的黄金时代，附"),time.sleep(TIME_DELAY)
    print("近的人类城镇凡度林也因此而发展壮大。但在兽人横扫整个费伦大路北面和剑湾"),time.sleep(TIME_DELAY)
    print("的时候，这座矿坑并未幸免于难。"),time.sleep(TIME_DELAY)
    print("                                                                 "),time.sleep(TIME_DELAY)
    print("一个强大而唯利是图的兽人法师企图攻占回浪洞穴的矿坑来占据那里大量魔法财"),time.sleep(TIME_DELAY)
    print("宝，而人类法师和他们的矮人、侏儒盟友为了守卫魔法物品工厂而与兽人展开了"),time.sleep(TIME_DELAY)
    print("血腥厮杀。这场战斗摧毁了大部分的矿坑，只有很少的人活着逃了出来，从此回"),time.sleep(TIME_DELAY)
    print("浪洞穴的位置就失落了。"),time.sleep(TIME_DELAY)
    print("                                                                 "),time.sleep(TIME_DELAY)
    print("几百年来，被埋藏的珍宝吸引着宝藏猎人们来到凡度林，但没有人能成功地找到"),time.sleep(TIME_DELAY)
    print("失落的矿脉。在最近，人类重新在这个地方定居，凡度林再次兴盛。更重要的是，"),time.sleep(TIME_DELAY)
    print("寻石者兄弟——三个矮人——已经找到了通往回浪洞穴的入口，他们准备重新开启这"),time.sleep(TIME_DELAY)
    print("个矿坑。"),time.sleep(TIME_DELAY)
    print("                                                                 "),time.sleep(TIME_DELAY)
    print("不幸的是，寻石者兄弟并不是唯一一个对矿坑有兴趣的人，一个神秘的人物，称"),time.sleep(TIME_DELAY)
    print("为黑蜘蛛，控制着当地的强盗帮派和哥布林部落，同时也派出了间谍跟踪寻石者"),time.sleep(TIME_DELAY)
    print("兄弟企图找到矿脉。现在黑蜘蛛网图独吞这个洞穴，同时在采取行动对付其他对"),time.sleep(TIME_DELAY)
    print("洞穴有着企图的对手。"),time.sleep(TIME_DELAY)
    print("                                                                 "),time.sleep(TIME_DELAY)
    print("......"),time.sleep(TIME_DELAY)
    break
# encoding: UTF-8

import random   # 导入随机数模块

class Hero:
    """创建一个英雄，并初始化其属性。"""
    def __init__(self, name, gender):
        """
        param:  name —— 名字
                gender —— 性别
        function: 初始化类对象 Hero
        """
        self.name = name    # 姓名
        self.gender = gender    # 性别
        self.HP = 10 + random.randint(1,6)  # 生命值
        self.AC = 10 + random.randint(1,3)  # 护甲值
        self.STR = 10 + random.randint(1,3) # 力量
        self.DEX = 10 + random.randint(1,3) # 敏捷
        self.CON = 10 + random.randint(1,3) # 体质
        self.INT = 10 + random.randint(1,3) # 智力
        self.WIS = 10 + random.randint(1,3) # 感知
        self.CHA = 10 + random.randint(1,3) # 魅力
        self.exp = 0    # 经验值
        self.level = 1  # 级别

    def __str__(self):
        return "姓名: %s\n性别: %s\n生命: %d\n护甲: %d\n力量: %d\n敏捷: %d\n体质: %d\n智力: %d\n感知: %d\n魅力: %d\n经验值:  %d\n级别: Lv.%d" % (self.name, self.gender, self.HP, self.AC, self.STR, self.DEX, self.CON, self.INT, self.WIS, self.CHA, self.exp, self.level)

    def savetxt(self):
        f = open("player.txt",'r+',encoding='utf-8')
        f.write("姓名: %s\n性别: %s\n生命: %d\n护甲: %d\n力量: %d\n敏捷: %d\n体质: %d\n智力: %d\n感知: %d\n魅力: %d\n经验值:  %d\n级别: Lv.%d" % (self.name, self.gender, self.HP, self.AC, self.STR, self.DEX, self.CON, self.INT, self.WIS, self.CHA, self.exp, self.level))
        f.close()


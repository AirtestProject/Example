# -*- encoding=utf8 -*-
__author__ = "zhangqi2011"

from airtest.core.api import *

auto_setup(__file__)

# 初始化Poco，重要！
from poco.drivers.unity3d import UnityPoco
poco = UnityPoco()

money = int(poco("Money").child('Text').get_text())

cost = int(poco("2024").child("Upgrade").child("NonFullPanel").child("Cost").child("Number").get_text())

# 点击待测道具的升级按钮
poco("2024").child("Upgrade").child("NonFullPanel").child("UpgradeBtn").click()

current_money = int(poco("Money").child('Text').get_text())

assert_equal(money-cost, current_money, "成功扣除对应金币")
poco(text="600")

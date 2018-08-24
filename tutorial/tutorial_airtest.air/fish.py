# -*- encoding=utf8 -*-
__author__ = "airtest"

from airtest.core.api import *

auto_setup(__file__)

start_app("com.netease.dyll")  # 传入包名，打开这个待测app

sleep(10)

wait(Template(r"tpl1530603956757.png", record_pos=(0.001, -0.023), resolution=(1920, 1080)))  # 等待，直到游戏画面出现


touch(Template(r"tpl1530588210942.png", record_pos=(-0.177, 0.167), resolution=(1920, 1080)))

sleep(1)  # 等待1秒，确保切换到了下一个场景画面

# 把关卡选择画面滑动到最右边，直到看到鲨鱼图案才停下
while not exists(Template(r"tpl1530603698872.png", record_pos=(0.374, -0.001), resolution=(1920, 1080))):
    swipe((959, 609), vector=[-0.1706, 0.0025])

touch(Template(r"tpl1530603939766.png", record_pos=(0.365, 0.102), resolution=(1920, 1080)))

assert_exists(Template(r"tpl1530604090919.png", record_pos=(-0.385, -0.173), resolution=(1920, 1080)), "断言是否进入了第20关")

snapshot(msg="当前画面截图.")

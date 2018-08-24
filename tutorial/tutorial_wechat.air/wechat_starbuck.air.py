# -*- encoding=utf8 -*-
__author__ = "suyuchen"

from airtest.core.api import *

from poco.drivers.ios import iosPoco
auto_setup(__file__)
#connect_device("ios:///http://10.254.51.239:8100")
poco = iosPoco()
poco("微信").click()

touch(Template(r"tpl1528888459176.png", record_pos=(-0.372, -0.544), resolution=(750, 1334)))
sleep(1)
snapshot()
while not poco("有你真好").exists():
    poco.scroll(direction='vertical', percent=0.3, duration=1.0)

sleep(1)
poco("有你真好").click()
sleep(1)
poco("当季特饮").click()
touch(Template(r"tpl1528888543521.png", record_pos=(-0.424, -0.221), resolution=(750, 1334)))
touch(Template(r"tpl1528888551098.png", record_pos=(0.395, 0.237), resolution=(750, 1334)))
poco("\r 购买\r").click()







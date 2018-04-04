# -*- encoding=utf8 -*-
__author__ = "gzliuxin"
__title__ = "test script title"
__desc__ = """
this is a test script.
"""

# install demo apk
PKG = "com.NetEase.PocoDemo"
if PKG not in device().list_app():
    import os
    path = os.path.join(args.script, "poco-demo.apk")
    device().install_app(path)

# restart app
stop_app(PKG)
start_app(PKG)
wait(Template(r"tpl1522812811402.png", record_pos=(0.001, -0.084), resolution=(1920, 1080)))

# init UnityPoco
from poco.drivers.unity3d import UnityPoco
poco = UnityPoco()

poco(text="Start").click()
poco(text="basic").click()

# assert empty
result = poco(type="Text", name="Text").get_text()
assert_equal(bool(result), False)

# input text
poco(type="InputField").set_text("Hello World")
sleep(1.0)

# assert text 
result = poco(type="Text", name="Text").get_text()
assert_equal(result, "Hello World")

poco(text="Back").click()




# -*- encoding=utf8 -*-
__author__ = "gzliuxin"
__title__ = "test script title"
__desc__ = """this is a test script."""

# start your script here

from poco.drivers.android.uiautomation import AndroidUiautomationPoco

PKG = "com.google.android.calculator"
if PKG not in device().list_app():
    import os
    path = os.path.join(args.script, "com.google.android.calculator.apk")
    device().install_app(path)
                
stop_app(PKG)
start_app(PKG)

poco = AndroidUiautomationPoco()

# test (1+2)==3
poco("com.google.android.calculator:id/digit_1").click()
poco("com.google.android.calculator:id/op_add").click()
poco("com.google.android.calculator:id/digit_2").click()
poco("com.google.android.calculator:id/eq").click()
result = poco("com.google.android.calculator:id/result").get_text()
assert_equal(result, "3")

## test swipe
poco("com.google.android.calculator:id/arrow").click()
sleep(1.0)
fun_log = poco("com.google.android.calculator:id/fun_log").exists()
assert_equal(fun_log, True)
poco("com.google.android.calculator:id/arrow").swipe([0.6884, 0.01])
sleep(1.0)

## touch all numbers for fun
poco("com.google.android.calculator:id/clr").click()
for btn in poco(nameMatches="com.google.android.calculator:id/digit_\d"):
    print(btn)
    btn.click()

result2 = poco("com.google.android.calculator:id/formula").get_text()
assert_equal(result2, "7894561230")

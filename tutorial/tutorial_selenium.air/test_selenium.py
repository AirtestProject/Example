# -*- encoding=utf8 -*-
from airtest.core.api import *

__author__ = "zxfn4514"

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from airtest_selenium.proxy import WebChrome
driver = WebChrome()
driver.implicitly_wait(20)

driver.get("https://github.com/AirtestProject")
driver.find_element_by_xpath("//*[@id=\"js-pjax-container\"]/div/header/div/nav/a[2]").click()
driver.find_element_by_xpath("//a[@data-hotkey='g b']").click()
driver.airtest_touch(Template(r"tpl1534930299434.png", record_pos=(12.015, 2.275), resolution=(100, 100)))
driver.assert_template(Template(r"tpl1534930307633.png", record_pos=(8.61, 2.925), resolution=(100, 100)), "Please fill in the test point.")


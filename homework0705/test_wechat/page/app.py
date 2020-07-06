
"""
主要用于 app的一些常用操作：启动app，关闭app，重启app，进入主页
"""
from appium import webdriver

from page.base import BasePage
from test_wechat.page.main import MainPage


class App(BasePage):

    def start(self):
        if self._driver == None:
            print(self._driver)
            caps = {}
            caps["deviceName"] = "127.0.0.1:7555"
            caps["platformName"] = "Android"
            caps["appPackage"] = "com.tencent.wework"
            caps["appActivity"] = ".launch.WwMainActivity"
            caps["noReset"] = True
            self._driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
        else:
            print(self._driver)
            self._driver.launch_app()
        self._driver.implicitly_wait(10)
        return self

    def restart(self):
        pass

    def close(self):
        self._driver.quit()

    def main(self):
        return MainPage(self._driver)
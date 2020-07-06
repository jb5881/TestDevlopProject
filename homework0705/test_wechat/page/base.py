import yaml
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait

"""
存放基本的操作
1、实例化driver对象
2、find方法
3、appium底层操作
"""


class BasePage:
    _driver: WebDriver

    def __init__(self, driver: WebDriver = None):
        self._driver = driver

    def find(self, locator):
        return self._driver.find_element(*locator)

    def find_by_scroll(self, text):
        return self._driver.find_element_by_android_uiautomator(f'new UiScrollable(new UiSelector().scrollable(true)\
                                                         .instance(0)).scrollIntoView(new UiSelector()\
                                                         .text("{text}").instance(0));')

    def find_and_click(self, locator):
        self.find(locator).click()

    def get_toast(self, locator):
        return self.find(locator).text

    def back(self, num=1):
        for i in range(num):
            self._driver.back()

    def show_wait_until_not(self, text):
        res = WebDriverWait(self._driver, 15).until_not(lambda x: x.find_element_by_android_uiautomator(
            f'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("{text}").instance(0));'))
        return res

    def show_wait_until(self, text):
        res = WebDriverWait(self._driver, 15).until(lambda x: x.find_element_by_android_uiautomator(f'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("{text}").instance(0));'))
        return res

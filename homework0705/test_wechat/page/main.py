from appium.webdriver.common.mobileby import MobileBy

from page.address_list import AddressList
from page.base import BasePage


class MainPage(BasePage):
    _address_list = (MobileBy.XPATH, "//android.widget.TextView[@text='通讯录']")
    # 进入到通讯录

    def goto_address_list(self):
        self.find_and_click(self._address_list)
        return AddressList(self._driver)

    def goto_message(self):
        pass

    def goto_workbench(self):
        pass
from appium.webdriver.common.mobileby import MobileBy


from page.base import BasePage


class DeleteMember(BasePage):
    _confirm = (MobileBy.XPATH, "//*[@text='确定']")
    _cancel = (MobileBy.XPATH, "//*[@text='取消']")

    def click_confirm(self):
        self.find_and_click(self._confirm)
        from page.address_list import AddressList
        return AddressList(self._driver)

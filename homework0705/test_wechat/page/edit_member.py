from appium.webdriver.common.mobileby import MobileBy

from page.base import BasePage
from page.delete_member import DeleteMember


class EditMember(BasePage):
    _del_member = (MobileBy.XPATH, "//*[@text='删除成员']")

    def click_del_memeber(self):
        self.find_and_click(self._del_member)
        return DeleteMember(self._driver)
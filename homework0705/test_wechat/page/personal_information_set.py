from appium.webdriver.common.mobileby import MobileBy

from page.base import BasePage
from page.edit_member import EditMember


class PersonalInformationSet(BasePage):
    _edit_member = (MobileBy.XPATH, "//*[@text='编辑成员']")

    def click_edit_member(self):
        self.find_and_click(self._edit_member)
        return EditMember(self._driver)


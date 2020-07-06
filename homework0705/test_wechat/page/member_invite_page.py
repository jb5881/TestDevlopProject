# from page.contact_add_page import ContactAddPage
from appium.webdriver.common.mobileby import MobileBy

from page.base import BasePage


class MemberInvitePage(BasePage):
    _add_member_manual = (MobileBy.XPATH, "//*[@text='手动输入添加']")
    _toast = (MobileBy.XPATH, "//*[@class='android.widget.Toast']")

    def add_memeber_manual(self):
        from page.contact_add_page import ContactAddPage
        self.find_and_click(self._add_member_manual)
        return ContactAddPage(self._driver)

    def get_result(self):
        return self.get_toast(self._toast)
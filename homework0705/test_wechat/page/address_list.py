from page.base import BasePage
from page.member_invite_page import MemberInvitePage
from page.personal_information import PersonalInformation


class AddressList(BasePage):
    _add_memeber_text = "添加成员"
    # 点击添加成员

    def click_add_memeber(self):
        self.find_by_scroll(self._add_memeber_text).click()
        return MemberInvitePage(self._driver)

    def cilck_memeber_name(self, name):
        self.find_by_scroll(name).click()
        return PersonalInformation(self._driver)
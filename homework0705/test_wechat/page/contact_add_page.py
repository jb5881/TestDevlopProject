from appium.webdriver.common.mobileby import MobileBy

from page.base import BasePage
from page.member_invite_page import MemberInvitePage


class ContactAddPage(BasePage):
    _name_element = (MobileBy.XPATH, "//*[contains(@text,'姓名')]/following-sibling::*[1]")
    _gender_element = (MobileBy.XPATH, "//*[contains(@text,'性别')]//following-sibling::*[1]//*[@text='男']")
    _female_element = (MobileBy.XPATH, "//*[contains(@text,'女')]")
    _male_element = (MobileBy.XPATH, "//*[contains(@text,'男')]")
    _phone_element = (MobileBy.XPATH, "//*[contains(@text,'手机')]/following-sibling::*[1]//*[@text='手机号']")
    _save_element = (MobileBy.XPATH, "//*[@text='保存']")

    # 编辑用户名

    def edit_name(self, name):
        self.find(self._name_element).send_keys(name)
        return self

    def edit_gender(self, gender):
        self.find_and_click(self._gender_element)
        if gender == "女":
            self.find_and_click(self._female_element)
        else:
            self.find_and_click(self._male_element)
        return self

    def edit_phone_num(self, phone_num):
        self.find(self._phone_element).send_keys(phone_num)
        return self

    def click_save(self):
        self.find_and_click(self._save_element)
        return MemberInvitePage(self._driver)
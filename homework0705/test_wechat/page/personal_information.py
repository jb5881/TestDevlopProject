from appium.webdriver.common.mobileby import MobileBy

from page.base import BasePage
from page.personal_information_set import PersonalInformationSet


class PersonalInformation(BasePage):
    _set_element = (MobileBy.XPATH, "//*[@text='个人信息']/../../../../following-sibling:: *[1]")

    def click_set(self):
        self.find_and_click(self._set_element)
        return PersonalInformationSet(self._driver)
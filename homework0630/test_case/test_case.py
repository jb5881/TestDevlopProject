from time import sleep

import pytest
import yaml
from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

with open('../datas/data.yml', encoding="utf-8") as f:
    file = yaml.safe_load(f)
    add_contacts = file['add_contacts']
    del_contacts = file['del_contacts']


class TestCase:

    def setup_class(self):
        caps = {}
        caps["deviceName"] = "127.0.0.1:7555"
        caps["platformName"] = "Android"
        caps["appPackage"] = "com.tencent.wework"
        caps["appActivity"] = ".launch.WwMainActivity"
        caps["noReset"] = True
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)

    def setup(self):
        self.driver.implicitly_wait(5)

    @pytest.mark.parametrize('data', add_contacts)
    def test_add_contacts(self, data):
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='通讯录']").click()
        self.driver.find_element_by_android_uiautomator('new UiScrollable(new UiSelector().'
                                                        'scrollable(true).instance(0)).'
                                                        'scrollIntoView(new UiSelector().text("添加成员").'
                                                        'instance(0));').click()

        self.driver.find_element_by_xpath("//*[@text='手动输入添加']").click()
        self.driver.find_element_by_xpath("//*[contains(@text,'姓名')]/following-sibling::*[1]").send_keys(data['name'])
        self.driver.find_element_by_xpath("//*[contains(@text,'性别')]//following-sibling::*[1]//*[@text='男']").click()
        if data['gender'] == "女":
            self.driver.find_element_by_xpath("//*[contains(@text,'女')]").click()
        else:
            self.driver.find_element_by_xpath("//*[contains(@text,'男')]").click()
        self.driver.find_element_by_xpath(
            "//*[contains(@text,'手机')]/following-sibling::*[1]//*[@text='手机号']").send_keys(data['phone_num'])
        self.driver.find_element_by_xpath("//*[@text='保存']").click()
        toast_text = self.driver.find_element_by_xpath("//*[@class='android.widget.Toast']").text
        assert "添加成功" == toast_text
        self.driver.back()

    @pytest.mark.parametrize('data', del_contacts)
    def test_del_contacts(self, data):
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='通讯录']").click()
        self.driver.find_element_by_android_uiautomator(f'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text(\"{data["name"]}\").instance(0));').click()
        self.driver.find_element_by_xpath("//*[@text='个人信息']/../../../../following-sibling:: *[1]").click()
        self.driver.find_element_by_xpath("//*[@text='编辑成员']").click()
        self.driver.find_element_by_xpath("//*[@text='删除成员']").click()
        self.driver.find_element_by_xpath("//*[@text='确定']").click()
        WebDriverWait(self.driver, 15).until_not(lambda x:x.find_element_by_android_uiautomator(f'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text(\"{data["name"]}\").instance(0));'))







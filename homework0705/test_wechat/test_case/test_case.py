import pytest
import yaml
from appium import webdriver

from page.app import App

with open('../datas/data.yml', encoding="utf-8") as f:
    file = yaml.safe_load(f)
    add_contacts = file['add_contacts']
    del_contacts = file['del_contacts']


class TestCase:

    def setup_class(self):
        self.app = App()
        self.main = self.app.start().main()

    @pytest.mark.parametrize('data', add_contacts)
    def test_add_memeber(self, data):
        toast = self.main.goto_address_list().click_add_memeber().add_memeber_manual()\
            .edit_name(data['name']).edit_gender(data['gender']).edit_phone_num(data['phone_num']).click_save().get_result()
        assert '添加成功' == toast
        self.main.back()

    @pytest.mark.parametrize('data', del_contacts)
    def test_del_contact(self, data):
        assert self.main.goto_address_list().cilck_memeber_name(
            data['name']).click_set().click_edit_member().click_del_memeber().click_confirm().show_wait_until_not(data['name'])




from page.add_memeber_page import AddMemeber
from page.base_page import BasePage
from page.contact_page import ContactPage
from page.import_contact_page import ImportContact


class MainPage(BasePage):
    _base_url = 'https://work.weixin.qq.com/wework_admin/frame#index'

    def goto_add_member(self, name: list):
        """
        跳转到添加成员页面
        :param name: 每个元素的别名，便于识别
        :return:
        """
        self.steps('../page/main.yml', name)
        return AddMemeber()

    def goto_import_contact(self, name: list):
        """
        跳转到导入联系人页面
        :param name: 每个元素的别名，便于识别
        :return:
        """
        self.steps('../page/main.yml', name)
        return ImportContact()

    def goto_contacts(self, name: list):
        """
        跳转到联系人页面
        :param name: 每个元素的别名，便于识别
        :return:
        """
        self.steps('../page/common.yml', name)
        return ContactPage()

    # def goto_member_join(self):
    #     self.steps('../page/main.yml', ['成员加入'])
    #     return MemeberJoin()
    #
    # def goto_mass_news(self):
    #     self.steps('../page/main.yml', ['消息群发'])
    #     return MassNews()
    #
    # def goto_customer_contact(self):
    #     self.steps('../page/main.yml', ['客户联系'])
    #     return CustomerContact()
    #
    # def goto_clock_in(self):
    #     self.steps('../page/main.yml', ['打卡'])
    #     return ClockIn()
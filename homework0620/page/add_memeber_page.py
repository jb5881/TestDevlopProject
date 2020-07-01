from page.base_page import BasePage
from page.contact_page import ContactPage


class AddMemeber(BasePage):
    def add_memeber(self, name: list, *args):
        """
        获取所有成员的姓名
        :param name: 每个元素的别名，便于识别
        :param args: 需要替换yml文件中值
        :return:
        """
        self._params['value'] = args
        self.steps('../page/add_member.yml', name)
        return ContactPage()
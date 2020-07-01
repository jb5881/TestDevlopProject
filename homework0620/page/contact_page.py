from page.base_page import BasePage


class ContactPage(BasePage):
    def get_member(self, name: list, *args):
        """
        获取所有成员的姓名
        :param name: 每个元素的别名，便于识别
        :param args: 需要替换yml文件中值
        :return:
        """
        self._params['value'] = args
        elements = self.steps('../page/contact.yml', name)
        return elements

    def delete_member(self, name: list, *args):
        """
        获取所有成员的姓名
        :param name: 每个元素的别名，便于识别
        :param args: 需要替换yml文件中值
        :return:
        """
        self._params['value'] = args
        self.steps('../page/contact.yml', name)
        return ContactPage()


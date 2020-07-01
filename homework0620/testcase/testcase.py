from page.main_page import MainPage
from random import choice

from utils.get_path.get_path import GetPath
from utils.random_util import RandomUtil


class TestCase:
    def setup(self):
        self.main = MainPage()
        ran_util = RandomUtil()
        self.str_name = ran_util.get_random_str_num(4, 2)
        self.acct_num = ran_util.get_random_num(9)
        self.mail = ran_util.get_random_num(9)
        self.path = GetPath().get_path('../test.xls')

    def test_add_member(self):
        assert self.str_name in self.main.goto_add_member(['添加成员']).add_memeber(['姓名', '帐号', '邮箱', '保存'], [self.str_name, self.acct_num, f'{self.mail}@qq.com']).get_member(['姓名'], ['title'])

    def test_upload_file(self):
        assert 'test.xls' == self.main.goto_import_contact(['导入通讯录']).upload_file(['上传文件', '获取文件名'], [self.path])

    def test_delete_member(self):
        before_names = self.main.goto_contacts(['通讯录']).get_member(['姓名'], ['title'])
        before_names.pop()  # 去除微信的本人，避免删除失败
        after_names = self.main.goto_contacts(['通讯录']).delete_member(['勾选框', '删除', '删除确认'], [choice(before_names)]).get_member(['姓名'],
                                                                                                              ['title'])
        assert 0 == len([i for i in [after_names] if i in before_names])


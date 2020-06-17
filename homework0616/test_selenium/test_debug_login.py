from selenium import webdriver
from selenium.webdriver.chrome import options
from selenium.webdriver.common.by import By


class TestLogin:
    def test_login(self):
        # 实例化
        option = options.Options()
        # 设置远程连接地址
        option.debugger_address = '127.0.0.1:9222'
        # 启动谷歌浏览器
        driver = webdriver.Chrome(options=option)
        # 访问登录的URL
        driver.get('https://work.weixin.qq.com/wework_admin/loginpage_wx')
        text_name = driver.find_element(By.CSS_SELECTOR, '#menu_index .frame_nav_item_title').text
        print(text_name)
        assert "首页" == text_name
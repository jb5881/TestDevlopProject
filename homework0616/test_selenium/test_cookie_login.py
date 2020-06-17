import json
import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestLogin:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('https://work.weixin.qq.com/wework_admin/loginpage_wx')

    def teardown(self):
        self.driver.quit()

    def test_save_cookies(self):
        time.sleep(15)
        cookies = self.driver.get_cookies()
        # 将拿到的cookie, dict类型的数据格式转换成str类型，并写入文件
        with open('cookie.json', 'w') as f:
            json.dump(cookies, f)
        # print(f"cookies: {cookies}")
        # print(os.path.getsize('cookie.json'))
        assert True == os.path.exists('cookie.json') and os.path.getsize('cookie.json') > 0

    def test_cookie_login(self):
        cookies = json.load(open('cookie.json'))
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        while True:
            self.driver.refresh()
            ret = WebDriverWait(self.driver, 10).until(
                expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, '#menu_index')))
            if ret is not None:
                break
        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, 'a[node-type="import"]')))
        self.driver.find_element(By.CSS_SELECTOR, 'a[node-type="import"]').click()
        WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "input[value='上传文件']")))
        self.driver.find_element(By.CSS_SELECTOR, "input[value='上传文件']").send_keys(
            'D:\\PythonSET\\homework0616\\test_selenium\\datas\\test.xlsx')
        WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located((By.CSS_SELECTOR, '#upload_file_name')))
        file_name = self.driver.find_element(By.CSS_SELECTOR, '#upload_file_name').text
        assert "test.xlsx" == file_name

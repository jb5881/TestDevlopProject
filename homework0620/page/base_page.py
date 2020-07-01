import yaml
from selenium import webdriver
from selenium.webdriver.chrome import options
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By


class BasePage:
    # 指定访问的URL
    _base_url = ""
    # 针对页面的一些弹窗处理，如更新之类
    _black_list = [(By.ID, 'image_cancel')]
    # 定位错误的次数
    _error_count = 0
    # 定位错误的最大次数
    _error_max = 10
    # 用于浏览器操作时，需要输入值，或者需要根据输入的值来改变yml中的某些参数
    _params = {}

    def __init__(self, driver_basepage: WebDriver = None):
        if driver_basepage == None:
            # 声明并实例化一个 配置chrome启动时属性的类
            option = options.Options()
            # 设置ChromeDriver实例连接到的远程的地址
            option.debugger_address = "127.0.0.1:9222"
            # 以远程连接启动的方式启动已有的Chrome浏览器
            self._driver = webdriver.Chrome(options=option)
            # 隐式等待
            self._driver.implicitly_wait(5)
        else:
            # 如果driver_basepage不是None，就不用重新再初始化
            self._driver = driver_basepage
        # 判断如果_base_url有传入值，就进行访问，避免写死
        if self._base_url != "":
            # 驱动浏览器访问URL
            self._driver.get(self._base_url)

    def find(self, by, locator=None):
        """
        用于元素定位
        :param by: 是以什么样的属性进行定位，如
                    ID = "id"
                    XPATH = "xpath"
                    LINK_TEXT = "link text"
                    PARTIAL_LINK_TEXT = "partial link text"
                    NAME = "name"
                    TAG_NAME = "tag name"
                    CLASS_NAME = "class name"
                    CSS_SELECTOR = "css selector"
        :param locator: 元素的定位写法
        :return:
        """
        try:
            element = self._driver.find_elements(*by) if isinstance(by, tuple) else self._driver.find_element(by, locator)
            self._error_count = 0
            return element
        except Exception as e:
            self._error_count += 1
            if self._error_count > self._error_max:
                raise e
            for black in self._black_list:
                elements = self._driver.find_elements(*black)
                if len(elements) > 0:
                    elements[0].click()
                    return self.find(by, locator)
            raise e

    def send(self, value, by, locator=None):
        """
        用于向文本框输入值的操作
        :param value: 输入的值
        :param by: 是以什么样的属性进行定位
        :param locator: 元素的定位写法
        :return:
        """
        try:
            self.find(by, locator).send_keys(value)
        except Exception as e:
            self._error_count += 1
            if self._error_count > self._error_max:
                raise e
            for black in self._black_list:
                elements = self._driver.find_elements(*black)
                if len(elements) > 0:
                    elements[0].click()
                    return self.send(value, by, locator)
            raise e

    def steps(self, path, name: list):
        """
        对元素进行的具体操作，如点击，输入，获取属性
        :param path: 要读的有yml文件
        :param name: 每个元素的别名，便于识别
        :return:
        """
        with open(path, encoding="utf-8") as f:
            steps: list = yaml.safe_load(f)
            for i in range(len(name)):
                for step in steps:
                    if "action" in step[name[i]][0].keys():
                        if "click" == step[name[i]][0]['action']:
                            if 'value' in step[name[i]][0]:
                                for param in self._params["value"][0]:
                                    content: str = step[name[i]][0]["locator"]
                                    locator = content.split('name')[0] + param + content.split('name')[1]
                                    self.find(step[name[i]][0]["by"], locator).click()
                            else:
                                element = self.find(step[name[i]][0]["by"], step[name[i]][0]["locator"])
                                element.click()
                        if "send" == step[name[i]][0]['action']:
                            param = self._params["value"][0][i]
                            self.send(param, step[name[i]][0]["by"], step[name[i]][0]["locator"])
                        if "attribute" in step[name[i]][0]['action']:
                            elements = self.find((step[name[i]][0]["by"], step[name[i]][0]["locator"]))
                            param = self._params["value"][0]
                            return [ele.get_attribute(par) for ele in elements for par in param]
                        if "text" in step[name[i]][0]['action']:
                            element = self.find(step[name[i]][0]["by"], step[name[i]][0]["locator"])
                            return element.text

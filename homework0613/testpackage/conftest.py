

import pytest
import yaml


from calc.calc import Calculator

'''
    1.计算器实例化
    2.读取yml数据
'''


@pytest.fixture(scope='class', autouse=True)
def pre_class():
    cal = Calculator()
    yield cal


@pytest.fixture(scope='function', autouse=True)
def pre_method():
    print("\n********************开始计算***********************")
    yield
    print("\n********************计算结束***********************")


def pytest_generate_tests(metafunc):
    """
        根据测试配置或定义测试函数的类或模块中指定的值生成测试用例, 在测试用例参数化收集前调用此钩子函数
        :param metafunc:共有五个属性值
                         metafunc.fixturenames:参数化收集时的参数名称
                         metafunc.module:使用参数名称进行参数化的测试用例所在的模块d对象
                         metafunc.config:测试用例会话
                         metafunc.function:测试用例对象,即函数或方法对象
                         metafunc.cls: 测试用例所属的类的类对象
        :return: none
    """
    # print(f"metafunc.fixturenames: {metafunc.fixturenames}")
    # print(f"metafunc.module: {metafunc.module}")
    # print(f"metafunc.config: {metafunc.config}")
    # print(f"metafunc.function: {metafunc.function}")
    # print(f"metafunc.cls: {metafunc.cls}")
    if "param" in metafunc.fixturenames:
        with open('../datas/data.yml') as f:
            data = yaml.safe_load(f)
        # print(data)
        # print(metafunc.function.__qualname__)
        for i in ['add', 'sub', 'mul', 'div']:
            if i in (metafunc.function.__qualname__):
                data = data[i]
                metafunc.parametrize("param", data, scope='function')


def pytest_addoption(parser, pluginmanager):
    mygroup = parser.getgroup("testGroup")
    mygroup.addoption("--env",
                      default='test',
                      help='set your run env')
    mygroup.addoption("--env0",
                      default='test',
                      help='set your run env0')


@pytest.fixture(scope='session', autouse=True)
def cmdoption(request):
    myenv = request.config.getoption("--env", default='test')
    if myenv == 'test':
        with open ('../datas/test/test.yml') as f:
            datas = yaml.safe_load(f)
    elif myenv == 'dev':
        with open ('../datas/dev/dev.yml') as f:
            datas = yaml.safe_load(f)
    elif myenv == 'st':
        with open ('../datas/dev/dev.yml') as f:
            datas = yaml.safe_load(f)
    return datas



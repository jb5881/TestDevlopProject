

import pytest
import yaml


from calc.calc import Calculator

'''
    1.计算器实例化
    2.读取yml数据
'''


@pytest.fixture(scope='class', autouse=True, params=[0, 1, 2])
def pre_class(request):
    cal = Calculator()
    with open('data.yml') as f:
        data = yaml.safe_load(f)
    yield cal, data, request.param


@pytest.fixture(scope='function', autouse=True)
def pre_method():
    print("\n********************开始计算***********************")
    yield
    print("\n********************计算结束***********************")



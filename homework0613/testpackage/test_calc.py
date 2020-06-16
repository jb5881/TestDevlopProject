import pytest
import yaml


class TestCalc:

    @pytest.mark.dependency(name='add')
    @pytest.mark.run(order=1)
    def test_add(self, pre_class, pre_method, param, cmdoption):
        calc = pre_class
        print(f"\n环境信息：{cmdoption}")
        assert param['c'] == calc.add(param['a'], param['b'])

    @pytest.mark.dependency(depends=["add"])
    @pytest.mark.run(order=2)
    def check_sub(self, pre_class, pre_method, param, cmdoption):
        calc = pre_class
        print(f"\n环境信息：{cmdoption}")
        assert param['c'] == calc.sub(param['a'], param['b'])

    @pytest.mark.dependency(name='mul')
    @pytest.mark.run(order=3)
    def test_mul(self, pre_class, pre_method, param, cmdoption):
        calc = pre_class
        print(f"\n环境信息：{cmdoption}")
        assert param['c'] == calc.mul(param['a'], param['b'])

    @pytest.mark.dependency(depends=["mul"])
    @pytest.mark.run(order=4)
    def check_div(self, pre_class, pre_method, param, cmdoption):
        calc = pre_class
        print(f"\n环境信息：{cmdoption}")
        assert param['c'] == calc.div(param['a'], param['b'])

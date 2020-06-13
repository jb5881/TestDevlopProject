import pytest


class TestCalc:

    def test_add(self, pre_class, pre_method):
        calc, data, index = pre_class
        assert data['add'][index]['c'] == calc.add(data['add'][index]['a'], data['add'][index]['b'])

    def test_sub(self, pre_class, pre_method):
        calc, data, index = pre_class
        assert data['sub'][index]['c'] == calc.sub(data['sub'][index]['a'], data['sub'][index]['b'])

    def test_mul(self, pre_class, pre_method):
        calc, data, index = pre_class
        assert data['mul'][index]['c'] == calc.mul(data['mul'][index]['a'], data['mul'][index]['b'])

    def test_div(self, pre_class, pre_method):
        calc, data, index = pre_class
        assert data['div'][index]['c'] == calc.div(data['div'][index]['a'], data['div'][index]['b'])

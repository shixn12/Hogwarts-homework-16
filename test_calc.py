import pytest
from pythoncode.calculator import Calculator
# 1、补全计算器（加减乘除）的测试用例
# 2、使用参数完成测试用例的自动生成
# 3、在调用测试方法之前打印【开始计算】，在调用测试方法之后打印【计算结束】
class TestCalc:
    def setup_class(self):
        self.calc = Calculator()
        print("开始计算")
    def teardown_class(self):
        print("结束计算")

    @pytest.mark.parametrize("a,b,expect",[(5,9,14),(-1,-5,-6),(100,500,600),(1.22,2.335,3.555)],ids=["int","minus","bigint","deci"])
    def test_add(self,a,b,expect):
        assert self.calc.add(a,b) == expect

    @pytest.mark.parametrize("a,b,expect",[(10,2,8),(-1,-3,2),(1000,2,998),(8.216,5.1,3.116)])
    def test_sub(self,a,b,expect):
        assert self.calc.sub(a,b) == expect

    @pytest.mark.parametrize("a,b,expect",[(1,2,2),(-8,-9,72),(100,1000,100000),(1.555,2,3.11)])
    def test_mul(self,a,b,expect):
        assert self.calc.mul(a,b) == expect

    @pytest.mark.parametrize("a,b,expect",[(4,4,1),(-3,2,-1.5),(999,111,9),(4.50,2,2.25)])
    def test_div(self,a,b,expect):
        assert self.calc.div(a,b) == expect


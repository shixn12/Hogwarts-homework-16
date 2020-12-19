import pytest
import yaml
from pythoncode.calculator import Calculator
# 练习1
# 使用【测试数据的数据驱动】的方法完成加减乘除测试
# 使用fixture替换setup和teardown
# 将fixture方法放在conftest.py里面，设置scope=module
# 修改运行规则，pytest.ini文件
# 练习2(选做)
# 控制用例的执行顺序，如：加减乘除
# 结合allure生成测试结果报告



class TestCalc:
    def setup_class(self):
        self.calc = Calculator()

    def get_datas():
        with open("./work2.yml") as f:
            datas = yaml.safe_load(f)
            print(datas)
            add_datas = datas["add_datas"]
            add_ids = datas["add_ids"]
            sub_datas = datas["sub_datas"]
            mul_datas = datas["mul_datas"]
            div_datas = datas["div_datas"]
            return [add_datas,add_ids,sub_datas,mul_datas,div_datas]

    @pytest.mark.run(order=1)
    @pytest.mark.add
    @pytest.mark.parametrize("a,b,expect",get_datas()[0],ids = get_datas()[1])
    def test_add(self,a,b,expect,work2_fixture1):
        assert self.calc.add(a,b) == expect

    @pytest.mark.sub
    @pytest.mark.parametrize("a,b,expect",get_datas()[2])
    def test_sub(self,a,b,expect):
        assert self.calc.sub(a,b) == expect

    @pytest.mark.run(order=2)
    @pytest.mark.parametrize("a,b,expect",get_datas()[3])
    def test_mul(self,a,b,expect):
        assert self.calc.mul(a,b) == expect


    @pytest.mark.parametrize("a,b,expect",get_datas()[4])
    def test_div(self,a,b,expect):
        assert self.calc.div(a,b) == expect


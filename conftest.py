import pytest
# @pytest.fixture(autouse="true") #每个方法都执行
# @pytest.fixture(scope="class")
#
# def myfixture():
#     print("执行myfixture")

# fixture中使用作用域设置：@pytest.fixture(scope ="class")，默认是functionx 级别
# scope参数有四种选择：function（测试函数级别），class（测试类级别），module（测试模块“.py”级别），session（多个文件级别）。默认是function级别。
# @pytest.fixture(scope = "class")

# fixture函数可以参数化，在这种情况下，它们将被多次调用，每次执行一组相关测试，即依赖于这个fixture的测试
# fixture函数需要传入特殊的request对象
# 函数里面可通过request.param访问每个参数的值
# 也可加ids指定参数名字
# 固定写法，只需记住
from pythoncode.calculator import Calculator


@pytest.fixture(params=["参数1","参数2"])
def myfixture(request):
    print("执行我的fixture,里面的参数是%s"% request.param)
    # 可以返回参数
    return request.param
@pytest.fixture(params=["--参数1","--参数2"])
def connectdb(request):
    print("执行我的fixture-connectdb")
    # yield与return的区别：yield执行完后还会执行下一语名(根据设置的作用域确定何时执行，相当于teardown)，return不会
    yield request.param
    print("执行teardown,关闭数据库连接")


@pytest.fixture(scope = "module")
def work2_fixture1():
        print("开始计算")
        yield
        print("结束计算")


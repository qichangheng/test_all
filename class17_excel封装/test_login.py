"""测试登录功能（函数）"""
import unittest
import ddt

from class17_excel封装.excel_handler import ExcelHandler


def login(username=None, password=None):
    """登录"""
    if (not username) or (not password):
        # 用户名或者密码为空
        return {"msg": "empty"}

    if username == 'yuz' and password == '123456':
        # 正确的用户名和密码
        return {"msg": "success"}

    return {"msg": "error"}


# def login(username=None, password=None):
#     """登录"""
#     if username != None and password != None:
#         if username == 'yuz' and password == '123456':
#             return {"msg": "login success"}
#         else:
#             return {"msg": "username or password error"}
#     else:
#         return {"msg": "username or password is empty"}


cases = ExcelHandler('cases.xlsx').read_data('Sheet1')


@ddt.ddt
class TestLogin(unittest.TestCase):


    @classmethod
    def setUpClass(cls):
        print("一个测试类只执行一次的前置")

    @classmethod
    def tearDownClass(cls):
        print("一个测试类只执行一次的后置")

    # 固定的名称，不改
    def setUp(self):
        """前置"""
        print("链接数据库")

    def tearDown(self):
        """后置"""
        print("断开数据库")



    @ddt.data(*cases) # 装饰器
    def test_login(self, case_info):
        # case_info ===>  {"username": "yuz", "password": "123456", "expected": {"msg": "success"}},
        print(case_info)

        # 每个用例数据不是独立的，被当成一个用例在执行
        # 当前面的数据报错，后面的用例就不会执行了。
        # 数据驱动测试： ddt,  data driven testing
        # for case in cases:

        # 细节
        data = eval(case_info['data'])

        username = data["username"]
        password = data["password"]
        expected_response = case_info["expected"]

        actual_response = login(username, password) # {"msg": "error"}

        self.assertTrue(expected_response == actual_response["msg"])


    #
    # # 测试用例的方法
    # def test_login_01_success(self):
    #     """登录成功用例"""
    #     username = 'yuz'
    #     password = '123456'
    #     expected_response = {"msg": "login success"}
    #     # 调用被测试的单元，
    #     actual_response = login(username, password)
    #
    #     self.assertTrue( expected_response == actual_response )
    #
    #     # if expected_response == actual_response:
    #     #     print("测试用例")
    #     # else:
    #     #     print("测试用例")
    #
    # def test_login_02_error(self):
    #     username = ''
    #     password = ''
    #     expected_response = {"msg": "username or password error"}
    #     actual_response = login(username, password)
    #     self.assertTrue(expected_response == actual_response)


if __name__ == '__main__':
    # 使用 python 运行这个模块里面的测试用例
    unittest.main()

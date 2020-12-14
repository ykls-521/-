# 自动化执行excel用例
# 1- 先获取对应的用例数据
# from teach_sq.tools.excelMethod import get_excelData, set_excelData
from teach_sq.lib.apiLib.login import Login
import json, os
import pytest
import allure  # 导入库
from teach_sq.tools.getYamlData import get_yaml_data


# testData = get_excelData('1-登录接口',2,5)#列表[(bdoy,repsData),(),(),()]
# 测试类--登录模块
@allure.feature('登录模块')  # 一级标签
class TestLogin:
    # 数据驱动
    @allure.story('登录接口')  # 二级
    @allure.title('登录接口用例')  # 用例标签
    # @pytest.mark.parametrize('body,repsData',get_excelData('1-登录接口',2,5))
    @pytest.mark.parametrize('body,repsData', get_yaml_data())
    def test_login(self, body, repsData):
        '''登录接口---描述'''
        res = Login().login(json.loads(body), flag=True)  # 获取登录的响应数据
        print(res)
        if "message" not in json.loads(repsData):
            print("登陆成功")
        else:
            # print(type(json.loads(repsData)["message"]))
            # print(res['message'])
            assert res['message'] == json.loads(repsData)["message"]  # 断言
        # x = print("登陆成功") if "message" not in json.loads(repsData) else  assert res['message'] == json.loads(repsData)["message"]


if __name__ == '__main__':
    # 使用pytest框架，执行对应的模块，生成报告需要的数据文件  放到../report/tmp
    pytest.main(['test_login.py', '-s', '--alluredir', '../report/tmp'])

    # 方案一：直接生成报告
    # os.system('allure generate ../report/tmp -o  ../report/report --clean')
    # 方案二：直接启动一个服务，自动打开浏览器
    os.system('allure serve ../report/tmp')

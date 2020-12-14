#课程模块--测试类
import pytest
from teach_sq.lib.apiLib.login import Login
from teach_sq.lib.apiLib.lesson import Lesson
from teach_sq.tools.excelMethod import get_excelData
import json,allure
import os,time

#标签
@allure.feature('课程模块')#一级标签
@pytest.mark.lesson
@pytest.mark.usefixtures('lesson_delete_fixture_class')#类级别的
class TestLesson:
    loginData = Login().login(json.dumps({'username': '18715036677', 'password': '18715036677'}), True)['retcode']

    def setup_class(self):
        print('----类级别，只要调用这个测试类，我就第一个执行')
        self.session = Login().login(json.dumps({'username':'18715036677','password':'18715036677'}))

    # 1- 课程新增
    # @pytest.mark.skip("无条件跳过---我就跳过你")
    # @pytest.mark.skipif(loginData != 0,
    #                     reason='登录失败')
    # @pytest.mark.lesson_add
    @allure.story('课程新增接口')#二级
    @allure.title('课程新增用例')#用例标签
    @allure.description('这是一个课程新增的接口')#接口描述
    @pytest.mark.parametrize('body,repsData',get_excelData('2-课程模块',2,26))
    def test_lesson_add(self,body,repsData):
        res = Lesson(self.session).lesson_add(body)
        assert res['retcode']== json.loads(repsData)['retcode']

    # 2- 课程列出
    # @pytest.mark.skipif(1==1,
    #                     reason='需要前面完成某一个步骤---前面条件为真就跳过一下操作')
    # @pytest.mark.skipif(loginData != 0,
    #                     reason='登录失败')
    @allure.story('课程列出接口')#二级
    @allure.title('课程列出用例')#用例标签
    @pytest.mark.lesson_list
    @pytest.mark.usefixtures('lesson_add_fixture')#
    # @pytest.mark.usefixtures('xinian_test_fixture')#先近后远（从下到上）
    @pytest.mark.parametrize('body,repsData',get_excelData('2-课程模块',27,38))
    def test_lesson_list(self,body,repsData):
        res = Lesson(self.session).lesson_list(body)
        assert res['retcode']== json.loads(repsData)['retcode']

    # 3- 课程删除
    @allure.story('课程删除接口')#二级
    @allure.title('课程删除用例')#用例标签
    @pytest.mark.lesson_delete
    @pytest.mark.usefixtures('lesson_add_fixture')
    @pytest.mark.parametrize('body,repsData',get_excelData('2-课程模块',39,46))
    def test_lesson_delete(self,body,repsData):
        res = Lesson(self.session).lesson_delete(body)
        assert res['retcode']== json.loads(repsData)['retcode']
    # 4- 课程修改
    @allure.story('课程修改接口')#二级
    @allure.title('课程修改用例')#用例标签
    @pytest.mark.parametrize('body,repsData',get_excelData('2-课程模块',47,49))
    def test_lesson_modify(self,body,repsData):
        res = Lesson(self.session).lesson_modify(body)
        assert res['retcode']== json.loads(repsData)['retcode']
'''
一个：
    '-m','lesson_add'
多个：
    '-m','lesson_add or lesson_list'
排除法：
        '-m','not lesson_add '
排除法  多个：
        '-m','not (lesson_add or lesson_list)'
'''

if __name__ == '__main__':
    #使用pytest框架，执行对应的模块，生成报告需要的数据文件  放到../report/tmp
    pytest.main(['test_lesson.py','-s','--alluredir','../report/tmp'])
    # pytest.main(['test_lesson.py', '-s','-m','not (lesson_add or lesson_list) '])
    #方案一：直接生成报告
    #os.system('allure generate ../report/tmp -o  ../report/report --clean')
    #方案二：直接启动一个服务，自动打开浏览器
    os.system('allure serve ../report/tmp')

    #pytest.main(['test_lesson.py', '-s'])


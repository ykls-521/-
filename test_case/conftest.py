import pytest
import requests,json
from teach_sq.lib.apiLib.login import Login
from teach_sq.lib.apiLib.lesson import Lesson

#包级别的初始化操作
@pytest.fixture(scope='session',autouse=True)
def start_demo(request):
    print('我是整个包的初始化操作')
    def fin():
        print('---测试完成，包的数据清除---')

    request.addfinalizer(fin)


#类级别的初始化操作
@pytest.fixture(scope='class')
def lesson_delete_fixture_class():
    #1- 登录操作
    session = Login().login(json.dumps({'username': 'auto', 'password': 'sdfsdfsdf'}))
    #2- 列出课程
    testData2 = '''{"action": "list_course", "pagenum": 1, "pagesize": 20}'''
    lessonList = Lesson(session).lesson_list(testData2)['retlist']#[{},{}]

    #3- 删除所有的课程
    for lesson in lessonList:
        Lesson(session).lesson_delete(lesson['id'],idMode=True)
    # print('----lesson_delete_fixture_class-----')

#方法级别的初始化操作
@pytest.fixture()#scope='function'   默认
def lesson_add_fixture(request):
    #1- 登录操作
    session = Login().login(json.dumps({'username': 'auto', 'password': 'sdfsdfsdf'}))
    #2- 新增课程
    for one in range(0,5):
        lessonData = {"name":f"初中化学{one:0>3}","desc":"初中化学课程","display_idx":f"{one}"}
        Lesson(session).lesson_add(json.dumps(lessonData))#[{},{}]
    # print('----lesson_add_fixture-----')
    def fin():

        # 2- 列出课程
        testData2 = '''{"action": "list_course", "pagenum": 1, "pagesize": 20}'''
        lessonList = Lesson(session).lesson_list(testData2)['retlist']  # [{},{}]
        # 3- 删除所有的课程
        for lesson in lessonList:
            Lesson(session).lesson_delete(lesson['id'], idMode=True)
        # print('--用例执行完，删除该测试数据---')

    request.addfinalizer(fin)


@pytest.fixture()#scope='function'   默认
def xinian_test_fixture():
    print('********fixture_test********')

@echo off
echo ����-�̹�ϵͳ�ӿ��Զ�������׼����ʼ......
@echo on



del /f /s /q  G:\SongQin\Python\Demo\teach_sq\report\tmp\*.json
del /f /s /q  G:\SongQin\Python\Demo\teach_sq\report\tmp\*.jpg
del /f /s /q  G:\SongQin\Python\Demo\teach_sq\report\report



@echo off
echo �����ļ�ɾ��������ɣ���ʼ���нű�......
@echo on

G:
cd  G:/SongQin/Python/Demo/teach_sq/test_case
pytest  -sq --alluredir=../report/tmp

allure serve ../report/tmp


@echo off
echo �ӿ��Զ������гɹ�
pause
 

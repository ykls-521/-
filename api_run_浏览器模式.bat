@echo off
echo 松勤-教管系统接口自动化运行准备开始......
@echo on



del /f /s /q  G:\SongQin\Python\Demo\teach_sq\report\tmp\*.json
del /f /s /q  G:\SongQin\Python\Demo\teach_sq\report\tmp\*.jpg
del /f /s /q  G:\SongQin\Python\Demo\teach_sq\report\report



@echo off
echo 环境文件删除工作完成，开始运行脚本......
@echo on

G:
cd  G:/SongQin/Python/Demo/teach_sq/test_case
pytest  -sq --alluredir=../report/tmp

allure serve ../report/tmp


@echo off
echo 接口自动化运行成功
pause
 

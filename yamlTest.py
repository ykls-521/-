import yaml  # 导入库

yamlDir = './config/test.yaml'  # 路径
# 1- 打开操作
fo = open(yamlDir, 'r', encoding='utf-8')
# 2- 使用库操作--load--加载--读取的概念
res = yaml.load_all(fo, Loader=yaml.FullLoader)
for one in res:
    print(one)
#
#
# if res['testMode']:
#      print('---该模式已经运行----')


# yamlDir = './config/logindata.yaml'#路径
# #1- 打开操作
# fo = open(yamlDir,'w',encoding='utf-8')
# runData = {'info':'normal','time':'2020-08-12'}
# res = yaml.dump(runData,fo)

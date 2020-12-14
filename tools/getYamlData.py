import yaml
import json
import pprint


def get_yaml_data():  # [(),()]
    yamlDir = '../config/logindata.yaml'  # 路径
    # 1- 打开操作
    fo = open(yamlDir, 'r', encoding='utf-8')
    # 2- 使用库操作--load--加载--读取的概念
    res = yaml.load(fo, Loader=yaml.FullLoader)
    # pprint.pprint(res)
    resList = []  # 存放结果---[(),()]
    for one in res:
        resList.append((json.dumps(one['data']), json.dumps(one['reps'])))
    return resList


# print(get_yaml_data())
if __name__ == '__main__':
    reslists = get_yaml_data()
    print(reslists)

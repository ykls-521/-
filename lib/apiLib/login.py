# 1- 使用请求库 requests
import requests, json
# 2- url---考虑可维护性--
from teach_sq.config import HOST
import json
# import flask
# from flask import request
# '''
# flask： web框架，通过flask提供的装饰器@server.route()将普通函数转换为服
# '''
# # 创建一个服务，把当前这个python文件当做一个服务
# server = flask.Flask(__name__)
#
#
# # @server.route()可以将普通函数转变为服务 登录接口的路径、请求方式
# @server.route('/login', methods=['get', 'post'])
# def login():
#     # 获取通过url请求传参的数据
#     username = request.values.get('name')
#     # 获取url请求传的密码，明文
#     pwd = request.values.get('pwd')
#     # 判断用户名、密码都不为空
#     if username and pwd:
#         if username == 'ceshi' and pwd == '123456':
#             resu = {'code': 200, 'message': '登录成功'}
#             return json.dumps(resu, ensure_ascii=False)  # 将字典转换字符串
#         else:
#             resu = {'code': -1, 'message': '账号密码错误'}
#             return json.dumps(resu, ensure_ascii=False)
#     else:
#         resu = {'code': 10001, 'message': '参数不能为空！'}
#         return json.dumps(resu, ensure_ascii=False)
#
#
# if __name__ == '__main__':
#     server.run(debug=True, port=8888, host='127.0.0.1')



class Login:
    def login(self, inData, flag=False):  # 登录方法
        url = f'{HOST}/sys/login'
        header = {'Content-Type': 'application/json'}
        payload = inData  # 字符串---变成----字典
        reps = requests.post(url, json=payload)
        if flag == False:  # 这个登录的接口会作为后续接口的前置条件
            return reps.cookies['JSESSIONID']
        else:  # 本身这个登录接口需要调用
            return reps.json()


if __name__ == '__main__':  # ctrl+j
    res = Login().login({'username': '18715036677', 'password': '18715036677'}, True)
    print(res)

import hashlib


def get_md5Data(psw):
    password = f'zr{psw}hg'
    # 1- 首先创建一个md5对象
    md5 = hashlib.md5()
    # 2- 加密 update
    md5.update(password.encode('utf-8'))  # hashlib.md5(b‘zr111111hg’).hexdigest()
    # 3- 要输出结果
    return md5.hexdigest()

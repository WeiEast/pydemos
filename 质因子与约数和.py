#! python3
# -*- coding: utf-8 -*-

import sys


def zhishu(n):  # 判断质数
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def zhiyinzi(m):  # 分解出质因子到列表中
    aa = 2
    zyz = []
    while aa < m + 1:
        if m % aa == 0 and zhishu(aa):
            zyz.append(aa)
            m = m / aa
            continue
        else:
            aa += 1
    return zyz


def qiuhe(n, c):
    h = 0
    for i in range(c + 1):
        h += n ** i
    return h

while 1:
    start_num = 236147801 ** 2
    if start_num == 'quit':
        sys.exit()
    try:
        start_num = int(start_num)
    except:

        pass
    print('正在计算中，如果时间超过5秒，请停止等待并重启程序换另一个数字再试')

    zz = zhiyinzi(start_num)
    print('该数的质因子为：', zz)
    he = 1
    for i in set(zz):
        he *= qiuhe(i, zz.count(i))
    print(he, '\n', '--------------------------------------------------------')
    ss = '用户给出的数字：' + \
        str(start_num) + '\n' + '质因子：' + str(zz) + '\n' + \
        '约数和：' + str(he) + '\n-----------------------\n'
    with open('运算结果历史.txt', 'a') as f:
        f.write(ss)

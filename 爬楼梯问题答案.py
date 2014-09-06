#! python3

# 爬楼梯递归,原理：F(n)=F(n-1)+F(n-2)+...F(n-a)


# 爬楼梯迭代
from functools import reduce


def f(n, m):
    init = [2 ** i for i in range(m)]
    return reduce(lambda x, y: x + [sum(x[-len(init):])], range(n - len(init)), init)[-1]

print("爬楼梯方案总数", f(24, 3))

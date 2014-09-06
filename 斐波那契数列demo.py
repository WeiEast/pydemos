#! python3
def fib(n):
    """返回小于指定值的斐波那契数列偶数和"""
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a + b
    return result
print(fib(10000))
# print(sum([aa for aa in fib(30000000000000000) if aa % 2 == 0]))
# 11708364174233842
#[Finished in 0.4s]

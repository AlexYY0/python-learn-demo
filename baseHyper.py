from collections.abc import Iterable
import os
from typing import Iterator


# 斐波拉契数列
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1
    return 'done'


# 斐波拉契数列生成器
def fib_g(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'


# 生成器demo：调用generator函数会创建一个generator对象，多次调用generator函数会创建多个相互独立的generator。
def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield (3)
    print('step 3')
    yield (5)
    return "demo-ok"


# 杨辉三角生成器
def triangles():
    L = [1]
    while True:
        yield L
        L = [1] + [L[i] + L[i + 1] for i in range(len(L) - 1)] + [1]


if __name__ == '__main__':
    print('高级特性')
    print('--------------------------切片------------------------------')
    L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
    print([L[0], L[1], L[2]])
    # List切片
    print(L[0:3])
    print(L[:3])
    print(L[1:3])
    # List倒数切片
    print(L[-2:])
    # List步长截取
    print(L[::2])
    print(L[::-1])
    # List复制
    print(L[:])
    # Tuple切片
    print((0, 1, 2, 3, 4, 5)[:3])
    # 字符串切片
    print('ABCDEFG'[::2])
    print('--------------------------迭代------------------------------')
    d = {'a': 1, 'b': 2, 'c': 3}
    # 因为dict的存储不是按照list的方式顺序排列，所以，迭代出的结果顺序很可能不一样
    for key in d:
        print(key)
    for value in d.values():
        print(value)
    for k, v in d.items():
        print(k, v)
    # 字符串迭代
    for ch in 'ABC':
        print(ch)
    # 是否为迭代对象判断
    print(isinstance('abc', Iterable))  # str是否可迭代
    print(isinstance([1, 2, 3], Iterable))  # list是否可迭代
    print(isinstance(123, Iterable))  # 整数是否可迭代
    # enumerate函数可以把一个list变成索引-元素对
    for i, value in enumerate(['A', 'B', 'C']):
        print(i, value)
    for x, y in [(1, 1), (2, 4), (3, 9)]:
        print(x, y)
    print('-------------------------列表生成式-------------------------------')
    # 生成list [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(list(range(1, 11)))
    # 生成[1x1, 2x2, 3x3, ..., 10x10]
    print([x * x for x in range(1, 11)])
    # 生成仅偶数的平方
    print([x * x for x in range(1, 11) if x % 2 == 0])
    # 使用两层循环，生成全排列
    print([m + n for m in 'ABC' for n in 'XYZ'])
    # 简单demo
    print([d for d in os.listdir('.')])  # os.listdir可以列出文件和目录
    # 列表生成式也可以使用两个变量来生成list
    print([k + '=' + str(v) for k, v in d.items()])
    print([s.lower() for s in L])
    # 注意：后面的if是筛选条件，不能加else
    print([x for x in range(1, 11) if x % 2 == 0])
    # 注意：前面的if必须加else，是生成的表达式
    print([x if x % 2 == 0 else -x for x in range(1, 11)])
    print('-------------------------生成器-------------------------------')
    # 只要把一个列表生成式的[]改成()，就创建了一个generator
    ll = [x * x for x in range(10)]
    print(ll)
    lg = (x * x for x in range(10))
    print(lg)
    for n in lg:
        print(n)
    print('斐波拉契数列')
    fib(6)
    print('斐波拉契数列生成器')
    for e in fib_g(6):
        print(e)
    o = odd()
    print(next(o))
    print(next(o))
    print(next(o))
    g = fib_g(6)
    while True:
        try:
            x = next(g)
            print('g:', x)
        except StopIteration as e:
            print('Generator return value:', e.value)
            break
    # 杨辉三角测试
    print('杨辉三角')
    n = 0
    results = []
    for t in triangles():
        results.append(t)
        n = n + 1
        if n == 10:
            break
    for t in results:
        print(t)
    print('-------------------------迭代器-------------------------------')
    # 使用isinstance()判断一个对象是否是Iterable、Iterator对象
    print(isinstance({}, Iterable))
    # 注意：生成器都是Iterator对象，但list、dict、str虽然是Iterable，却不是Iterator
    print(isinstance([], Iterator))
    print(isinstance((x for x in range(10)), Iterable))
    print(isinstance((x for x in range(10)), Iterator))
    # 把list、dict、str等Iterable变成Iterator可以使用iter()函数
    print(isinstance(iter([]), Iterator))

    # Iterator对象表示的是一个数据流，是一个惰性计算的有序序列

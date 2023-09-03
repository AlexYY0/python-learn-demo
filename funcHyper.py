import functools
from functools import reduce

DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}


def f(x):
    return x * x


def add(x, y):
    return x + y


def fn(x, y):
    return x * 10 + y


# map/reduce完整示例
def str2int(s):
    def fn(x, y):
        return x * 10 + y

    def char2num(s):
        return DIGITS[s]

    return reduce(fn, map(char2num, s))


# lambda简化版本
def str2int_lambda(s):
    return reduce(lambda x, y: x * 10 + y, map(lambda x: DIGITS[x], s))


# filter示例：是否为奇数
def is_odd(n):
    return n % 2 == 1


# filter示例：是否为null或空字符串
def not_empty(s):
    return s and s.strip()


# 返回函数：闭包（Closure）[返回函数不要引用任何循环变量，或者后续会发生变化的变量]
def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax

    return sum


# 返回的函数并没有立刻执行，而是直到调用了f()才执行
def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i * i

        fs.append(f)
    return fs


# 如果一定要引用循环变量怎么办？方法是再创建一个函数，用该函数的参数绑定循环变量当前的值，无论该循环变量后续如何更改，已绑定到函数参数的值不变
def count_new():
    def f(j):
        def g():
            return j * j

        return g

    fs = []
    for i in range(1, 4):
        fs.append(f(i))  # f(i)立刻被执行，因此i的当前值被传入f()
    return fs


# 使用闭包时，对外层变量赋值前，需要先使用nonlocal声明该变量不是当前函数的局部变量。
def inc():
    x = 0

    def fn():
        nonlocal x
        x = x + 1
        return x

    return fn


def build(x, y):
    return lambda: x * x + y * y


# 无参decorator装饰器
def log_noparam(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)

    return wrapper


# 效果等同于now_noparam = log_noparam(now_noparam)
@log_noparam
def now_noparam():
    print('2023-09-03')


def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)

        return wrapper

    return decorator


# 效果等同于now = log('execute')(now)
@log('execute')
def now():
    print('2023-09-03')


if __name__ == '__main__':
    print('高阶函数')
    print('--------------------------map------------------------------')
    # map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回。
    # 结果r是一个Iterator惰性序列
    r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
    print(list(r))
    print(list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9])))
    print('--------------------------reduce------------------------------')
    # reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，执行累积计算：reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
    print(reduce(add, [1, 3, 5, 7, 9]))
    # 把序列[1, 3, 5, 7, 9]变换成整数13579
    print(reduce(fn, [1, 3, 5, 7, 9]))
    print(str2int(['1', '3', '5', '7', '9']))
    print(str2int_lambda(['1', '3', '5', '7', '9']))
    print('--------------------------filter------------------------------')
    # filter()函数返回的是一个Iterator，也就是一个惰性序列，所以要强迫filter()完成计算结果，需要用list()函数获得所有结果并返回list
    print(list(filter(is_odd, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15])))
    print(list(filter(not_empty, ['A', '', 'B', None, 'C', '  '])))
    print('--------------------------sorted------------------------------')
    print(sorted([36, 5, -12, 9, -21]))
    # 接收一个key函数来实现自定义的排序，例如按绝对值大小排序
    print(sorted([36, 5, -12, 9, -21], key=abs))
    # 忽略大小写的排序
    print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower))
    # 忽略大小写的倒排序
    print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True))
    print('--------------------------返回函数------------------------------')
    # 调用lazy_sum()时，每次调用都会返回一个新的函数
    f = lazy_sum(1, 3, 5, 7, 9)
    print(f)
    print(f())
    f1, f2, f3 = count()
    print(f1())
    print(f2())
    print(f3())
    f_new1, f_new2, f_new3 = count_new()
    print(f_new1())
    print(f_new2())
    print(f_new3())
    f = inc()
    print(f())  # 1
    print(f())  # 2
    print('--------------------------匿名函数------------------------------')
    print(list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9])))
    fl = lambda x: x * x
    print(fl)
    ld = build(2, 3)
    print(ld())
    print('--------------------------装饰器------------------------------')
    f = now_noparam
    print(now_noparam.__name__)
    print(f.__name__)
    f()
    now()
    print('--------------------------偏函数------------------------------')
    # functools.partial就是帮助我们创建一个偏函数的
    # 简单总结functools.partial的作用就是，把一个函数的某些参数给固定住（也就是设置默认值），返回一个新的函数，调用这个新函数会更简单
    int2 = functools.partial(int, base=2)
    print(int2('1000000'))  # 默认转换二进制字符为数字
    print(int2('1000000', base=10))

    # 创建偏函数时，实际上可以接收函数对象、*args和**kw这3个参数（根据规则自动归纳参数）

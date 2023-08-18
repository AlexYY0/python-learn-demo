import math


def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x


def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny


# 位置参数（默认参数）【有多个默认参数时，调用的时候，既可以按顺序提供默认参数；也可以不按顺序提供部分默认参数。当不按顺序提供部分默认参数时，需要把参数名写上。】
def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s


# Python函数在定义的时候，默认参数L的值就被计算出来了，即[]，因为默认参数L也是一个变量，它指向对象[]，
# 每次调用该函数，如果改变了L的内容，则下次调用时，默认参数的内容就变了，不再是函数定义时的[]了。
# 定义默认参数要牢记一点：默认参数必须指向不变对象！
def add_end(L=[]):
    L.append('END')
    return L


# 可以用None这个不变对象来实现
def add_end_better(L=None):
    if L is None:
        L = []
    L.append('END')
    return L


# 可变参数
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum


# 关键字参数
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)


def person_check1(name, age, **kw):
    if 'city' in kw:
        # 有city参数
        pass
    if 'job' in kw:
        # 有job参数
        pass
    print('name:', name, 'age:', age, 'other:', kw)


# 命名关键字参数
def person_check(name, age, *, city, job):
    print(name, age, city, job)


# 有一个可变参数的命名关键字参数
def person_check_more(name, age, *args, city, job):
    print(name, age, args, city, job)


# 命名关键字参数可以有缺省值
def person_check_default(name, age, *, city='Beijing', job):
    print(name, age, city, job)


if __name__ == '__main__':
    print('--------------------------------------------------------')
    # print(my_abs('13'))
    print(my_abs(-13))
    x, y = move(100, 100, 60, math.pi / 6)
    print(x, y)
    print('--------------------------------------------------------')
    print(power(5))
    print(power(5, 3))
    print('--------------------------------------------------------')
    print(add_end([1, 2, 3]))
    print(add_end())
    print(add_end())
    print('--------------------------------------------------------')
    print(add_end_better())
    print(add_end_better())
    print('--------------------------------------------------------')
    print(calc())
    print(calc(1, 2))
    nums = [1, 2, 3]
    print(calc(*nums))
    print('--------------------------------------------------------')
    print(person('Michael', 30))
    print(person('Adam', 45, gender='M', job='Engineer'))
    extra = {'city': 'Beijing', 'job': 'Engineer'}
    print(person('Jack', 24, **extra))
    print('--------------------------------------------------------')
    print(person_check('Jack', 24, city='Beijing', job='Engineer'))
    # print(person_check('Jack', 24, city='Beijing', job='Engineer', job1='job1'))
    print(person_check_more('Jack', 24, city='Beijing', job='Engineer'))
    print(person_check_default('Jack', 24, job='Engineer'))
    print('--------------------------------------------------------')
    # 参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。

    # 对于任意函数，都可以通过类似func(*args, **kw)的形式调用它，无论它的参数是如何定义的

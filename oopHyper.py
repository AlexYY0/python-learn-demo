from enum import Enum, unique
from types import MethodType

from hello import Hello
from metaclass_orm.field import IntegerField, StringField
from metaclass_orm.model import Model


class Student(object):
    pass


# __slots__存在继承的时候
class StudentSlots(object):
    # __slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的
    # 除非在子类中也定义__slots__，这样，子类实例允许定义的属性就是自身的__slots__加上父类的__slots__
    __slots__ = ('name', 'age')  # 用tuple定义允许绑定的属性名称
    pass


class SonOfStudentSlots(StudentSlots):
    __slots__ = ('score')
    pass


# @property的使用
class StudentProperty(object):

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

    # birth是可读写属性
    @property
    def birth(self):
        # 属性的方法名不要和实例变量重名，否则会造成无限递归，最终导致栈溢出报错RecursionError
        return self._birth

    @birth.setter
    def birth(self, value):
        self._birth = value

    # age是只读属性
    @property
    def age(self):
        return 2023 - self._birth


class StudentCustom(object):
    def __init__(self, name):
        self.name = name

    # 定制类
    def __str__(self):
        return 'Student object (name: %s)' % self.name

    # 当调用不存在的属性时，比如score，Python解释器会试图调用__getattr__(self, 'score')来尝试获得属性，这样，我们就有机会返回score的值
    def __getattr__(self, attr):
        if attr == 'score':
            return 99
        # 返回函数也是完全可以的
        if attr == 'age':
            return lambda: 25
        # 否则抛出AttributeError的错误
        raise AttributeError('\'Student\' object has no attribute \'%s\'' % attr)


# 多重继承：多进程模式的TCP服务
# class MyTCPServer(TCPServer, ForkingMixIn):
#     pass


# 多重继承：多线程模式的UDP服务
# class MyUDPServer(UDPServer, ThreadingMixIn):
#     pass

# 利用完全动态的__getattr__，写出一个链式调用
class Chain(object):

    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        if path == 'users':
            return lambda name: Chain('%s/%s/%s' % (self._path, path, name))
        return Chain('%s/%s' % (self._path, path))

    # 把对象当作函数一样的的调用：Chain()('name')
    def __call__(self, name):
        return Chain('%s/%s' % (self._path, name))

    def __str__(self):
        return self._path

    # 直接显示变量（直接敲变量不用print）调用的不是__str__()，而是__repr__()，
    # 两者的区别是__str__()返回用户看到的字符串，而__repr__()返回程序开发者看到的字符串，也就是说，__repr__()是为调试服务的
    __repr__ = __str__


# 需要更精确地控制枚举类型，从Enum派生出自定义类
@unique  # @unique装饰器可以帮助我们检查保证没有重复值。
class Weekday(Enum):
    Sun = 0  # Sun的value被设定为0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6


# 定义一个函数作为实例方法
def set_age(self, age):
    self.age = age


def set_score(self, score):
    self.score = score


def fn(self, name='world'):  # 先定义函数
    print('Hello, %s.' % name)


# metaclass是类的模板，所以必须从`type`类型派生：
class ListMetaclass(type):
    # 当前准备创建的类的对象,类的名字,类继承的父类集合,类的方法集合
    def __new__(cls, name, bases, attrs):
        print('cls = ', cls)  # <class '__main__.ListMetaclass'>
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)


# 我们传入关键字参数metaclass时，魔术就生效了，它指示Python解释器在创建MyList时，要通过ListMetaclass.__new__()来创建，
# 在此，我们可以修改类的定义，比如，加上新的方法，然后，返回修改后的定义
class MyList(list, metaclass=ListMetaclass):
    pass


# metaclass测试：用metaclass实现一个ORM
class User(Model):
    # 定义类的属性到列的映射：
    id = IntegerField('id')
    name = StringField('username')
    email = StringField('email')
    password = StringField('password')


if __name__ == '__main__':
    print('--------------------------类操作------------------------------')
    # 给实例绑定一个属性
    s = Student()
    # 动态给实例绑定一个属性
    s.name = 'Michael'
    print(s.name)
    # 给实例绑定一个方法：给一个实例绑定的方法，对另一个实例是不起作用的
    s.set_age = MethodType(set_age, s)
    s.set_age(25)  # 调用实例方法
    print(s.age)
    # 给一个实例绑定的方法，对另一个实例是不起作用的
    s2 = Student()  # 创建新的实例
    # s2.set_age(25)  # 尝试调用方法
    # 为了给所有实例都绑定方法，可以给class绑定方法
    Student.set_score = set_score
    s.set_score(100)
    print(s.score)
    s2.set_score(99)
    print(s2.score)
    print('--------------------------__slots__------------------------------')
    s1 = StudentSlots()  # 创建新的实例
    s1.name = 'Michael'  # 绑定属性'name'
    s1.age = 25  # 绑定属性'age'
    print("s1 name:", s1.name)
    print("s1 age:", s1.age)
    # s1.score = 99  # 绑定属性'score'
    # slots = 子类 + 父类
    ss = SonOfStudentSlots()
    ss.name = "Son of Michael"
    ss.age = 18
    ss.score = 100
    # ss.grade = 9  # grade没有被定义
    print("ss name:", ss.name)
    print("ss age:", ss.age)
    print("ss score:", ss.score)
    # print("ss grade:", ss.grade)
    print('--------------------------@property------------------------------')
    sp = StudentProperty()
    sp.score = 60  # OK，实际转化为s.set_score(60)
    print(sp.score)  # OK，实际转化为s.get_score()
    # sp.score = 9999 # OK，会抛出异常
    print('--------------------------多重继承------------------------------')
    # class MyTCPServer(TCPServer, ForkingMixIn):
    # class MyUDPServer(UDPServer, ThreadingMixIn):
    print('--------------------------定制类------------------------------')
    sc = StudentCustom('EmperorWS')
    # 自动调用定制类__str__()
    print(sc)
    print(sc.score)
    # __getattr__返回了函数
    print(sc.age())
    # __getattr__，写出一个链式调用
    print(Chain("api.emperorws.club").status.user.timeline.list)
    # 非__call__实现
    print(Chain().users('michael').repos)  # /users/michael/repos
    # __call__实现
    print(Chain('/usersCall')('name'))  # __call__调用-->/usersCall/name
    print(Chain().usersCall('michael').repos)  # /usersCall/michael/repos
    # 判断一个变量是对象还是函数呢-->判断一个对象是否能被调用（判断一个对象是否是“可调用”对象）
    print(callable(Student()))  # False
    print(callable(Chain()))  # True
    print(callable(max))  # True
    print(callable([1, 2, 3]))  # False
    print(callable(None))  # False
    print(callable('str'))  # False
    print('--------------------------枚举类------------------------------')
    # 枚举类型：每个常量都是class的一个唯一实例
    Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
    print(Month.Jan, Month.Jan.name, Month.Jan.value)
    for name, member in Month.__members__.items():
        print(name, '=>', member, ',', member.value)
    # 若干种方法访问这些枚举类型
    day1 = Weekday.Mon
    print(Weekday.Mon)
    # 用成员名称引用枚举常量
    print(Weekday['Mon'])
    # 根据value的值获得枚举常量
    print(Weekday(1))
    print(Weekday.Mon.name)
    print(Weekday.Mon.value)
    print(day1 == Weekday.Mon)
    print(day1 == Weekday.Tue)
    print('--------------------------元类------------------------------')
    h = Hello()
    print(h.hello())
    # type()函数可以查看一个类型或变量的类型
    print(type(Hello))  # Hello是一个class，它的类型就是type
    print(type(h))  # h是一个实例，它的类型就是class Hello
    # 运行时动态创建class的方法就是使用type()函数
    HelloRun = type('HelloRun', (object,), dict(hello=fn, hello1=fn))  # 创建Hello class
    hr = HelloRun()
    print(hr.hello())
    print(hr.hello1())
    print(type(HelloRun))
    print(type(hr))
    # metaclass
    print('metaclass')
    L = MyList()
    L.add(1)
    print(L)
    L2 = list()
    # L2.add(1)  # 异常，因为普通list没有add方法
    # metaclass实现一个ORM框架
    u = User(id=12345, name='Michael', email='test@orm.org', password='my-pwd')
    u.save()

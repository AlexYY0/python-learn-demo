from types import MethodType


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


# 多重继承：多进程模式的TCP服务
# class MyTCPServer(TCPServer, ForkingMixIn):
#     pass


# 多重继承：多线程模式的UDP服务
# class MyUDPServer(UDPServer, ThreadingMixIn):
#     pass


# 定义一个函数作为实例方法
def set_age(self, age):
    self.age = age


def set_score(self, score):
    self.score = score


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

import types


class Student(object):
    # 类属性，归Student类所有
    name = 'Student'

    def __init__(self, name, score):
        self.__name = name
        self.score = score

    def print_score(self):
        print('%s: %s' % (self.__name, self.score))

    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name


# 继承
class Animal(object):
    def run(self):
        print('Animal is running...')


class Dog(Animal):
    def run(self):
        print('Dog is running...')

    def __len__(self):
        return 100

    def eat(self):
        print('Eating meat...')


class Cat(Animal):
    def run(self):
        print('Cat is running...')


# 对于Python这样的动态语言来说，则不一定需要传入Animal类型。我们只需要保证传入的对象有一个run()方法就可以了
# 这就是动态语言的“鸭子类型”，它并不要求严格的继承体系，一个对象只要“看起来像鸭子，走起路来像鸭子”，那它就可以被看做是鸭子。
class Timer(object):
    def run(self):
        print('Start...')


# 对于静态语言（例如Java）来说，如果需要传入Animal类型，则传入的对象必须是Animal类型或者它的子类，否则，将无法调用run()方法
# 对于Python这样的动态语言来说，则不一定需要传入Animal类型。我们只需要保证传入的对象有一个run()方法就可以了
def run_twice(animal):
    animal.run()
    animal.run()


if __name__ == '__main__':
    bart = Student('Bart Simpson', 59)
    lisa = Student('Lisa Simpson', 87)
    bart.print_score()
    lisa.print_score()
    print(bart)
    print(lisa)
    print(Student)
    print(bart.score)
    print(lisa.get_name(), lisa.get_grade())
    # 仍然可以通过_Student__name来访问__name变量：但是强烈建议你不要这么干
    print(lisa._Student__name)
    # 实际上这个__name变量和class内部的__name变量不是一个变量！内部的__name变量已经被Python解释器自动改成了_Student__name，而外部代码给lisa新增了一个__name变量
    lisa.__name = 'New Name'
    print(lisa.__name)
    print(lisa.get_name())
    print('--------------------------继承------------------------------')
    dog = Dog()
    dog.run()

    cat = Cat()
    cat.run()
    print(isinstance(dog, Animal))
    print(isinstance(dog, Dog))
    run_twice(dog)
    run_twice(Timer())  # file-like object
    print('--------------------------获取对象信息------------------------------')
    # 基本类型都可以用type()判断
    print(type(123))
    print(type('str'))
    print(type(None))
    print(type(abs))
    print(type(dog))
    print(type(123) == type(456))  # True
    print(type(123) == int)  # True
    print(type('abc') == type('123'))  # True
    print(type('abc') == str)  # True
    print(type('abc') == type(123))  # False
    # 判断基本数据类型可以直接写int，str等，判断一个对象是否是函数可以使用types模块中定义的常量
    print('判断是否是函数')
    print(type(run_twice) == types.FunctionType)  # True
    print(type(abs) == types.BuiltinFunctionType)  # True
    print(type(lambda x: x) == types.LambdaType)  # True
    print(type((x for x in range(10))) == types.GeneratorType)  # True
    # 判断class的类型，可以使用isinstance()函数
    print('判断class的继承关系')
    print(isinstance(dog, Dog))  # True
    print(isinstance(dog, Animal))  # True
    print(isinstance('a', str))  # True
    print(isinstance(123, int))  # True
    print(isinstance(b'a', bytes))  # True
    # 还可以判断一个变量是否是某些类型中的一种
    print(isinstance([1, 2, 3], (list, tuple)))  # True
    print(isinstance((1, 2, 3), (list, tuple)))  # True
    # 获得一个对象的所有属性和方法
    print(dir('ABC'))
    # 在len()函数内部，它自动去调用该对象的__len__()方法，所以，下面的代码是等价的
    print(len('ABC') == 'ABC'.__len__())
    # 我们自己写的类，如果也想用len(myObj)的话，就自己写一个__len__()方法
    print(len(dog))
    # getattr()、setattr()以及hasattr()，可以直接操作一个对象的状态
    print(hasattr(lisa, 'score'))  # 有属性'score'吗？ True
    print(hasattr(lisa, 'name'))  # 有属性'name'吗？ False
    setattr(lisa, 'y', 19)  # 设置一个属性'y'
    print(hasattr(lisa, 'y'))  # 有属性'y'吗？ True
    print(getattr(lisa, 'y'))  # 获取属性'y'
    print(lisa.y)  # 获取属性'y'
    # 如果试图获取不存在的属性，会抛出AttributeError的错误
    print(getattr(lisa, 'z', 404))  # 获取属性'z'，如果不存在，返回默认值404
    # 也可以获得对象的方法
    print(hasattr(lisa, 'print_score'))  # 有属性'print_score'吗？ True
    print(getattr(lisa, 'print_score'))  # 获取属性'print_score'
    fn = getattr(lisa, 'print_score')  # 获取属性'print_score'并赋值到变量fn
    print(fn)
    fn()  # 调用fn()与调用lisa.print_score()是一样的
    print('--------------------------实例属性和类属性------------------------------')
    s = Student('test', 100)  # 创建实例s
    print(s.name)  # 打印name属性，因为实例并没有name属性，所以会继续查找class的name属性-->Student
    print(Student.name)  # 打印类的name属性-->Student
    s.name = 'Michael'  # 给实例绑定name属性
    print(s.name)  # 由于实例属性优先级比类属性高，因此，它会屏蔽掉类的name属性-->Michael
    print(Student.name)  # 但是类属性并未消失，用Student.name仍然可以访问-->Student
    del s.name  # 如果删除实例的name属性
    print(s.name)  # 再次调用s.name，由于实例的name属性没有找到，类的name属性就显示出来了-->Student

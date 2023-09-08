import json
import os
import pickle
import shutil
from io import BytesIO
from io import StringIO


class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score


# 转换函数（为对象序列化做准备，Class对象转为dict）
def student2dict(std):
    return {
        'name': std.name,
        'age': std.age,
        'score': std.score
    }


# 转换函数（为对象序列化做准备，dict转Class对象）
def dict2student(d):
    return Student(d['name'], d['age'], d['score'])


if __name__ == '__main__':
    print('--------------------------文件读写------------------------------')
    print('--------------------------文本文件读------------------------------')
    # 读文件
    with open('file/mytxtfile.txt', 'r', encoding='utf-8', errors='ignore') as f:  # 文件名和标示符
        # print(f.read(1024))
        # print(f.read())
        for line in f.readlines():
            print(line.strip())  # 把末尾的'\n'删掉
    print('--------------------------二进制文件读------------------------------')
    with open('file/pic.PNG', 'rb') as f:  # 文件名和标示符
        print(f.read())  # 十六进制表示的字节
    print('--------------------------写文件------------------------------')
    # w：覆盖写；a：追加写
    with open('file/mytxtfilewrite.txt', 'w', encoding='gbk') as f:  # 传入标识符'w'或者'wb'表示写文本文件或写二进制文件
        f.write('Hello, world!')
    with open('file/mytxtfilewrite.txt', 'a', encoding='gbk') as f:  # 传入标识符'a'表示追加写
        f.write('\nappend!')
    print('--------------------------内存读写------------------------------')
    # StringIO操作的只能是str，如果要操作二进制数据，就需要使用BytesIO
    print('--------------------------StringIO------------------------------')
    f = StringIO()
    f.write('hello')
    f.write(' ')
    f.write('world!')
    print(f.getvalue())
    # 支持初始化赋值
    f = StringIO('Hello!\nHi!\nGoodbye!')
    while True:
        s = f.readline()
        if s == '':
            break
        print(s.strip())
    print('--------------------------BytesIO------------------------------')
    f = BytesIO()
    f.write('中文'.encode('utf-8'))
    print(f.getvalue())
    f = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
    print(f.read())
    print('--------------------------操作文件和目录------------------------------')
    print(os.name)  # 操作系统类型
    # print(os.uname()) # 注意uname()函数在Windows上不提供，也就是说，os模块的某些函数是跟操作系统相关的
    # os.environ
    print(os.environ)
    print(os.environ.get('PATH'))
    # 操作文件和目录
    # 查看当前目录的绝对路径
    print(os.path.abspath('.'))
    # 在某个目录下创建一个新目录，首先把新目录的完整路径表示出来
    print(os.path.join('file', 'testdir'))
    # 然后创建一个目录
    os.mkdir('file/testdir')
    # 删掉一个目录
    os.rmdir('file/testdir')
    # 通过os.path.join()函数，可以正确处理不同操作系统的路径分隔符；拆分路径时，也要通过os.path.split()函数
    print(os.path.split('/Users/michael/testdir/file.txt'))
    # 获取文件扩展名
    print(os.path.splitext('/Users/michael/testdir/file.txt'))
    # 复制文件
    shutil.copyfile("file/mytxtfile.txt", 'file/text.txt')
    # 对文件重命名
    os.rename('file/text.txt', 'file/textRe.txt')
    # 删掉文件
    os.remove('file/textRe.txt')
    # 实战demo
    print([x for x in os.listdir('.') if os.path.isdir(x)])
    print([x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.py'])
    print('--------------------------序列化------------------------------')
    d = dict(name='Bob', age=20, score=88)
    # 把任意对象序列化成一个bytes
    print(pickle.dumps(d))
    # 把对象序列化后写入一个file-like Object
    with open('file/dump.txt', 'wb') as f:
        pickle.dump(d, f)
    # 用pickle.load()方法从一个file-like Object中直接反序列化出对象（或pickle.loads()）
    with open('file/dump.txt', 'rb') as f:
        dn = pickle.load(f)
        print(dn)
    print(pickle.loads(
        b'\x80\x04\x95$\x00\x00\x00\x00\x00\x00\x00}\x94(\x8c\x04name\x94\x8c\x03Bob\x94\x8c\x03age\x94K\x14\x8c\x05score\x94KXu.'))
    print('--------------------------JSON------------------------------')
    print('序列化为JSON', json.dumps(d))
    json_str = '{"age": 20, "score": 88, "name": "Bob"}'
    print('JSON转Python对象（dict）', json.loads(json_str))  # 或者使用load()
    # 对象序列化
    s = Student('Bob', 20, 88)
    print('Class序列化为JOSN', json.dumps(s, default=student2dict))
    # 通常class的实例都有一个__dict__属性，它就是一个dict，用来存储实例变量。也有少数例外，比如定义了__slots__的class
    print('Class序列化为JOSN', json.dumps(s, default=lambda obj: obj.__dict__))
    # JSON反序列化为Class对象
    print('JOSN转Class', json.loads(json_str, object_hook=dict2student))

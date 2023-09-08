import os
import shutil

from io import BytesIO
from io import StringIO

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
    shutil.copyfile("file/mytxtfile.txt",'file/text.txt')
    # 对文件重命名
    os.rename('file/text.txt', 'file/textRe.txt')
    # 删掉文件
    os.remove('file/textRe.txt')
    # 实战demo
    print([x for x in os.listdir('.') if os.path.isdir(x)])
    print([x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py'])
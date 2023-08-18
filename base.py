# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # nameStr = input('please enter your name: ')
    # print('Hi', nameStr)
    # print_hi('PyCharm',nameStr)
    print('--------------------------------------------------------')
    print('I\'m \"OK\"!')
    print('Hell', 'World!')
    print(r'我\n爱\t你\r')
    print('''line1
    line2
    ... line3''')
    print('--------------------------------------------------------')
    print(10 / 3)
    print(9 / 3)
    print(10 // 3)
    print(10 % 3)
    print('--------------------------------------------------------')
    print(ord('A'))
    print(chr(65))
    print('中文'.encode('utf-8'))
    print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))
    print(b'\xe4\xb8\xad\xff'.decode('utf-8', errors='ignore'))
    print(len('中文'))
    print(len('中文'.encode('utf-8')))
    print('--------------------------------------------------------')
    print('Hello, %s' % 'world')
    print('Hi, %s, you have $%d.' % ('Michael', 1000000))
    print('Hi, %s, you have $%d.%f' % ('Michael', 1000000, 1.0))
    print('growth rate: %d %%' % 7)
    print('Hello, {0}, 成绩提升了 {1:.1f}%'.format('小明', 17.125))
    r = 2.5
    s = 3.14 * r ** 2
    print(f'The area of a circle with radius {r} is {s:.2f}')
    print('--------------------------------------------------------')
    classmates = ['Michael', 'Bob', 'Tracy']
    print('classmates len is', len(classmates))
    print(classmates[-1], classmates[-2], classmates[-3])
    classmates.append('Adam')
    print(classmates)
    classmates.pop()
    print(classmates)
    classmates.pop(1)
    print(classmates)
    classmates[0] = True
    print(classmates)
    listList = ['python', 'java', ['asp', 'php'], 'scheme']
    print(listList)
    print(listList[2][0])
    print('--------------------------------------------------------')
    classmatesTuple = ('Michael', 'Bob', 'Tracy')
    t = (1, 2)
    print(t)
    t = (1)  # 这是数字1
    print(t)
    t = (1,)  # 这是只有一个元素的tuple
    print(t)
    # “可变的”tuple
    t = ('a', 'b', ['A', 'B'])
    print(t)
    t[2][0] = 'X'
    t[2][1] = 'Y'
    print(t)
    print('--------------------------------------------------------')
    age = 3
    if age >= 18:
        print('adult')
    elif age >= 6:
        print('teenager')
    else:
        print('kid')
    # x = 0
    # x = ''
    x = []
    if x:
        print('True')
    else:
        print('False')
    s = '1990'
    birth = int(s)
    if birth < 2000:
        print('00前')
    else:
        print('00后')
    print('--------------------------------------------------------')
    sum = 0
    for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
        sum = sum + x
    print(sum)

    rangeList = list(range(5))
    print(rangeList)
    sum = 0
    for x in range(101):
        sum = sum + x
    print(sum)

    sum = 0
    n = 99
    while n > 0:
        sum = sum + n
        n = n - 2
    print(sum)
    print('--------------------------------------------------------')
    d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
    print(d['Michael'])
    d['Adam'] = 67
    print(d)
    print('Thomas' in d)
    print(d.get('Thomas'))
    print(d.get('Thomas', 0))
    d.pop('Bob')
    print(d)
    # key必须是不可变对象
    # key = [1, 2, 3]
    # d[key] = 'a list'
    print('--------------------------------------------------------')
    s = set([1, 1, 2, 2, 3, 3])
    print(s)
    s.add(4)
    print(s)
    s.remove(4)
    print(s)
    s1 = set([1, 2, 3])
    s2 = set([2, 3, 4])
    print(s1 & s2)  # 交集
    print(s1 | s2)  # 并集
    print('--------------------------------------------------------')
    a = 'abc'
    b = a.replace('a', 'A')
    print(a)
    print(b)
    a.replace('a', 'A')
    print(a)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

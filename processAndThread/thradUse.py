import os
import random
import subprocess
import threading
import time
from multiprocessing import Pool, Queue
# 跨平台版本的多进程模块
from multiprocessing import Process


# 子进程要执行的代码
def run_proc(name):
    print('Run child process %s (%s)...' % (name, os.getpid()))


def long_time_task(name):
    print('Run task %s (%s)...' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))


# 写数据进程执行的代码:
def write(q):
    print('Process to write: %s' % os.getpid())
    for value in ['A', 'B', 'C']:
        print('Put %s to queue...' % value)
        q.put(value)
        time.sleep(random.random())


# 读数据进程执行的代码:
def read(q):
    print('Process to read: %s' % os.getpid())
    while True:
        value = q.get(True)
        print('Get %s from queue.' % value)


# 新线程执行的代码:
def loop():
    print('thread %s is running...' % threading.current_thread().name)
    n = 0
    while n < 5:
        n = n + 1
        print('thread %s >>> %s' % (threading.current_thread().name, n))
        time.sleep(1)
    print('thread %s ended.' % threading.current_thread().name)


# 假定这是你的银行存款:
balance = 0

# 创建一个锁
lock = threading.Lock()


# 多线程并发执行的函数
def change_it(n):
    # 先存后取，结果应该为0:
    global balance
    balance = balance + n
    balance = balance - n


# 多线程并发执行的函数
def run_thread(n):
    for i in range(100000):
        # 先要获取锁:
        lock.acquire()
        try:
            # 放心地改吧:
            change_it(n)
        finally:
            # 改完了一定要释放锁:
            lock.release()


# 死循环测试函数
def loopAll():
    x = 0
    while True:
        x = x ^ 1


# 创建全局ThreadLocal对象:
local_school = threading.local()


# ThreadLocal测试函数
def process_student():
    # 获取当前线程关联的student:
    std = local_school.student
    print('Hello, %s (in %s)' % (std, threading.current_thread().name))


# ThreadLocal测试函数
def process_thread(name):
    # 绑定ThreadLocal的student:
    local_school.student = name
    process_student()


if __name__ == '__main__':
    print('--------------------------多进程------------------------------')
    print('Parent Process (%s) start...' % os.getpid())
    # Only works on Unix/Linux/Mac:
    # pid = os.fork()
    # if pid == 0:
    #     print('I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid()))
    # else:
    #     print('I (%s) just created a child process (%s).' % (os.getpid(), pid))
    p = Process(target=run_proc, args=('test',))
    print('Child process will start.')
    p.start()
    p.join()
    print('Child process end.')
    print('--------------------------进程池------------------------------')
    # 使用进程池
    p = Pool(4)
    for i in range(5):
        p.apply_async(long_time_task, args=(i,))
    print('Waiting for all subprocesses done...')
    p.close()
    p.join()
    print('All subprocesses done.')
    print('--------------------------外部子进程------------------------------')
    # 控制外部子进程
    print('$ nslookup www.python.org')
    # r = subprocess.run(['nslookup', 'www.python.org'])
    r = subprocess.call(['nslookup', 'www.python.org'])
    print('Exit code:', r)
    print('--------------------------外部子进程交互------------------------------')
    # 外部子进程时存在输入交互
    print('$ nslookup')
    p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, err = p.communicate(b'set q=mx\npython.org\nexit\n')
    print(output.decode('gb2312'))
    print('Exit code:', p.returncode)
    print('--------------------------进程间通信------------------------------')
    # 进程间通信（是通过Queue、Pipes等实现的）
    # 父进程创建Queue，并传给各个子进程：
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    # 启动子进程pw，写入:
    pw.start()
    # 启动子进程pr，读取:
    pr.start()
    # 等待pw结束:
    pw.join()
    # pr进程里是死循环，无法等待其结束，只能强行终止:
    pr.terminate()
    print('--------------------------多线程------------------------------')
    print('thread %s is running...' % threading.current_thread().name)
    t = threading.Thread(target=loop, name='LoopThread')
    t.start()
    t.join()
    print('thread %s ended.' % threading.current_thread().name)
    print('--------------------------多线程加锁------------------------------')
    # Lock
    t1 = threading.Thread(target=run_thread, args=(5,))
    t2 = threading.Thread(target=run_thread, args=(8,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print(balance)
    # 死循环测试（由于GIL锁的问题，多线程在Python中只能交替执行，无法利用多核）
    # for i in range(multiprocessing.cpu_count()):
    #     t = threading.Thread(target=loopAll)
    #     t.start()
    print('--------------------------ThreadLocal------------------------------')
    t1 = threading.Thread(target=process_thread, args=('Alice',), name='Thread-A')
    t2 = threading.Thread(target=process_thread, args=('Bob',), name='Thread-B')
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print('--------------------------分布式进程------------------------------')
    # 请看task_master.py和task_worker.py

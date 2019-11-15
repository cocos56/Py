import os
import time
from multiprocessing import Process  # 进程模块

def func():
     time.sleep(10)
     while(1):
          time.sleep(0.2)
          print('in func',os.getpid(),os.getppid())

if __name__ == '__main__':
     print('in main',os.getpid(),os.getppid())
     p1 = Process(target=func)  # 进程对象
     p1.start()  # 向操作系统提交了一个开启子进程的申请
     print(p1)
     p2 = Process(target=func)  # 进程对象
     p2.start()  # 向操作系统提交了一个开启子进程的申请
     print(p2)
     print('主进程 的 代码执行结束了')
# 原理
# if __name__ == '__main__':
    # 使用python都是调用操作系统的命令来启动进程
    # 同样使用python 不同的操作系统的操作是不同的
    # 对于windows来说 必要加if __name__ == '__main__':
    # 对于linux ios来说 不必要加if __name__ == '__main__':

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module '

__author__ = 'EmperorWS'

import sys


def test():
    args = sys.argv
    if len(args) == 1:
        print('Hello, world!', args[0])
    elif len(args) == 2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments!')


# name两边各有2个下划线__name__有2个取值：当模块是被调用执行的，取值为模块的名字（当前模块的命名空间）；当模块是直接执行的，则该变量取值为：__main__
if __name__ == '__main__':
    test()

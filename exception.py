import logging

# log的配置
logging.basicConfig(level=logging.INFO)


def foo(s):
    return 10 / int(s)


def bar(s):
    return foo(s) * 2


# 自定义异常
class FooError(ValueError):
    pass


def fooWithExcept(s):
    n = int(s)
    if n == 0:
        raise FooError('invalid value: %s' % s)
    return 10 / n


if __name__ == '__main__':
    print('--------------------------异常处理------------------------------')
    # 所有的错误类型都继承自BaseException
    print('--------------------------异常------------------------------')
    try:
        print('try...')
        r = 10 / 0
        print('result:', r)
    except ZeroDivisionError as e:
        print('except:', e)
    finally:
        print('finally...')
    print('END')
    print('--------------------------多个异常------------------------------')
    try:
        print('try...')
        r = 10 / int('a')
        print('result:', r)
    except ValueError as e:
        print('ValueError:', e)
    except ZeroDivisionError as e:
        print('ZeroDivisionError:', e)
    finally:
        print('finally...')
    print('END')
    print('--------------------------异常加else------------------------------')
    try:
        print('try...')
        r = 10 / int('2')
        print('result:', r)
    except ValueError as e:
        print('ValueError:', e)
    except ZeroDivisionError as e:
        print('ZeroDivisionError:', e)
    else:
        print('no error!')
    finally:
        print('finally...')
    print('END')
    print('--------------------------使用日志记录异常------------------------------')
    try:
        bar('0')
    except Exception as e:
        logging.exception(e)
    print('END')
    print('--------------------------使用自定义异常------------------------------')
    # fooWithExcept('0')
    print('--------------------------原样抛出异常------------------------------')
    try:
        foo('0')
    except ZeroDivisionError as e:
        print('ZeroDivisionError!')
        # raise
    print('--------------------------异常转化------------------------------')
    try:
        10 / 0
    except ZeroDivisionError:
        print('ZeroDivisionError --> ValueError')
        # raise ValueError('input error!')
    print('--------------------------使用logging------------------------------')
    n = 0
    logging.info('n = %d' % n)
    print('--------------------------使用Python的调试器pdb！！！------------------------------')

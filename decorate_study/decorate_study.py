# -*- coding:utf-8 -*-
import logging as LOG


def func():
    print("I am a function")


# 现在有一个新的需求，希望可以记录下函数的执行日志，于是在代码中添加日志代码：
def func():
    print("i am a function")
    LOG.info("fun is running")


# 写代码要遵循开发封闭原则,简单来说，它规定已经实现的功能代码不允许被修改，但可以被扩展，即：
# 封闭：已实现的功能代码块
# 开放：对扩展开发
# 如果fun2 fun3有类似需求。怎么做，在每个函数里面写？这样造成大量重复代码。我们可以这样做，重新定义一个函数：专门处理日志 ，日志处理完之后再执行真正的业务代码
def use_log(func):
    LOG.info("%s is running" % func.__name__)
    func()


# 使用时候
use_log(func)


# 这样写很容易理解 我们每次都要将一个函数作为参数传递给use_logging函数。
# 而且这种方式已经破坏了原有的代码逻辑结构，之前执行业务逻辑时，执行运行func()，但是现在不得不改成use_logging(func)。那么有没有更好的方式的呢？当然有，答案就是装饰器。

# 简单装饰器
def use_logging(func):
    def wrapper(*args, **kwargs):
        LOG.warn("%s is running" % func.__name__)
        return func(*args, **kwargs)

    return wrapper


def func():
    print('I am func')


f = use_logging(func)
f()

"""
函数use_logging就是装饰器，它把执行真正业务方法的func包裹在函数里面，
看起来像bar被use_logging装饰了。在这个例子中，函数进入和退出时 ，
被称为一个横切面(Aspect)，这种编程方式被称为面向切面的编程(Aspect-Oriented Programming)。

@符号是装饰器的语法糖，在定义函数的时候使用，避免再一次赋值操作
"""


def use_logging(func):
    def wrapper(*args, **kwargs):
        LOG.warn("%s is running" % func.__name__)
        return func(*args)

    return wrapper


@use_logging
def func():
    print("i am func")


@use_logging
def func2():
    print("i am func2")


func()
func2()
"""
如上所示，这样我们就可以省去func = use_logging(func)这一句了，直接调用func()即可得到想要的结果。
如果我们有其他的类似函数，我们可以继续调用装饰器来修饰函数，而不用重复修改函数或者增加新的封装。
这样，我们就提高了程序的可重复利用性，并增加了程序的可读性。
装饰器在Python使用如此方便都要归因于Python的函数能像普通的对象一样能作为参数传递给其他函数，
可以被赋值给其他变量，可以作为返回值，可以被定义在另外一个函数内。
"""

# ----------------------------------------------------------------------------------------------

"""
带参数的装饰器
装饰器还有更大的灵活性，例如带参数的装饰器：在上面的装饰器调用中，
比如@use_logging，该装饰器唯一的参数就是执行业务的函数。
装饰器的语法允许我们在调用时，提供其它参数，比如@decorator(a)。
这样，就为装饰器的编写和使用提供了更大的灵活性。
"""


def use_logging(level):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if level == "warn" or level == "WARN":
                LOG.warn("%s is running" % func.__name__)
            return func(*args)

        return wrapper

    return decorator


@use_logging(level="warn")
def func(name='foo'):
    print("i am %s" % name)


func()

"""
上面的use_logging是允许带参数的装饰器。它实际上是对原有装饰器的一个函数封装，并返回一个装饰器。
我们可以将它理解为一个含有参数的闭包。当我 们使用@use_logging(level="warn")调用的时候，
Python能够发现这一层的封装，并把参数传递到装饰器的环境中。

类装饰器
再来看看类装饰器，相比函数装饰器，类装饰器具有灵活度大、高内聚、封装性等优点。
使用类装饰器还可以依靠类内部的\_\_call\_\_方法，当使用 @ 形式将装饰器附加到函数上时，就会调用此方法。
"""


class Foo(object):
    def __init__(self, func):
        self._func = func

    def __call__(self):
        print('class decorator runing')
        self._func()
        print('class decorator ending')


@Foo
def bar():
    print('bar')


bar()

"""
functools.wraps

使用装饰器极大地复用了代码，但是他有一个缺点就是原函数的元信息不见了，比如函数的docstring、__name__、参数列表，先看例子：

装饰器
"""


def logged(func):
    def with_logging(*args, **kwargs):
        print(func.__name__ + " was called")
        return func(*args, **kwargs)

    return with_logging


# 函数
@logged
def f(x):
    """does some math"""
    return x + x * x


# 该函数完成等价于：
def f(x):
    """does some math"""
    return x + x * x


f = logged(f)
# 不难发现，函数f被with_logging取代了，当然它的docstring，__name__就是变成了with_logging函数的信息了。

print(f.__name__)  # prints 'with_logging'
print(f.__doc__)  # prints None

"""
这个问题就比较严重的，好在我们有functools.wraps，wraps本身也是一个装饰器，
它能把原函数的元信息拷贝到装饰器函数中，这使得装饰器函数也有和原函数一样的元信息了。
"""

from functools import wraps


def logged(func):
    @wraps(func)
    def with_logging(*args, **kwargs):
        print(func.__name__ + " was called")
        return func(*args, **kwargs)

    return with_logging


@logged
def f(x):
    """does some math"""
    return x + x * x


print(f.__name__)  # prints 'f'
print(f.__doc__)  # prints 'does some math'

"""
内置装饰器
@staticmathod、@classmethod、@property

装饰器的顺序
"""

# @a
# @b
# @c
# def f ():
#     pass
#
# #等效于
#  f = a(b(c(f)))

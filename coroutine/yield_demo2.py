def generator_1():
    total = 0
    while True:
        x = yield
        print('加', x)
        if not x:
            break
        total += x
    return total


def generator_2():  # 委托生成器
    while True:
        total = yield from generator_1()  # 子生成器
        print('加和总数是:', total)


def main():  # 调用方
    # g1 = generator_1()
    # g1.send(None)
    # g1.send(2)
    # g1.send(3)
    g2 = generator_2()
    g2.send(None)
    g2.send(2)
    g2.send(3)
    g2.send(None)


if __name__ == '__main__':
    main()
    """
    输出
    加 2
    加 3
    加 None
    加和总数是: 5
    
    【3】借用上述例子，这里有几个概念需要理一下：

    【子生成器】：yield from后的generator_1()生成器函数是子生成器
    【委托生成器】：generator_2()是程序中的委托生成器，它负责委托子生成器完成具体任务。
    【调用方】：main()是程序中的调用方，负责调用委托生成器。
    yield from在其中还有一个关键的作用是：建立调用方和子生成器的通道，
    
    在上述代码中main()每一次在调用send(value)时，value不是传递给了委托生成器generator_2()，而是借助yield from传递给了子生成器generator_1()中的yield
    同理，子生成器中的数据也是通过yield直接发送到调用方main()中。
    之后我们的代码都依据调用方-子生成器-委托生成器的规范形式书写。
    --------------------- 
    作者：SL_World 
    来源：CSDN 
    原文：https://blog.csdn.net/SL_World/article/details/86597738 
    版权声明：本文为博主原创文章，转载请附上博文链接！
    
    """

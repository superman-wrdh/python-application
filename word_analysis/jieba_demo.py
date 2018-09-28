# pip3 install jieba
import jieba


def fun1():
    seg_list = jieba.cut("我来到北京清华大学", cut_all=True)
    arr = list(seg_list)
    print(arr)
    print("全模式: " + "/ ".join(arr))  # 全模式


def fun2():
    seg_list = jieba.cut("我来到北京清华大学", cut_all=False)
    print("精确模式: " + "/ ".join(seg_list))  # 精确模式

    seg_list = jieba.lcut("我来到北京清华大学", cut_all=False)
    print(seg_list)


def fun3():
    seg_list = jieba.lcut("我来到北京清华大学，我又来到北京清华大学", cut_all=False)
    print(seg_list)  # 不会去重

    seg_list = jieba.cut("他来到了网易杭研大厦")  # 默认是精确模式
    print("默认模式: " + "/ ".join(seg_list))


def fun4():
    seg_list = jieba.cut_for_search("小明硕士毕业于中国科学院计算所，后在日本京都大学深造")  # 搜索引擎模式
    print(", ".join(seg_list))

    seg_list = jieba.lcut_for_search("小明硕士毕业于中国科学院计算所，后在日本京都大学深造")
    print(seg_list)


if __name__ == '__main__':
    fun1()
    fun2()
    fun3()
    fun4()
    username = 1

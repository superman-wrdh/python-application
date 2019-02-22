def generator_1(titles):
    yield titles


def generator_2(titles):
    yield from titles


titles = ['Python', 'Java', 'C++']
for title in generator_1(titles):
    print('生成器1:', title)
for title in generator_2(titles):
    print('生成器2:', title)

"""
生成器1: ['Python', 'Java', 'C++']
生成器2: Python
生成器2: Java
生成器2: C++
在这个例子中yield titles返回了titles完整列表，而yield from titles实际等价于：
for title in titles:　# 等价于yield from titles
    yield title　
"""

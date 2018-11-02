import os
from collections import Counter

file_list_content = []


def scan_file(path):
    dirs = os.listdir(path)
    full_dir = [os.path.join(path, i) for i in dirs]
    for i in full_dir:
        if os.path.isdir(i):
            scan_file(i)
        else:
            if i.endswith(".py"):
                file_list_content.append(i)


def read_file(path):
    f = open(path, 'r', encoding='utf8')
    string = f.read()
    return string


if __name__ == '__main__':
    from pprint import pprint

    scan_file(r'D:\usr\count')
    strings = ""
    for i in file_list_content:
        s = read_file(i)
        strings = strings + s
    alpha = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
    abcs = list(strings)
    abcs = [i for i in abcs if i in alpha]
    count_dict = dict(Counter(abcs))
    values = list(count_dict.values())
    print("总字符数")
    pprint(sum(values))
    od = sorted(count_dict.items(), key=lambda x: x[1], reverse=True)
    print("字母统计-降序排列")
    pprint(od)

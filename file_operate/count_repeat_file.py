# -*- coding:utf-8 -*-
import os
import hashlib
count = 0


def get_md5(file_full_path):
    f = open(file_full_path, 'rb')
    md5_obj = hashlib.md5()
    while True:
        # 64M 大小约等于磁盘读取速度最高
        d = f.read(1024*1024*64)
        if not d:
            break
        md5_obj.update(d)
    hash_code = md5_obj.hexdigest()
    f.close()
    md5_str = str(hash_code).upper()
    return md5_str


def scan(path, record_file_name=None):
    if record_file_name is None:
        record_file_name = str(path).replace("/", "-").replace("\\", "-").replace(":", "-")+".txt"
    file = open(record_file_name, "w", encoding="utf-8")
    # 记录MD5

    def read_directory(path):
        global count
        if path:
            paths = list(os.listdir(path))
            for i in paths:
                # windows系统下$开头的目录是系统标记特殊目录没有权限访问
                if not str(i).startswith("$"):
                    full_path = os.path.join(path, i)
                    if os.path.isdir(full_path):
                        read_directory(full_path)
                    else:
                        md5 = get_md5(full_path)
                        file.write(str(count)+"\t"+full_path+"\t"+md5+"\n")
                        print(count, ":", full_path, ":", md5)
                        count += 1
        else:
            print("read directory finished")
    if isinstance(path, str):
        print("str")
        read_directory(path)
    elif isinstance(path, list):
        print("list ")
        [read_directory(p) for p in path]
    else:
        print("error")
        raise "Parameter types are not supported"
    file.close()

    # 根据记录文件MD5算重复文件
    file = open(record_file_name, "r", encoding="utf8")
    content = []
    md5_set = set()
    while True:
        line = file.readline()
        if line:
            items = line.split("\n")[0].split("\t")
            content.append({
                "id": items[0],
                "path": items[1],
                "md5": items[2],
            })
            md5_set.add(items[2])
        else:
            file.close()
            break

    md5_map = {key: [] for key in md5_set}
    from pprint import pprint
    {md5: md5_map[md5].append(i) for md5 in md5_map for i in content if md5 == i["md5"]}
    file_re = open("重复文件列表-"+record_file_name, "w", encoding="utf8")
    file_re.write("编号\t\t重复数量\t\tMD5\t\t目录\n")
    index = 0
    for key, value in md5_map.items():
        if len(value) > 1:
            pprint(value)
            file_re.write(str(index)+"\t\t"+str(len(value))+"\t\t"+key+"\n")
            for i in value:
                file_re.write("\t    \t    "+i["path"]+"\n")
            file_re.write("\n")
            index += 1

    print(md5_map)
    return md5_map


if __name__ == '__main__':
    # 递归读取改文件夹下面文件 并根据MD5找出重复文件
    # 用法 第二个参数可选
    # scan("D:\测试文件夹") scan(["D:\测试文件夹", "D:\测试文件夹"])
    scan(["D:\测试文件夹", "D:\测试文件2"])


from __future__ import division
import math
import csv
import json
from pprint import pprint
import argparse

import requests
from bs4 import BeautifulSoup
import sys
reload(sys)
sys.setdefaultencoding('utf8')

HEADERS = {
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 '
                  '(KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
}

VERSION = "VERSION 0.0.2"


def search(kw, num, sort_by):
    """
    :param kw: 资源名称
    :param num: 资源数量
    :param sort_by: 排序方式。0：按磁力时间排序，1：按磁力大小排序
    """
    print("Crawling data for you.....")
    domain = "http://bt2.bt87.cc"

    # 确保 num 有效
    if num < 0 or num > 200:
        num = 20
    # 每页最多 20 条磁力信息
    page = int(math.ceil(num / 20))
    urls = []
    for p in range(1, page + 1):
        url = domain + "/index.php?r=files%2Findex&kw={kw}&page={p}".\
            format(kw=kw, p=p)
        try:
            resp = requests.get(url, headers=HEADERS).text
            try:
                bs = BeautifulSoup(resp, "lxml").find(
                    "ul", class_="row list-group").find_all("li")
                urls.extend([domain + b.find("a")["href"] for b in bs])
            except:
                pass
        except Exception:
            print("Crawling Exception, may be you should check your network!")

    magnets = []
    if not urls:
        print("Sorry, found nothing :(")

    for url in urls:
        try:
            resp = requests.get(url, headers=HEADERS).text
            magnet = BeautifulSoup(resp, 'lxml').find("h4", id="magnet").text[8:]
            magnet_name = BeautifulSoup(resp, 'lxml').find("h3").text
            magnet_date, magnet_size = (
                str(BeautifulSoup(resp, 'lxml').find("h4").text).split(maxsplit=1))
            magnets.append({
                "magnet": magnet,               # 磁力链接
                "magnet_name": magnet_name,     # 磁力名称
                "magnet_date": magnet_date,     # 磁力日期
                "magnet_size": magnet_size      # 磁力大小
            })
        except Exception:
            print("Crawling Exception, may be you should check your network!")
    return sort_magnets(magnets, sort_by, num)


def sort_magnets(magnets, sort_by, num):
    """ 排序磁力

    :param magnets: 磁力列表
    :param sort_by: 排序方式
    """
    # 按日期排序，默认
    if sort_by == 0:
        _magnets = sorted(magnets,
                          key=lambda x: x["magnet_date"],
                          reverse=True)
    # 按大小排序，统一单位为 kb
    else:
        for m in magnets:
            unit = m["magnet_size"].split()
            if unit[1] == "GB":
                _size = float(unit[0]) * 1024 * 1024
            elif unit[1] == "MB":
                _size = float(unit[0]) * 1024
            else:
                _size = float(unit[0])
            m["magnet_size_kb"] = _size
        _magnets = sorted(magnets,
                          key=lambda x: x["magnet_size_kb"],
                          reverse=True)
    return _magnets[:num]


def _print(magnets, is_show_magnet_only):
    """ 在终端界面输出结果

    :param magnets: 磁力列表
    :param is_show_magnet_only: 单行输出
    """
    if is_show_magnet_only:
        for row in magnets:
            print(row["magnet"], row["magnet_size"], row["magnet_date"])
    else:
        for row in magnets:
            if "magnet_size_kb" in row:
                row.pop("magnet_size_kb")
            pprint(row)


def _output(magnets, path):
    """ 将数据保存到本地文件

    :param magnets: 磁力列表
    :param path: 文件路径，支持 csv 和 json 两种文件格式
    """
    if path:
        if str(path).endswith("csv"):
            try:
                with open(path, mode="w+", encoding="utf-8") as fout:
                    f_csv = csv.writer(fout)
                    f_csv.writerow((
                        "magnet_name", "magnet_date", "magnet_size", "magnet"))
                    for row in magnets:
                        f_csv.writerow((
                            row["magnet_name"], row["magnet_date"],
                            row["magnet_size"], row["magnet"]))
            except Exception:
                print("Failed to save the file!")
        if str(path).endswith("json"):
            try:
                with open(path, mode="w+", encoding="utf-8") as fout:
                    fout.write(json.dumps(magnets))
            except Exception:
                print("Failed to save the file!")


# if __name__ == "__main__":
#     # 命令行操作方式
#     # command_line_runner()
#     data = search("变形金刚", 10, 0)
#     #_print(data, False)
#     for i in data:
#         pprint(i)

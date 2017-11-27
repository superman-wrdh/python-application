# -*- coding:utf-8 -*-
import re
import os
import time
import threading
from multiprocessing import Pool, cpu_count
import requests
from bs4 import BeautifulSoup

HEADERS = {
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 '
                  '(KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
    'Referer': 'http://www.mzitu.com'
}

DIR_PATH = r"D:\mzitu"      # 下载图片保存路径


def save_pic(pic_src, pic_cnt):
    """ 保存图片到本地
    """
    try:
        img = requests.get(pic_src, headers=HEADERS, timeout=10)
        imgname = "pic_cnt_{}.jpg".format(pic_cnt + 1)
        with open(imgname, 'ab') as f:
            f.write(img.content)
            print(imgname)
    except Exception as e:
        print(e)


def make_dir(folder_name):
    """ 新建文件夹并切换到该目录下
    """
    path = os.path.join(DIR_PATH, folder_name)
    # 如果目录已经存在就不用再次爬取了，去重，提高效率。存在返回 False，否则反之
    if not os.path.exists(path):
        os.makedirs(path)
        print(path)
        os.chdir(path)
        return True
    print("Folder has existed!")
    return False


def delete_empty_dir(dir):
    """ 如果程序半路中断的话，可能存在已经新建好文件夹但是仍没有下载的图片的情况
    但此时文件夹已经存在所以会忽略该套图的下载，此时要删除空文件夹
    """
    if os.path.exists(dir):
        if os.path.isdir(dir):
            for d in os.listdir(dir):
                path = os.path.join(dir, d)     # 组装下一级地址
                if os.path.isdir(path):
                    delete_empty_dir(path)      # 递归删除空文件夹
        if not os.listdir(dir):
            os.rmdir(dir)
            print("remove the empty dir: {}".format(dir))
    else:
        print("Please start your performance!")


# http://www.zhuoku.com/zhuomianbizhi/star/index-1.htm
# http://www.zhuoku.com/zhuomianbizhi/star/index-109.htm
def get_entrance_all_page():
    base_url = "http://www.zhuoku.com/zhuomianbizhi/star/"
    page_url = "http://www.zhuoku.com/zhuomianbizhi/star/index-1.htm"
    try:
        # 获取所有页码
        ops = BeautifulSoup(
            requests.get(page_url, headers=HEADERS, timeout=10).text,
            'lxml').findAll('option')
        for i in ops:
            print(i.attrs["value"])
    except Exception as e:
        print(e)


def page_entrance():
    page_url = "http://www.zhuoku.com/zhuomianbizhi/star/index-1.htm"
    try:
        bs = BeautifulSoup(
            requests.get(page_url, headers=HEADERS, timeout=10).text,
            'lxml').findAll('div', attrs={"class": "bizhiin"})
        for i in bs:
            print(i.a.attrs["href"])
    except Exception as e:
        print(e)


def main():
    pass


if __name__ == '__main__':
    page_entrance()
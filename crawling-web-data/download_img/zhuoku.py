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
# step one
def get_entrance_all_page():
    base_url = "http://www.zhuoku.com/zhuomianbizhi/star/"
    page_url = "http://www.zhuoku.com/zhuomianbizhi/star/index-1.htm"
    url = []
    try:
        # 获取所有页码
        ops = BeautifulSoup(
            requests.get(page_url, headers=HEADERS, timeout=10).text,
            'lxml').findAll('option')
        tmp = []
        for i in ops:
            tmp.append(str(i.attrs["value"]))
        url = [base_url+u for u in tmp]
    except Exception as e:
        print(e)
    return url


# step three
def page_item(page_url, base):
    # base = "http://www.zhuoku.com"
    # page_url = "http://www.zhuoku.com/zhuomianbizhi/star/index-1.htm"
    result = []
    try:
        bs = BeautifulSoup(
            requests.get(page_url, headers=HEADERS, timeout=10).text,
            'lxml').findAll('div', attrs={"class": "bizhiin"})
        tmp = []
        for i in bs:
            tmp.append(i.a.attrs["href"])
        result = [base+i for i in tmp]
    except Exception as e:
        print(e)
    return result


# step three
def get_step_two_page(url):
    base = url[0:url.rindex("/")+1]
    result = []
    try:
        bs = BeautifulSoup(
            requests.get(url, headers=HEADERS, timeout=10).text,
            'lxml').findAll("option")
        tmp = []
        for i in bs:
            tmp.append(str(i.attrs["value"]))
        result = [base+i for i in tmp]
    except Exception as e:
        print(e)
    return result


# step four
def find_large_img():
    pass


def main():
    pass


if __name__ == '__main__':
    for i in get_step_two_page("http://www.zhuoku.com/zhuomianbizhi/star-starcn/20171125213622.htm"):
        print(i)


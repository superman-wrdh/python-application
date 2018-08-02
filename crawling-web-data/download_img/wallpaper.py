# -*- encoding: utf-8 -*-
import re
import os
from threading import Thread
import time
import threading
from multiprocessing import Pool, cpu_count

import requests
from bs4 import BeautifulSoup


HEADERS = {
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 '
                  '(KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
    'Referer': 'http://www.win4000.com'
}

DIR_PATH = "/root/disk/win4000/img"      # 下载图片保存路径


def get_img_name(img_url):
    return img_url[img_url.rindex("/")+1:]


def page_get_page(page_url):
    try:
        bs = BeautifulSoup(
            requests.get(page_url, headers=HEADERS, timeout=10).text,
            'lxml').find('div', attrs={"class": "ptitle"})
        if bs is not None:
            title = bs.h1.text
            # start = int(bs.span.text)
            end = int(bs.em.text)
            left = page_url[0:page_url.rindex(".")]
            pages = [left+"_"+str(i)+".html" for i in range(2, end+1)]
            if len(pages) == 0:
                pages = None
            pages.append(page_url)
            return {
                "title": title,
                "pages": pages
            }
        else:
            print("empty url", page_url)
            return None
    except Exception as e:
        print(e)


def get_url_large_img(page_url):
    img_urls = []
    try:
        bs = BeautifulSoup(
            requests.get(page_url, headers=HEADERS, timeout=10).text,
            'lxml').find('div', attrs={"class": "pic-meinv"})
        result = re.findall(r"(?<=src=)\S+", str(bs))
        img_url = [url.replace('"', "") for url in result]
        img_urls.extend(img_url)
    except Exception as e:
        print(e)
    return img_urls


def save_pic(pic_src, imgname):
    """ 保存图片
    """
    if not os.path.exists(imgname):
        try:
            img = requests.get(pic_src, headers=HEADERS, timeout=10)
            with open(imgname, 'ab') as f:
                f.write(img.content)
                print(imgname)
        except Exception as e:
            print("exception", e)
    else:
        print("img file", imgname, "exit will not write")


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
    """ 要删除空文件夹
    """
    if os.path.exists(dir):
        if os.path.isdir(dir):
            for d in os.listdir(dir):
                path = os.path.join(dir, d)
                if os.path.isdir(path):
                    delete_empty_dir(path)
        if not os.listdir(dir):
            os.rmdir(dir)
            print("remove the empty dir: {}".format(dir))
    else:
        print("Please start your performance!")


# http://www.win4000.com/wallpaper_detail_138600.html
# http://www.win4000.com/wallpaper_detail_39895.html
def main():
    """ 获取 win4000 网站下所有套图的 url
    http://www.win4000.com/wallpaper_detail_128403.html
    """
    page_urls = ['http://www.win4000.com/wallpaper_detail_{cnt}.html'.format(cnt=cnt)
                 for cnt in range(49295, 128407)]
    print("Please wait for second ...")
    for page_url in page_urls:
        print("now will to %s" % page_url)
        d = DownLoadThread(page_url)
        d.start()
        time.sleep(5)


class DownLoadThread(Thread):
        def __init__(self, url):
            Thread.__init__(self)
            self.url = url
            print("thread init ")
            print("will download url %s" % url)

        def run(self):
            print("thread start download ")
            import time
            import random
            time.sleep(random.randint(1, 10) / 10)
            page = page_get_page(self.url)
            if page:
                title = page.get("title", None)
                pages = page.get("pages", None)
                if make_dir(title):
                    images = []
                    for purl in pages:
                        img = get_url_large_img(purl)
                        images.extend(img)
                    for i in images:
                        save_pic(i, get_img_name(i))
                print("thread start download finished ")


if __name__ == '__main__':
    main()
# -*-encoding:utf-8-*-
from threading import Thread
import requests
import urllib.request
from pyquery import PyQuery as pq
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.75 Safari/537.36'}


def get_html_img(url):
    response = requests.get(url=url, headers=headers)
    html = response.text
    doc = pq(html)
    items = doc("img")
    result = []
    for item in items:
        doc = pq(item)
        src = doc.attr("src")
        if src.startswith("http"):
            result.append(src)
    return result


def get_folder(string):
    end = string.rindex('/')
    string = string[0:end]
    start = string.rindex('/')
    return string[start + 1:]


def get_img_name(url):
    if url.count('/') == 0:
        return url
    else:
        index = url.rindex('/')
        return url[index:len(url)]


def download_img_from_url(url, save_path):
    print('---start down a group images---')
    imgs = get_html_img(url)
    flag = False
    import os
    for i in imgs:
        req = urllib.request.Request(url=i, headers=headers)
        name = get_img_name(i)
        print('savepath', save_path)
        if not os.path.exists(save_path):
            os.makedirs(save_path)
        file = open(save_path + name, 'wb')
        try:
            file.write(urllib.request.urlopen(req).read())
        except Exception as e:
            flag = True
            print('download img  %s  failed ' % i)
        file.close()
        if not flag:
            print('download img  %s  successful ' % i)
        else:
            import os
            os.remove(save_path + name)
    print('---download a group images finished---')


class DownLoadThread(Thread):
    def __init__(self, url, base_path):
        Thread.__init__(self)
        self.url = url
        self.base_path = base_path
        print("thread init ")

    def run(self):
        print("thread start download ")
        import time
        import random
        time.sleep(random.randint(1, 10)/10)
        download_img_from_url(self.url, self.base_path)
        print("thread start download finished ")


if __name__ == '__main__':
    result = []
    import time
    for i in range(1, 5584):
        time.sleep(5)
        save_path = "/home/img//"+str(i)+"//"
        url = "http://www.meizitu.com/a/"+str(i)+".html"
        print(url)
        d = DownLoadThread(url, save_path)
        d.start()


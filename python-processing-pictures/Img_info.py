# -*- encoding: utf-8 -*-
from PIL import Image, ImageFont, ImageDraw
import os
from threading import Thread
BASE_PATH = "D:\\img\\"


def img_info(path):
    im = Image.open(path)
    size = im.size
    l = max(size)
    s = min(size)
    return {"max": l, "min": s}


def del_img(path):
    info = img_info(path)
    if info["max"] < 1600 and info["min"] < 1200:
        print("img info max=%s min = %s  %s will delete" % (info["max"], info["min"], path))
        os.remove(path)


def load_img(path):
    im = Image.open(path)
    im.show()
    draw = ImageDraw.getdraw(im)
    draw.text()


def get_path(path):
    paths = os.listdir(path)
    print(paths)
    abs_paths = [os.path.join(path, p) for p in paths if os.path.isdir(os.path.join(path, p))]
    return abs_paths


def get_dir_file(path):
    files = os.listdir(path)
    return [os.path.join(path, f) for f in files]


class ThreadDel(Thread):
    def __init__(self, path):
        Thread.__init__(self)
        self.path = path

    def run(self):
        jpgs = get_dir_file(self.path)
        for i in jpgs:
            del_img(i)


def main():
    paths = get_path(BASE_PATH)
    for i in paths:
        pass


# def del_empty_dir(path):
#     if os.path.isdir(path):
#         if len(os.listdir(path)) == 0:
#             os.remove(path)


def delete_empty(dir):
    """ 如果程序半路中断的话，可能存在已经新建好文件夹但是仍没有下载的图片的情况
    但此时文件夹已经存在所以会忽略该套图的下载，此时要删除空文件夹
    """
    if os.path.exists(dir):
        if os.path.isdir(dir):
            for d in os.listdir(dir):
                path = os.path.join(dir, d)     # 组装下一级地址
                if os.path.isdir(path):
                    delete_empty(path)      # 递归删除空文件夹
        if not os.listdir(dir):
            os.rmdir(dir)
            print("remove the empty dir: {}".format(dir))
    else:
        print("Please start your performance!")


if __name__ == '__main__':
    delete_empty("D:\\img\\f")
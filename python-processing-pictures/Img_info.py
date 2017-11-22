# -*- encoding: utf-8 -*-
from PIL import Image, ImageFont, ImageDraw


def img_info(path):
    im = Image.open(path)
    size = im.size
    l = max(size)
    s = min(size)
    return {"max": l, "min": s}


def load_img(path):
    im = Image.open(path)
    im.show()
    draw = ImageDraw.getdraw(im)
    draw.text()


def main():
    print(img_info("D:\\img\\59cf49d4f3d93.jpg"))


if __name__ == '__main__':
    main()
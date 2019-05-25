# encoding utf8
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from datetime import datetime
from io import BytesIO
from utils.cache_iml import redis_cache




def generate_image(image_src=None, text=None):
    from random import randint
    BASE_DIR = ""
    import os
    if text is None:
        texts = ["今日鸡汤:努力不一定成功，但是不努力一定很轻松",
                 "今日鸡汤:人生在世，先被别人笑笑，再去笑笑别人，然后就含笑九泉了",
                 "今日鸡汤:只要是石头，到哪里都不会发光。",
                 "今日鸡汤:趁着年轻多出来走走看看，不然你都不会知道呆在家里有多爽。",
                 "今日鸡汤:岁月是把杀猪刀，是针对那些好看的人，它对长得丑的人一点办法都没有。"]
        text = texts[randint(0, len(texts)) - 1]

    names = ["超人", "羊群", "苏苏", "万万", "乔妹妹", "家宾"]
    name = names[randint(0, len(names)) - 1]
    date = "----- 尼古拉斯.{}".format(name) + str(datetime.now().date())
    if image_src is None:
        arr = os.listdir(os.path.join(BASE_DIR, "utils", "image", "resources"))
        # arr = ["83.jpg", "084.jpg", "085.jpg", "086.jpg"]
        index = randint(0, len(arr) - 1)

        image_src = os.path.join(BASE_DIR, "utils", "image", "resources", arr[index])

    imageFile = image_src
    im1 = Image.open(imageFile)

    wight, height = im1.size

    font_size = int(wight / (len(text)) + 2)
    font = ImageFont.truetype("simsun.ttc", font_size, encoding="unic")

    draw = ImageDraw.Draw(im1)

    draw.text((2, height * 0.2), text, (255, 0, 0), font=font)
    draw.text((wight * 0.1, height * 0.2 + font_size * 2), date, (148, 0, 211), font=font)
    draw = ImageDraw.Draw(im1)  # Just draw it!

    bio = BytesIO()
    im1.save(bio, "png")
    bio.seek(0)
    return bio

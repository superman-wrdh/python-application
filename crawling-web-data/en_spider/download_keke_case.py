import hashlib
import os
import requests
import en_spider.english_spider as sp

keke = ["http://www.kekenet.com/broadcast/201801/537260.shtml", "http://www.kekenet.com/broadcast/201712/537184.shtml",
        "http://www.kekenet.com/broadcast/201712/537091.shtml", "http://www.kekenet.com/broadcast/201712/536937.shtml"]


def download(url, name=None, save_location=None):
    try:
        HEADERS = {
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 '
                          '(KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
        }

        if name is None:
            name = url[url.rindex("/") + 1:]
        if save_location is None:
            save_location = ""
        else:
            if not os.path.exists(save_location):
                os.makedirs(save_location)
        response = requests.get(url=url, headers=HEADERS)
        if response.status_code == 200:
            with open(os.path.join(save_location, name), "wb") as f:
                f.write(response.content)
                return True
    except Exception as e:
        print(e)
        return False
    return False


def write_article(content_list, name, save_location=None):
    try:
        if save_location is None:
            save_location = ""
        else:
            if not os.path.exists(save_location):
                os.makedirs(save_location)
        with open(os.path.join(save_location, name), "w", encoding="utf8") as f:
            for p in content_list:
                f.write(p + "\n")
            return False
    except Exception as e:
        print("write error:", e)
        return False


def keke_test():
    for url in keke:
        data = sp.spider_kekenet_cnn(url)

        mp3_url = data.get("mp3")
        english = data.get("English")
        chinese = data.get("Chinese")
        if mp3_url and english:
            abs_dir = url[url.replace("//", "  ").index("/") + 1:url.rindex(".")]

            # 一级目录
            save_dir = os.path.join("keke", abs_dir)

            # 下载MP3
            download(url=mp3_url, save_location=save_dir)

            # 下载图片
            [download(i, save_location=save_dir) for i in english.get("images")]

            # 英文文本名字
            txt_name = url[url.rindex("/") + 1:url.rindex(".")] + ".txt"

            save_location = os.path.join(save_dir)

            # 保存英文文本
            write_article(english.get("article_split"), name=txt_name, save_location=save_location)

            if chinese:
                # 保存中文文本
                write_article(chinese.get("article_split"), name="Zh-" + txt_name, save_location=save_location)


if __name__ == '__main__':
    keke_test()

import os
import requests

keke = ["http://www.kekenet.com/broadcast/201801/537260.shtml", "http://www.kekenet.com/broadcast/201712/537184.shtml",
        "http://www.kekenet.com/broadcast/201712/537091.shtml", "http://www.kekenet.com/broadcast/201712/536937.shtml"]


def download(url, name=None, save_location=None, over_write=False):
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
            write_path = os.path.join(save_location, name)
            is_exit = os.path.exists(write_path)
            if not over_write and is_exit:
                print("does not write because file exit and over write is false")
                return
            with open(write_path, "wb") as f:
                f.write(response.content)
                return True
    except Exception as e:
        print(e)
        return False
    return False


def write_article(content_list, name, save_location=None, over_write=False):
    try:
        if save_location is None:
            save_location = ""
        else:
            if not os.path.exists(save_location):
                os.makedirs(save_location)

        write_path = os.path.join(save_location, name)
        is_exit = os.path.exists(write_path)
        if not over_write and is_exit:
            print("does not write because file exit and over write is false")
            return

        with open(write_path, "w", encoding="utf8") as f:
            for p in content_list:
                f.write(p + "\n")
            return False
    except Exception as e:
        print("write error:", e)
        return False


def write_article_double(content_list, name, save_location=None, over_write=False):
    try:
        if save_location is None:
            save_location = ""
        else:
            if not os.path.exists(save_location):
                os.makedirs(save_location)

        write_path = os.path.join(save_location, name)
        is_exit = os.path.exists(write_path)
        if not over_write and is_exit:
            print("does not write because file exit and over write is false")
            return

        with open(os.path.join(save_location, name), "w", encoding="utf8") as f:
            for dp in content_list:
                f.write(dp.get("English") + "\n")
                f.write(dp.get("Chinese") + "\n")
                f.write("\r\n")
            return False
    except Exception as e:
        print("write error:", e)
        return False


def keke_writer(url, data, base_path="keke_v5"):
    # for url in keke:
    try:
        # data = sp.spider_kekenet_cnn(url)

        mp3_url = data.get("mp3")
        english = data.get("English")
        chinese = data.get("Chinese")
        double = data.get("double")
        if mp3_url and english:
            # 相对路径
            abs_dir = url[url.replace("//", "  ").index("/") + 1:url.rindex(".")]

            # 一级目录
            save_dir = os.path.join(base_path, abs_dir)

            # 下载MP3
            download(url=mp3_url, save_location=save_dir)

            # 下载图片
            if english.get("images"):
                [download(url, save_location=save_dir) for url in english.get("images") if english.get("images")]

            # 文本名字 取文章id
            txt_name = url[url.rindex("/") + 1:url.rindex(".")] + ".txt"

            save_location = os.path.join(save_dir)

            # 保存英文文本
            write_article(english.get("article_split"), name="En" + txt_name, save_location=save_location)

            if chinese:
                # 保存中文文本
                write_article(chinese.get("article_split"), name="Zh-" + txt_name, save_location=save_location)

            # 保存中英文
            if double:
                write_article_double(double, name="Double-" + txt_name, save_location=save_location)
    except Exception as e:
        print(e)
        print("url:{} write error ")


if __name__ == '__main__':
    keke_writer()

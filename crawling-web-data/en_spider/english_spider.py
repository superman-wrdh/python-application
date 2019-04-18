# encoding:utf8
import requests
from bs4 import BeautifulSoup
import re

HEADERS = {
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 '
                  '(KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
}

""" 
CCN NEWS
http://www.kekenet.com/broadcast/CNN/
中英双语-日常更新
"""


########################################################################################################################

def spider_kekenet_cnn(url=None):
    domain = "http://www.kekenet.com/"
    if not url:
        url = "http://www.kekenet.com/broadcast/201801/537260.shtml"
    else:
        if not url.startswith(domain):
            print("Does not support domain")
            return {}
    response = requests.get(url=url, headers=HEADERS)
    if response.status_code == 200:
        html = response.text
        # 获去中文翻译链接
        ul = BeautifulSoup(html, 'lxml').find("ul", attrs={"style": "padding:10px 0;"})
        chinese_page = domain + ul.find_all('li')[1].a['href']

        # 获去mp3链接
        bs = BeautifulSoup(html, 'lxml').find_all("script")
        lines = bs[5].text.split("\r\n\t\t")
        mp3_url = lines[0][lines[0].index("'") + 1:lines[0].rindex("'")] + lines[1][
                                                                           lines[1].index('"') + 1:lines[1].rindex('"')]
        chinese_info = {}

        def parsing_page(html):

            # 文章的html dom
            article = BeautifulSoup(html, 'lxml').find("div", attrs={"id": "article"})

            # 去除display:None的标签
            [i.extract() for i in article.find_all('span', attrs={"style": "display:none"})]
            # 去除文章中script标签
            [i.extract() for i in article.find_all('script')]

            images = article.find_all("img")
            # 文章中的图片
            images_url = [i.get("src") for i in images]

            # 文章不分段的结果
            ps = article.find_all("p")
            texts = [p.text for p in ps][0:-2]
            article_text = " ".join(texts)

            # 文章 分段的结果
            paragraphs = str(article).split("<br/>")
            content = []
            for p in paragraphs:
                plines = BeautifulSoup(p, "lxml").find_all("p")
                texts = [p.text for p in plines if str(p.text).strip()]
                a_paragraphs = " ".join(texts)
                if str(a_paragraphs).strip():
                    content.append(a_paragraphs)

            # 去掉最最后一段js代码 如果有
            if content[-1].count("R("):
                content[-1] = content[-1][:content[-1].index("R(")]

            return {
                "images": images_url,  # list
                "article": article_text,  # str
                "article_split": content  # list
            }

        en_article_info = parsing_page(html)

        zh_response = requests.get(url=chinese_page, headers=HEADERS)
        if zh_response.status_code == 200:
            zh_html = zh_response.content.decode("utf8")
            zh_article_info = parsing_page(zh_html)
            file = open("test.text", 'w', encoding='utf8')
            file.write(zh_article_info.get("article"))
            chinese_info.update(zh_article_info)

        zd = zip(en_article_info.get("article_split"), chinese_info.get("article_split"))
        double = [{"english": i[0], "chinese": i[1]} for i in zd]

        return {
            "Chinese": chinese_info,
            "English": en_article_info,
            "mp3": mp3_url,
            "double": double
        }

    else:
        print("spider error")
        return {}


#################################################################################################################

"""
同上
NPR NEWS
http://www.kekenet.com/broadcast/NPR/
中英双语-日常更新
"""

"""
同上
FOX NEWS
http://www.kekenet.com/broadcast/foxnews/
中英双语-日常更新
"""

"""
同上
TIMES
http://www.kekenet.com/Article/17287/
中英双语-日常更新
"""

"""
同上
有声阅读（以书为单位）
https://www.24en.com/audiobook/
中英双语-已经对齐排版
"""


def spider_24en(url=None):
    domain = "https://www.24en.com"
    if not url:
        url = "https://www.24en.com/voa/134601.html"
    else:
        if not url.startswith(domain):
            print("Does not support domain")
            return {}
    response = requests.get(url=url, headers=HEADERS)
    if response.status_code == 200:
        html = response.text
        bs = BeautifulSoup(html, 'lxml').find_all("script")
        text = bs[7].text
        mp3_url = text[text.index("https:"):text.index(".mp3") + 4]
        en_article = BeautifulSoup(html, 'lxml').find("div", attrs={"id": "tab_1"})
        zh_article = BeautifulSoup(html, 'lxml').find("div", attrs={"id": "tab_7"})
        en_data = {
            "images": None,
            "article": en_article.text,
            "article_split": [i.text for i in en_article.find_all("p")]
        }
        zh_data = {
            "images": None,
            "article": zh_article.text,
            "article_split": [i.text for i in zh_article.find_all("p")]
        }

        return {
            "Chinese": zh_data,
            "English": en_data,
            "mp3": mp3_url
        }

    else:
        print("spider error")
        return {}


"""
演讲稿100篇
http://www.tingclass.net/list-5673-1.html
原版英文+原版录音-已经分段
"""


def spider_tingclass(url=None):
    domain = "http://www.tingclass.net"
    if not url:
        url = "http://www.tingclass.net/show-5673-10737-1.html"
    else:
        if not url.startswith(domain):
            print("Does not support domain")
            return {}
    response = requests.get(url=url, headers=HEADERS)
    if response.status_code == 200:
        html = response.text
        mp3_url = BeautifulSoup(html, 'lxml').find("div", attrs={"id": "mp3"}).text
        article = BeautifulSoup(html, 'lxml').find("div", attrs={"id": "arti_tab_1"})

        [i.extract() for i in article.find_all('script')]
        [i.extract() for i in article.find_all('a')]
        [i.extract() for i in article.find_all('div', attrs={"style": "margin-bottom:10px; margin-top:10px;"})]
        article.find("div", attrs={"class": "linkme"}).extract()

        art_ps = str(article).split("<br/>")[1:-1]
        art_ps = [i.strip() for i in art_ps if i.strip()]
        en_data = {
            "images": None,
            "article": article.text.strip(),
            "article_split": art_ps
        }

        return {
            "Chinese": None,
            "English": en_data,
            "mp3": mp3_url
        }

    else:
        print("spider error")
        return {}


if __name__ == '__main__':
    from pprint import pprint

    data = spider_kekenet_cnn("http://www.kekenet.com/broadcast/201712/536937.shtml")  # Done

    # data = spider_tingclass()  # Done

    # en24_data = spider_24en() # Done
    pass

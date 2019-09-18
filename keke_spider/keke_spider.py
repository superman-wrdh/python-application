import requests
from bs4 import BeautifulSoup
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

HEADERS = {
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 '
                  '(KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
}


def get_html(url=None):
    response = requests.get(url=url, headers=HEADERS)
    if response.status_code == 200:
        html = response.content.decode("utf8")
        return html
    else:
        return None


class KeKeSpider:
    def __init__(self, url):
        self.url = url
        self.domain = "http://www.kekenet.com/"
        self._data = {}

    def get_html(self, url=None):
        spider_url = url if url else self.url

        if not spider_url.startswith(self.domain):
            print("Does not support domain")
            return None

        response = requests.get(url=spider_url, headers=HEADERS)
        if response.status_code == 200:
            html = response.content.decode("utf8")
            return html
        else:
            return None

    def _get_chinese_page_url(self, html):
        try:
            ul = BeautifulSoup(html, 'lxml').find("ul", attrs={"style": "padding:10px 0;"})
            chinese_page_url = self.domain + ul.find_all('li')[1].a['href']
            return chinese_page_url
        except Exception as e:
            s = "get chinese page failed", str(e)
            print(s)
            logger.error(s)
            return None

    def _get_mp3(self, html):
        try:
            # 获取mp3链接
            bs = BeautifulSoup(html, 'lxml').find_all("script")
            lines = bs[5].text.split("\r\n\t\t")
            mp3_url = lines[0][lines[0].index("'") + 1:lines[0].rindex("'")] + lines[1][
                                                                               lines[1].index('"') + 1:lines[1].rindex(
                                                                                   '"')]
            self._data.update({"mp3": mp3_url})
            return True
        except Exception as e:
            s = "get mp3 failed", str(e)
            print(s)
            logger.error(s)
            return False

    # 中文 英文提取
    def _parsing_page(self, html, language="en"):
        try:

            # 文章的html dom
            article = BeautifulSoup(html, 'lxml').find("div", attrs={"id": "article"})

            # 去掉中文版权说明
            if language == "zh":
                [i.extract() for i in article.find_all('span', attrs={"style": "color:#FF0000;"})]

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

            if language == "en":
                self._data.update({"English": {
                    "images": images_url,  # list
                    "article": article_text,  # str
                    "article_split": content  # list
                }})
            elif language == "zh":
                self._data.update({"Chinese": {
                    "images": images_url,  # list
                    "article": article_text,  # str
                    "article_split": content  # list
                }})
            return True
        except Exception as e:
            s = "get article {} failed :{}".format(language, str(e))
            print(s)
            logger.error(s)
            return False

    def get_data(self):
        html = self.get_html()
        if html:
            self._get_mp3(html)

            en_status = self._parsing_page(html)

            chinese_url = self._get_chinese_page_url(html)

            chinese_html = self.get_html(chinese_url)

            chinese_status = self._parsing_page(chinese_html, language="zh")

            if en_status and chinese_status:
                zd = zip(self._data.get("English").get("article_split"), self._data.get("Chinese").get("article_split"))
                double = [{"English": i[0], "Chinese": i[1]} for i in zd]
                self._data.update({"double": double})
        return self._data


class KeKeArticleSpider:
    def __init__(self, url):
        self.url = url
        self._data = {}

    def _get_mp3(self, html):
        try:
            # 获取mp3链接
            bs = BeautifulSoup(html, 'lxml').find_all("script")
            lines = bs[5].text.split("\r\n\t\t")
            mp3_url = lines[0][lines[0].index("'") + 1:lines[0].rindex("'")] + lines[1][
                                                                               lines[1].index('"') + 1:lines[1].rindex(
                                                                                   '"')]
            self._data.update({"mp3": mp3_url})
            return True
        except Exception as e:
            s = "get mp3 failed", str(e)
            print(s)
            logger.error(s)
            return False

    def ge_html(self):
        html = get_html(url=self.url)
        return html

    def get_article(self, html):
        bs = BeautifulSoup(html, 'lxml')
        article = bs.find("div", attrs={"id": "article"})
        en = article.find_all("div", attrs={"class": "qh_en"})
        zg = article.find_all("div", attrs={"class": "qh_zg"})
        en_article_split = [e.text for e in en]
        # 去掉最后其版权说明 英文有中文没有
        en_article_split = en_article_split[0:-1]

        self._data.update({"English": {
            "images": None,  # list
            "article": " ".join(en_article_split),  # str
            "article_split": en_article_split  # list
        }})

        zg_article_split = [e.text for e in zg]

        self._data.update({"Chinese": {
            "images": None,  # list
            "article": " ".join(zg_article_split),  # str
            "article_split": zg_article_split  # list
        }})

        if en_article_split and zg_article_split:
            zd = zip(self._data.get("English").get("article_split"), self._data.get("Chinese").get("article_split"))
            double = [{"English": i[0], "Chinese": i[1]} for i in zd]
            self._data.update({"double": double})

    def get_data(self):
        html = get_html(self.url)
        if html:
            self._get_mp3(html)
            self.get_article(html)
            return self._data
        return {}


class KeKeNRPSpider:
    def __init__(self, url):
        self.url = url

    def get_data(self):
        url = self.url
        return {"data": "TODO", "url": url}


class EN24Spider:
    def __init__(self, url):
        self.url = url
        self._data = {}

    def get_html(self):
        html = get_html(self.url)
        return html

    def _get_mp3(self, html):
        try:
            ss = BeautifulSoup(html, 'lxml').find_all("script")
            sl = [s.text for s in ss]
            s7 = sl[7]
            mp3_url = s7[s7.rindex("https:"):s7.rindex("mp3") + 3]
            self._data.update(
                {"mp3": mp3_url}
            )
        except Exception as e:
            print("get mp3 failed:{}".format(e))

    def get_data(self):
        html = self.get_html()
        if html:
            self._get_mp3(html)
            en_article = BeautifulSoup(html, 'lxml').find("div", attrs={"id": "tab_1"})
            zh_article = BeautifulSoup(html, 'lxml').find("div", attrs={"id": "tab_7"})
            en_data = {
                "images": None,
                # "article": en_article.text,
                "article_split": [i.text for i in en_article.find_all("p")]
            }
            zh_data = {
                "images": None,
                # "article": zh_article.text,
                "article_split": [i.text for i in zh_article.find_all("p")]
            }

            self._data.update({
                "Chinese": zh_data,
                "English": en_data,
            })

            # if en_data.get("article_split") and zh_data.get("article_split"):
            #     zd = zip(self._data.get("English").get("article_split"), self._data.get("Chinese").get("article_split"))
            #     double = [{"English": i[0], "Chinese": i[1]} for i in zd]
            #     self._data.update({"double": double})

            return self._data
        else:
            return {}


class KeKeSpiderProxy:
    def __init__(self, url):
        self.url = url
        self.url = url
        self.domain = "http://www.kekenet.com/"

    def get_spider(self):
        spider_map = {
            1: KeKeSpider,  # CNN,福克斯
            2: KeKeSpider,  # NPR
            3: KeKeArticleSpider,  # Article
            4: EN24Spider  # 24en
        }
        response = requests.get(url=self.url, headers=HEADERS)
        page_type = -1
        if response.status_code == 200:
            html = response.content.decode("utf8")
            title = BeautifulSoup(html, 'lxml').find("title")
            title = str(title)
            if title.count("福克斯") and title.count("新闻"):
                page_type = 1
            elif title.count("CNN") or title.count("cnn"):
                page_type = 1
            elif self.url.count("Article"):
                page_type = 3
            elif title.count("NPR") or title.count("npr"):
                page_type = 2
            elif self.url.startswith("https://www.24en.com/voa"):
                page_type = 4
            print(page_type)
            return spider_map.get(page_type)
        else:
            return None

    def get_data(self):
        spider = self.get_spider()
        if spider:
            data = spider(self.url).get_data()
            return data
        else:
            return None


"""
CCN NEWS
http://www.kekenet.com/broadcast/CNN/
中英双语-日常更新

NPR NEWS
http://www.kekenet.com/broadcast/NPR/
中英双语-日常更新

FOX NEWS
http://www.kekenet.com/broadcast/foxnews/
中英双语-日常更新

TIMES
http://www.kekenet.com/Article/17287/
中英双语-日常更新


24EN
https://www.24en.com/audiobook/

"""

#
# if __name__ == '__main__':
#     # test_data = {
#     #     "福克斯": "http://www.kekenet.com/broadcast/201904/582689.shtml",
#     #     "CNN": "http://www.kekenet.com/broadcast/201712/537184.shtml",
#     #     "Article": "http://www.kekenet.com/Article/17287/",
#     #     "NPR": "http://www.kekenet.com/broadcast/201402/277490.shtml"
#     # }
#     # for key, url in test_data.items():
#     #     sp = KeKeSpiderProxy(url)
#     #     d = sp.get_data()
#     #     print(d)
#     # spider = KeKeArticleSpider("http://www.kekenet.com/Article/201904/583846.shtml")
#     spider = EN24Spider("https://www.24en.com/voa/134601.html")
#     data = spider.get_data()
#     print(data)

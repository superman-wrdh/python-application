import requests
from bs4 import BeautifulSoup
import logging
import os

logger = logging.getLogger()
logger.setLevel(logging.INFO)

HEADERS = {
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 '
                  '(KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
}


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


class KeKeDownload:
    def __init__(self, url, data, base_dir=None):
        self.data = data
        self.url = url
        self.base_dir = base_dir

    @staticmethod
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

    @staticmethod
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

    @staticmethod
    def write_article_double(content_list, name, save_location=None):
        try:
            if save_location is None:
                save_location = ""
            else:
                if not os.path.exists(save_location):
                    os.makedirs(save_location)
            with open(os.path.join(save_location, name), "w", encoding="utf8") as f:
                for dp in content_list:
                    f.write(dp.get("english") + "\n")
                    f.write(dp.get("chinese") + "\n")
                    f.write("\r\n")
                return False
        except Exception as e:
            print("write error:", e)
            return False

    def run(self):
        data = self.data
        url = self.url

        base_dir = "" if not self.base_dir else self.base_dir
        mp3_url = data.get("mp3")
        english = data.get("English")
        chinese = data.get("Chinese")
        double = data.get("double")
        if mp3_url and english:
            # 相对路径
            abs_dir = url[url.replace("//", "  ").index("/") + 1:url.rindex(".")]

            # 一级目录
            save_dir = os.path.join(base_dir, abs_dir)

            # 下载MP3
            self.download(url=mp3_url, save_location=save_dir)

            # 下载图片
            [self.download(url, save_location=save_dir) for url in english.get("images")]

            # 文本名字 取文章id
            txt_name = url[url.rindex("/") + 1:url.rindex(".")] + ".txt"

            save_location = os.path.join(save_dir)

            # 保存英文文本
            self.write_article(english.get("article_split"), name="En" + txt_name, save_location=save_location)

            if chinese:
                # 保存中文文本
                self.write_article(chinese.get("article_split"), name="Zh-" + txt_name, save_location=save_location)

            # 保存中英文
            if double:
                self.write_article_double(double, name="Double-" + txt_name, save_location=save_location)


class KeKeEntry:
    def __init__(self, url):
        self.entry_url = url
        self.urls = []
        self.domain = "http://www.kekenet.com"

    # 获取入口地址 step 1
    def get_entry_item(self):
        response = requests.get(url=self.entry_url, headers=HEADERS)
        if response.status_code == 200:
            html_text = response.text
            bs = BeautifulSoup(html_text, "lxml")
            element = bs.find("div", attrs={"class": "lb_box"})
            aa = element.find_all("a")
            index_urls = [self.domain + a['href'] for a in list(aa) if a and a['href']]
            return index_urls
        return []

    # 获取该栏目所有地址 step 2
    def get_item_page(self):
        items = self.get_entry_item()
        for item in items:
            urls = self.get_page_article_list(item)
            self.urls.extend(urls)

    def get_page_article_list(self, page):
        response = requests.get(url=page, headers=HEADERS)
        if response.status_code == 200:
            html_text = response.text
            bs = BeautifulSoup(html_text, "lxml")
            article_list_box = bs.find("ul", attrs={"id": "menu-list"})
            lis = article_list_box.find_all("li")
            urls = [self.domain + i.a['href'] for i in lis if i and i.a['href']]
            return urls
        return []

    def get_next_page(self):
        return []

    def main(self):
        self.get_item_page()
        print(self.urls)


if __name__ == '__main__':
    from pprint import pprint

    keke_entry = KeKeEntry(url="http://www.kekenet.com/broadcast/CNN/")
    # keke_entry.get_entry_item()
    # spider_urls = keke_entry.get_page_article_list("http://www.kekenet.com/broadcast/CNN/Jul2017/")
    keke_entry.main()
    pass

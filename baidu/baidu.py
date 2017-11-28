# -*- encoding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
HEADERS = {
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 '
                  '(KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
    'Referer': 'http://www.mzitu.com'
}


def search(word):
    url = "https://www.baidu.com/s?wd="+word
    bs = BeautifulSoup(
        requests.get(url, headers=HEADERS, timeout=10).text,
        'lxml').findAll('div', attrs={"class": "c-container"})
    print("-------------------search "+word+"-----------------------------")
    result = []
    for i in bs:
        result.append({
            "title": str(i.h3.a.text).replace("百度", "超锅"),
            "source": i.h3.a.attrs["href"]
        })
    return result


if __name__ == '__main__':
    search("idea")


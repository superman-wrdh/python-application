# -*- encoding: utf-8 -*-
import requests
import re
from bs4 import BeautifulSoup
HEADERS = {
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 '
                  '(KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
    'Referer': 'https://www.baidu.com'
}


def search(word):
    url = "https://www.baidu.com/s?wd="+word
    bs = BeautifulSoup(
        requests.get(url, headers=HEADERS, timeout=10).text,
        'lxml').findAll('div', attrs={"class": "c-container"})
    print("-------------------search "+word+"-----------------------------")
    result = []
    for i in bs:
        if i.h3:
            title = i.h3.a.text
            source = i.h3.a.attrs["href"]
        else:
            title = i.div.a.text
            source = i.div.a.attrs["href"]
        result.append({
            "title": title,
            "source": source
        })

    return result


if __name__ == '__main__':
    for i in search("java"):
        print(i)


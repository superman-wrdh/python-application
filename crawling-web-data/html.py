import requests
from lxml import etree


if __name__ == '__main__':
    response = requests.get(url='https://66super.com/blog/articles/125.html')
    if response.status_code == 200:
        text = response.text
        html = etree.HTML(text)
        xpath = """//*[@id="index_view"]/ul/span/p[10]/img"""
        tag = html.xpath(xpath)
        pass
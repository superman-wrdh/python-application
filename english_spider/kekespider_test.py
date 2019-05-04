test_data = {

    # CCN NEWS
    # http://www.kekenet.com/broadcast/CNN/
    # 中英双语-日常更新
    "cnn": [
        {"url": "http://www.kekenet.com/broadcast/201801/537260.shtml", "pass": False},
        {"url": "http://www.kekenet.com/broadcast/201712/537184.shtml", "pass": False},
        {"url": "http://www.kekenet.com/broadcast/201712/537091.shtml", "pass": False},
        {"url": "http://www.kekenet.com/broadcast/201712/536204.shtml", "pass": False},
        {"url": "http://www.kekenet.com/broadcast/201712/536083.shtml", "pass": False},
        {"url": "http://www.kekenet.com/broadcast/201712/535508.shtml", "pass": False},
    ],

    # NPR NEWS
    # http://www.kekenet.com/broadcast/NPR/
    # 中英双语-日常更新
    "nrp": [
        {"url": "http://www.kekenet.com/broadcast/201801/537261.shtml", "pass": False},
        {"url": "http://www.kekenet.com/broadcast/201712/537190.shtml", "pass": False},
        {"url": "http://www.kekenet.com/broadcast/201712/537108.shtml", "pass": False},
        {"url": "http://www.kekenet.com/broadcast/201712/536996.shtml", "pass": False},
        {"url": "http://www.kekenet.com/broadcast/201712/535890.shtml", "pass": False},
        {"url": "http://www.kekenet.com/broadcast/201712/535508.shtml", "pass": False},
        {"url": "http://www.kekenet.com/broadcast/201712/535217.shtml", "pass": False},
        {"url": "http://www.kekenet.com/broadcast/201712/535365.shtml", "pass": False},
    ],

    # FOX NEWS
    # http://www.kekenet.com/broadcast/foxnews/
    # 中英双语-日常更新
    "foxnews": [
        {"url": "http://www.kekenet.com/broadcast/201904/582824.shtml", "pass": False},
        {"url": "http://www.kekenet.com/broadcast/201904/582689.shtml", "pass": False},
        {"url": "http://www.kekenet.com/broadcast/201904/582570.shtml", "pass": False},
        {"url": "http://www.kekenet.com/broadcast/201903/581221.shtml", "pass": False},
        {"url": "http://www.kekenet.com/broadcast/201903/580076.shtml", "pass": False},
        {"url": "http://www.kekenet.com/broadcast/201903/582070.shtml", "pass": False},
    ],

    # TIMES
    # http://www.kekenet.com/Article/17287/
    # 中英双语-日常更新
    "Article": [
        {"url": "http://www.kekenet.com/Article/201904/583588.shtml", "pass": False},
        {"url": "http://www.kekenet.com/Article/201904/583846.shtml", "pass": False},
        {"url": "http://www.kekenet.com/Article/201904/583522.shtml", "pass": False},
        {"url": "http://www.kekenet.com/Article/201904/583481.shtml", "pass": False},
        {"url": "http://www.kekenet.com/Article/201904/583258.shtml", "pass": False},
        {"url": "http://www.kekenet.com/Article/201904/583215.shtml", "pass": False},
        {"url": "http://www.kekenet.com/Article/201904/582977.shtml", "pass": False},
        {"url": "http://www.kekenet.com/Article/201903/582060.shtml", "pass": False},
    ],

    "en24": [
        {"url": "https://www.24en.com/voa/134601.html", "pass": True},
        {"url": "https://www.24en.com/voa/134600.html", "pass": True},
        {"url": "https://www.24en.com/voa/134509.html", "pass": True},
        {"url": "https://www.24en.com/voa/134202.html", "pass": True},
        {"url": "https://www.24en.com/voa/122656.html", "pass": True},
        {"url": "https://www.24en.com/voa/122372.html", "pass": True},
    ]

}


def main():
    from english_spider.keke_spider import KeKeSpiderProxy
    from english_spider.keke_download import keke_writer
    for k, v in test_data.items():
        for d in v:
            if d.get("pass"):
                url = d.get("url")
                print("start spider:{}".format(url))
                spider = KeKeSpiderProxy(url=url)
                data = spider.get_data()
                keke_writer(url=url, data=data, base_path=k)


if __name__ == '__main__':
    main()

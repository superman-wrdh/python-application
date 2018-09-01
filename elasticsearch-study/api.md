## elasticsearch REST API总结


## 查询所有
### get方式 /索引/_search
### http://192.168.199.139:9200/news/_search
### GET
    {
        "took": 21,
        "timed_out": false,
        "_shards": {
            "total": 5,
            "successful": 5,
            "skipped": 0,
            "failed": 0
        },
        "hits": {
            "total": 4,
            "max_score": 1,
            "hits": [
                {
                    "_index": "news",
                    "_type": "politics",
                    "_id": "RHEqFmUBe8x1mZ2ZrbJ5",
                    "_score": 1,
                    "_source": {
                        "title": "中韩渔警冲突调查：韩警平均每天扣1艘中国渔船",
                        "date": "2011-12-17",
                        "url": "https://news.qq.com/a/20111216/001044.htm"
                    }
                },
                {
                    "_index": "news",
                    "_type": "politics",
                    "_id": "QnEqFmUBe8x1mZ2ZrLI0",
                    "_score": 1,
                    "_source": {
                        "title": "美国留给伊拉克的是个烂摊子吗",
                        "date": "2011-12-16",
                        "url": "http://view.news.qq.com/zt2011/usa_iraq/index.htm"
                    }
                },
                {
                    "_index": "news",
                    "_type": "politics",
                    "_id": "Q3EqFmUBe8x1mZ2ZrbJG",
                    "_score": 1,
                    "_source": {
                        "title": "公安部：各地校车将享最高路权",
                        "date": "2011-12-16",
                        "url": "http://www.chinanews.com/gn/2011/12-16/3536077.shtml"
                    }
                },
                {
                    "_index": "news",
                    "_type": "politics",
                    "_id": "RXEqFmUBe8x1mZ2ZrbKS",
                    "_score": 1,
                    "_source": {
                        "title": "中国驻洛杉矶领事馆遭亚裔男子枪击 嫌犯已自首",
                        "date": "2011-12-18",
                        "url": "http://news.ifeng.com/world/detail_2011_12/16/11372558_0.shtml"
                    }
                }
            ]
        }
    }












## DSL搜索
### http://192.168.199.139:9200/news/_search
### POST
    {
        "query":{"match":{"title":"中国"}}
    }
# 已经安装了ik分词器
### 返回
    {
        "took": 9,
        "timed_out": false,
        "_shards": {
            "total": 5,
            "successful": 5,
            "skipped": 0,
            "failed": 0
        },
        "hits": {
            "total": 2,
            "max_score": 0.2876821,
            "hits": [
                {
                    "_index": "news",
                    "_type": "politics",
                    "_id": "RHEqFmUBe8x1mZ2ZrbJ5",
                    "_score": 0.2876821,
                    "_source": {
                        "title": "中韩渔警冲突调查：韩警平均每天扣1艘中国渔船",
                        "date": "2011-12-17",
                        "url": "https://news.qq.com/a/20111216/001044.htm"
                    }
                },
                {
                    "_index": "news",
                    "_type": "politics",
                    "_id": "RXEqFmUBe8x1mZ2ZrbKS",
                    "_score": 0.2876821,
                    "_source": {
                        "title": "中国驻洛杉矶领事馆遭亚裔男子枪击 嫌犯已自首",
                        "date": "2011-12-18",
                        "url": "http://news.ifeng.com/world/detail_2011_12/16/11372558_0.shtml"
                    }
                }
            ]
        }
    }
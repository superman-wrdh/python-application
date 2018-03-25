# -*- coding:utf-8 -*-
import redis
import requests


def get_video():
    heades = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36 LBBROWSER"}
    response = requests.get(
        url="http://gslb.miaopai.com/stream/Vz7CG3bfP~6HoheT3yURbFAPXKE~3BT7bfTDNw__.mp4?yx=&refer=weibo_app&Expires=1521191451&ssig=bnxU%2FzFgIG&KID=unistore,video",
        headers=heades)
    if response.status_code == 200:
        print("download")
        file = open("v.mp4", "wb")
        file.write(response.content)
        file.close()


def fun(yyyy):
    pass


if __name__ == '__main__':
    get_video()
    # r = redis.Redis(host='192.168.31.117', port=6379)
    # # r.hset(name="key1", key="name", value="hc")
    # # r.hset(name="key2", key="name", value="hc")
    # # r.hset(name="key3", key="name", value="hc")
    #
    # r.set(name="SetKey", value={1, 2, 3})
    # print(r.keys())
    # print(r.get("SetKey"))
    fun("")
    print(".xxx")

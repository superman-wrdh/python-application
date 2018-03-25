# encoding:utf-8
import requests
from pprint import pprint
from threading import Thread
import time
import random
from queue import Queue


HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 '
                  '(KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
    'Cookie': 'token=53156ED9A08F4C8489575BCFC1C4D2B5',
    'Access-Control-Allow-Credentials': 'true',
    'Access-Control-Allow-Origin': 'http://saian.geneapps.cn',
    'Origin': 'http://saian.geneapps.cn',
    'Referer':'http://saian.geneapps.cn/'
}


url = "http://106.15.52.253:8080/medical/team/59DDAB6D619B31477EF216AB/sample?analysisStatus=SUCCESS&page="
def get_data():
    all_id = []
    for p in range(1, 208):
        u = url+str(p)
        print(u)
        response = requests.get(u, headers = HEADERS)
        try:
            result = response.json()['data']['content']
            for i in result:
                all_id.append(i['medicalAnalysisList'][0]['id'])
        except Exception as e:
            print(p, e)
    print("========= finished get data========", len(all_id))
    for i in all_id:
        start(i)
        time.sleep(2)

def start(analysis_id):
    start_url = "http://106.15.52.253:8080/medical/analysis/"+analysis_id+"/start"
    response = requests.post(url=start_url, headers=HEADERS)
    code = response.json()["code"]
    print(analysis_id, code)


class DownLoadThread(Thread):
    def __init__(self, res_id, queue):
        Thread.__init__(self)
        self.res_id = res_id
        self.queue = queue

    def download(self):
        """
        下载 io密集任务
        """
        all_id = []
        response = requests.get(url + "p", headers=HEADERS)
        result = response.json()['data']['content']
        for i in result:
            print("get res", i['medicalAnalysisList'][0]['id'])
            all_id.append(i['medicalAnalysisList'][0]['id'])
        return all_id

    def run(self):
        data = self.download()
        for i in data:
            self.queue.put((i))


class ConvertThread(Thread):
    def __init__(self, queue):
        Thread.__init__(self)
        self.queue = queue

    @staticmethod
    def convert(data_res):
        """
        生成报告
        """
        start(data_res)
        print("end--", data_res)

    def run(self):
        while True:
            sid = self.queue.get()
            if sid == -1:
                break
            self.convert(sid)
            print("。。。 。finished convert res %s " % sid)


if __name__ == '__main__':
    # q = Queue()
    # d_Threads = [DownLoadThread(i, q) for i in range(0, 208)]
    # c_Thread = ConvertThread(q)
    # c_Thread.start()
    # for t in d_Threads:
    #     t.start()
    #
    # for t in d_Threads:
    #     t.join()
    # q.put((-1, "None"))
    #start("5A430823619B3154EF3D9652")
    get_data()
    #start("5A3B82C3619B312765B4CB9E")

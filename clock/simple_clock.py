import time
from datetime import datetime
import win32com.client

speaker = win32com.client.Dispatch("SAPI.SpVoice")

if __name__ == '__main__':
    while True:
        now = datetime.now()
        h, m, s = now.hour, now.minute, now.second
        h, m, s = 22, 0, 0
        t_str = "hello "
        if h in range(8, 24):
            if m == 0 and h <= 8:
                t_str = "现在是北京时间 {h}时 {m}分".format(h=h, m=m, )
            if h == 23:
                t_str = "现在是北京时间 {h}时 {m}分 该睡觉了".format(h=h, m=m)
            if m == 0:
                t_str = "准点报时，现在是北京时间 {h}时 {m}分".format(h=h, m=m)
        if h in range(7, 8):
            t_str = "现在是北京时间早上 {h}时 {m}分 该起床了".format(h=h, m=m)
        speaker.Speak(t_str)
        print(t_str)
        time.sleep(60)

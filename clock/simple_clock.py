import time
from datetime import datetime
import win32com.client
speaker = win32com.client.Dispatch("SAPI.SpVoice")


if __name__ == '__main__':
    while True:
        time.sleep(5)
        now = datetime.now()
        h, m, s = now.hour, now.minute, now.second
        t_str = "现在是北京时间 {h}时 {m}分 {s}秒 ".format(h=h, m=m, s=s)
        speaker.Speak(t_str)
        print(t_str)

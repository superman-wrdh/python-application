import PySimpleGUI as sg

layout = [[sg.Text('语音时钟1.0', size=(20, 2), justification='center')],
          [sg.Text('', size=(10, 2), font=('Helvetica', 20), justification='center', key='_OUTPUT_')],
          [sg.T(' ' * 5), sg.Button('开始/结束', focus=True), sg.Quit("退出")]]

window = sg.Window('时钟').Layout(layout)
from datetime import datetime
import time

timer_running = True
i = 0
while True:
    # Event Loop
    while True:
        now = datetime.now()
        h, m, s = now.hour, now.minute, now.second
        i += 1 * (timer_running is True)
        event, values = window.Read(timeout=10)  # Please try and use a timeout when possible
        if event is None or event == '退出':  # if user closed the window using X or clicked Quit button
            window.Close()
        elif event == '开始/结束':
            timer_running = not timer_running
        window.FindElement('_OUTPUT_').Update('{:02d}:{:02d}.{:02d}'.format(h, m, s))

# -*- encoding: utf-8 -*-
"""
https://pysimplegui.readthedocs.io/cookbook/

Pattern 1 - "One-shot Window" - Read int list (The Most Common Pattern)

This will be the most common pattern you'll follow if you are not using an "event loop"
(not reading the window multiple times). The window is read and then closes.

Because no "keys" were specified in the window layout, the return values will be a list of values.
If a key is present, then the values are a dictionary. See the main readme document or
 further down in this document for more on these 2 ways of reading window values.

"""
import PySimpleGUI as sg

layout = [[sg.Text('选择文件')],
          [sg.InputText(), sg.FileBrowse("浏览")],
          [sg.Submit("提交"), sg.Cancel("退出")]]

window = sg.Window('标题').Layout(layout)

event, values = window.Read()
print(values)
window.Close()

source_filename = values[0]

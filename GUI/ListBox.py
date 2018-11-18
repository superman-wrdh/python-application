# -*- encoding: utf-8 -*-
import requests
from pprint import pprint


def get_data():
    url = "https://www.66super.com/api/blog/list.do"
    response = requests.post(url=url, json={"page": 1})
    if response.status_code == 200:
        result = response.json()
        return result
    else:
        return {}


def render_ui():
    import PySimpleGUI as sg

    sg.ChangeLookAndFeel('GreenTan')
    layout = [
        [sg.Listbox(values=('Listbox 1', 'Listbox 2', 'Listbox 3'), size=(30, 3))],
        [sg.Submit(), sg.Cancel()]
    ]
    windows = sg.Window("测试", default_button_element_size=(40, 1)).Layout(layout)
    button, values = windows.Read()
    sg.Popup(button, values)


if __name__ == '__main__':
    v = get_data()
    pprint(v)
    render_ui()

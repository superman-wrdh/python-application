# -*- encoding: utf-8 -*-
import PySimpleGUI as sg

# Very basic window.  Return values as a list

layout = [
    [sg.Text('Please enter your Name, Address, Phone')],
    [sg.Text('Name', size=(15, 1)), sg.InputText()],
    [sg.Text('Address', size=(15, 1)), sg.InputText()],
    [sg.Text('Phone', size=(15, 1)), sg.InputText()],
    [sg.Submit(), sg.Cancel()]
]

window = sg.Window('Simple data entry window').Layout(layout)
while True:
    event, values = window.Read()
    if event == "Submit":
        if len(values[2]) != 11:
            print("输入错误")
        else:
            print("正确输入")
            break
window.Close()
print(event, values[0], values[1], values[2])
# -*- encoding: utf-8 -*-
import PySimpleGUI as sg

# Very basic window.  Return values as a dictionary

layout = [
    [sg.Text('Please enter your Name, Address, Phone')],
    [sg.Text('Name', size=(15, 1)), sg.InputText('name', key='_NAME_')],
    [sg.Text('Address', size=(15, 1)), sg.InputText('address', key='_ADDRESS_')],
    [sg.Text('Phone', size=(15, 1)), sg.InputText('phone', key='_PHONE_')],
    [sg.Submit(), sg.Cancel()]
]

window = sg.Window('Simple data entry GUI').Layout(layout)

event, values = window.Read()

window.Close()

print(event, values['_NAME_'], values['_ADDRESS_'], values['_PHONE_'])

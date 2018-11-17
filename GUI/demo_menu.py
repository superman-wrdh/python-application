import PySimpleGUI as sg

sg.ChangeLookAndFeel('LightGreen')
sg.SetOptions(element_padding=(0, 0))

# ------ Menu Definition ------ #      
menu_def = [['File', ['Open', 'Save', 'Exit']],
            ['Edit', ['Paste', ['Special', 'Normal', ], 'Undo'], ],
            ['Help', 'About...'], ]

# ------ GUI Defintion ------ #      
layout = [
    [sg.Menu(menu_def, )],
    [sg.Output(size=(60, 20))]
]

window = sg.Window("Windows-like program", default_element_size=(12, 1), auto_size_text=False, auto_size_buttons=False,
                   default_button_element_size=(12, 1)).Layout(layout)

# ------ Loop & Process button menu choices ------ #      
while True:
    event, values = window.Read()
    if event == None or event == 'Exit':
        break
    print('Button = ', event)
    # ------ Process menu choices ------ #      
    if event == 'About...':
        sg.Popup('About this program', 'Version 1.0', 'PySimpleGUI rocks...')
    elif event == 'Open':
        filename = sg.PopupGetFile('file to open', no_window=True)
        print(filename)

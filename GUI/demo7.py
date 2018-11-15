# -*- encoding: utf-8 -*-
import PySimpleGUI as sg
import sys

if len(sys.argv) == 1:
    event, (fname,) = sg.Window('My Script').Layout([[sg.Text('Document to open')],
                                                     [sg.In(), sg.FileBrowse()],
                                                     [sg.CloseButton('Open'), sg.CloseButton('Cancel')]]).Read()
else:
    fname = sys.argv[1]

if not fname:
    sg.Popup("Cancel", "No filename supplied")
    raise SystemExit("Cancelling: no filename supplied")
print(event, fname)

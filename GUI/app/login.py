import PySimpleGUI as sg

layout = [[sg.Text("用户名:", size=(6, 1)), sg.Input()],
          [sg.Text("密码:", size=(6, 1)), sg.Input()],
          [sg.Submit("提交", size=(8, 1)), sg.Cancel("退出", size=(8, 1))]
          ]

windows = sg.Window("登录").Layout(layout)
while True:
    event, values = windows.Read()
    if event == "退出":
        windows.Close()
        print("cancel")
        break
    elif event == "提交":
        if values[0] == "hc" and values[1] == "123456":
            sg.Popup('信息', '登录成功')
        else:
            sg.Popup('警告', '用户名或密码错误')
windows.Close()

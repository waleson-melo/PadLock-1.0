import PySimpleGUI as sg

import src.view.DashboardView as dbv


class LoginView:

    def __init__(self):
        user_image = "icons/user.png" 

        col1 = [
            [sg.Text(text='Nome:')], 
            [sg.Input(size=(21,1))],
            [sg.Text(text='Senha:')],
            [sg.Input(size=(21,1), password_char='*')],
            [sg.Button(button_text='Entrar', size=(6,1)), sg.Button(button_text='Sair', size=(6,1))]
        ]

        frame_image = [
            [sg.Image(user_image)]
        ]

        layout = [
            [sg.Frame(title='', layout=frame_image), sg.Col(col1)],
        ]

        self.window = sg.Window("Entrar no sistema", layout=layout, finalize=True)

    def start(self):
         
        while True:
            event, values = self.window.read()

            if event == sg.WINDOW_CLOSED or event == 'Sair':
                break

            if event == 'Entrar':
                self.window.hide()
                dashboard_window = dbv.DashboardView()
                dashboard_window.start()
                self.window.un_hide()

        self.window.close()

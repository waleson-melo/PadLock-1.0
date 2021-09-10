import PySimpleGUI as sg

import src.controller.LoginController as lgc


class LoginView:

    def __init__(self):
        user_image = "icons/user.png" 

        col1 = [
            [sg.Text(text='Nome:')], 
            [sg.Input(size=(21,1), key='-IN_NOME_USUARIO-')],
            [sg.Text(text='Senha:')],
            [sg.Input(size=(21,1), password_char='*',
                key='-IN_SENHA_USUARIO-')],
            [sg.Button(button_text='Entrar', size=(6,1), bind_return_key=True),
                sg.Button(button_text='Sair', size=(6,1))]
        ]

        frame_image = [
            [sg.Image(user_image)]
        ]

        layout = [
            [sg.Frame(title='', layout=frame_image), sg.Col(col1)],
        ]

        self.window = sg.Window("Entrar no sistema", layout=layout,
                                finalize=True)

    def start(self):
         
        while True:
            event, values = self.window.read()

            if event == sg.WINDOW_CLOSED or event == 'Sair':
                break

            if event == 'Entrar':
                nome = values['-IN_NOME_USUARIO-']
                senha = values['-IN_SENHA_USUARIO-']
                
                loginc = lgc.LoginController()

                if nome != '' and senha != '':
                    if loginc.validar_usuario(login=nome, senha=senha):
                        self.window.hide()

                        loginc.start_dashboard()

                        self.window.un_hide()
                        self.window['-IN_NOME_USUARIO-'].update('')
                        self.window['-IN_NOME_USUARIO-'].set_focus()
                        self.window['-IN_SENHA_USUARIO-'].update('')
                    else:
                        sg.PopupError('Usuario ou senha incorreta.',
                            title='Erro', auto_close=True,
                            auto_close_duration=3)
                else:
                    sg.popup_ok('Preenha os campos.', title='Aviso',
                        auto_close=True, auto_close_duration=3)

        self.window.close()

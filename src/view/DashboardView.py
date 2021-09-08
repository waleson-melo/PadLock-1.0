import PySimpleGUI as sg

import src.view.SenhaView as snv


class DashboardView:

    def __init__(self):
        menu_bar = [
            ['&Gerenciar', ['&Senhas', '&Usuário']],
            ['&Ajuda', 'So&bre']
        ]

        col_senhas = [
            [sg.Input('Pesquisar', expand_x=True, key='-IN_PESQUISA-')],
            [sg.Listbox([], size=(38,6))],
            [sg.Button('Novo', size=(7,1)), sg.Button('Atualizar', size=(7,1))]
        ]

        size_text = (12,1)
        col_usuario = [
            [sg.Text('Código:', size=size_text), sg.Input('', expand_y=True,
                key='-IN_CODIGO_USUARIO-', disabled=True)],
            [sg.Text('Nome:', size=size_text), sg.Input('', expand_y=True,
                key='-IN_NOME_USUARIO-')],
            [sg.Text('Senha:', size=size_text), sg.Input('', expand_y=True,
                key='-IN_SENHA_USUARIO-')],
            [sg.Text('Repetir senha:', size=size_text),
                sg.Input('', expand_y=True, key='-IN_REPETIR_SENHA_USUARIO-')],
            [sg.Checkbox('Marque aqui para editar.', default=False,
                enable_events=True, key='-CHECKBOX_EDITAR-')],
            [sg.Button('Salvar Usuário')]
        ]

        layout = [
            [sg.Text('Senhas', font='Ubuntu 15 normal', key='-TEXT_OPCAO-')],
            [sg.Menu(menu_bar, tearoff=False)],
            [sg.Column(col_senhas, key='-COL_SENHAS-'), sg.Canvas(size=(0,0), pad=(0,0))],
            [sg.Column(col_usuario, key='-COL_USUARIO-'), sg.Canvas(size=(0,0), pad=(0,0))]
        ]

        self.window = sg.Window('Gerenciador de Senhas', layout=layout, 
                                finalize=True, size=(300,250), margins=(3,3))

        self.window['-COL_USUARIO-'].update(visible=False)


    def start(self):
        while True:
            event, values = self.window.read()

            if event == sg.WINDOW_CLOSED or event == 'Sair':
                break

            if event == 'Usuário':
                self.window['-TEXT_OPCAO-'].update('Usuário')
                self.window['-IN_NOME_USUARIO-'].set_focus()
                self.window['-COL_SENHAS-'].update(visible=False)
                self.window['-COL_USUARIO-'].update(visible=True)
            
            if event == 'Senhas':
                self.window['-TEXT_OPCAO-'].update('Senhas')
                self.window['-IN_PESQUISA-'].set_focus()
                self.window['-COL_USUARIO-'].update(visible=False)
                self.window['-COL_SENHAS-'].update(visible=True)
            
            if event == 'Novo':
                nova_senha_window = snv.SenhaView('NOVO')
                self.window.hide()
                nova_senha_window.start()
                self.window.un_hide()
                
        self.window.close()   


if __name__ == '__main__':
    dash = DashboardView()

    dash.start()

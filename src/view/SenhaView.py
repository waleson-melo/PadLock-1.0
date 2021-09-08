import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import Window


class SenhaView:

    def __init__(self, opcao='NOVO'):
        if opcao == 'NOVO':
            self.title_window = 'Nova Senha'
            size_text = (18,1)
            size_input = (30,1)
            self.layout = [
                [sg.Text('Título:', size=size_text), sg.Input('', size=(size_input),
                    key='-IN_TITULO_SENHA-')],
                [sg.Text('Login:', size=size_text), sg.Input('', size=(size_input),
                    key='-IN_LOGIN_SENHA-')],
                [sg.Text('Senha:', size=size_text), sg.Input('', size=(size_input),
                    key='-IN_SENHA_SENHA-')],
                [sg.Text('URL do login:', size=size_text), sg.Input('', size=(size_input),
                    key='-IN_URL_SENHA-')],
                [sg.Text('Data de modificação:', size=size_text), sg.Input('', size=(size_input),
                    key='-IN_DATAMODIFICACAO_SENHA-')],
                [sg.Text('Observações:', size=size_text), sg.Input('', size=(size_input),
                    key='-IN_OBSERVACOES_SENHA-')],
                [sg.Button('Salvar'), sg.Button('Limpar'),
                    sg.Button('Cancelar')]
            ]
        elif opcao == 'ALTERAR':
            self.title_window = 'Alterar Senha'
            size_text = (18,1)
            size_input = (30,1)
            size_button = (7,1)
            self.layout = [
                [sg.Text('Código:', size=size_text), sg.Input('',
                    size=size_input, disabled=True, key='-IN_CODIGO_SENHA-')],
                [sg.Text('Título:', size=size_text), sg.Input('', 
                    size=size_input, key='-IN_TITULO_SENHA-')],
                [sg.Text('Login:', size=size_text), sg.Input('',
                    size=size_input, key='-IN_LOGIN_SENHA-')],
                [sg.Text('Senha:', size=size_text), sg.Input('',
                    size=size_input, key='-IN_SENHA_SENHA-')],
                [sg.Text('URL do login:', size=size_text), sg.Input('',
                    size=size_input, key='-IN_URL_SENHA-')],
                [sg.Text('Data de modificação:', size=size_text), sg.Input('',
                    size=(21,1), disabled=True, key='-IN_DATAMODIFICACAO_SENHA-'),
                    sg.CalendarButton('Data', target='-IN_DATAMODIFICACAO_SENHA-')],
                [sg.Text('Observações:', size=size_text), sg.Input('',
                    size=size_input, key='-IN_OBSERVACOES_SENHA-')],
                [sg.Button('Salvar', size=size_button),
                    sg.Button('Apagar', size=size_button),
                    sg.Button('Cancelar', size=size_button)]
            ]
        else:
            self.title_window = 'ERRO'
            self.layout = [
                [sg.Text('Erro no argumento passado.')]
            ]

        self.window = sg.Window(self.title_window, layout=self.layout,
                                finalize=False)

    def start(self):
        while True:
            event, values = self.window.read()
            
            if event == sg.WINDOW_CLOSED:
                break

            if event == 'Cancelar':
                if sg.popup_yes_no('Você deseja realmente cancelar?',
                                    'Alguns dados seram perdidos.') == 'Yes':
                    break

        self.window.close()


if __name__ == '__main__':
    senha_view = SenhaView(opcao='ALTERAR')

    senha_view.start()
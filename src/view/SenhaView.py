import PySimpleGUI as sg


class SenhaView:

    def __init__(self, opcao='NOVO'):
        if opcao == 'NOVO':
            self.title_window = 'Nova Senha'
            self.layout = [
                [sg.Text('Título:')],
                [sg.Text('Login:')],
                [sg.Text('Senha:')],
                [sg.Text('URL do login:')],
                [sg.Text('Data de modificação:')],
                [sg.Text('Observações:')]
            ]
        elif opcao == 'ALTERAR':
            self.title_window = 'Alterar Senha'
            self.layout = [
                [sg.Text('Altarar a senha do app')]
            ]
        else:
            self.title_window = 'ERRO'
            self.layout = [
                [sg.Text('Erro no argumento passado.')]
            ]

        self.window = sg.Window(self.title_window, layout=self.layout,
                                finalize=True)

    def start(self):
        while True:
            event, values = self.window.read()
            
            if event == sg.WINDOW_CLOSED:
                break

        self.window.close()


if __name__ == '__main__':
    senha_view = SenhaView(opcao='ALTERAR')

    senha_view.start()
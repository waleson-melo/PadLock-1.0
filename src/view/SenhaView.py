import PySimpleGUI as sg

import src.controller.SenhaController as snc


class SenhaView:

    def __init__(self, opcao='NOVO'):
        if opcao == 'NOVO':
            self.title_window = 'Nova Senha'
            size_text = (18,1)
            size_input = (30,1)
            size_button = (6,1)
            self.layout = [
                [sg.Text('Título:', size=size_text), sg.Input('',
                    size=(size_input), key='-IN_TITULO_SENHA-')],
                [sg.Text('Login:', size=size_text), sg.Input('',
                    size=(size_input), key='-IN_LOGIN_SENHA-')],
                [sg.Text('Senha:', size=size_text), sg.Input('',
                    size=(size_input), key='-IN_SENHA_SENHA-')],
                [sg.Text('URL do login:', size=size_text), sg.Input('',
                    size=(size_input), key='-IN_URL_SENHA-')],
                [sg.Text('Data de modificação:', size=size_text), sg.Input('',
                    size=(size_input[0]-(size_button[0]*2),1),
                    key='-IN_DATAMODIFICACAO_SENHA-',
                    disabled=True), sg.CalendarButton('Data', size=size_button,
                    format='%d/%m/%Y', target='-IN_DATAMODIFICACAO_SENHA-')],
                [sg.Text('Observações:', size=size_text), sg.Input('',
                    size=(size_input), key='-IN_OBSERVACOES_SENHA-')],
                [sg.Button('Salvar', size=size_button, bind_return_key=True),
                    sg.Button('Limpar', size=size_button),
                    sg.Button('Cancelar', size=size_button)]
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
        self.opcao = opcao

    def start(self):
        while True:
            event, values = self.window.read()
            
            if event == sg.WINDOW_CLOSED:
                break

            if event == 'Cancelar':
                if sg.popup_yes_no('Você deseja realmente cancelar?',
                                    'Alguns dados seram perdidos.') == 'Yes':
                    break

            if self.opcao == 'NOVO':
                if event == 'Salvar':
                    titulo = values['-IN_TITULO_SENHA-']
                    login = values['-IN_LOGIN_SENHA-']
                    senha = values['-IN_SENHA_SENHA-']
                    url = values['-IN_URL_SENHA-']
                    data_modificacao = values['-IN_DATAMODIFICACAO_SENHA-']
                    observacoes = values['-IN_OBSERVACOES_SENHA-']

                    values_inputs = [
                        titulo != '',
                        login != '',
                        senha != '',
                    ]

                    if self.verificar_campos_vazios(values_inputs):
                        nova_senha = snc.SenhaController()
                        ret = nova_senha.salvar_senha(titulo=titulo,
                            login=login, senha=senha, url=url,
                            data_modificacao=data_modificacao,
                            observacoes=observacoes)
                        if ret is not None:
                            sg.popup_ok('Senha salva com sucesso',
                                title='Sucesso', auto_close=True,
                                auto_close_duration=3)
                        else:
                            sg.popup_error('Erro ao salvar senha.',
                                title='Erro', auto_close=True,
                                auto_close_duration=3)
                    else:
                        sg.popup_ok('Preencha os campos obrigatórios',
                            'Aviso!', auto_close=True, auto_close_duration=3)

        self.window.close()
    
    def verificar_campos_vazios(self, campos: list[str,]) -> bool:
        if all(campos):
            return True
        return False


if __name__ == '__main__':
    senha_view = SenhaView(opcao='ALTERAR')

    senha_view.start()
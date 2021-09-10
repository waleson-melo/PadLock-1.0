import src.model.SenhaModel as snm


class SenhaController:

    def __init__(self):
        pass

    def salvar_senha(self, titulo='', login='', senha='', url='',
            data_modificacao='', observacoes=''):
        nova_senha = snm.SenhaModel(titulo=titulo, login=login,
            senha=senha, url=url, data_modificacao=data_modificacao,
            observacoes=observacoes)
        return nova_senha.salvar_senha()

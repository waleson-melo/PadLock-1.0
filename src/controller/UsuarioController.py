import src.model.UsuarioModel as usm


class UsuarioController:

    def __init__(self):
        pass

    def pegar_dados(self):
        usuariom = usm.UsuarioModel()
        return usuariom.pegar_dados()
    
    def salvar_usuario(self, codigo=1, login='admin', senha='admin'):
        usuariom = usm.UsuarioModel(codigo=codigo, login=login, senha=senha)
        return usuariom.salvar_usuario()

import src.model.UsuarioModel as usm


class UsuarioController:

    def __init__(self):
        pass

    def pegar_dados(self):
        usuariom = usm.UsuarioModel()
        return usuariom.pegar_dados()

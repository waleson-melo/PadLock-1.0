import src.model.LoginModel as lgm
import src.view.DashboardView as dsv


class LoginController:

    def __init__(self):
        pass
    
    def validar_usuario(self, login: str, senha: str):
        valid = lgm.LoginModel(login=login, senha=senha)

        return valid.validar_usuario()
    
    def start_dashboard(self):
        dashboard = dsv.DashboardView()
        dashboard.start()

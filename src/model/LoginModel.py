import src.util.ConnectionDB as conn

class LoginModel:

    def __init__(self, login: str, senha: str):
        self.login = login
        self.senha = senha

    @property
    def login(self):
        return self.__login
    
    @property
    def senha(self):
        return self.__senha
    
    @login.setter
    def login(self, value):
        if value is None:
            raise ValueError('Login nao pode ser None')
        
        self.__login = value.strip()

    @senha.setter
    def senha(self, value):
        if value is None:
            raise ValueError('Senha nao pode ser None')
        
        self.__senha = value.strip()


if __name__ == '__main__':
    log = LoginModel(login='None', senha='admin')

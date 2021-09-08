import src.util.ConnectionDB as conn

class LoginModel(conn.ConnectionDB):

    def __init__(self, login: str, senha: str):
        super().__init__()
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

    def validar_usuario(self):
        self.connect_database()

        sql = """
            SELECT * FROM usuario WHERE nome = ? AND senha = ?
        """
        dados = self.conn.execute(sql, (self.login, self.senha)).fetchone()

        self.desconnect_db()

        if dados is not None:
            return True
        else:
            return False

if __name__ == '__main__':
    log = LoginModel(login='None', senha='admin')

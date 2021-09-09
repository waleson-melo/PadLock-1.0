import sqlite3
import src.util.ConnectionDB as conn


class UsuarioModel(conn.ConnectionDB):

    def __init__(self, codigo=0, login='', senha=''):
        super().__init__()
        self.codigo = codigo
        self.login = login
        self.senha = senha

    @property
    def codigo(self):
        return self.__codigo

    @property
    def login(self):
        return self.__login
    
    @property
    def senha(self):
        return self.__senha
    
    @codigo.setter
    def codigo(self, value):
        if value is None:
            raise ValueError('Codigo nao pode ser None')

        self.__codigo = int(value)

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

    def pegar_dados(self):
        self.connect_database()

        sql = """
            SELECT codigo, nome, senha FROM usuario
        """
        dados = self.conn.execute(sql).fetchone()

        self.desconnect_db()
        return dados

    def salvar_usuario(self):
        try:
            self.connect_database()

            sql = """
                UPDATE usuario SET nome = ?, senha = ? WHERE codigo = ?;
            """
            dados = self.conn.execute(sql, (self.login, self.senha,
                self.codigo))

            self.desconnect_db()

            return True
        except sqlite3.Error as e:
            print('erro ao alterar usuario. ', e)
            return False
        
if __name__ == '__main__':
    usm = UsuarioModel()
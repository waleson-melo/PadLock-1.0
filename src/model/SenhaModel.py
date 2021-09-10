import sqlite3
import src.util.ConnectionDB as conn


class SenhaModel(conn.ConnectionDB):

    def __init__(self, titulo='', login='', senha='', url='',
            data_modificacao='', observacoes='', codigo=1):
        self.codigo = codigo
        self.titulo = titulo
        self.login = login
        self.senha = senha
        self.url = url
        self.data_modificacao = data_modificacao
        self.observacoes = observacoes

    @property
    def codigo(self):
        return self.__codigo

    @property
    def titulo(self):
        return self.__titulo
    
    @property
    def login(self):
        return self.__login
    
    @property
    def senha(self):
        return self.__senha

    @property
    def url(self):
        return self.__url
    
    @property
    def data_modificacao(self):
        return self.__data_modificacao
    
    @property
    def observacoes(self):
        return self.__observacoes

    @codigo.setter
    def codigo(self, value):
        if value is None:
            raise ValueError('codigo nao pode ser None')
        
        self.__codigo = int(value)

    @titulo.setter
    def titulo(self, value):
        if value is None:
            raise ValueError('titulo nao pode ser None')
        
        self.__titulo = value.strip().upper()
    
    @login.setter
    def login(self, value):
        if value is None:
            raise ValueError('login nao pode ser None')
        
        self.__login = value.strip()
    
    @senha.setter
    def senha(self, value):
        if value is None:
            raise ValueError('senha nao pode ser None')
        
        self.__senha = value

    @url.setter
    def url(self, value):
        if value is None:
            raise ValueError('url nao pode ser None')
        
        self.__url = value.strip()

    @data_modificacao.setter
    def data_modificacao(self, value):
        if value is None:
            raise ValueError('data_modificacao nao pode ser None')
        
        self.__data_modificacao = value.strip()
    
    @observacoes.setter
    def observacoes(self, value):
        if value is None:
            raise ValueError('observacoes nao pode ser None')
        
        self.__observacoes = value.strip().upper()

    def salvar_senha(self):
        try:
            self.connect_database()

            sql = """
                INSERT INTO senha
                    (titulo, login, senha, url, data, observacoes)
                VALUES (?, ?, ?, ?, ?, ?)
            """
            codigo = self.conn.execute(sql, (self.titulo, self.login,
                self.senha, self.url, self.data_modificacao,
                self.observacoes)).lastrowid

            self.desconnect_db()

            return codigo
        except sqlite3.Error as e:
            print('erro ao salvar senha, ', e)

        return None

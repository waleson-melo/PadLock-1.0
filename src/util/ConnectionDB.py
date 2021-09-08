from sqlite3 import connect
from os import path, makedirs

class ConnectionDB:
    
    def __init__(self):
        self.create_tables()

    def connect_database(self):
        if not path.isdir('.programas/senhas/database'):
            makedirs('.programas/senhas/database')
        self.conn = connect('.programas/senhas/database/dbsistema.db')
        self.cursor = self.conn.cursor()

    def desconnect_db(self):
        self.conn.commit()
        self.cursor.close()

    def create_tables(self):
        self.connect_database()

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS "senha" (
                "codigo"	INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
                "titulo"	TEXT NOT NULL UNIQUE,
                "login"	TEXT NOT NULL,
                "senha"	TEXT NOT NULL,
                "url" TEXT,
                "data" TEXT,
                "observacoes" TEXT
            );
        """)
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS "usuario" (
                "codigo"	INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
                "nome"	TEXT NOT NULL,
                "senha"	TEXT NOT NULL
            );
        """)

        # se a quantidade for 0 é adcionado um usuario padrao
        quant_usuario = self.cursor.execute("""
            SELECT count(1) FROM usuario
        """).fetchall()
        quant_usuario = list(quant_usuario)[0]
        if quant_usuario[0] == 0:
            self.cursor.execute("""
                INSERT INTO usuario (nome, senha) 
                VALUES ('admin', 'admin')
            """)

        self.desconnect_db()

if __name__ == '__main__':
    con = ConnectionDB()

    con.connect_database()

    dados = con.cursor.execute("""
        SELECT nome FROM usuario WHERE nome = ? AND senha = ?
    """, ('admin', 'admin')).fetchone()

    print(dados)

    if dados is not None:
        print('encontrado')
    else:
        print('nao encontrado')

    con.desconnect_db()
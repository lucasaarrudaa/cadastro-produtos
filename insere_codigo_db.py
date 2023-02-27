import mysql.connector
from mysql.connector import Error

def conectar():
    try:
        global con
        con = mysql.connector.connect(host='localhost', user='root', password='884316', database='materiais')
    except Error as erro:
        print('Erro de conexão {}'.format(erro))
    return conectar

def insere(sql):
    try:
        global cursor
        conectar()
        altera_quantidade = sql
        cursor = con.cursor()
        cursor.execute(altera_quantidade)
        con.commit()
        print("Quantidade inserida com sucesso")
    except Error as erro:
        print("Falha ao inserir dados na tabela: {}".format(erro))
    finally:
        if (con.is_connected()):
            con.close()
            cursor.close()
    return insere

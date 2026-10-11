import psycopg

def obter_conexao():
    return psycopg.connect(
        host="200.18.128.54",
        database="aula",
        user="aula",
        password="aula"
    )

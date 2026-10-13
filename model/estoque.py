from connect import obter_conexao

def listar_todas():
    with obter_conexao() as conn:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM pedrosilva.estoque ORDER BY id")
            # fetchall() traz todas as linhas registradas no banco
            return cursor.fetchall()

def inserir(rua, numero, bairro, cidade, estado, cep):
    with obter_conexao() as conn:
        with conn.cursor() as cursor:
            # O %s previne ataques de SQL Injection
            cursor.execute(
                "INSERT INTO pedrosilva.estoque (rua, numero, bairro, cidade, estado, cep) VALUES (%s, %s, %s, %s, %s, %s)",
                (rua, numero, bairro, cidade, estado, cep)
            )
            #commit é como se fosse dar enter
            conn.commit()

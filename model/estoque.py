from conexao import obter_conexao

def listar_todas():
    with obter_conexao() as conn:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM pedrosilva.estoque ORDER BY id")
            # fetchall() traz todas as linhas registradas no banco
            return cursor.fetchall()

def inserir(nome, quantidade, preco):
    with obter_conexao() as conn:
        with conn.cursor() as cursor:
            # O %s previne ataques de SQL Injection
            cursor.execute(
                "INSERT INTO pedrosilva.estoque (nome, quantidade, preco) VALUES (%s, %s, %s)",
                (nome, quantidade, preco)
            )
            # Como alteramos o banco, precisamos dar commit
            conn.commit()

import sqlite3 

conn = sqlite3.connect('exemplo.db')

#criar um cursor para executar comandos SQL
cursor = conn.cursor()

############# CRIAR TABELA.
cursor.execute(
    '''
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY,
        nome TEXT,
        idade INTEGER
    )
    '''
)

############# ADICIONAR LINHAS
cursor.execute(
    "INSERT INTO usuarios ( nome, idade )  VALUES (?,?)",
    ('Luiz', 25)
)

cursor.execute(
    "INSERT INTO usuarios ( nome, idade )  VALUES (?,?)",
    ('Junio', 20)
)

conn.commit()


############# FAZER QUERY CONSULTA
cursor.execute(
    "SELECT * FROM usuarios"
)

for registro in cursor.fetchall():
    print(registro)

############# ATUALIZAR UMA LINHA
cursor.execute(
    "UPDATE usuarios SET idade = ? WHERE nome = ?",
    ( 30, 'Junio' )
)
    
conn.commit()

############# DELETAR UMA LINHA
cursor.execute(
    "DELETE FROM usuarios WHERE nome = ?",
    ('Junio',)
)
    
conn.commit()

############# FAZER QUERY CONSULTA
cursor.execute(
    "SELECT * FROM usuarios"
)

for registro in cursor.fetchall():
    print(registro)

cursor.close()
conn.close()
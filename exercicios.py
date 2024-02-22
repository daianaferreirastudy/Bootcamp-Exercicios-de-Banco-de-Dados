import sqlite3

banco = sqlite3.connect('database.db')

cursor = banco.cursor()

"""
1. Crie uma tabela chamada "alunos" com os seguintes campos: id
(inteiro), nome (texto), idade (inteiro) e curso (texto).
"""
cursor.execute("CREATE TABLE alunos (id INT, nome VARCHAR(100),idade INT,curso VARCHAR(100))")


"""
2. Insira pelo menos 5 registros de alunos na tabela que você criou no
exercício anterior.
"""
cursor.execute("INSERT INTO alunos VALUES (1,'Maria',40,'Gestão de Empresas')")
cursor.execute("INSERT INTO alunos VALUES (2,'Pedro',29,'Marketing')")
cursor.execute("INSERT INTO alunos VALUES (3,'Joana',21,'Sistemas de Informação')")
cursor.execute("INSERT INTO alunos VALUES (4,'Leila',26,'Educação Fisica')")
cursor.execute("INSERT INTO alunos VALUES (5,'Daniela',23,'Comercio Exterior')")
cursor.execute("INSERT INTO alunos VALUES (6,'Larissa',19,'Engenharia')")
cursor.execute("INSERT INTO alunos VALUES (7,'Fabiola',22,'Engenharia')")
cursor.execute("INSERT INTO alunos VALUES (8,'Josiana',30,'Engenharia')")


"""
3. Consultas Básicas
Escreva consultas SQL para realizar as seguintes tarefas:
a) Selecionar todos os registros da tabela "alunos".
b) Selecionar o nome e a idade dos alunos com mais de 20 anos.
c) Selecionar os alunos do curso de "Engenharia" em ordem
alfabética.
d) Contar o número total de alunos na tabela
"""
#a)
cursor.execute("SELECT * FROM alunos")
print(cursor.fetchall())

#b)
cursor.execute('SELECT nome,idade FROM alunos GROUP BY nome HAVING idade>20')
print(cursor.fetchall())

#c)
cursor.execute('SELECT nome,curso FROM alunos GROUP BY nome HAVING curso="Engenharia"')
#print(cursor.fetchall())

#d)
cursor.execute('SELECT Count(*) FROM alunos')
print(cursor.fetchall())


"""
4. Atualização e Remoção
a) Atualize a idade de um aluno específico na tabela.
b) Remova um aluno pelo seu ID.
"""
#a)
cursor.execute('UPDATE alunos SET idade=35 WHERE id=1')
print(cursor.fetchall())

#b)
cursor.execute('DELETE FROM alunos where id=2')
print(cursor.fetchall())


"""
5. Criar uma Tabela e Inserir Dados
Crie uma tabela chamada "clientes" com os campos: id (chave
primária), nome (texto), idade (inteiro) e saldo (float). Insira alguns
registros de clientes na tabela.
"""
cursor.execute("CREATE TABLE clientes (id INTEGER PRIMARY KEY, nome VARCHAR(100),idade INT,saldo float)")

cursor.execute("INSERT INTO clientes VALUES (1,'Pedro',48,500.28)")
cursor.execute("INSERT INTO clientes VALUES (2,'Joaquim',18,121.02)")
cursor.execute("INSERT INTO clientes VALUES (3,'Manuella',33,5012.89)")
cursor.execute("INSERT INTO clientes VALUES (4,'Daniel',21,936.41)")
cursor.execute("INSERT INTO clientes VALUES (5,'Flavia',30,20.00)")
cursor.execute("INSERT INTO clientes VALUES (6,'Vanessa',32,9011.89)")
cursor.execute("INSERT INTO clientes VALUES (7,'Miguel',22,509.56)")
cursor.execute("INSERT INTO clientes VALUES (8,'Luiz',30,1003.12)")

cursor.execute("SELECT * FROM clientes")
print(cursor.fetchall())



"""
6. Consultas e Funções Agregadas
Escreva consultas SQL para realizar as seguintes tarefas:
a) Selecione o nome e a idade dos clientes com idade superior a
30 anos.
b) Calcule o saldo médio dos clientes.
c) Encontre o cliente com o saldo máximo.
d) Conte quantos clientes têm saldo acima de 1000.
"""
#a)
cursor.execute('SELECT nome,idade FROM clientes GROUP BY nome HAVING idade>30')
print(cursor.fetchall())

#b)
cursor.execute('SELECT AVG(saldo) FROM clientes')
print(cursor.fetchall())

#c)
cursor.execute('SELECT nome,MAX(saldo) FROM clientes')
print(cursor.fetchall())

#d)
cursor.execute('SELECT nome,saldo FROM clientes GROUP BY nome HAVING saldo>1000')
print(cursor.fetchall())



"""
7. Atualização e Remoção com Condições
a) Atualize o saldo de um cliente específico.
b) Remova um cliente pelo seu ID
"""
#a)
cursor.execute('UPDATE clientes SET saldo=969.89 WHERE id=5')
print(cursor.fetchall())

#b)
cursor.execute('DELETE FROM clientes where id=7')
print(cursor.fetchall())


cursor.execute("SELECT * FROM clientes")
print(cursor.fetchall())


"""
8. Junção de Tabelas
Crie uma segunda tabela chamada "compras" com os campos: id
(chave primária), cliente_id (chave estrangeira referenciando o id
da tabela "clientes"), produto (texto) e valor (real). Insira algumas
compras associadas a clientes existentes na tabela "clientes".
Escreva uma consulta para exibir o nome do cliente, o produto e o
valor de cada compra.
"""

cursor.execute("CREATE TABLE compras (id INTEGER PRIMARY KEY,clientes_id INTERGER,produto VARCHAR(100),valor REAL, FOREIGN KEY(clientes_id) REFERENCES clientes(id)")


cursor.execute("INSERT INTO compras VALUES (10,'Camisa Regata',59.90)")
cursor.execute("INSERT INTO compras VALUES (22,'Cinto Feminino',21.89)")
cursor.execute("INSERT INTO compras VALUES (34,'Mochila',129.69)")
cursor.execute("INSERT INTO compras VALUES (56,'Calça',105.85)")
cursor.execute("INSERT INTO compras VALUES (14,'Cardigam',66.39)")
cursor.execute("INSERT INTO compras VALUES (5,'camisa Polo',89.99)")
cursor.execute("INSERT INTO compras VALUES (2,'Bermuda',79.89)")
cursor.execute("INSERT INTO compras VALUES (7,'Jaqueta Jeans',209.89)")



cursor.execute("SELECT nome,produto,valor FROM clientes JOIN compras ON cliente_id = 2  ORDER BY nome, produto")
print(cursor.fetchall())

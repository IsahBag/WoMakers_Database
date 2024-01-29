"""EXERCÍCIOS:
1. Crie uma tabela chamada "alunos" com os seguintes campos: id(inteiro), nome(texto), idade(inteiro) e curso(texto).
2. Insira pelo menos 5 registros de alunos na tabela que você criou no exercício anterior.
3. Consultas Básicas - Escreva consultas SQL para realizar as seguintes tarefas:
 a) Selecionar todos os registros da tabela "alunos".
 b) Selecionar o nome e a idade dos alunos com mais de 20anos.
 c) Selecionar os alunos do curso de "Engenharia" em ordem alfabética.
 d) Contar o número total de alunos na tabela.
4. Atualização e Remoção:
 a) Atualize a idade de um aluno específico na tabela.
 b) Remova um aluno pelo seu ID
5. Criar uma Tabela e Inserir Dados:
 Crie uma tabela chamada "clientes" com os campos: id (chave primária), nome (texto), idade (inteiro) e saldo (float). Insira alguns registros
 de clientes na tabela
6. Consultas e Funções Agregadas
 Escreva consultas SQL para realizar as seguintes tarefas:
 a) Selecione o nome e a idade dos clientes com idade superior a 30 anos.
 b) Calcule o saldo médio dos clientes. 
 c) Encontre o cliente com o saldo máximo.
 d) Conte quantos clientes têm saldo acima de 1000.
7. Atualização e Remoção com Condições:
 a) Atualize osaldo de um cliente específico.
 b) Remova um cliente pelo seu ID.
8. Junção de Tabelas:
 Crie uma segunda tabela chamada "compras" com os campos: id(chaveprimária), cliente_id(chave estrangeira referenciando o id da tabela "clientes"),
 produto(texto) e valor(real). Insira algumas compras associadas a clientes existentes na tabela "clientes". Escreva uma consulta para exibir o 
 nome do cliente, o produto e o valor de cada compra."""

import sqlite3

conexao = sqlite3.connect('banco-teste')
cursor = conexao.cursor()

#1. Criando tabela "alunos:"
#cursor.execute('CREATE TABLE alunos(id INT, nome VARCHAR(70), idade INT, curso VARCHAR(100))')

#2. Inserindo 5 registro na tabela "alunos"
#cursor.execute('INSERT INTO alunos(id,nome,idade,curso) VALUES(1,"Aline",19,"SQL")')
#cursor.execute('INSERT INTO alunos(id,nome,idade,curso) VALUES(2,"Bruna",21,"Python")')
#cursor.execute('INSERT INTO alunos(id,nome,idade,curso) VALUES(3,"César",18,"C#")')
#cursor.execute('INSERT INTO alunos(id,nome,idade,curso) VALUES(4,"Danilo",17,"JavaScript")')
#cursor.execute('INSERT INTO alunos(id,nome,idade,curso) VALUES(5,"Eduardo",28,"Java")')
#cursor.execute('INSERT INTO alunos(id,nome,idade,curso) VALUES(4,"Ana",19,"Engenharia")')
#cursor.execute('INSERT INTO alunos(id,nome,idade,curso) VALUES(5,"Larissa",27,"Engenharia")')

#3. Realizando consultas:
#alunos = cursor.execute('SELECT * FROM alunos')   # selecionando todos os registros
#for aluno in alunos:
#    print (aluno)
#alunos = cursor.execute('SELECT nome,idade FROM alunos WHERE idade > 20')   # selecionando os com mais de 20 anos
#for aluno in alunos:
#    print (aluno)
#alunos = cursor.execute('SELECT nome FROM alunos WHERE curso = "Engenharia" ORDER BY nome')  # selecionando os alunos de Engenharia em ordem alfabética
#for aluno in alunos:
#    print (aluno)
#alunos = cursor.execute('SELECT COUNT(*) FROM alunos')  # selecionando os alunos de Engenharia em ordem alfabética   # conta o total de alunos
#for aluno in alunos:
#    print (aluno)

#4. Atualizando e removendo alunos:
#cursor.execute('UPDATE alunos SET idade="20" WHERE id="1"')    # atualiza idade
#cursor.execute('DELETE FROM alunos where id ="2"')   # remove dado pelo ID

#5. Criando tabela "clientes:"
#cursor.execute('CREATE TABLE clientes(id INT, nome VARCHAR(70), idade INT, saldo FLOAT, PRIMARY KEY(id))')   # criando tabela
#cursor.execute('INSERT INTO clientes(id,nome,idade,saldo) VALUES(1,"Francisco",27,132.45)')   # adicionando registros
#cursor.execute('INSERT INTO clientes(id,nome,idade,saldo) VALUES(2,"Alberto",67,12675.89)')
#cursor.execute('INSERT INTO clientes(id,nome,idade,saldo) VALUES(3,"Maria",45,98653.54)')
#cursor.execute('INSERT INTO clientes(id,nome,idade,saldo) VALUES(4,"Patrícia",58,11.45)')
#cursor.execute('INSERT INTO clientes(id,nome,idade,saldo) VALUES(5,"Mauro",42,43765.98)')
#cursor.execute('INSERT INTO clientes(id,nome,idade,saldo) VALUES(4,"Pedro",37,4589.76)')

#6. Consultas:
#clientes = cursor.execute('SELECT nome,idade FROM clientes WHERE idade > 30')  # selecionando clientes 30+
#for cliente in clientes:
#    print(cliente)
#clientes = cursor.execute('SELECT AVG(saldo) FROM clientes')  # calculando a renda média
#for cliente in clientes:
#    print(cliente)
#clientes = cursor.execute('SELECT nome, MAX(saldo) FROM clientes')  # selecionando clientes 30+
#for cliente in clientes:
#    print(cliente)
#clientes = cursor.execute('SELECT COUNT(*) FROM clientes WHERE saldo > 1000')  # contando clientes com pelo menos R$1000,00 de saldo
#for cliente in clientes:
#    print(cliente)

#7.Atualizando e Removendo alunos:
#cursor.execute('UPDATE clientes SET saldo="13675.43" WHERE id="5"')    # atualiza idade
#cursor.execute('DELETE FROM clientes where id ="4"')   # remove dado pelo ID

#8.Junção de tabelas:
#cursor.execute('CREATE TABLE compras(id INT PRIMARY KEY, cliente_id INT, produto VARCHAR(70), valor FLOAT, CONSTRAINT fk_clientescompras FOREIGN KEY(id) REFERENCES clientes(id))')   # criando a tabela "vendas" refereciando a tabela "clientes"
#cursor.execute('INSERT INTO compras(id,cliente_id,produto,valor) VALUES(1,1,"fone de ouvido",78.90)')   # adicionando registros
#cursor.execute('INSERT INTO compras(id,cliente_id,produto,valor) VALUES(2,2,"geladeira",2399.90)')
#cursor.execute('INSERT INTO compras(id,cliente_id,produto,valor) VALUES(3,3,"fogão",999.99)')
#cursor.execute('INSERT INTO compras(id,cliente_id,produto,valor) VALUES(4,5,"cadeira",65.90)')
#cursor.execute('INSERT INTO compras(id,cliente_id,produto,valor) VALUES(5,4,"televisão",4399.90)')
#clientes = cursor.execute('SELECT nome, produto, valor FROM compras INNER JOIN clientes ON compras.id = clientes.id')   # consulta pelo nome, produto e valor
#for cliente in clientes:
#    print(cliente)

conexao.commit()
conexao.close()
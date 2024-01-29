
#DDL: CREATE/ALTER/DROP
#DML: INSERT/SELECT/UPDATE/DELETE

import sqlite3

conexao = sqlite3.connect('banco-teste')
cursor = conexao.cursor()

#criando tabela:
#cursor.execute('CREATE TABLE usuarios(id INT, nome VARCHAR(100), endereco VARCHAR(100), email VARCHAR(100))')   
#cursor.execute('CREATE TABLE gerentes(id INT, nome VARCHAR(100), endereco VARCHAR(100), email VARCHAR(100))') 
  
#cursor.execute('DROP TABLE produtos')       # exclui tabela

#cursor.execute('ALTER TABLE usuarios RENAME TO usuario')      # renomeia a tabela

#adicionar coluna:
#cursor.execute('ALTER TABLE usuario ADD COLUMN telefoni INT')     

#cursor.execute('ALTER TABLE usuario RENAME COLUMN telefoni TO telefone')       # renomeia coluna

# adicionando dados:
#cursor.execute('INSERT INTO usuario(id,nome,endereco,email,telefone) VALUES(1,"Isadora","França","isa@email.com",123456)')  
#cursor.execute('INSERT INTO usuario(id,nome,endereco,email,telefone) VALUES(1,"Matheus","Brasil","ma@email.com",234556)')
#cursor.execute('INSERT INTO usuario(id,nome,endereco,email,telefone) VALUES(1,"Flávia","Itália","fla@email.com",345678)')
#cursor.execute('INSERT INTO gerentes(id,nome,endereco,email) VALUES(3,"Luíza","Brasil","lu@email.com")')

#cursor.execute('DELETE FROM usuario where nome ="Isadora"')     # exclui dados

#cursor.execute('UPDATE usuario SET id="3" WHERE nome="Bruno"')     # altera dado
    
#visualizando dados no python:
    #dados = cursor.execute('SELECT nome,endereco FROM usuario WHERE id = 1') 
    #for usuario in dados:
    #    print (usuario)

#ordenando dados
#dados = cursor.execute('SELECT * FROM usuario ORDER BY nome DESC')    # para ordem decrescente adicionar o DESC no final
#for usuario in dados:
#    print (usuario)

#distinguindo:
#dados = cursor.execute('SELECT DISTINCT * FROM usuario LIMIT 3')  # o LIMIT limita o número de dados retornados
#for usuario in dados:
#    print (usuario)

#agrupando informações:
#dados = cursor.execute('SELECT nome,id FROM usuario GROUP BY nome HAVING id > 1')   # depois de 'GROUP BY' utiliza-se o HAVING ao invés de WHERE
#for usuario in dados:
#    print (usuario)

#agrupando informações em mais de uma tabela:
#INNER JOIN:
#dados = cursor.execute('SELECT * FROM usuario INNER JOIN gerentes ON usuario.id = gerentes.id')  #retorna as informações de acordo com a condição 
#for usuario in dados:
#    print (usuario)
#LEFT JOIN:
#dados = cursor.execute('SELECT * FROM usuario LEFT JOIN gerentes ON usuario.nome = gerentes.nome')  #agrupa os dados na tabela à esquerda
#for usuario in dados:
#    print (usuario)
#RIGHT JOIN:
#dados = cursor.execute('SELECT * FROM usuario RIGHT JOIN gerentes ON usuario.nome = gerentes.nome')  #ragrupa os dados na tabela à direita
#for usuario in dados:
#    print (usuario)
#FULL JOIN:
#dados = cursor.execute('SELECT * FROM usuario FULL JOIN gerentes ON usuario.nome = gerentes.nome')  #retorna todas as correspondências de ambas tabelas 
#for usuario in dados:
#    print (usuario)

#subconsultas:
#dados = cursor.execute('SELECT * FROM usuario WHERE nome IN(SELECT nome FROM gerentes)')    #consultas SQL que são aninhadas dentro da consulta principal
#for usuario in dados:
#    print (usuario)


conexao.commit()
conexao.close()
# Importar a biblioteca
import mysql.connector

# Conexão com o MySQL
conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Luanmilagre.123",
    database="teste"
)
cursor = conexao.cursor()

#Produto que será excluído
nome_produto = "chocolate"

# Comando SQL para deletar dados
comando = "DELETE FROM vendas WHERE nome_produto = %s"

# Dados que serão inseridos no comando
dados = (nome_produto)

# Executa o comando
cursor.execute(comando, dados)
conexao.commit()  # Confirma as alterações no banco de dados

# Fecha a conexão
cursor.close()
conexao.close()

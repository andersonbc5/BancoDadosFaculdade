import sqlite3 as conector

def conectar_banco(nome_banco):
    conexao = conector.connect(nome_banco)
    return conexao

def criar_tabela(conexao):
    cursor = conexao.cursor()
    
    try:
        cursor.execute('''CREATE TABLE IF NOT EXISTS Produtos (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nome TEXT NOT NULL,
                        preco REAL NOT NULL,
                        estoque INTEGER NOT NULL);''')
        
        cursor.execute('''CREATE TABLE IF NOT EXISTS Clientes (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nome TEXT NOT NULL,
                        email TEXT NOT NULL);''')
        
        cursor.execute('''CREATE TABLE IF NOT EXISTS Pedidos (
                      id INTEGER PRIMARY KEY AUTOINCREMENT,
                      cliente_id INTEGER NOT NULL,
                      produto_id INTEGER NOT NULL,
                      quantidade INTEGER NOT NULL,
                      data_pedido TEXT NOT NULL,
                      FOREIGN KEY (cliente_id) REFERENCES Clientes(id),
                      FOREIGN KEY (produto_id) REFERENCES Produtos(id))''')
        
        print('Tabelas criadas')
        conexao.commit()
    
    except conector.IntegrityError as e:
        print(f"Erro de integridade: {e}")
        conexao.rollback()
        return False
        
    except conector.OperationalError as e:
        print(f"Erro operacional (banco travado?): {e}")
        conexao.rollback()
        return False
        
    except Exception as e:
        print(f"Erro inesperado: {e}")
        conexao.rollback()
        return False
        
    finally:
        cursor.close()

def inserir_dados(conexao):
    cursor = conexao.cursor()
    
    try:
        produtos = [('Notebook', 2999.99, 10),
                    ('Smartphone', 1999.99, 20),
                    ('Tablet', 999.99, 30)]
       
        clientes = [('Alice', 'alice@example.com'),
                    ('Bob', 'bob@example.com'),
                    ('Charlie', 'charlie@example.com')]
       
        pedidos = [(1, 1, 2, '2023-06-15'),
                   (2, 2, 1, '2023-06-16'),
                   (3, 3, 3, '2023-06-17')]
       
        cursor.executemany('INSERT INTO Produtos (nome, preco, estoque) VALUES (?, ?, ?)', produtos)
        cursor.executemany('INSERT INTO Clientes (nome, email) VALUES (?, ?)', clientes)
        cursor.executemany('INSERT INTO Pedidos (cliente_id, produto_id, quantidade, data_pedido) VALUES (?, ?, ?, ?)', pedidos)
       
        conexao.commit()
        print("Dados inseridos com sucesso!")
    
    except conector.IntegrityError as e:
        print(f"Erro de integridade (chave estrangeira/primária): {e}")
        conexao.rollback()
        return False
        
    except conector.OperationalError as e:
        print(f"Erro operacional (banco travado?): {e}")
        conexao.rollback()
        return False
        
    except Exception as e:
        print(f"Erro inesperado ao inserir dados: {e}")
        conexao.rollback()
        return False
        
    finally:
        cursor.close()

if __name__ == '__main__':
    
    try:
        conexao = conectar_banco('ecommerce.db')
        criar_tabela(conexao)
        inserir_dados(conexao)
    
    except Exception as e:
        print(f"Erro na conexão com o banco: {e}")
        
    finally:
        if 'conexao' in locals():
            conexao.close()
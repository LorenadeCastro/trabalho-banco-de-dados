import sqlite3

# Conectar ao banco de dados (ou criar se não existir)
conn = sqlite3.connect('loja.db')
cursor = conn.cursor()

# Criar tabelas
cursor.execute('''
CREATE TABLE Clientes (
    id_cliente INTEGER PRIMARY KEY,
    nome TEXT NOT NULL,
    email TEXT NOT NULL
)
''')

cursor.execute('''
CREATE TABLE Pedidos (
    id_pedido INTEGER PRIMARY KEY,
    id_cliente INTEGER,
    data_pedido TEXT NOT NULL,
    valor_total REAL NOT NULL,
    FOREIGN KEY (id_cliente) REFERENCES Clientes(id_cliente)
)
''')

cursor.execute('''
CREATE TABLE Produtos (
    id_produto INTEGER PRIMARY KEY,
    nome_produto TEXT NOT NULL,
    preco REAL NOT NULL
)
''')

cursor.execute('''
CREATE TABLE ItensPedido (
    id_item INTEGER PRIMARY KEY,
    id_pedido INTEGER,
    id_produto INTEGER,
    quantidade INTEGER NOT NULL,
    preco REAL NOT NULL,
    FOREIGN KEY (id_pedido) REFERENCES Pedidos(id_pedido),
    FOREIGN KEY (id_produto) REFERENCES Produtos(id_produto)
)
''')

# Confirmar as alterações
conn.commit()


# Inserir dados na tabela Clientes
cursor.execute("INSERT INTO Clientes (nome, email) VALUES ('João Silva', 'joao@exemplo.com')")
cursor.execute("INSERT INTO Clientes (nome, email) VALUES ('Maria Souza', 'maria@exemplo.com')")

# Inserir dados na tabela Produtos
cursor.execute("INSERT INTO Produtos (nome_produto, preco) VALUES ('Notebook', 3000.00)")
cursor.execute("INSERT INTO Produtos (nome_produto, preco) VALUES ('Mouse', 50.00)")

# Inserir dados na tabela Pedidos
cursor.execute("INSERT INTO Pedidos (id_cliente, data_pedido, valor_total) VALUES (1, '2023-05-01', 3050.00)")
cursor.execute("INSERT INTO Pedidos (id_cliente, data_pedido, valor_total) VALUES (2, '2023-05-02', 50.00)")

# Inserir dados na tabela ItensPedido
cursor.execute("INSERT INTO ItensPedido (id_pedido, id_produto, quantidade, preco) VALUES (1, 1, 1, 3000.00)")
cursor.execute("INSERT INTO ItensPedido (id_pedido, id_produto, quantidade, preco) VALUES (1, 2, 1, 50.00)")
cursor.execute("INSERT INTO ItensPedido (id_pedido, id_produto, quantidade, preco) VALUES (2, 2, 1, 50.00)")

# Confirmar as alterações
conn.commit()

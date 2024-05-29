# trabalho-banco-de-dados
Trabalho desenvolvido para o curso de Introdução a Programação da Proz - cursos técnicos.

BANCO DE DADOS:

Esquema do Banco de Dados

Tabela Clientes:

    id_cliente (INTEGER, PRIMARY KEY)
    nome (TEXT)
    email (TEXT)

Tabela Pedidos:

    id_pedido (INTEGER, PRIMARY KEY)
    id_cliente (INTEGER, FOREIGN KEY para Clientes)
    data_pedido (TEXT)
    valor_total (REAL)

Tabela Produtos:

    id_produto (INTEGER, PRIMARY KEY)
    nome_produto (TEXT)
    preco (REAL)

Tabela ItensPedido:

    id_item (INTEGER, PRIMARY KEY)
    id_pedido (INTEGER, FOREIGN KEY para Pedidos)
    id_produto (INTEGER, FOREIGN KEY para Produtos)
    quantidade (INTEGER)
    preco (REAL)

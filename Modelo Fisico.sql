-- Criando as tabelas no banco de dados

CREATE TABLE produtos (
    id_produto INT PRIMARY KEY,
    nome_produto VARCHAR(255),
    categoria VARCHAR(100),
    preco_custo DECIMAL(10, 2),
    preco_venda DECIMAL(10, 2)
);

CREATE TABLE clientes (
    id_cliente INT PRIMARY KEY,
    nome_completo VARCHAR(255),
    cpf VARCHAR(20),
    cidade VARCHAR(100),
    estado CHAR(2)
);

CREATE TABLE vendas (
    id_venda INT PRIMARY KEY,
    data_venda TIMESTAMP,
    id_cliente INT,
    id_produto INT,
    quantidade INT,
    valor_unitario DECIMAL(10, 2),
    montante_total DECIMAL(10, 2),
    -- Relacionando as tabelas
    CONSTRAINT fk_cliente FOREIGN KEY (id_cliente) REFERENCES clientes(id_cliente),
    CONSTRAINT fk_produto FOREIGN KEY (id_produto) REFERENCES produtos(id_produto)
);
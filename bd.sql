CREATE DATABASE  if not exists Ecommerce;
use Ecommerce;

-- Definindo o Cliente
CREATE TABLE Cliente(
	idCliente INT auto_increment PRIMARY KEY,
    Nome VARCHAR(50) not NULL,
    Endereço VARCHAR(50),
	CPF CHAR (11) not NULL,
    CNPJ VARCHAR(18) not NULL,
    ClientType enum('PF', 'PJ') not NULL,
    CONSTRAINT unique_cpf_cliente UNIQUE (CPF),
    CONSTRAINT unique_cnpj_cliente UNIQUE (CNPJ)
    );
DESC Cliente;


-- Definindo o Produto
CREATE TABLE Produto(
	idProduto INT auto_increment PRIMARY KEY,
    categoria VARCHAR(50),
    descrição VARCHAR(50),
	valor FLOAT
);
DESC Produto;


-- Defininfo o Pagamento
CREATE TABLE Pagamento(
	idPagamento INT auto_increment PRIMARY KEY,
    PagoPeloCliente INT,
    cartão VARCHAR(50),
    bandeira VARCHAR(50),
    numero VARCHAR(50),
    CONSTRAINT fk_pagamento_cliente FOREIGN KEY (PagoPeloCliente) REFERENCES Cliente(idCliente)
);
DESC Pagamento;

-- Definindo a Entrega
CREATE TABLE Entrega(
	idEntrega INT auto_increment PRIMARY KEY,
    statusEntrega BOOL,
    codeRastreio VARCHAR(50),
    date_entrega DATE
);
DESC Entrega;

-- Definindo o Pedido
CREATE TABLE Pedido(
	idPedido INT auto_increment PRIMARY KEY,
    statusPedido BOOL DEFAULT FALSE,
    frete FLOAT,
    descrição VARCHAR(50),
    CONSTRAINT fk_entrega FOREIGN KEY (idPedido) REFERENCES Entrega(idEntrega)
);
DESC Pedido;

-- Definindo o Estoque
CREATE TABLE Estoque(
	idEstoque INT auto_increment PRIMARY KEY,
    Local VARCHAR(50)
);
DESC Estoque;

-- Definindo o Estoque
CREATE TABLE EstoqueDeProdutos(
	idProduto INT PRIMARY KEY,
    idEstoqueDeProdutos INT,
    Qntd INT,
    CONSTRAINT fk_estoque FOREIGN KEY (idProduto) REFERENCES Produto(idProduto),
    CONSTRAINT fk_produto_estoque FOREIGN KEY (idEstoqueDeProdutos) REFERENCES Estoque(idEstoque)
);
DESC EstoquedeProdutos;

--  Definindo o Fornecedor
CREATE TABLE Fornecedor(
	idFornecedor INT auto_increment PRIMARY KEY,
    RazãoSocial VARCHAR(50),
    CPF CHAR (11) not NULL,
    CNPJ VARCHAR(18) not NULL,
    FornecedorType enum('PF', 'PJ') not NULL,
    CONSTRAINT unique_cpf_cliente UNIQUE (CPF),
    CONSTRAINT unique_cnpj_cliente UNIQUE (CNPJ)
);
DESC Fornecedor;

-- Definindo o Pedido do Produto
CREATE TABLE PedidoProduto(
	idPedido INT,
    idProduto INT,
    Qntd INT DEFAULT 1,
    CONSTRAINT fk_pedido FOREIGN KEY (idPedido) REFERENCES terceiro_forne(idTerceiro),
    CONSTRAINT fk_produto FOREIGN KEY (idProduto) REFERENCES Produto(idProduto)
);
DESC PedidoProduto;

-- Definindo o Pedido para o Fornecedor
CREATE TABLE PedidoFornecedor(
	idCompraForne INT,
    idPedidoFornecedor INT,
    Qntd INT DEFAULT 1,
    CONSTRAINT fk_pedido_forncedor FOREIGN KEY (idCompraForne) REFERENCES Fornecedor(idFornecedor),
    CONSTRAINT fk_fornecedor_pedido FOREIGN KEY (idPedidoFornecedor) REFERENCES Pedido(idPedido)
);
DESC PedidoFornecedor;

-- Definindo o Produto no Estoque do Fornecedor 
CREATE TABLE EstoqueFornecedor(
	idEstoqueFornecedor INT,
    idProdutoForne INT,
    CONSTRAINT fk_EstoqueFornecedor FOREIGN KEY (idEstoqueFornecedor) REFERENCES Fornecedor(idFornecedor),
    CONSTRAINT fk_produtos_forne FOREIGN KEY (idProdutoForne) REFERENCES Produto(idProduto)
);
DESC EstoqueFornecedor;

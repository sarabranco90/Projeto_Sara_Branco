create database loja

use loja

create table produtos (
id int auto_increment primary key,
nome varchar(255) not null,
descricao text,
preco decimal(10, 2) not null,
categoria varchar(255)
);

create table clientes (
id int auto_increment primary key,
nome varchar(255) not null,
email varchar(255) not null unique,
telefone varchar(20),
endereco text
);

create table pedidos (
id int auto_increment primary key,
cliente_id int,
data_pedido datetime default current_timestamp,
estado varchar(50),
foreign key (cliente_id) references clientes(id)
);

create table itens_pedido (
id int auto_increment primary key,
pedido_id int,
produto_id int,
quantidade int,
preco_unitario decimal(10, 2),
foreign key (pedido_id) references pedidos(id),
foreign key (produto_id) references produtos(id)
);
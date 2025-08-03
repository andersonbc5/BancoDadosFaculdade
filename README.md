## BancoDadosFaculdade - Sistema de E-commerce com Python e SQLite

# 📚 Visão Geral
Este projeto acadêmico demonstra a integração entre Python e SQLite para criar um sistema básico de e-commerce. O código implementa um banco de dados relacional com três tabelas principais (Produtos, Clientes e Pedidos) e inclui funcionalidades para criação de estrutura e população inicial com dados de exemplo.

# ✨ Funcionalidades Principais
Criação automática do banco de dados (ecommerce.db)

Gerenciamento de tabelas:

Produtos: Cadastro de itens à venda

Clientes: Registro de clientes

Pedidos: Histórico de compras com relacionamentos

Tratamento robusto de erros durante operações no banco

População inicial com dados de exemplo

# 🛠️ Estrutura do Banco de Dados
Tabela	Colunas	Descrição
Produtos	id, nome, preco, estoque	Itens disponíveis para venda
Clientes	id, nome, email	Informações dos clientes
Pedidos	id, cliente_id, produto_id, quantidade, data_pedido
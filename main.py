# Instalar pip install mysql-connector-python
import mysql.connector

# Conexão com a base de dados em MySQL Workbench
def conectar():
    try:
        return mysql.connector.connect(
            host="localhost",
        
             # Colocar o user e a password conforme foram configurados aquando da instalação do MySQL Workbench
            user="root",
            password="root",
            database="loja"
    )
    except mysql.connector.Error as erro:
        print("Erro ao conectar com a base de dados em MySQL Workbench:", erro)
        return None
    
# Funções para a Gestão de Produtos    
def registar_produto(nome, descricao, preco, categoria):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("INSERT INTO produtos (nome, descricao, preco, categoria) VALUES (%s, %s, %s, %s)", (nome, descricao, preco, categoria))
    conexao.commit()
    cursor.close()
    conexao.close()

def listar_produtos():
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM produtos")
    produtos = cursor.fetchall()
    cursor.close()
    conexao.close()
    return produtos

def atualizar_produto(produto_id, nome, descricao, preco, categoria):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("UPDATE produtos SET nome = %s, descricao = %s, preco = %s, categoria = %s WHERE id = %s", 
                   (nome, descricao, preco, categoria, produto_id))
    conexao.commit()
    cursor.close()
    conexao.close()

def remover_produto(produto_id):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("DELETE FROM produtos WHERE id = %s", (produto_id,))
    conexao.commit()
    cursor.close()
    conexao.close()

# Funções para a Gestão de Pedidos
def processar_pedido(cliente_id, itens):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("INSERT INTO pedidos (cliente_id, estado) VALUES (%s, 'em processamento')", (cliente_id,))
    pedido_id = cursor.lastrowid
    for item in itens:
        cursor.execute("INSERT INTO itens_pedido (pedido_id, produto_id, quantidade, preco_unitario) VALUES (%s, %s, %s, %s)", (pedido_id, item['produto_id'], item['quantidade'], item['preco_unitario']))
    conexao.commit()
    cursor.close()
    conexao.close()

def listar_pedidos():
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM pedidos")
    pedidos = cursor.fetchall()
    cursor.close()
    conexao.close()
    return pedidos

def atualizar_estado_pedido(pedido_id, estado):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("UPDATE pedidos SET estado = %s WHERE id = %s", (estado, pedido_id))
    conexao.commit()
    cursor.close()
    conexao.close()

# Funções para a Gestão de Clientes
def registar_cliente(nome, email, telefone, endereco):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("INSERT INTO clientes (nome, email, telefone, endereco) VALUES (%s, %s, %s, %s)", (nome, email, telefone, endereco))
    conexao.commit()
    cursor.close()
    conexao.close()

def listar_clientes():
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM clientes")
    clientes = cursor.fetchall()
    cursor.close()
    conexao.close()
    return clientes

def atualizar_cliente(cliente_id, nome, email, telefone, endereco):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("UPDATE clientes SET nome = %s, email = %s, telefone = %s, endereco = %s WHERE id = %s", 
                   (nome, email, telefone, endereco, cliente_id))
    conexao.commit()
    cursor.close()
    conexao.close()

def remover_cliente(cliente_id):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("DELETE FROM clientes WHERE id = %s", (cliente_id,))
    conexao.commit()
    cursor.close()
    conexao.close()

# Menu Principal
def menu_principal():
    while True:
        print("\nMenu Principal")
        print("1. Gestão de Produtos")
        print("2. Gestão de Pedidos")
        print("3. Gestão de Clientes")
        print("4. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            menu_produtos()
        elif opcao == '2':
            menu_pedidos()
        elif opcao == '3':
            menu_clientes()
        elif opcao == '4':
            print("Programa encerrado.")
            break
        else:
            print("Opção inválida. Tente novamente.")
            
            
# Menu de Gestão de Produtos
def menu_produtos():
    while True:
        print("\nGestão de Produtos")
        print("1. Registar novo produto")
        print("2. Listar produtos")
        print("3. Atualizar produto")
        print("4. Remover produto")
        print("5. Voltar ao menu principal")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            nome = input("Nome do produto: ")
            descricao = input("Descrição do produto: ")
            preco = float(input("Preço do produto: "))
            categoria = input("Categoria do produto: ")
            registar_produto(nome, descricao, preco, categoria)
            print("Produto registado com sucesso!")
        elif opcao == '2':
            produtos = listar_produtos()
            for produto in produtos:
                print(produto)
        elif opcao == '3':
            produto_id = int(input("ID do produto: "))
            nome = input("Nome do produto: ")
            descricao = input("Descrição do produto: ")
            preco = float(input("Preço do produto: "))
            categoria = input("Categoria do produto: ")
            atualizar_produto(produto_id, nome, descricao, preco, categoria)
            print("Produto atualizado com sucesso!")
        elif opcao == '4':
            produto_id = int(input("ID do produto: "))
            remover_produto(produto_id)
            print("Produto removido com sucesso!")
        elif opcao == '5':
            break
        else:
            print("Opção inválida. Tente novamente.")

# Menu de Gestão de Pedidos
def menu_pedidos():
    while True:
        print("\nGestão de Pedidos")
        print("1. Processar novo pedido")
        print("2. Listar pedidos")
        print("3. Atualizar estado do pedido")
        print("4. Voltar ao menu principal")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            cliente_id = int(input("ID do cliente: "))
            itens = []
            while True:
                produto_id = int(input("ID do produto: "))
                quantidade = int(input("Quantidade: "))
                preco_unitario = float(input("Preço unitário: "))
                itens.append({'produto_id': produto_id, 'quantidade': quantidade, 'preco_unitario': preco_unitario})
                continuar = input("Pretende adicionar mais itens? (s/n): ")
                if continuar.lower() != 's':
                    break
            processar_pedido(cliente_id, itens)
            print("Pedido processado com sucesso!")
        elif opcao == '2':
            pedidos = listar_pedidos()
            for pedido in pedidos:
                print(pedido)
        elif opcao == '3':
            pedido_id = int(input("ID do pedido: "))
            estado = input("Estado do pedido: ")
            atualizar_estado_pedido(pedido_id, estado)
            print("Estado do pedido atualizado com sucesso!")
        elif opcao == '4':
            break
        else:
            print("Opção inválida. Tente novamente.")
            
# Menu de Gestão de Clientes
def menu_clientes():
    while True:
        print("\nGestão de Clientes")
        print("1. Registar novo cliente")
        print("2. Listar clientes")
        print("3. Atualizar cliente")
        print("4. Remover cliente")
        print("5. Voltar ao menu principal")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            nome = input("Nome do cliente: ")
            email = input("Email do cliente: ")
            telefone = input("Telefone do cliente: ")
            endereco = input("Endereço do cliente: ")
            registar_cliente(nome, email, telefone, endereco)
            print("Cliente registado com sucesso!")
        elif opcao == '2':
            clientes = listar_clientes()
            for cliente in clientes:
                print(cliente)
        elif opcao == '3':
                cliente_id = int(input("ID do cliente: "))
                nome = input("Nome do cliente: ")
                email = input("Email do cliente: ")
                telefone = input("Telefone do cliente: ")
                endereco = input("Endereço do cliente: ")
                atualizar_cliente(cliente_id, nome, email, telefone, endereco)
                print("Cliente atualizado com sucesso!")
        elif opcao == '4':
            cliente_id = int(input("ID do cliente: "))
            remover_cliente(cliente_id)
            print("Cliente removido com sucesso!")
        elif opcao == '5':
            break
        else:
            print("Opção inválida. Tente novamente.")

menu_principal()
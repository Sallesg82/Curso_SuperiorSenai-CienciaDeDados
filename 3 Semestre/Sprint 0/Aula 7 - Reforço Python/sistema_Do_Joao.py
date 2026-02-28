produtos = []


# Vai ser usada para armazenar os dados do
# produto.
def total_produtos(lista):  # Função vai receber a
    # lista como parametro que vai ser PRODUTOS e retonar
    # todo o valor de todos os produtos

    soma_total = 0
    for item in lista:
        total_item = item[1] * item[2]
        soma_total += total_item

    # multiplica o valor pela quantidade de cada item
    # e junta tudo
    return soma_total  # retorna o valor total


while True:
    produto = []  # Armazenar os valores de 1 produto
    print("Deseja cadastrar um produto?")
    resposta_user = input("S/N").upper()
    # Pergutar ao usuario se ele deseja cadastrar
    # um produto e guardando a resposta
    if resposta_user == "S":
        # Se o usuario quer proceguir...
        nome_produto = input("Qual o nome do produto: ")
        valor_produto = float(input("Valor do produto: "))
        quantidade_produto = int(input("Quantidade do produto: "))

        # Coletando os dados do usuario
        produto.append(nome_produto)
        produto.append(valor_produto)
        produto.append(quantidade_produto)
        # Colocando todos os dados em um vetor
        produtos.append(produto)
        # Colocar o produto junto com todos os outros
        # produtos
    else:  # encerrar o sistema
        valor_total = total_produtos(produtos)
        print("Valor total em produtos: ", valor_total)
        break  # mostra o tatal a encerrar

import csv 

def gravar_itens(lista_de_itens):
    with open('estoque.csv', 'a', encoding="utf-8") as arquivo:
        for linha in lista_de_itens:
            arquivo.write(linha)
            arquivo.write('\n')
            arquivo.close()
    print('Gravado o produto') 

# def remover_itens(lista_de_itens):
#     with open('estoque.csv', 'a', encoding="utf-8") as arquivo:
    #     for linha in lista_de_itens:
    #         linha = linha.rstrip('\n')
    #         arquivo.write(linha)
    #         arquivo.write('\n')
    #         arquivo.close()
    # print('Gravado o produto')

def ler_itens(): 
    leitura = []
    with open('estoque.csv', 'r', encoding="utf-8") as arquivo:
        for linha in arquivo:
            resultado = linha.split(sep=',')
            resultado = linha.rstrip('\n')
            leitura.append(resultado)
    print(leitura)


def ler_itens2(): 
    leitura = []
    with open('estoque.csv', 'r', encoding="utf-8") as arquivo:
        for linha in arquivo:
            resultado = linha.split(sep=',')
            resultado = linha.rstrip('\n')
            leitura.append(resultado)
    print(leitura)


print("=================================")
print("OQUE DESEJA FAZER?")
print("=================================")
print("ADICONAR UM ITEM - Digite 1\nVER ESTOQUES - Digite 2\nREMOVER UM ITEM - Digite 3")
print("=================================")

lista_de_itens = ler_itens()

resposta = int(input("Escreva aqui o número...\n"))

if resposta == 1:
    produto_add = input('Escreva o nome do produto que deseja adicionar...\n')
    lista_de_itens = []
    lista_de_itens.append(produto_add)
    gravar_itens(lista_de_itens)

if resposta == 2:
    # with open('estoque.csv', 'r', encoding="utf-8") as arquivo:
    #     linha = arquivo.readlines()
    #     while linha:
    #         print(linha)
    #         linha = arquivo.readlines()
    ler_itens()
 
if resposta == 3:
    produto_rem = input('Escreva o produto que deseja remover...')
    lista_de_itens.remove(produto_rem)

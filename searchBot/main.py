from lxml import html
from googlesearch import search
import requests, re, functions

# <---------------------| Path e Arquivo |-------------------->

while True:
    nomeArquivo = input("Nome do arquivo\n> ")

    if not nomeArquivo:
        print("Por favor, digite um nome válido.\n")

    path = input("\nDigite o path que deseja salvar o arquivo.\n> ")

    try:
        arquivo = open(f"{path}\\{nomeArquivo}.txt", "x")
        arquivo.close()
        break
    except:
        print("Path incorreto, por favor tente novamente.\n")

# <---------------------| Variaveis Globais |-------------------->

# Exibição dos sites no txt
sitesTXT = ["Kabum", "Mercado Livre"]

# Dict para ser usado nas buscas
dictSites = {   'Kabum': 'www.kabum.com.br',
                'Mercado Livre 1': 'produto.mercadolivre.com.br',
                'Mercado Livre 2': 'www.mercadolivre.com.br',
                'Mercado Livre 3': 'lista.mercadolivre.com.br',
                'Mercado Livre 4': 'informatica.mercadolivre.com.br',
                'Mercado Livre 5': 'loja.mercadolivre.com.br'
                }

# <---------------------| Sites Usados |-------------------->

# O que vai buscar no google
busca = input("\nDigite o que você quer buscar:\n> ")

# Quantos links do google ele vai buscar    
limite = functions.numInt("\nQuantos links do google deseja buscas?\n> ")
    
# Pega os links da busca
links = search(query = busca, start = 0, stop = limite, pause = 2)

# Filtra os sites de acordo com o <dictSites>
sites = functions.sitesFuncionais(links, dictSites)

# <---------------------| Busca nos Sites |-------------------->

# Pega os preços e links dos produtos
pKabum, lKabum = functions.kabum(sites, dictSites)
pML, lML = functions.mercadolivre(sites, dictSites)

# Junta todos os preços e links
todosPreco = (pKabum, pML)
todosLinks = (lKabum, lML)

# <---------------------| Debug |-------------------->

# print(pML)
# print(lML)
print("DEU CERTO!!!!!!!!!!!!!!!")

# <---------------------| Arquivo de Texto |-------------------->

arquivo = open(f"{path}\\{nomeArquivo}.txt", "w+")

arquivo.write(f"Busca realizada: {busca}\n\n")

for p in range(len(todosPreco)):
    for i in range(len(todosPreco[p])):
        arquivo.write(f"""Site: {sitesTXT[p]}
Preço: R$ {str(todosPreco[p][i]).replace(".", ",")}
Link: {todosLinks[p][i]}

""")

arquivo.close()

input("Programa finalizado, precione ENTER para fechar.")
import matplotlib.pyplot as plt
import csv
import numpy as np

from colorama import init, Fore, Style
init()

dados = []

def carrega_dados():
    with open('brazil_covid19.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for linha in csv_reader:
            dados.append(linha)


def titulo(texto, traco="-"):
    print()
    print(Fore.RED + texto + Style.RESET_ALL)
    print(traco*40)


#1 função 
def resumo_dados():
    titulo("Visão Geral")

    casos_por_estado = {}
    mortes_por_regiao = {}
    total_casos = 0
    total_mortes = 0

    for linha in dados:
        regiao = linha['region']
        estado = linha['state']
        casos = float(linha['cases']) if linha['cases'] else 0
        mortes = int(linha['deaths']) if linha['deaths'] else 0

        casos_por_estado[estado] = casos_por_estado.get(estado, 0) + casos
        mortes_por_regiao[regiao] = mortes_por_regiao.get(regiao, 0) + mortes

        total_casos += casos
        total_mortes += mortes

    estado_mais_casos = max(casos_por_estado, key=casos_por_estado.get)
    regiao_mais_mortes = max(mortes_por_regiao, key=mortes_por_regiao.get)

    print("Estado com mais casos:", estado_mais_casos)
    print("Região com mais mortes:", regiao_mais_mortes)
    print(f"\nTotal de mortes no país todo: {total_mortes}")


#2 função 
def casos_regiao():
    titulo("Casos por Região")
    
    casos_regiao = {} 

    for linha in dados:
        regiao = linha['region']
        casos = float(linha['cases']) if linha['cases'] else 0

        if regiao not in casos_regiao or casos > casos_regiao[regiao]:
            casos_regiao[regiao] = casos

    regioes = list(casos_regiao.keys())
    valores = list(casos_regiao.values())

    plt.figure(figsize=(10, 6))
    plt.bar(regioes, valores, color='skyblue')
    plt.xlabel('Região')
    plt.title('Casos de COVID-19 por Região')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()


#3 função 
def casos_RS():
    titulo("Mortes no RS - 2020 e 2021")

    mortes_RS_2020 = {}
    mortes_RS_2021 = {}

    dados_RS = [linha for linha in dados if linha['state'] == 'RS']

    for linha in dados_RS:
        data = linha['date']
        ano = int(data.split('-')[0])  

        mortes = int(linha['deaths']) if linha['deaths'] else 0

        if ano == 2020:
            if data in mortes_RS_2020:
                mortes_RS_2020[data] = max(mortes, mortes_RS_2020[data])
            else:
                mortes_RS_2020[data] = mortes
        elif ano == 2021:
            if data in mortes_RS_2021:
                mortes_RS_2021[data] = max(mortes, mortes_RS_2021[data])
            else:
                mortes_RS_2021[data] = mortes

    valores_2020 = list(mortes_RS_2020.values())
    valores_2021 = list(mortes_RS_2021.values())

    maximo_2020 = max(valores_2020)
    maximo_2021 = max(valores_2021)

    plt.figure(figsize=(8, 6))
    plt.plot(valores_2020, color='blue', label='Máx. Mortes em 2020', linestyle='-', linewidth=1)
    plt.plot(valores_2021, color='red', label='Máx. Mortes em 2021', linestyle='-', linewidth=1)
    plt.ylim(0, max(maximo_2020, maximo_2021))
    plt.ylabel('Pico de Mortes')
    plt.title('Comparação de Mortes em 2020 e 2021 no Estado do Rio Grande do Sul')
    plt.legend()
    plt.tight_layout()
    plt.show()


# -------------------------------------------- Programa Principal
carrega_dados()

while True:
    titulo("Coronavírus no Brasil", "=")
    print("1. Resumo dos Dados")
    print("2. Casos por Região - Gráfico")
    print("3. Mortes no RS - 2020 - 2021 - Gráfico")
    print("4. Finalizar")
    opcao = int(input("Opção: "))
    if opcao == 1:
        resumo_dados()
    elif opcao == 2:
        casos_regiao()
    elif opcao == 3:
        casos_RS()
    else:
        break
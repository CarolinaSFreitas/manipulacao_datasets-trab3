import matplotlib.pyplot as plt
import csv

dados = []


def carrega_dados():
    with open('brazil_covid19.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for linha in csv_reader:
            dados.append(linha)


def titulo(msg, traco="-"):
    print()
    print(msg)
    print(traco*40)


# 1 Função para calcular dados gerais por região e total
def dados_gerais(dados):
    casos_por_regiao = {}
    mortes_por_regiao = {}
    total_casos = 0
    total_mortes = 0

    for linha in dados:
        regiao = linha['region']
        casos = float(linha['cases']) if linha['cases'] else 0
        mortes = int(linha['deaths']) if linha['deaths'] else 0

        # Calcula casos e mortes por região
        casos_por_regiao[regiao] = casos_por_regiao.get(regiao, 0) + casos
        mortes_por_regiao[regiao] = mortes_por_regiao.get(regiao, 0) + mortes

        # Calcula total de casos e mortes
        total_casos += casos
        total_mortes += mortes

    # Encontrar região com mais casos e mortes
    regiao_mais_casos = max(casos_por_regiao, key=casos_por_regiao.get)
    regiao_mais_mortes = max(mortes_por_regiao, key=mortes_por_regiao.get)

    # Exibe os resultados
    print("Região com mais casos:", regiao_mais_casos)
    print("Região com mais mortes:", regiao_mais_mortes)
    print(f"\nTotal de mortes no país todo: {total_mortes}")


# 2 Função para criar gráfico de colunas com a quantidade de mortes por estado
def mortesPorEstado(dados):
    estados = []
    mortes = []

    for linha in dados:
        estado = linha['state']
        qtd_mortes = int(linha['deaths']) if linha['deaths'] else 0
        estados.append(estado)
        mortes.append(qtd_mortes)

    plt.figure(figsize=(8, 8))
    plt.pie(mortes, labels=estados, autopct='%1.1f%%', startangle=140)
    plt.axis('equal')  # Assegura que o gráfico de pizza é desenhado como um círculo
    plt.title('Distribuição de Mortes por Estado')
    plt.tight_layout()
    plt.show()


# 3 Função com os dados de casos e mortes por mês
def casosMortesMes(dados):
    meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
    casos_por_mes = [0] * 12
    mortes_por_mes = [0] * 12
    recuperados_por_mes = [0] * 12

    for linha in dados:
        data = linha['date']
        mes = int(data.split('-')[1])
        casos = float(linha['cases']) if linha['cases'] else 0
        mortes = int(linha['deaths']) if linha['deaths'] else 0

        # Acumula os casos e mortes por mês
        casos_por_mes[mes - 1] += casos
        mortes_por_mes[mes - 1] += mortes

    plt.figure(figsize=(10, 6))

    bar_width = 0.25
    index = range(len(meses))

    plt.bar(index, casos_por_mes, bar_width, label='Casos')
    plt.bar([i + bar_width for i in index], mortes_por_mes, bar_width, label='Mortes')

    plt.xlabel('Mês')
    plt.ylabel('Quantidade')
    plt.title('Casos e Mortes de COVID-19 por Mês')
    plt.xticks([i + bar_width / 2 for i in index], meses)
    plt.legend()

    plt.tight_layout()
    plt.show()

# -------------------------------------- Programa Principal
carrega_dados()

while True:
    titulo("Coronavírus no Brasil", "=")
    print("1. Resumo dos Dados")
    print("2. Mortes por Estado - Gráfico de Pizza")
    print("3. Casos e Mortes por mês - Gráfico de Barras")
    print("4. Finalizar")
    opcao = int(input("Opção: "))
    if opcao == 1:
        resumoDosDados()
    elif opcao == 2:
        mortesPorEstado()
    elif opcao == 3:
        casosMortesMes()
    else:
        break

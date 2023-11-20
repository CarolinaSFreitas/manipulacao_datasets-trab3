import matplotlib.pyplot as plt
import numpy as np
import csv

from colorama import init, Fore, Style
init()

diabetes = []

def carrega_dados():
    with open('diabetes.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for linha in csv_reader:
            diabetes.append(linha)

def titulo(texto, traco="-"):
    print()
    print(Fore.CYAN + texto + Style.RESET_ALL)
    print(traco*40)


def print_com_cor(texto, cor):
    print(cor + texto + Style.RESET_ALL)


def resumoDosDados():
    titulo("Resumo dos Dados")

    total_mulheres = 0
    mulheres_diabeticas = 0
    mulheres_sem_diabetes = 0
    primeira_mulher = diabetes[0]
    idade_minima = int(primeira_mulher['Age'])
    idade_maxima = int(primeira_mulher['Age'])

    for mulher in diabetes:
        total_mulheres += 1
        idade = int(mulher['Age'])

        if int(mulher['Outcome']) == 1:
            mulheres_diabeticas += 1
        else:
            mulheres_sem_diabetes += 1

        if idade < idade_minima:
            idade_minima = idade
        if idade > idade_maxima:
            idade_maxima = idade

    print(f"Nº Mulheres: {total_mulheres}")
    print(f"Nº Mulheres Diabéticas: {mulheres_diabeticas}")
    print(f"Nº Mulheres Sem Diabetes: {mulheres_sem_diabetes}")
    print(f"Faixa Etária das Mulheres: {idade_minima} até {idade_maxima} anos")


def graficoDePizza():
    titulo("Gráfico Comparativo de Diabéticas por Gestação")

    gestacoes_ate_2 = 0
    gestacoes_3_5 = 0
    gestacoes_6_8 = 0
    gestacoes_acima_8 = 0

    for mulher in diabetes:
        if int(mulher['Outcome']) == 1:
            gestacoes = int(mulher['Pregnancies'])

            if gestacoes <= 2:
                gestacoes_ate_2 += 1
            elif 3 <= gestacoes <= 5:
                gestacoes_3_5 += 1
            elif 6 <= gestacoes <= 8:
                gestacoes_6_8 += 1
            else:
                gestacoes_acima_8 += 1

    labels = ['Até 2 gestações', 'Entre 3 e 5 gestações',
              'Entre 6 e 8 gestações', 'Acima de 8 gestações']
    sizes = [gestacoes_ate_2, gestacoes_3_5, gestacoes_6_8, gestacoes_acima_8]

    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
    plt.axis('equal')
    plt.show()


def graficoDeBarra():
    titulo("Gráfico Comparativo de Taxas de Glicose")

    diabeticas = {'Até 99': 0, 'Entre 100 e 130': 0,
                  'Entre 131 e 160': 0, 'Acima de 160': 0}
    nao_diabeticas = {'Até 99': 0, 'Entre 100 e 130': 0,
                      'Entre 131 e 160': 0, 'Acima de 160': 0}

    for mulher in diabetes:
        taxa_glicose = int(mulher['Glucose'])

        if taxa_glicose <= 99:
            if int(mulher['Outcome']) == 1:
                diabeticas['Até 99'] += 1
            else:
                nao_diabeticas['Até 99'] += 1
        elif 100 <= taxa_glicose <= 130:
            if int(mulher['Outcome']) == 1:
                diabeticas['Entre 100 e 130'] += 1
            else:
                nao_diabeticas['Entre 100 e 130'] += 1
        elif 131 <= taxa_glicose <= 160:
            if int(mulher['Outcome']) == 1:
                diabeticas['Entre 131 e 160'] += 1
            else:
                nao_diabeticas['Entre 131 e 160'] += 1
        else:
            if int(mulher['Outcome']) == 1:
                diabeticas['Acima de 160'] += 1
            else:
                nao_diabeticas['Acima de 160'] += 1

    labels = ['Até 99', 'Entre 100 e 130', 'Entre 131 e 160', 'Acima de 160']
    x = range(len(labels))
    width = 0.35

    fig, ax = plt.subplots()
    bar1 = ax.bar(x, diabeticas.values(), width, label='Diabéticas')
    bar2 = ax.bar([i + width for i in x], nao_diabeticas.values(),
                  width, label='Não Diabéticas')

    ax.set_xlabel('Taxa de Glicose')
    ax.set_ylabel('Número de Mulheres')
    ax.set_title('Gráfico Comparativo de Taxas de Glicose')
    ax.set_xticks([i + width/2 for i in x])
    ax.set_xticklabels(labels)
    ax.legend()
    plt.show()


# -------------------------------------- Programa Principal
carrega_dados()

while True:
    titulo("Previsão de Diabetes", "=")
    print_com_cor("1. Resumo dos Dados", Fore.GREEN)
    print_com_cor("2. Gráfico Comparativo de Diabéticas por Gestação", Fore.YELLOW)
    print_com_cor("3. Gráfico Comparativo de Taxas de Glicose", Fore.MAGENTA)
    print_com_cor("4. Finalizar", Fore.RED)
    opcao = int(input("Opção: "))
    if opcao == 1:
        resumoDosDados()
    elif opcao == 2:
        graficoDePizza()
    elif opcao == 3:
        graficoDeBarra()
    else:
        break

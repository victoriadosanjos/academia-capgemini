import datetime
import json
import os

def calcData():
    # Formatando data inicial
    ano,mes,dia = map(int, dataInicial.split('-'))
    d1 = datetime.date(ano, mes, dia)
    # Formatando data final
    ano,mes,dia = map(int, dataTermino.split('-'))
    d2 = datetime.date(ano, mes, dia)
    # calculo convertendo em dias
    quantidadeDedias = abs((d2 - d1).days)
    return quantidadeDedias

def calcValorInvestido(v):
    # Calculo de dias
    dias = calcData()
    # Calculo valor investido
    valorInvestido = dias * v
    return valorInvestido

def calcVisualizacaoOriginal():
    # Calculo de visualizacao Original
    visualizacaoOriginal = int(calcValorInvestido(valorPorDia) * 30)
    return visualizacaoOriginal

def calcCliques():
    cliques = int(calcVisualizacaoOriginal() * 0.12)
    return cliques

def calcCompartilhamento():
    compartilhamento = int((calcCliques() * 0.15) * 4)
    return compartilhamento

def calcNovasVisualizacoes(): 
    novasVisualizacoes = calcCompartilhamento() * 40
    return novasVisualizacoes

def calcVisualizacaoTotal():
    visualizacaoTotal = int(calcNovasVisualizacoes() + calcVisualizacaoOriginal())
    return visualizacaoTotal

def funcaoCasdastro():
    global nomeAnuncio, cliente, dataInicial, dataTermino, valorPorDia
    nomeAnuncio = input('Digite o nome do anúncio : ')
    cliente = input('Digite o nome do cliente : ')
    dataInicial = input('Digite a data de inicio (Formato YYYY-MM-DD) : ')
    dataTermino = input('Digite a data do termino (Padrao YYYY-MM-DD) : ')
    valorPorDia = float(input('Digite o valor do investimento por dia: .2f'))

    data = {}
    data[cliente] = []
    data[cliente].append({
        "anuncio": nomeAnuncio,
        "cliente": cliente,
        "dataInicio": dataInicial,
        "dataTermino": dataTermino,
        "valorInvestido": calcValorInvestido(valorPorDia),
        "qtVisualizacoes": calcVisualizacaoTotal(),
        "qtCliques": calcCliques(),
        "qtCompartilhamentos": calcCompartilhamento()
    })
    
    with open('data.json','r+') as file: 
        file_data = json.load(file)
        file_data.update(data)
        file.seek(0)
        json.dump(file_data, file, indent = 4)

def funcaoRelatorio():
    opcao = input("Digite o nome do cliente que deseja consultar: ")
    with open('data.json','r') as file:
        data = json.load(file)
        print(json.dumps(data[opcao], indent=4))

def menu():
    opcao = int(input("Informe um 1 para cadastrar anuncio, 2 para gerar relatorio ou 0 para sair: "))

    if opcao == 0:
        exit
    elif opcao == 1:
        funcaoCasdastro()
        menu()
    elif opcao == 2:
        funcaoRelatorio()
        menu()
    else:
        print("Opcao selecionada nao existe")
        exit

menu()

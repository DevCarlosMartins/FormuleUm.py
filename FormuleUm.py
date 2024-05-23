"""  pip install requests """

import requests

DELIMITADOR: str = ";"

url : str = "https://ergast.com/api/f1/2010/5/results.json"

response : requests.Response = requests.get(url)
api_date: dict = response.json()
# print(api_date["MRData"]["series"])

races = api_date["MRData"]["RaceTable"]["Races"][0]["Results"]

def menu_principal():
    print("====== Menu Principal ======")
    print("=                          =")
    print("= 1 - Corridas             =")
    print("= 2 - Pilotos              =")
    print("= 3 - Equipe               =")
    print("= 4 - Equipe Participantes =")
    print("= 5 - Resumo Estatistico   =")
    print("= 6 - Exportar Dados       =")
    print("= 7 - Importar Dados       =")
    print("= 8 - Limpar Dados         =")
    print("=                          =")
    print("= 0 - Sair                 =")
    print("============================")

def get_opcao():
    opcoes_validas = ["0", "Corridas", "2", "3", "4", "5", "6", "7", "8"]
    opcao = input("Opção: ")
    while opcao not in opcoes_validas:
        opcao = input("Opção Invalida! Digite novamente: ")
    return opcao



def corridas() :    
    for race in races:
        print(" ")
        print("Piloto  : " + race["Driver"]["familyName"])
        print("Posição : " + race["position"])
        print("Voltas  : " + race["FastestLap"]["lap"])
        print("_____")

def equipes ():
    for race in races: 
        print(" ")
        print("Nome       : " + race["Constructor"]["name"])
        print("Piloto     : " + race["Driver"]["familyName"])
        print("_____")

while True:
    menu_principal()
    opcao = get_opcao()
    print(opcao)
    
    if opcao == "0":
        break

    #elif opcao == "1":
        #races = corridas()

    elif opcao:
        race = corridas()
    
    elif opcao == "3":
        races = equipes()
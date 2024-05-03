import mysql.connector
from mysql.connector import errorcode

# Parâmetros de conexão
host = "3306"
user = "root"
password = "MMClara_19"
database = "Projeto_integradorI"

print("Programa para cadastrar produto, calcular o preço de vendas e classificação de lucro\n")

try:
    cod_pro = int(input("Digite o Código:"))
    if cod_pro <= 0: 
        print("O código deve ser maior que zero.")
    else: 
        nome = input("Digite o nome do produto: ").upper()
        descricao = input("Digite a descrição do produto: ").upper()
        CP = float(input("Digite o custo do produto: "))
        CF_p = float(input("Digite o custo fixo/Administrativo do produto: "))
        IV_p = float(input("Digite o Imposto do produto: "))
        CM_p = float(input("Digite Comissão de Vendas do produto: "))
        ML = float(input("Digite a Margem de lucro: "))
        print()
    
    #preço de venda
    PV = CP / (1 - ((CF_p + CM_p + IV_p + ML) / 100))
    #rentabilidade
    RB = PV - CP
    #MargemFinal
    ML_final =(PV * ML)/100
    

   
    #verificar lucro
    
    if ML_final > 20:
        print("-"*25)
        print(f"O lucro do produto é Alto", "|")
        print("-"*25)
    elif ML_final > 10:
        print("-"*25)
        print(f"O lucro do produto é Médio", "|")
        print("-"*25)
    elif ML_final > 0:
        print("-"*23)
        print(f"O lucro do produto é Baixo", "|" )
        print("-"*23)
    elif ML_final == 0:
        print("-"*23)
        print(f"O lucro do produto é Equilibrado", "|" )
        print("-"*23)
    else:
        print("-"*23)
        print(f"O produto dá Prejuízo", "|")
        print("-"*23)
        
    #PORCENTUAL
    CP_p = (CP * 100)/PV
    PV_p = (PV * 100)/PV
    RB_p = (RB * 100) /PV
    CF = (CF_p * PV)/100
    IV = (IV_p * PV)/100
    CM = (CM_p *PV)/100
    #Outros CUSTOS
    OC = CF+ CM + IV
    OC_p = (100 * OC )/PV
    #Margem de lucro
    ML_p = ML
    
    menu = ["DESCRIÇÃO", "VALOR", "%"]
    
    tabela = [
        ["A - PREÇO DE VENDA", PV, PV_p],
        ["B - CUSTO DE AQUISIÇÃO",CP, CP_p],
        ["C - RECEITA BRUTA", RB, RB_p],
        ["D - CUSTO FIXO/ADMINISTRATIVO", CF, CF_p],
        ["E - IMPOSTOS", IV, IV_p],
        ["F - COMISSÃO DE VENDAS", CM, CM_p],
        ["G - OUTROS CUSTOS", OC, OC_p],
        ["H - RENTABILIDADE", ML_final, ML_p]
        
    ]
 
    print("\n{: <40}{: <20}{: <10}".format(*menu))
    for row in tabela:
        print("{: <40}{: <20.2f}{: <10.2f}%".format(row[0], row[1], row[2]))
    
except ValueError:
    print("\nEntrada inválida.")
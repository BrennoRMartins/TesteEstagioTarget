import json

def percentual(dados):
    soma = 0
    num = 0
    percent= []


    for i in range(len(dados)):
        if (float(dados[i]["valor"])) > 0:
            num = num + 1
            soma = soma + (float(dados[i]["valor"]))
    
    for item in dados:
        porcentagem = ((item["valor"])/soma) * 100
        f_porcentagem = f"{porcentagem:.4f}"
        dict = {"estado" : item["estado"], "percentual" : f_porcentagem}
        percent.append(dict)

    return percent

        

def main():
    
    with open('estados.json', 'r') as file:
        dados = json.load(file)

    resposta = percentual(dados)
    
    print("Estado | Participação")
    for i in range(len(resposta)):
        print(f"{resposta[i]["estado"]} | {resposta[i]["percentual"]}%")
    




if __name__ == "__main__":
    main()


# Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado:
#• SP – R$67.836,43
#• RJ – R$36.678,66
#• MG – R$29.229,88
#• ES – R$27.165,48
#• Outros – R$19.849,53

#Escreva um programa na linguagem que desejar onde calcule o percentual de representação que cada estado teve dentro do valor total mensal da distribuidora.  
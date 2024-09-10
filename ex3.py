import json

def acharMenor(dados):
    menor = dados[0]

    for i in range(len(dados)):
        if float(dados[i]["valor"] == 0):
            menor = menor
        elif float(dados[i]["valor"]) < float(menor["valor"]):
            menor = dados[i]
    
    return menor

def acharMaior(dados):
    maior = dados[0]

    for i in range(len(dados)):
        if float(dados[i]["valor"]) > float(maior["valor"]):
            maior = dados[i]
    
    return maior

def acharDiasAcimaDaMedia(dados):
    soma = 0
    num = 0
    media = 0
    diasAcimaDaMedia = 0

    for i in range(len(dados)):
        if (float(dados[i]["valor"])) > 0:
            num = num + 1
            soma = soma + (float(dados[i]["valor"]))
    
    media = soma/num

    for k in range(len(dados)):
        if (float(dados[k]["valor"])) > media:
            diasAcimaDaMedia = diasAcimaDaMedia + 1
    
    return diasAcimaDaMedia


def main():
    with open('dados.json', 'r') as file:
        dados = json.load(file)
    
    menor = acharMenor(dados)
    maior = acharMaior(dados)
    diasAcimaDaMedia = acharDiasAcimaDaMedia(dados)

    print(f'O menor faturamento foi de ${menor["valor"]} no dia {menor["dia"]}')
    print(f'O maior faturamento foi de ${maior["valor"]} no dia {maior["dia"]}')
    print(f'O faturamento foi maior que a media em {diasAcimaDaMedia} dias')



if __name__ == "__main__":
    main()
#3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
#• O maior valor de faturamento ocorrido em um dia do mês;
#• Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

#IMPORTANTE:
#a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
#b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média;

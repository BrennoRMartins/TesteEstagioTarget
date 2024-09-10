
def inverter(texto):
    inverso = ""
    for c in texto:
        inverso = c + inverso #a cada iteração adiciona o próximo caractere no início
    return inverso



def main():
    print("Digite alguma coisa")
    texto = input()
    
    print("Texto invertido: " + inverter(texto))


if __name__ == "__main__":
    main()
#Escreva um programa que inverta os caracteres de um string.
def fibonacci(n):
    if(n == 1):
        return [0]
    elif(n ==2):
        return [0,1]
    elif(n <= 0):
        return[]
    else:
        sequencia = fibonacci(n-1)
        prox = sequencia[-1] + sequencia[-2]
        sequencia.append(prox)
        return sequencia


def verificar(n,sequencia):
    for i in range(len(sequencia)):
        if sequencia[i] == n:
            return f'O número {n} está na sequência de Fibonacci'
    
    return f'O número {n} não está na sequência de Fibonacci'


def main():
    print("Digite um número")
    n_str = input()
    n = int(n_str)
    sequencia = fibonacci(n)
    print(sequencia)

    resposta = verificar(n, sequencia)
    print(resposta)

if __name__ == "__main__":
    main()


#2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos
#2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem
#que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem
#avisando se o número informado pertence ou não a sequência.

#IMPORTANTE: Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código;
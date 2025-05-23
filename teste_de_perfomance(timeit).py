# timeit é um módulo do Python usado para medir o tempo de execução de pequenos trechos de código. Ele executa o código várias vezes para obter uma média precisa,
# ajudando a analisar a performance de funções ou expressões.


import timeit

def soma_com_loop():
    total = 0
    for i in range(10000):
        total += i
    return total

def soma_com_sum():
    return sum(range(10000))

tempo_loop = timeit.timeit(soma_com_loop, number=1000)
tempo_sum = timeit.timeit(soma_com_sum, number=1000)

print(f"Tempo com loop: {tempo_loop:.4f} segundos")
print(f"Tempo com sum(): {tempo_sum:.4f} segundos")

# Função para ler um número positivo
def numeroPositivoLeitura():
    while True:
        numero = float(input("Digite um número positivo: "))
        if numero > 0:
            return numero
        else:
            print("O número deve ser positivo. Tente novamente.")

# Inicializar o vetor Q com 20 elementoos
Q = [0] * 20

# Preenche o vetor Q com números positivos
for i in range(20):
    Q[i] = numeroPositivoLeitura()

# Inicializar as variáveis para armazenar o maior e o menor elementos e suas posições
maior_elemento = Q[0]
posicao_maior_elemento = 0
menor_elemento = Q[0]
posicao_menor_elemento = 0


for i in range(1, 20):
    if Q[i] > maior_elemento:
        maior_elemento = Q[i]
        posicao_maior_elemento = i
    if Q[i] < menor_elemento:
        menor_elemento = Q[i]
        posicao_menor_elemento = i

# Imprir os resultados
print("O maior elemento de Q é", maior_elemento, "e ele ocupa a posição", posicao_maior_elemento)
print("O menor elemento de Q é", menor_elemento, "e ele ocupa a posição", posicao_menor_elemento)

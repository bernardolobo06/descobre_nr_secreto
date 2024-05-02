def descobre_nr_secreto():
  # altera este código
  x = 34
  # a distancia de x para o número secreto é dada por segredo.distancia(x)
  # podes chamar a função segredo.distancia() várias vezes com valores diferentes
  distancia_para_x = segredo.distancia(x)
  return ...






















import sys


class Seg():
    def __init__(self, numero_secreto):
        self.numero_secreto = numero_secreto

    def distancia(self, N):
        if not isinstance(N, int):
            print("o argumento da função segredo.distancia(N) tem que ser um número inteiro!")
            sys.exit(-1)
        if N < -50 or N > 50:
            print("o argumento da função segredo.distancia(N) tem que ser um número entre -50 e 50!")
            sys.exit(-1)
        return abs(N - self.numero_secreto)


numero_secreto = int(input("Número secreto: "))
segredo = Seg(numero_secreto)
x = descobre_nr_secreto()
if x == numero_secreto:
    print(f"Acertaste! Era {x}")
else:
    print(f"Falhaste! Era {numero_secreto} e disseste {x}")
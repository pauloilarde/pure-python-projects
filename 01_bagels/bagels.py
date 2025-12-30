"""
Bagels - Jogo de lógica dedutiva
Adivinhe um número baseado em pistas.
Baseado no projeto de Al Sweigart
"""

import random
NUM_DIGITOS = 3
MAX_TENTATIVAS = 10

def main():
  print("Bagels - Jogo de lógica dedutiva")
  print("=" * 46)
  # TODO: implementar lógica do jogo


def getNumeroSecreto():
  numeros = list("0123456789")

  random.shuffle(numeros)

  numero_secreto = ""
  for i in range(NUM_DIGITOS):
    numero_secreto += str(numeros[i])
  
  return numero_secreto


if __name__ == "__main__":
  main()


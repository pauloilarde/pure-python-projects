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


def getPistas(palpite, numero_secreto):

  if palpite == numero_secreto:
    return "✅ Você acertou!"
  
  pistas = []

  for i in range(len(palpite)):
    if palpite[i] == numero_secreto[i]:
      pistas.append("Fermi")
    elif palpite[i] in numero_secreto:
      pistas.append("Pico")
  
  if len(pistas) == 0:
    return "Bagels"
  
  pistas.sort()

  return " ".join(pistas)

if __name__ == "__main__":
  main()


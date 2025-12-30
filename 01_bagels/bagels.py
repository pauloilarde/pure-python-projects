"""
Bagels - Jogo de lógica dedutiva
Adivinhe um número baseado em pistas.
Baseado no projeto de Al Sweigart
"""

import random
NUM_DIGITOS = 3
MAX_TENTATIVAS = 10

def main():
  print("""Bagels - Jogo de lógica dedutiva
        Estou pensando em um número de {NUM_DIGITOS} dígitos sem repetições.
        Tente adivinhar. Aqui estão as pistas:

        Quando eu disser:    Significa:
        Pico                 Um dígito está correto mas na posição errada
        Fermi                Um dígito está correto e na posição correta
        Bagels               Nenhum dígito está correto

        Por exemplo, se o número secreto fosse 248 e seu palpite fosse 843,
        as pistas seriam: Fermi Pico
        
        """)
  
  
  while True:
    numero_secreto = getNumeroSecreto()
    print("Pensei em um número.")
    print("Você tem {MAX_TENTATIVAS} tentativas.\n")

    num_tentativas = 1
    while num_tentativas <= MAX_TENTATIVAS:
      palpite = ""

      while True:
        print(f"Tentativa #{num_tentativas}: ", end="")
        palpite = input()

        if not palpite.isdecimal():
          print("❌ Digite apenas números!")
          continue

        if len(palpite) != NUM_DIGITOS:
          print(f"❌ O número precisa ter exatamente {NUM_DIGITOS} dígitos!")
          continue

        if len(set(palpite)) != len(palpite):
          print("❌ O número não pode ter dígitos repetidos!")
          continue

        break

      pistas = getPistas(palpite, numero_secreto)
      print(pistas)
      num_tentativas += 1

      if palpite == numero_secreto:
        break


    if num_tentativas > MAX_TENTATIVAS:
      print("\n ❌ Suas tentativas acabaram!")
      print(f"A resposta era {numero_secreto}.")
    
    break # temporário - remove depois

  print("Obrigado por jogar!" )



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


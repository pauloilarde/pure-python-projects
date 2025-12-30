"""
Paradoxo do aniversário
Maiores informações: https://pt.wikipedia.org/wiki/Paradoxo_do_anivers%C3%A1rio
Baseado no projeto de Al Sweigart
"""

import datetime
import random

MESES = ('Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez')

def main():
  print(""" Paradoxo do aniversário
        
        O paradoxo do aniversário mostra que em um grupo de N pessoas,
a chance de duas delas terem o mesmo aniversário é surpreendentemente alta.

Este programa faz uma simulação de Monte Carlo (simulações aleatórias
repetidas) para explorar este conceito.

(Não é realmente um paradoxo, é apenas um resultado surpreendente!)

""")

  while True:
    print("Quantos aniversários devo gerar? (Máximo 100)")
    resposta = input("> ")

    if resposta.isdecimal() and (0 < int(resposta) <= 100):
      num_aniversarios = int(resposta)
      break
    else:
      print("❌ Digite um número entre 1 e 100!")

  print()

  # TODO: Gerar e exibir aniversários
  # TODO: Rodar simulações
  
  pass


def getBirthdays(quantidade):
  aniversarios = []

  for i in range(quantidade):
    inicio_ano = datetime.date(2000, 1, 1)

    dias_aleatorios = datetime.timedelta(random.randint(0,364))

    aniversario = inicio_ano + dias_aleatorios    
    aniversarios.append(aniversario)

  return aniversarios

def getMatch(aniversarios):
  if len(aniversarios) == len(set(aniversarios)):
    return None
  
  for a, aniversarioA in enumerate(aniversarios):
    for b, aniversarioB in enumerate(aniversarios[a + 1:]):
      if aniversarioA == aniversarioB:
        return aniversarioA


if __name__ == "__main__":
  main()
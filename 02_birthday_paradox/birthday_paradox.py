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

  print(f"Aqui estão {num_aniversarios} aniversários:")
  aniversarios = getBirthdays(num_aniversarios)

  for i, aniversario in enumerate(aniversarios):
    if i != 0:
      print(", ", end="")
    print(formatarData(aniversario), end="")

  coincidencia = getMatch(aniversarios)

  print("Nesta simulação, ", end="")
  if coincidencia is not None:
    print(f"Várias pessoas fazem aniversário em {formatarData(coincidencia)}")
  else:
    print("não há aniversários coincidentes.")

  print()

  print(f"Gerando {num_aniversarios} aniversários aleatórios 100.000 vezes...")
  input("Pressione ENTER para começar...")

  print("Executando 100.000 simulações...")
  coincidencias = 0

  for i in range(100_000):
    if i % 10_000 == 0:
      print(f"{i:,} simulações executadas...".replace(',', '.'))

    aniversarios_sim = getBirthdays(num_aniversarios)
    if getMatch(aniversarios_sim) is not None:
      coincidencias += 1
    
  print("100.000 simulações concluídas!")
  print()
  
  
  probabilidade = round(coincidencias / 100_000 * 100, 2)

  print(f" Das 100.000 simulações de {num_aniversarios} pessoas, houve")
  print(f"aniversário coincidente em {coincidencias:,} vezes.".replace(',', '.'))
  print(f"Isso significa que {num_aniversarios} pessoas tem {probabilidade}%")
  print("de chance de ter aniversário coincidente no grupo")
  print("Provavelment mais do que você imaginaria!")


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

def formatarData(data):
  nome_mes = MESES[data.month - 1]
  return f"{nome_mes} {data.day}"

if __name__ == "__main__":
  main()
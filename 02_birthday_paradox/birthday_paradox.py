"""
Paradoxo do aniversário
Maiores informações: https://pt.wikipedia.org/wiki/Paradoxo_do_anivers%C3%A1rio
Baseado no projeto de Al Sweigart
"""

import datetime
import random

MESES = ('Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez')

def main():
  """Função principal"""
  # TODO: implementar lógica
  pass


def getBirthdays(quantidade):
  aniversarios = []

  for i in range(quantidade):
    inicio_ano = datetime.date(2000, 1, 1)

    dias_aleatorios = datetime.timedelta(random.randint(0,364))

    aniversario = inicio_ano + dias_aleatorios    
    aniversarios.append(aniversario)

  return aniversarios

if __name__ == "__main__":
  main()
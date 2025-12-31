"""
Bitmap Message - Exibe mensagem usando bitmap
Mostra texto de acordo com uma imagem bitmap fornecida.
Baseado no projeto de Al Sweigart

"""

import sys

BITMAP = """
....................................................................
   **************   *  *** **  *      ******************************
  ********************* ** ** *  * ****************************** *
 **      *****************       ******************************
          *************          **  * **** ** ************** *
           *********            *******   **************** * *
            ********           ***************************  *
   *        * **** ***         *************** ******  ** *
               ****  *         ***************   *** ***  *
                 ******         *************    **   **  *
                 ********        *************    *  ** ***
                   ********         ********          * *** ****
                   *********         ******  *        **** ** * **
                   *********         ****** * *           *** *   *
                     ******          ***** **             *****   *
                     *****            **** *            ********
                    *****             ****              *********
                    ****              **                 *******   *
                    ***                                       *    *
                    **     *                    *
....................................................................

"""


def main():
  print("Bitmap Message")
  print("=" * 50)
  print("Digite a mensagem para exibir no bitmap.")
  print("(A mensagem será repetida para preencher o bitmap)")

  mensagem = input("> ")

  if mensagem == "":
    print("❌Mensagem não pode estar vazia")
    sys.exit()

  print()

  for linha in BITMAP.splitlines():
    for i, bit in enumerate(linha):
      if bit == " ":
        print(" ", end="")
      else:
        print(mensagem[i % len(mensagem)], end="")
    
    print()
  


if __name__ == "__main__":
  main()

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

  # TODO: Processar bitmap
  


if __name__ == "__main__":
  main()

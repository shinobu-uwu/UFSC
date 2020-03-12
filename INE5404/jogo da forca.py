#import os
import random


palavras = ["computador", "dicionário", "palavra", "mouse", "teclado", "computação", "água", "bombom"]

palavra = palavras[random.randrange(0, len(palavras))]

#palavra = input("Digite a palavra: ")

#os.system("clear")

print("""    O
   -|-
    ^ """)


segredo = [" _"] * len(palavra)

print(" _" * len(palavra) + "\n")


while True:
    resposta = input("Digite a letra: ")

    for i in range(len(palavra)):
        if palavra[i] == resposta.lower():
            segredo[i] = resposta
            print("")
            

    display = ""

    for char in segredo:
        display += char

    print(display + "\n")

    if " _" not in segredo:
        print(f"\nVocê ganhou!")
        break

import random
from os import system, name


def limpa_tela():
    
    #windows
    if name =='nt':
        _ = system ('cls')
    
    #linux
    else:
        _ = system('clear')

#funcao 
def game():
    
    limpa_tela()

    print("\nBem vindo ao jogo da forca!")
    print("Adivinhe a Plavra abaixo:\n")

    palavras = ['banana','uva','morango']

    palavra = random.choice(palavras)

    letras_descobertas = ['_' for letra in palavra]

    chances = 6

    letras_erradas = []

    while chances > 0:

        print(" ".join(letras_descobertas))
        print("\nChances restantes:",chances)
        print("Letras Erradas:"," ".join(letras_erradas))

        tentativa = input("\nDigite uma letra: ").lower()

        #condicao
        if tentativa in palavra:
            index = 0
            for letra in palavra:
                if tentativa == letra:
                    letras_descobertas[index] = letra
                index += 1
        else:
            chances -= 1
            letras_erradas.append(tentativa)         
        if "_" not in letras_descobertas:
            print("\nVoce venceu, a palavra era:", palavra)   
            break

    if "_" in letras_descobertas:
            print("\nVoce Perdeu, a palavra era:", palavra)   
                
if __name__ == "__main__":
    game()
    print("\nParabens vc esta aprendendo programaçao em paython com a DSA.: )\n")

import random
from os import system, name

#Funcao que limpa a tela    

def limpa_tela():
    
    #windows
    if name =='nt':
        _ = system ('cls')
    
    #linux
    else:
        _ = system('clear')

#Funçao de desenha o boneco na forca

def display_hangman(chances):
    # lista de estagios da forca
# Lista de estágios da forca
    stages = [  # estágio 6 (final)
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # estágio 5
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # estágio 4
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # estágio 3
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # estágio 2
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # estágio 1
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # estágio 0
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[chances]



def game():
    
    limpa_tela()

    print("\nBem vindo ao jogo da forca!")
    print("Adivinhe a Plavra abaixo:\n")

    palavras = ['banana','uva','morango']

    palavra = random.choice(palavras)

    #Lista de Letras da palavra
    lista_letras_palavras = [letra for letra in palavra]
    
    #cria o tabuleiro com o caracter "_" Multiplicado pelo comprimento
    tabuleiro = ["_"] * len(palavra)
    #Numero de chance
    chances = 6

    letras_tentativas = []

    #Loop enquanto número de chances for maioe do que zero
    while chances > 0:

        print(display_hangman(chances))
        print("Palavra",tabuleiro)
        print("\n")

        # Tentativas        
        tentativa = input("\nDigite uma letra: ")

        #condicao
        if tentativa in letras_tentativas:
           print("Voce ja tentou essa letra. Escolha Outra!")
           continue

        letras_tentativas.append(tentativa)
           
        if tentativa in lista_letras_palavras:
            print("Voce Acertou a Letra!")

            for indice in range(len(lista_letras_palavras)):

                if lista_letras_palavras[indice] == tentativa:
                    tabuleiro[indice] = tentativa

            if "_" not in tabuleiro:
                print("\nVoce Venceu, a palavra era:{}".format(palavra))
                break
        else:
            print("Ops. Essa Letra nao esta na palavra!")
            chances -= 1
    if "_" in tabuleiro:
        print("\nVoce perdeu! a palavra era: {}.".format(palavra))

                
if __name__ == "__main__":
    game()
    print("\nParabens vc esta aprendendo programaçao em paython com a DSA.: )\n")

# Hangman Game (Jogo da Forca) 
# Programação Orientada a Objetos

# Import
import random
from os import system, name

#funcao limpa tela

def limpa_tela():
    # windowns
    if name =='nt':
          _ = system('cls')
     #mac ou Linux
    else:
         _ = system('clear')

# Board (tabuleiro)
board = ['''

>>>>>>>>>>Hangman<<<<<<<<<<

+---+
|   |
    |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
|   |
    |
    |
=========''', '''

 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']


# Classe
class Hangman:

	# Método Construtor
     def __init__(self, palavra):
          self.palavra = palavra
          self.letras_erradas = []
          self.letras_escolhidas = []
     
	# Método para adivinhar a letra
	
     def guess(self, letra):
          if letra in self.palavra and letra not in self.letras_escolhidas:
               self.letras_escolhidas.append()
          elif letra not in self.palavra and letra not in self.letras_erradas:
               self.letras_erradas.append(letra)
          else: 
               return False
          return True
	# Método para verificar se o jogo terminou
     def hangman_over(self):

          return self.hangman_won() or (len(self.letras_erradas)== 6)
	# Método para verificar se o jogador venceu
     def hangman_won(self):

          if '_' not in self.hide_palavra():
               return True
          return False
		
	# Método para não mostrar a letra no board
     def hide_palavra(self):
          rtn = ''
          for letra in self.palavra:
              if letra not in self.letras_escolhidas:
                   rtn += '_'
              else:
                   rtn += letra
          return rtn

	# Método para checar o status do game e imprimir o board na tela
     def print_game_status(self):
          print(board[len(self.letras_erradas)])

          print ('\nPalavra: ' + self.hide_palavra())

          print('\nLetras erradas: ',)

          for letra in self.letras_erradas:
               print (letra,)
          print ()

          print('Letra corretas: ',)

          for letra in self.letras_escolhidas:
               print(letra,)
          print ()


     # lista de palavra para o jogo
def rand_palavra():

     palavra = ['banana','abacate','uva',' morango','laranja']

     palavra = random.choice(palavra)

     return palavra

# Método Main - Execuçao do Programa

def main():
     limpa_tela()

     #cria o objeto e seleciona uma palavra randomicamente
     game = Hangman(rand_palavra())

     #Enquanto o jogo nnao tiver terminado, print  do status, solicita uma letra e faz ua leitura do caracter

     while not game.hangman_over():
          
          # Status do game
          game.print_game_status()

          #recebe o input.
          user_input = input('\ndigite uma Letra: ')

          #verifica se a letra digitada faz parte da palavra
          game.guess(user_input)

     #Verifica o status do jogo
     game.print_game_status()
     if game.hangman_won():
          print('\nParabens VC Venceu!!')

     else: 
          print('\nGame Over! Voce Perdeu.')
          print('A palavra era ' + game.palavra)
     print('\n foi bom jogar com vc, agora va estudar')

if __name__ == "__main__":
     main()
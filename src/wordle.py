import random
from src.utils import print_grey,print_success,print_warning,print_error
class wordle:
     def __init__(self, file_path: str, word_len: int = 4, limit: int = 1000):
          self.word_len = word_len
          self.words = self.generate_word_frequency(file_path, word_len, limit)
          
     def generate_word_frequency(self, file_path: str, word_len: int , limit: int ):
          #Build data( words with frequency )
          words= []
          with open(file_path) as f:
               for line in f:
                    word, frequency = line.split(', ')
                    frequency = int(frequency)
                    words.append((word, frequency))

          #Filter and Sort Data        
          words = list(filter(lambda w_fre: len(w_fre[0]) == word_len, words))
          words = sorted(words, key= lambda w_fre: w_fre[1], reverse=True)

          #Limit Data
          words = words[:limit]

          #Drop Frequency Data
          words = [w_fre[0] for w_fre in words]
          
          return words

     def run(self, ):
          
          game_word = random.choice(self.words)
          game_word = game_word
          
          num_try = 6
          success = False
          
          while True:
               guess_word = input(f'Enter a {self.word_len} letter word (or q to exit): ')
               guess_word = guess_word
               if guess_word == 'q':
                    break
               #Word Length
               if len (guess_word) != self.word_len:
                    print(f'word must have {self.word_len} letters.you enterd {len(guess_word)} ! :)')
                    continue
               #check valid word
               
               if guess_word not in self.words:
                    
                    print_warning('Your word is Not valid')
                    continue
               #check valid positions 
               for game_letter, user_letter in zip(game_word, guess_word):
                    if game_letter == user_letter:
                         print_success(f' {user_letter} ', end='')
                         print(' ',end='')
                    elif user_letter in game_word:
                         print_warning(f' {user_letter} ', end='')
                         print(' ',end='')
                    else:
                         print_error(f' {user_letter} ', end='')
                         print(' ',end='')
                         
               print()
               #check success
               if game_word == guess_word:
                    print()
                    print_success('Congratulations!')
                    success = True
                    break

               num_try -=1
          if not success:
               print_warning(f'The word was {self.word} ):! GAME OVER !:(')
          
               

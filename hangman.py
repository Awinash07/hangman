import random
from collections import Counter

somewords = '''apple banana mango strawberry  
orange grape pineapple apricot lemon coconut watermelon 
cherry papaya berry peach lychee muskmelon'''

somewords = somewords.split(" ")

# randomly choose a secret word from our "somewords" LIST
word =random.choice(somewords)

if __name__ == '__main__':
    print("Guess a word! ,hint: its a fruit's name ")
    print(word)

# For printing the empty spaces for letters of the word
    for i in word:
        print("_" ,end =" ")
    print()

    playing = True
# list for storing the letters guessed by the player 
    letterguessed = ''               
    chances = len(word) + 2
    correct = 0
    flag = 0
    while ((chances!= 0) and flag == 0):
      print()
      chances -=1
      
      guess = str(input("Enter a letter"))
      print(guess)
# Validation of the guess 
      if not guess.isalpha():
          print("please enter a letter!")
          continue
      elif len(guess)>1:
          print("please enter a single letter")
          continue
      elif guess in letterguessed:
          print('You have already guessed that letter') 
          continue

      if guess in word:
          k = word.count(guess)
          for _ in range(k):
             letterguessed += guess
      
      for char in word:
          if char in letterguessed and (Counter(letterguessed) != Counter(word)):
              print(char, end = ' ') 
              correct += 1
          elif(Counter(letterguessed) == Counter(word)):
              print("The word is",end=" ")
              print(word)
              flag = 1
              print('Congratulations, You won!') 
              break # To break out of the for loop 
              break # To break out of the while loop
          else:
              print("_",end=" ")
    if chances == 0 and (Counter(letterguessed) != Counter(word)):
        print()
        print("try again!")
       
        print("the word was:",end=" ")
        print(word)




      
        
             
       





   



    





import time
import random
from hangman import hangman  #HANGMAN IS FILE WHICH IS CREATED IN THE SAME FOLDER,SO IT HAS BEEN IMPORTED 
print("Loading...")
time.sleep(6)  # THIS TO MAKE THE CODE EXECUTE AFTER 6 SECONDS

words = ["rabbit","snake","lion","tiger","eagle"]  #LIST WITH SET OF VALUES

word = random.choice(words) #PICKS UP A RANDOM VALUE
print("Welcome to the hangman game") #A WELCOME STATEMENT
def Game(word):
    guess_word = ["_" for i in word]  #THIS LIST HOLDS THE "_ _ _" BASED ON THE LENGTH OF THE WORD USED LIST COMPREHENSION
    print("Guess the word : {}".format(" _ ".join(guess_word))) #JOIN IS USED CONVERT LIST INTO STRING
    tries = 0 #NUMBER OF TURNS
    print(hangman[tries]) #INITIALLY TRIES IS ZERO SO THE INDEX 0 OF HANGMAN LIST GETS PRINTED
    
    while True: #WHILE LOOP IS SET TRUE 
        user_input = input("Enter a Word :")     #INPUT WORD FROM THE USER   
        
        if user_input in word:  #THIS BLOCK EXECUTES WHEN THE USER INPUT MATCHES THE RANDOM WORD
            index = [i for i in range(len(word)) if word[i]==user_input]    #THIS IS REPLACE THE "_" WITH THE CORRECT CHARACTER
            for i in index:
                guess_word[i] = user_input
            print(">"*20)   #THIS IS USED TO PRINT A DESIGN     
            print("good guess :{}".format("".join(guess_word)))
        
            if "".join(guess_word) == word:
                return "Wow! You Guessed...congrats"
            
                
        else:
            tries+=1
            print(hangman[tries])
            if tries == 6:
                print("you lose...")
                print("the secret word is :",word)
                break
if __name__ == "__main__":  #THIS FUNCTION CONSIDER EVERYTHING AS MAIN ONE AND EXECUTES it
    while True:
        print(Game(word)) #FUNCTION CALLING STATEMENT
          
        play = input("Do You Wanna continue(y/n) :")
        
        if play == "y":
            word = random.choice(words)
            
        else:
            break

            
    
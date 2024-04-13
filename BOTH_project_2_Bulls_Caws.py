"""
BOTH_project_2_Bulls_Caws.py: druhý projekt do Engeto Online Python Akademie Bulls and Caws

author: Pavel Both
email: pavelboth@gmail.com
discord: conjuctor Pavel Both
"""


import os
import random
import sys

######################################  DEF  ##########################################

def clear_terminal():
    if os.name == 'nt':  
        os.system('cls')
    else:  
        os.system('clear')
   
def secret_numbers():
    secret_number = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    while secret_number[0] == 0:
        random.shuffle(secret_number)
    secret_number = ''.join(map(str, secret_number[:4]))
    return secret_number    
 
def introduction():
    print("Hi there!")
    print("")
    print("WELCOME IN MY GAME >>> BULLS AND COWS <<<")
    print("-------------------------------------------------------------")
    print("Game description:")
    print("I've generated a random 4 digit number for you.")
    print("And you will guess this SECRET NUMBER .") 
    print("")
    print("Game rules:")
    print("You must enter a number with 4 unique digits, \nand the number must not start with 0. ")
    print("If you guess the digit contained in the secret number:")   
    print("   bulls - 1 point for each guessed number and its location")
    print("   caws - 1 point for each guessed number that is contained in the secret number")
    print("-------------------------------------------------------------")
    print("")
    print("Lets start the game :-) ")
    print("")
    print("-------------------------------------------------------------")
    print("h = help, e = exit")   
    print("-------------------------------------------------------------") 

def digits_error():
    print("-------------------------------------------------------------")
    print("Error: The number must contain exactly 4 different digits.")
    print("-------------------------------------------------------------")

def zero():
    print("-------------------------------------------------------------")
    print("Error: The number cannot start ' 0 '.")
    print("-------------------------------------------------------------")

def bulls():
    i = 0
    bull = 0
    for x in inserted_number:
        if inserted_number[i] == str(secret_number[i]):
            bull += 1
        i +=1 
    return bull

def caws():         
    caw = 0 
    for number in inserted_number:
        if number in str(secret_number):
            caw += 1
    return caw
    
def score():
    print("-------------------------------------------------------------")
    if bull < 2:
        print(f"bull > {bull} <") 
    else:
        print(f"bulls > {bull} <") 
    if caw < 2:
        print(f"caw > {caw} <") 
    else: 
        print(f"caws > {caw} <")
    print("-------------------------------------------------------------")      

def win():
    print("GREAT, YOU GESSED THE SECRET NUMBER")
    print(f"Number of attemps: {attemps}")
    print("-------------------------------------------------------------")

def gave_up():
    print("-------------------------------------------------------------")
    print("YOU GAVE UP  :-(")
    print("-------------------------------------------------------------")

def digit_help():
    print("-------------------------------------------------------------")  
    print(f"The first secret number is - {secret_number[help_no_1]} _ _ _ -")
    print("-------------------------------------------------------------")  
    

def end_game():
    clear_terminal()
    print("-------------------------------------------------------------")
    print("GAME OVER - THANK YOU")
    print("-------------------------------------------------------------")
    print("YOUR GAME STATISTICS:")
    print("-------------------------------------------------------------")
    print(f"Total guessed numbers: {guess_numbers}")
    print (f"Total attemps: {all_attemps}")
    print (f"Total success rate: {round(guess_numbers/all_attemps * 100, 2)} %")
    print(f"Average number of attempts per guessed number: {round(all_attemps/guess_numbers)}")
    print("-------------------------------------------------------------")       

def new_game():
    print("Great, a new geme begins :-)")
    print("-------------------------------------------------------------")
    print("I've generated new random 4 digit number for you.")
    print("h = help, e = exit")  
    print("-------------------------------------------------------------")

######################################  DEF  ##########################################

######################################  MAIN PROGRAM  ##########################################

clear_terminal()
introduction()
guess_numbers = 0
all_attemps = 0
help_no_1 = 0
bull = 0
caw = 0    
repete = ("y")
while repete != "n":
    secret_number = secret_numbers()
    #print(secret_number) # only for check of the secret number and for testing
    inserted_number = str("0")
    attemps = 0
    while inserted_number != secret_number:
        attemps += 1 
        inserted_number = str(input(f"Attemp no.: {attemps},  Enter a new number : "))
        if inserted_number == secret_number:
            print("")
        elif inserted_number == "e":
            gave_up()
            sys.exit()
        elif inserted_number == "h":  
            digit_help()
        elif not inserted_number.isdigit(): 
            digits_error()
        elif len(inserted_number) != 4: 
            digits_error()
        elif len(set(inserted_number)) < 4: 
            digits_error()
        elif inserted_number[0] == "0":
            zero()       
        else:
            bull = bulls()
            caw = caws()
            score()                           
        
    else:  
        win()      
        repete = input("Play again? y / n :  ")
        guess_numbers += 1
        all_attemps += attemps
        
    while repete != "y" and repete != "n": 
        repete = input("Play again? y / n :  ")
    else:
        if repete == "y":
            clear_terminal()
            new_game()
        else:
            end_game()

######################################  MAIN PROGRAM  ##########################################

            

            
  
                

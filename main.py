import random
import json
import time

# Python Password Generator made by zzixM
# instagram handle: @zzixm_
# github handle: https://github.com/zzixM

def passwordGen():
    uppercaseLetters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lowercaseLetters = uppercaseLetters.lower()
    didgits = "0123456789"
    specialChrs =  "!?_#@:;\\/*."

    upper, lower, nums, special = True, True, True, True

    all = ""
    if upper:
        all += uppercaseLetters
    if lower:
        all += lowercaseLetters
    if nums:
        all += didgits
    if special:
        all += specialChrs

    validLength = False
    while validLength == False:
        length = input(str("How long do you want the password to be? "))

        try:
            length = int(length)

            if length > 3 and length < 25:
                validLength = True
            else:
                print("Please keep the length between 4 and 24. \n")
    
        except TypeError as e:
            print("Please enter an number between 4 and 24\n")
    
        except ValueError as e:
            print("Please enter an number between 4 and 24\n")
    

    validAmount = False
    while validAmount == False:
        amount = input(str("How many passwords do you want? "))

        try:
            amount = int(amount)

            if amount > 1 and amount < 21:
                validAmount = True
            else:
                print("please keep the amount between 2 and 20\n")
    
        except TypeError as e:
            print("Please enter an number between 2 and 20\n")
    
        except ValueError as e:
            print("Please enter an number between 2 and 20\n")
    
    print(f"\nGenerating password of length \"{length}\".")
    print(f"\nGenerating \"{amount}\" passwords.\n")

    choicNum = 0  
    passwords = {
        
    }
    passwords["passwords"] = []

    for x in range(amount):
        password = "".join(random.sample(all, length))
        print(f"Password {choicNum} = {password}")
        choicNum = choicNum + 1 

        passwords["passwords"].append({choicNum : password})

    validUserChoice = False
    while validUserChoice == False:
        userChoice = input(str("\nWARNING: Do you want to save the generated passwords to a file?\nNote: the passwords will be saved in plain text. "))
        userChoice.lower()

        if userChoice == "yes":
            savePasswords(passwords)
            validUserChoice = True
    
        elif userChoice == "no":
            startMenu()
            validUserChoice = True
    
        else:
            print("\nplease answer yes or no.\n")


def getPasswords():
    
    with open('passwords.json', 'r') as readFile:
        usersPasswords = json.load(readFile)
        print(usersPasswords)
        readFile.close()

def savePasswords(passwords):

    validUserChoice = False
    while validUserChoice == False:
        userChoice = input(str("\nWARNING: You are about to save the generated passwords to a file. Are you sure?\nNote: the passwords will be saved in plain text. "))
        userChoice.lower()

        if userChoice == "yes":
            validUserChoice = True
    
        elif userChoice == "no":
            startMenu()
            validUserChoice = True
    
        else:
            print("\nplease answer yes or no.\n")
    
    with open ('passwords.json', 'w') as saveFile:
        json.dump(passwords, saveFile, indent = 4)
        print("Passwords saved")
        saveFile.close()
    
    startMenu()

def startMenu():
    
    print("")
    print("Welcome to zzixMs password generator\n")
    userChoice = input(str("Would you like to: \n1. Generate a Passwords \n2. Read Passwords\n3. Exit\n> "))

    if userChoice == "1":
        passwordGen()
    
    elif userChoice == "2":
        getPasswords()
    
    elif userChoice == "3":
        exit()
    
    else:
        startMenu()

if __name__ == "__main__":
    startMenu()
import random
import json

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
    choicNum = 1
    
    passwords = {

    }
    passwords["passwords"] = []

    for x in range(amount):
        password = "".join(random.sample(all, length))
        print(f"Password {choicNum} = {password}")
        choicNum = choicNum + 1 

        passwords["passwords"].append({choicNum : password})

    
    print(passwords)
    
    #savePasswords(passwords)


def getPasswords():
    pass

def savePasswords(passwords):
    pass

def startMenu():
    
    userChoice = input(str("Would you like to: \n1. Generate a Password \n2. Exit\n> "))

    if userChoice == "1":
        passwordGen()
    
    elif userChoice == "2":
        exit()
    
    else:
        startMenu()

if __name__ == "__main__":
    startMenu()
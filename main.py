import pyfiglet
from colorama import Fore
from authentication import sign_up
from authentication import sign_in

from hash_functions import hashing_menu

from RSA_encryption import rsa_menu

from certificate import certif_menu

def big_menu():
    print("~~~~ Please choose which function to try ! ~~~~")
    print("~~~~ 1 - Hash ~~~~")
    print("~~~~ 2 - RSA ~~~~")
    print("~~~~ 3 - Certificate ~~~~")
    print("~~~~ 0 - Back ~~~~")
    
text = pyfiglet.figlet_format("CryptoBox",justify="center",font="big")
print (Fore.GREEN + text)     
def welcome():
    print("~~~~ Welcome ~~~~")
    print("~~~~ 1 - Sign up ~~~~")
    print("~~~~ 2 - Sign in ~~~~")
    print("~~~~ 0 - Quit ~~~~")
def main():
        while True:
            choice = int(input("Enter your choice: "))
            match choice:
                case 1:
                    sign_up()
                    big_menu()
                    choix = int(input("Enter your choice: "))
                    match choix:
                        case 1: hashing_menu()
                        case 2: rsa_menu()
                        case 3: certif_menu()
                        case 0: quit() 
                        case default: print("Invalid option, please try again.")
    
                case 2:  
                    sign_in()
                    big_menu()
                    choix = int(input())
                    match choix:
                        case 1: hashing_menu()
                        case 2: rsa_menu()
                        case 3: certif_menu()
                        case 0: quit() 
                        case default: print("Invalid option, please try again.")
                case 0: 
                    quit()
                case default:
                    print("Error input")
                    """while True:
                        welcome()
                        break"""
            break
if __name__ == '__main__':
    welcome()
    main()
    
    

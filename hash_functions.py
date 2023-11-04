import hashlib
import bcrypt

def hash_word_sha256():
    word = input ('word:  ')
    sha256_hash = hashlib.sha256(word.encode()).hexdigest()
    print(sha256_hash)
    f = open ("hash_256.txt","w")
    f.write(sha256_hash)
    f.close()

def hash_word_bcrypt():
    word = input ('word: ')
    word_encoded = word.encode()
    salt = bcrypt.gensalt()
    bcrypt_hash = bcrypt.hashpw(word_encoded, salt)
    print (bcrypt_hash)
    f = open ("hash_bcrypt.txt","wb")
    f.write(bcrypt_hash)
    f.close()

def dictionary_attack():
    # Check if the word is present in the dictionary
        with open("dict.txt",'r') as dict_file:
            words = dict_file.read().splitlines()

        with open("hash_256.txt", 'r') as hashed_file:
            hashed_password = hashed_file.read().strip()
        for word in words:
            hashed_word = hashlib.sha256(word.encode()).hexdigest()
            if hashed_word == hashed_password:
                print (f"----- Password found !!!! : {word}  ------ ")
                print ("\n")
                break
            else : 
                print ("Sowwy! We couldn't find the password \n.Stay ethical tho.\n")
                break


def hashing_menu():
    while True:
        print("Hashing Menu:")
        print("1. Hash the word with SHA-256")
        print("2. Hash the word with a salt (bcrypt)")
        print("3. Dictionary attack on the hashed word")
        print("4. Quit")
        choice = input("Choose an option: ")

        if choice == "1":
            sha256_hash = hash_word_sha256()
            print(f"Hashed word with SHA-256!  ")
        elif choice == "2":
            bcrypt_hash = hash_word_bcrypt()
            print(f"Hashed word with bcrypt!  ")
        elif choice == "3":
            word = input("Enter the  word to  attack: ")
            attack_result = dictionary_attack()
        elif choice == "4":
            break
        else:
            print("Invalid option, please try again.")

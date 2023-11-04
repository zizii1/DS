import hashlib
import string
import random  #or secrets
import re
import maskpass


def isValid(email):
        regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
        if re.fullmatch(regex, email):
            return True
        else:
            return False
        
     

def sign_up():
    while True:  
            x=0  
            email=input("give ur email      ") 
            if isValid(email)  :
                x=1
                break
            else : 
                print("enter ur email again")
    while True:
            flag=0 
            pwd =maskpass.askpass(prompt="tap ur Password:",mask="#")
            if (len(pwd) >= 8 and
                re.search(r'[A-Z]', pwd) and
                re.search(r'[a-z]', pwd) and
                re.search(r'[!@#$%^&*_?]', pwd) and
                re.search(r'\d', pwd)):
                pwd_hash= hashlib.sha1(pwd.encode()).hexdigest()
                flag=1
                break 
            else :
                print ("incorrect password")     
    if (x==1 and flag == 1) :
        f = open ("db.txt","a")
        f.write("\n")
        f.write (email)
        f.write("---")
        f.write(pwd_hash)
        f.close

def sign_in():
    email=input ("tap ur email    ")
    pwd = maskpass.askpass ("tap ur password : ",mask="*")
    pwd_hash= hashlib.sha1(pwd.encode()).hexdigest()
    concat= email+"---"+pwd_hash
    f= open ("db.txt","r")
    x=1
    
    for ligne in f:
        if (ligne.strip() == concat) :
            x=(0)
            print ("Signed in!")
        else :
            print ("Error. Email or password is wrong ")  

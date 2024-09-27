#random password generator-----------


import string 
import random

password=""
print("----------------WELCOME TO RANDOM PASSWORD GENERATOR----------------")
while(True):
    length=int(input("ENTER THE LENGTH OF THE REQUIRED PASSWORD: "))
    password+="".join(random.choices(string.ascii_letters+string.digits+string.punctuation, k=length))
    print(f"YOUR GENERATED PASSWORD IS: {password}")
    user=input("DO YOU WANT TO CONTINUE (YES/NO): ")
    if(user.upper()=="NO"):
        break
import hashlib

#start this function is showing User what you want ? log in or create account
def start():
    with open('start.txt','r') as file2:
        lines = file2.readlines()
    countline=len(lines)
    with open('start.txt', 'r') as file:
        data = file.readline()
        while data is not None and data != "":
            print(data, end="")
            data = file.readline()
        print(end="\n")
        o = int(input("Enter Option Number: "))
        while o not in range(1,countline+1):
            print("Invalid Option")
            o = int(input("Please Enter Correct Option Number: "))
        return o

#veracity and signin function are the log in system part
def veracity(acid,pw):
    with open('veracity.txt', 'r') as ver:
        readver = ver.readline()
        while readver !="":
            a,b = readver.split()
            if acid == a:
                if pw == b:
                   return True
            readver = ver.readline()
        print("Wrong accountid or password")
        return False


def signin():
    ver = False
    while ver is False:
        acid = input("ID: ")
        pw = hashlib.sha512(input("PW: ").encode(encoding="utf-8")).hexdigest()
        if veracity(acid,pw) is True:
            ver = True
    print ("LogIn successful")


#after log in, menu function will show the option that user can choose in the booking system
def menu():
    with open('menu.txt','r') as file2:
        lines = file2.readlines()
    countline=len(lines)
    with open('menu.txt', 'r') as file:
        data = file.readline()
        while data is not None and data != "":
            print(data, end="")
            data = file.readline()
        print(end="\n")
        o = int(input("Enter Option Number: "))
        while o not in range(1,countline+1):
            print("Invalid Option")
            o = int(input("Please Enter Correct Option Number: "))
        return o

#This function is for create account.
def createaccount():
    acid=input("enter Account ID number: ")
    with open("veracity.txt",'r') as searching:
        for line in searching:
            if line.split()[0]==acid:
                print("Account ID number has been in database")
                return None
        acpw = hashlib.sha512(input("enter Account Password: ").encode(encoding="utf-8")).hexdigest()
        confrim = hashlib.sha512(input("enter Confirm Password: ").encode(encoding="utf-8")).hexdigest()
        while acpw!=confrim:
            acpw = hashlib.sha512(input("Please enter  again Account Password: ").encode(encoding="utf-8")).hexdigest()
            confrim = hashlib.sha512(input("enter Confirm Password: ").encode(encoding="utf-8")).hexdigest()
    with open("veracity.txt",'a') as adding:
        adding.write(f"{acid} {acpw}\n")
        print("Account Created")
        return None

#This part is the booking system how to run
systeminform="running"
while systeminform !="exit":
    userstartingoption = start()
    if userstartingoption == 1:
        signin()
        useroption = 0
        while useroption !=9:
            useroption=menu()
            if useroption ==1:
                booking()
                useroption=menu()
            elif useroption ==2:
                viewbooking()
                useroption=menu()
    elif userstartingoption == 2:
        createaccount()
    elif userstartingoption ==3:
        break
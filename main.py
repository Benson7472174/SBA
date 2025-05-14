#start this function is showing User what you want ? log in or create account
import hashlib


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
        print("Wrong ac or pw")
        return False


def signin():
    ver = False
    while ver is False:
        acid = input("ID: ")
        pw = input("PW: ")
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
    created=False
    while created is False:
        acid = input("Enter Account Number: ")
        acpw = hashlib.sha512(input("Enter Password: ").encode(encoding="utf-8")).hexdigest()
        confirm = hashlib.sha512(input("Confirm Password: ").encode(encoding="utf-8")).hexdigest()
        while confirm != acpw:
            print("Repeated Account Id or Wrong Password")
            acid=input("Enter Account Number: ")
            acpw=hashlib.sha512(input("Enter Account Password: ").encode(encoding="utf-8")).hexdigest()
            confirm=hashlib.sha512(input("Confirm Password: ").encode(encoding="utf-8")).hexdigest()
            with open('veracity.txt','r') as find:
                sameid=find.readline()
                while sameid is not None:
                    if sameid == acid:
                        print("Account already exists")
                        break
                    sameid=find.readline()
                created=True
    with open('veracity.txt','a+') as addaccount:
        addaccount.write(f"{acid} {acpw}\n")
        return

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
        print("Account Created")
    elif userstartingoption ==3:
        break



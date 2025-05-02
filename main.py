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
        
        
step=start()
if step ==1:
    signin()
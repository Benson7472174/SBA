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


signin()

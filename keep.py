def veracity(acid,pw):
    ver = None
    while ver is None:
        with open('veracity.txt','r') as veracity:
            countac=len(veracity.readlines)
            for i in range(0,countac+1):
                readver=veracity.readline()
                a,b=readver.split()
                if acid==a:
                    if pw==b:
                        return True
            print("Wrong ac or pw")

def signin():
    ver=None
    while ver is None:
        acid=input("ID: ")
        pw=input("PW: ")
        if ver(acid,pw) is True:
            break
    print("LogIn successful")


signin()

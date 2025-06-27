import hashlib

def hashlibsha512(a):
    o=hashlib.sha512(a.encode(encoding="utf-8")).hexdigest()
    return o

def isdifferent(search):
    with open("veracity.txt",'r') as searching:
        searchingitem=searching.readline().split()
        while searchingitem is not None:
            if hashlibsha512(search)==searchingitem[0]:
                return False
            searchingitem=searching.readline().split()
        return True

def createaccount():
    acid=input("Enter your Id: ")
    while acid is None or isdifferent(acid) is False:
        print("Your acid is empty or has been used ")
        acid=input("Enter your Id: ")
    acpw=input("Enter your password: ")
    confirm=input("Enter your password again: ")
    while acpw!=confirm:
        print("Your password is not same.")
        acpw=input("Enter your password: ")
        confirm=input("Enter your password again: ")
    with open("veracity.txt",'a') as adddata:
        acid=hashlibsha512(acid)
        acpw=hashlibsha512(acpw)
        adddata.write(f'{acid} {acpw}')
    return



createaccount()
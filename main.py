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
def SignIn():
    successful_account = 0
    account=input("Enter Account: ")
    password=input("Enter Password: ")
    verify=(account,password)
    return verify



print(SignIn())
ending=0
starting = start()
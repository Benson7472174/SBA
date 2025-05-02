def start():
    with open('start.txt','r') as file:
        data = file.readline()
        while data is not None and data!="":
            print(data,end="")
            data = file.readline()
start()


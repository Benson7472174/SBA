import getpass
import hashlib
import pymysql
import datetime
import string
import random

def validate_date(date):
    try:
        datetime.datetime.strptime(date, "%Y-%m-%d")
        return True
    except BaseException:
        return False

def validate_time(a,b):
    try:
        datetime.datetime.strptime(a, "%H:%M")
        datetime.datetime.strptime(b, "%H:%M")
    except BaseException:
        return False
    else:
        a = datetime.datetime.strptime(a, "%H:%M")
        b = datetime.datetime.strptime(b, "%H:%M")
        if b-a<datetime.timedelta(hours=1):
            return False
        else:
            return True

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
        print("Wrong account id or password")
        return False


def signin():
    ver = False
    while ver is False:
        acid = input("ID: ")
        pw = hashlib.sha512(input("Password: ").encode(encoding="utf-8")).hexdigest()
        if veracity(acid, pw):
            ver = True
    print ("LogIn successful")
    return acid

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

def viewbooking(acid):
    conn = pymysql.connect(host='localhost',
                           user='root',
                           password='v(e_8EP<loby',
                           db='studyroom_system')
    cursor = conn.cursor()
    sql = f"select * from booking where User_ID='{acid}'"
    cursor.execute(sql)
    records = cursor.fetchall()
    for record in records:
        bookingid = record[0]
        seat_id = record[1]
        date = record[2]
        start_time = record[3]
        end_time = record[4]
        print(bookingid, seat_id, date, start_time, end_time)

def generate_booking_id():
    characters = string.digits + string.ascii_uppercase
    return ''.join(random.choices(characters, k=8))

def check_seat_availability(date,seat_id, start_time, end_time):
    connect = pymysql.connect(host='localhost',
                           user='root',
                           password='v(e_8EP<loby',
                           db='studyroom_system')
    cursor = connect.cursor()
    cursor.execute(f"select * from booking where Date='{date}' and Seat_id = '{seat_id}' and ((Start_Time <= '{start_time}' and End_Time BETWEEN'{start_time}' and '{end_time}') or (Start_Time <= '{start_time}' and End_Time >= '{end_time}') or (End_Time >= '{end_time}' and Start_Time between '{start_time}' and '{end_time}'))" )
    if cursor.fetchone() is None:
        return True
    else:
        return False

def get_available_seats(date,start_time,end_time,zone_id):
    connect = pymysql.connect(host='localhost',
                           user='root',
                           password='v(e_8EP<loby',
                           db='studyroom_system')
    cursor = connect.cursor()
    cursor.execute(f"SELECT Seat_ID FROM seat WHERE Zone_ID = '{zone_id}'")
    all_seats =[row[0] for row in cursor.fetchall()]
    available_seats = []
    for seat_id in all_seats:
        if check_seat_availability(date,seat_id, start_time, end_time):
            available_seats.append(seat_id)
    return available_seats

def overlap(acid,start_time,end_time,date):
    connect = pymysql.connect(host='localhost',
                           user='root',
                           password='v(e_8EP<loby',
                           db='studyroom_system')
    cursor = connect.cursor()
    cursor.execute(f"select * from booking where Date='{date}' and User_ID = '{acid}' and ((Start_Time <= '{start_time}' and End_Time BETWEEN'{start_time}' and '{end_time}') or (Start_Time <= '{start_time}' and End_Time >= '{end_time}') or (End_Time >= '{end_time}' and Start_Time between '{start_time}' and '{end_time}'))" )
    if cursor.fetchone() is None:
        return True
    else:
        return False

def booking(acid):
    connect = pymysql.connect(host='localhost',
                           user='root',
                           password='v(e_8EP<loby',
                           db='studyroom_system')
    cursor = connect.cursor()
    print("="*50)
    print("Study Room Booking System")
    print("="*50)
    date = input("Please Enter Which Date You Need To Book?(YYYY-MM-DD): ")
    while not validate_date(date):
        date=input("Please Enter Again Which Date You Need To Book?(YYYY-MM-DD): ")
    date = datetime.datetime.strptime(date, "%Y-%m-%d")
    start_time,end_time = input("Please Enter Start Time And End Time, At Least 1 Hour(HH:MM-HH:MM): ").split("-")
    while not validate_time(start_time, end_time):
        print("Invalid Time")
        start_time, end_time = input("Please Enter Again Start Time And End Time, At Least 1 Hour(HH:MM-HH:MM): ").split("-")
    start_time = datetime.datetime.strptime(start_time, "%H:%M")
    end_time = datetime.datetime.strptime(end_time, "%H:%M")
    if not overlap(acid,start_time,end_time,date):
        print("You Can't Book As You Have Overlap Other Bookings.")
        return None
    cursor.execute(f"select * from zone")
    zones = cursor.fetchall()
    print("-"*50)
    print(" " * 10 + "STUDY ZONES")
    print("-"*50)
    print(f"{'Zone ID':<10}{'Capacity':<15}{'Power':<10}{'Quiet':<10}{'Description':<20}")
    print("-"*50)
    for zone in zones:
        print(zone[0],"\t",zone[2],"\t",zone[3],"\t",zone[4],"\t",zone[5])
    zone_id=input("Please Enter Which Zone You Need To Book?(A/B/C/D): ")
    while zone_id not in ["A", "B", "C", "D"]:
        print("Invalid Zone Selected")
        zone=input("Please Enter Again Which Zone You Need To Book?(A/B/C/D): ")
    print("There Are The Available Seats")
    available_seats = get_available_seats(date, start_time, end_time, zone_id)
    print("\n" + "-"*50)
    print(f"Available seats in Zone {zone_id}:")
    print("-"*50)
    for i, seat in enumerate(available_seats, 1):
        print(seat, end="\t")
        if i % 5 == 0:
            print()
    seat_id = input("Please Enter Seat ID: ").upper()
    while seat_id not in (get_available_seats(date,start_time,end_time,zone_id)):
        print("Invalid Seat ID")
        seat_id = input("Please Enter Again Seat ID: ").upper()
    booking_id = generate_booking_id()
    print("\n" + "="*50)
    print(" " * 15 + "BOOKING INFORMATION")
    print("="*50)
    print(f"{'Booking ID:':<15} {booking_id}")
    print(f"{'Seat ID:':<15} {seat_id}")
    print(f"{'Date:':<15} {date.strftime('%Y-%m-%d')}")
    print(f"{'Start Time:':<15} {start_time.strftime('%H:%M')}")
    print(f"{'End Time:':<15} {end_time.strftime('%H:%M')}")
    print(f"{'Zone:':<15} {zone_id}")
    print("="*50 + "\n")
    confirm = input("Confirm Booking?(Y/N): ").upper()
    if confirm == "Y":
        sql=f"insert into booking (Booking_ID, User_ID, Seat_ID, Date, Start_Time, End_Time) values ('{booking_id}','{acid}','{seat_id}','{date}','{start_time}','{end_time}')"
        cursor.execute(sql)
        print("Booking Has Been Added")
    else:
        print("Booking Has Been Canceled")
    connect.commit()
    return None

#This part is the booking system how to run
systeminform="running"
while systeminform !="exit":
    userstartingoption = start()
    if userstartingoption == 1:
        acid=signin()
        useroption = 0
        while useroption !=9:
            useroption = menu()
            if useroption ==1:
                booking(acid)
            elif useroption ==2:
                viewbooking(acid)
            elif useroption ==3:
                break
    elif userstartingoption == 2:
        createaccount()
    elif userstartingoption ==3:
        break
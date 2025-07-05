import pymysql
import datetime
import string
import random

def validate_date(date):
    try:
        datetime.datetime.strptime(date, "%Y-%m-%d")
        return True
    except ValueError:
        return False

def validate_time(a,b):
    try:
        datetime.datetime.strptime(a, "%H:%M")
        datetime.datetime.strptime(b, "%H:%M")
    except ValueError:
        return False
    else:
        a = datetime.datetime.strptime(a, "%H:%M")
        b = datetime.datetime.strptime(b, "%H:%M")
        if b-a<datetime.timedelta(hours=1):
            return False
        else:
            return True

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
    date = input("Please Enter Which Date You Need To Book?(YYYY-MM-DD): ")
    while not validate_date(date):
        date=input("Please Enter Again Which Date You Need To Book?(YYYY-MM-DD): ")
    date = datetime.datetime.strptime(date, "%Y-%m-%d")
    start_time,end_time = input("Please Enter Start Time And End Time, At Least 1 Hour(HH:MM-HH:MM): ").split("-")
    while not validate_time(start_time, end_time):
        print("Invalid Time")
        start_time = input("Please Enter Again Start Time(HH:MM): ")
        end_time = int(input("Please Enter Using Time(At least 1 Hour): "))
    start_time = datetime.datetime.strptime(start_time, "%H:%M")
    end_time = datetime.datetime.strptime(end_time, "%H:%M")
    if not overlap(acid,start_time,end_time,date):
        print("You Can't Book As You Have Overlap Other Bookings.")
        return None
    cursor.execute(f"select * from zone")
    zones = cursor.fetchall()
    print("Zone_ID Number_Of_People_Can_Be_Available Has_Power Is_Quiet Description")
    for zone in zones:
        print(zone[0], zone[2], zone[3], zone[4], zone[5])
    zone_id=input("Please Enter Which Zone You Need To Book?(A/B/C/D): ")
    while zone_id not in ["A", "B", "C", "D"]:
        print("Invalid Zone Selected")
        zone=input("Please Enter Again Which Zone You Need To Book?(A/B/C/D): ")
    print("There Are The Available Seats")
    print(get_available_seats(date,start_time,end_time,zone_id))
    seat_id = input("Please Enter Seat ID: ")
    while seat_id not in (get_available_seats(date,start_time,end_time,zone_id)):
        print("Invalid Seat ID")
        seat_id = input("Please Enter Seat ID: ")
    bookingid = generate_booking_id()
    print("There Is Your Booking Information")
    print("Booking_ID: ",bookingid)
    print("Seat_ID: ",seat_id)
    print("Date: ",date)
    print("Start Time: ",start_time)
    print("End Time: ",end_time)
    confirm = input("Confirm Booking?(Y/N): ")
    if confirm == "Y":
        sql=f"insert into booking (Booking_ID, User_ID, Seat_ID, Date, Start_Time, End_Time) values ('{bookingid}','{acid}','{seat_id}','{date}','{start_time}','{end_time}')"
        cursor.execute(sql)
        print("Booking Has Been Added")
    else:
        print("Booking Has Been Canceled")
    connect.commit()
    return None
booking("student")
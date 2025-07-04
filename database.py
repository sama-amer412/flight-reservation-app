import sqlite3
import os
import sys


# ⬇ Get correct path for .exe and .py
def get_db_path():
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, "flights.db")


def book_flight(name,flight_number,departure,destination,date,seat_number,time):

    db_path = get_db_path()
    con = sqlite3.connect(db_path)
    cur=con.cursor()
    # cur.execute("DROP TABLE flights")
    cur.execute("""CREATE TABLE IF NOT EXISTS flights (
    reservation_id INTEGER PRIMARY KEY AUTOINCREMENT,
    Name TEXT,
    Flight_Number TEXT,
    Departure TEXT,
    Destination TEXT,
    Date TEXT,
    Seat_Number TEXT,
    Time TEXT)""")
    cur.execute("""INSERT INTO flights (Name,Flight_Number,Departure,Destination,Date,Seat_Number,Time) 
     VALUES(?,?,?,?,?,?,?)""",(name,flight_number,departure,destination,date,seat_number,time))


    con.commit()
    con.close()
def view_reservation():
    db_path = get_db_path()
    con = sqlite3.connect(db_path)
    cur = con.cursor()
    stored_data=cur.execute("SELECT * FROM flights ")
    data=[]
    for row in stored_data:
        data.append(row)

    con.commit()
    con.close()
    return data
def delete_reservation(reservation_id):
    # con = sqlite3.connect("flights.db")
    db_path = get_db_path()
    con = sqlite3.connect(db_path)
    cur = con.cursor()
    cur.execute("DELETE FROM flights WHERE reservation_id=? ",(reservation_id,))
    con.commit()
    con.close()
    return True
def edit_reservation(reservation_id,updated_lst):

     # con=sqlite3.connect("flights.db")
     db_path = get_db_path()
     con = sqlite3.connect(db_path)
     cur=con.cursor()
     cur.execute("""UPDATE flights SET
      Name=? ,
      Flight_Number=? ,
      Departure=?,
      Destination=?,
      Date=?,
      Seat_Number=?,
      Time=?
     WHERE reservation_id=?""",(*updated_lst,reservation_id))
     con.commit()
     con.close()
     return True


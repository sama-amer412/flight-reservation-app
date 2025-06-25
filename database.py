import sqlite3

def book_flight(name,flight_number,departure,destination,date,seat_number):
    con=sqlite3.connect("flights.db")
    cur=con.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS flights (
    reservation_id INTEGER PRIMARY KEY AUTOINCREMENT,
    Name TEXT,
    Flight_Number TEXT,
    Departure TEXT,
    Destination TEXT,
    Date TEXT,
    Seat_Number TEXT)""")
    cur.execute("""INSERT INTO flights (Name,Flight_Number,Departure,Destination,Date,Seat_Number) 
    VALUES(?,?,?,?,?,?)""",(name,flight_number,departure,destination,date,seat_number))


    con.commit()
    con.close()
def view_reservation():
    con = sqlite3.connect("flights.db")
    cur = con.cursor()
    stored_data=cur.execute("SELECT * FROM flights ")
    data=[]
    for row in stored_data:
        data.append(row)

    con.commit()
    con.close()
    return data
def delete_reservation(reservation_id):
    con = sqlite3.connect("flights.db")
    cur = con.cursor()
    cur.execute("DELETE FROM flights WHERE reservation_id=? ",(reservation_id,))
    con.commit()
    con.close()
    return True
def edit_reservation(reservation_id,updated_lst):

     con=sqlite3.connect("flights.db")
     cur=con.cursor()
     cur.execute("""UPDATE flights SET
      Name=? ,
      Flight_Number=? ,
      Departure=?,
      Destination=?,
      Date=?,
      Seat_Number=?
     WHERE reservation_id=?""",(*updated_lst,reservation_id))
     con.commit()
     con.close()
     return True


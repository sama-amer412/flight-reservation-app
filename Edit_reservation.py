from tkinter import *
from tkinter import messagebox
from database import edit_reservation
from PIL import Image, ImageTk
import os
import sys
from tkcalendar import DateEntry
from tkinter import ttk

def edit_reservation_page(root, old_reservation_data, show_reservation_callback):
    screenwidth = root.winfo_screenwidth()
    screenheight = root.winfo_screenheight()
    canvas = Canvas(root, width=screenwidth, height=screenheight)
    canvas.pack(fill="both", expand=True)

    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    image_path = os.path.join(base_path, "images", "background.jpg")

    bg_image = Image.open(image_path)
    bg_image = bg_image.resize((screenwidth, screenheight))
    bg_photo = ImageTk.PhotoImage(bg_image)
    canvas.create_image(0, 0, anchor=NW, image=bg_photo)
    canvas.bg_photo = bg_photo  # Prevent garbage collection
    #old reservation data
    reservation_id=old_reservation_data[0]
    name_val=StringVar(value=old_reservation_data[1])
    flight_name_val=StringVar(value=old_reservation_data[2])
    departure_val=StringVar(value=old_reservation_data[3])
    destination_val=StringVar(value=old_reservation_data[4])
    date_val=StringVar(value=old_reservation_data[5])
    seat_val=StringVar(value=old_reservation_data[6])
    time_val=StringVar(value=old_reservation_data[7])

    # the data needed for reservation
    flight_schedule = {
        "Monday": [
            {"flight": "FS101", "from": "Cairo", "to": "Dubai", "time": "08:00"},
            {"flight": "FS201", "from": "New York", "to": "London", "time": "07:45"},
            {"flight": "FS301", "from": "Paris", "to": "Tokyo", "time": "13:00"},
            {"flight": "FS401", "from": "London", "to": "Berlin", "time": "09:30"},
        ],
        "Tuesday": [
            {"flight": "FS104", "from": "Cairo", "to": "Riyadh", "time": "09:00"},
            {"flight": "FS202", "from": "New York", "to": "Toronto", "time": "10:15"},
            {"flight": "FS302", "from": "Paris", "to": "Rome", "time": "12:50"},
            {"flight": "FS402", "from": "London", "to": "Madrid", "time": "16:30"},
        ],
        "Wednesday": [
            {"flight": "FS103", "from": "Cairo", "to": "Doha", "time": "16:45"},
            {"flight": "FS203", "from": "New York", "to": "Chicago", "time": "14:00"},
            {"flight": "FS303", "from": "Paris", "to": "Vienna", "time": "11:00"},
            {"flight": "FS403", "from": "London", "to": "Amsterdam", "time": "13:30"},
        ],
        "Thursday": [
            {"flight": "FS101", "from": "Cairo", "to": "Dubai", "time": "08:00"},
            {"flight": "FS204", "from": "New York", "to": "San Francisco", "time": "17:00"},
            {"flight": "FS304", "from": "Paris", "to": "Zurich", "time": "10:30"},
            {"flight": "FS404", "from": "London", "to": "Brussels", "time": "18:45"},
        ],
        "Friday": [
            {"flight": "FS102", "from": "Cairo", "to": "Jeddah", "time": "12:30"},
            {"flight": "FS205", "from": "New York", "to": "Miami", "time": "09:00"},
            {"flight": "FS305", "from": "Paris", "to": "Barcelona", "time": "13:15"},
            {"flight": "FS405", "from": "London", "to": "Lisbon", "time": "15:30"},
        ],
        "Saturday": [
            {"flight": "FS105", "from": "Cairo", "to": "Istanbul", "time": "14:00"},
            {"flight": "FS206", "from": "New York", "to": "Boston", "time": "07:00"},
            {"flight": "FS306", "from": "Paris", "to": "Munich", "time": "11:45"},
            {"flight": "FS406", "from": "London", "to": "Stockholm", "time": "17:00"},
        ],
        "Sunday": [
            {"flight": "FS110", "from": "Cairo", "to": "Abu Dhabi", "time": "13:45"},
            {"flight": "FS207", "from": "New York", "to": "Los Angeles", "time": "15:30"},
            {"flight": "FS307", "from": "Paris", "to": "Prague", "time": "10:20"},
            {"flight": "FS407", "from": "London", "to": "Oslo", "time": "12:00"},
        ]
    }

    # the booking form
    avl_dep = []
    avl_des = []




    # Transparent card (rectangle)
    card_x1 = screenwidth / 2 - 230
    card_y1 = screenheight / 2 - 320
    card_x2 = screenwidth / 2 + 230
    card_y2 = screenheight / 2 + 280

    canvas.create_rectangle(card_x1, card_y1, card_x2, card_y2, fill="#4682B4", outline="", stipple="gray50")
    # Title text
    canvas.create_text(screenwidth / 2, card_y1 + 40, text="Edit reservation", font=("Arial", 22, "bold"), fill="#1a5276")

    # the form

    name_label = Label(canvas, text="Full Name", font=("Arial", 15))
    name_entry = Entry(canvas, font=("Arial", 14),textvariable=name_val)
    name_label.place(x=480, y=130)
    name_entry.place(x=480, y=170, width=380, height=30)

    date_label = Label(canvas, text="Date ", font=("Arial", 15))
    style = ttk.Style()
    style.configure('my.DateEntry', font=('Arial', 10))
    date_entry = DateEntry(canvas, font=('Arial', 10), width=18, style='my.DateEntry', date_pattern="d-m-yyy",textvariable=date_val)
    date_entry.bind("<<DateEntrySelected>>", lambda e: update_flight_options())
    date_label.place(x=480, y=220)
    date_entry.place(x=480, y=260, width=380, height=30)

    departure_label = Label(canvas, text="Departure ", font=("Arial", 15))
    departure_label.place(x=480, y=310)
    dep_combo = ttk.Combobox(canvas, values=avl_dep, state="readonly", textvariable=departure_val)
    dep_combo.set(departure_val.get())
    dep_combo.place(x=480, y=350, width=170, height=30)
    dep_combo.bind("<<ComboboxSelected>>", lambda e: auto_fill_flight_and_time())

    destination_label = Label(canvas, text="Destination ", font=("Arial", 15))
    destination_label.place(x=690, y=310)
    des_combo = ttk.Combobox(canvas, values=avl_des, state="readonly", textvariable=destination_val)
    des_combo.set(destination_val.get())
    des_combo.place(x=690, y=350, width=170, height=30)
    des_combo.bind("<<ComboboxSelected>>", lambda e: auto_fill_flight_and_time())

    time_label = Label(canvas, text="Time ", font=("Arial", 15))
    time_entry = Entry(canvas, font=("Arial", 15),textvariable=time_val)
    time_label.place(x=480, y=400)
    time_entry.place(x=480, y=440, width=170, height=30)

    flight_name_label = Label(canvas, text="Flight Name", font=("Arial", 15))
    flight_name_entry = Entry(canvas, font=("Arial", 14),textvariable=flight_name_val)
    flight_name_label.place(x=690, y=400)
    flight_name_entry.place(x=690, y=440, width=170, height=30)

    seat_label = Label(canvas, text="Seat Number ", font=("Arial", 15))
    seat_combo = ttk.Combobox(canvas, font=("Arial", 15), textvariable=seat_val, state="readonly",
                              values=[f"{chr(r)}{c}" for r in range(65, 71) for c in range(1, 31)])
    seat_combo.set(seat_val.get())

    seat_label.place(x=480, y=490)
    seat_combo.place(x=480, y=530, width=380, height=30)

    # function for making options
    # set the date to get the available flights data

    def update_flight_options():

        selected_date = date_entry.get_date()
        day_name = selected_date.strftime("%A")
        avl_dep.clear()
        avl_des.clear()
        for flight in flight_schedule.get(day_name, []):
            avl_dep.append(flight["from"]) if flight["from"] not in avl_dep else None
            avl_des.append(flight["to"]) if flight["to"] not in avl_des else None

        dep_combo['values'] = avl_dep
        des_combo['values'] = avl_des
        dep_combo.set("Select Departure")
        des_combo.set("Select Destination")


    def auto_fill_flight_and_time():
        selected_date = date_entry.get_date()
        day_name = selected_date.strftime("%A")
        dep = dep_combo.get()
        des = des_combo.get()

        for flight in flight_schedule[day_name]:
            if flight["from"] == dep and flight["to"] == des:
                flight_name_entry.delete(0, END)
                flight_name_entry.insert(0, flight["flight"])
                time_entry.delete(0, END)
                time_entry.insert(0, flight["time"])
                break

    # function of buttons
    def update_flight_btn():
        updated_data = [name_val.get(), flight_name_val.get(), departure_val.get(), destination_val.get(),
                        date_val.get(), seat_val.get(),time_val.get()]
        success=edit_reservation(reservation_id,updated_data)
        if success:
            messagebox.showinfo("Updated","Reservation updated successfully.")
            canvas.pack_forget()
            show_reservation_callback()

        else:
            messagebox.showerror("Error","Updated failed,please try again")

    #buttons
    cancel_button = Button( canvas, text="Cancel", bg="#e7ecef", width=13,height=2, command=lambda:
    ( canvas.pack_forget(), show_reservation_callback()))
    # cancel_button.place(x=180, y=400, width=90, height=40)
    cancel_button.place(x=770, y=590)

    updated_button = Button( canvas, text="Update", bg="#3393ff", fg="white", width=13,height=2
                             , command=update_flight_btn)
    # updated_button.place(x=300, y=400, width=90, height=40)
    updated_button.place(x=650,y=590)
    return Canvas

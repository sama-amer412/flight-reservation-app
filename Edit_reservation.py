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

    

    
    # Transparent card (rectangle)
    card_x1 = screenwidth / 2 - 230
    card_y1 = screenheight / 2 - 280
    card_x2 = screenwidth / 2 + 230
    card_y2 = screenheight / 2 + 240

    canvas.create_rectangle(card_x1, card_y1, card_x2, card_y2, fill="#4682B4", outline="", stipple="gray50")
    # Title text
    canvas.create_text(screenwidth / 2, card_y1 + 40, text="Edit reservation", font=("Arial", 22, "bold"), fill="#1a5276")

    # the form
    name_label = Label(canvas, text="Full Name", font=("Arial", 15))
    name_entry = Entry(canvas, font=("Arial", 14),textvariable=name_val )
    name_label.place(x=480, y=170)
    name_entry.place(x=480, y=210, width=380, height=30)

    flight_name_label = Label(canvas, text="Flight Name", font=("Arial", 15))
    flight_name_entry = Entry(canvas, font=("Arial", 14),textvariable=flight_name_val)
    flight_name_label.place(x=480, y=260)
    flight_name_entry.place(x=480, y=300, width=380, height=30)

    departure_label = Label(canvas, text="Departure ", font=("Arial", 15))
    departure_entry = Entry(canvas, font=("Arial", 15),textvariable=departure_val)
    departure_label.place(x=480, y=350)
    departure_entry.place(x=480, y=390, width=170, height=30)

    destination_label = Label(canvas, text="Destination ", font=("Arial", 15))
    destination_entry = Entry(canvas, font=("Arial", 15),textvariable=destination_val)
    destination_label.place(x=690, y=350)
    destination_entry.place(x=690, y=390, width=170, height=30)

    date_label = Label(canvas, text="Date ", font=("Arial", 15))
    style = ttk.Style()
    style.configure('my.DateEntry', font=('Arial', 10))
    date_entry = DateEntry(canvas, font=('Arial', 10), width=18, style='my.DateEntry', date_pattern="d-m-yyy",textvariable=date_val)
    date_label.place(x=480, y=440)
    date_entry.place(x=480, y=480, width=170, height=30)

    seat_label = Label(canvas, text="Seat Number ", font=("Arial", 15))
    seat_entry = Entry(canvas, font=("Arial", 15),textvariable=seat_val)
    seat_label.place(x=690, y=440)
    seat_entry.place(x=690, y=480, width=170, height=30)

    # function of buttons
    def update_flight_btn():
        updated_data = [name_val.get(), flight_name_val.get(), departure_val.get(), destination_val.get(),
                        date_val.get(), seat_val.get()]
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
    cancel_button.place(x=770, y=540)

    updated_button = Button( canvas, text="Update", bg="#3393ff", fg="white", width=13,height=2
                             , command=update_flight_btn)
    updated_button.place(x=650, y=540)
    return Canvas

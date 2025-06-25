from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from database import book_flight

def booking(root, show_home_callback):
    screenwidth = root.winfo_screenwidth()
    screenheight = root.winfo_screenheight()

    canvas = Canvas(root, width=screenwidth, height=screenheight)
    canvas.pack(fill="both", expand=True)

    # Background Image
    bg_image = Image.open("images/background.jpg")
    bg_image = bg_image.resize((screenwidth, screenheight))
    bg_photo = ImageTk.PhotoImage(bg_image)
    canvas.create_image(0, 0, anchor=NW, image=bg_photo)
    canvas.bg_photo = bg_photo  # Prevent garbage collection

    # Transparent card (rectangle)
    card_x1 = screenwidth / 2 - 230
    card_y1 = screenheight / 2 - 280
    card_x2 = screenwidth / 2 + 230
    card_y2 = screenheight / 2 + 240

    canvas.create_rectangle(card_x1, card_y1, card_x2, card_y2, fill="#4682B4", outline="", stipple="gray50")

    # Title text
    canvas.create_text(screenwidth / 2, card_y1 + 40, text="Book a Flight", font=("Arial", 22, "bold"), fill="#1a5276")

    # the booking form
    name_label=Label(canvas,text="Full Name",font=("Arial",15))
    name_entry=Entry(canvas,font=("Arial", 14))
    name_label.place(x=480, y=170)
    name_entry.place(x=480, y=210, width=380, height=30)

    flight_name_label=Label(canvas,text="Flight Name",font=("Arial",15))
    flight_name_entry=Entry(canvas,font=("Arial", 14))
    flight_name_label.place(x=480, y=260)
    flight_name_entry.place(x=480, y=300, width=380, height=30)

    departure_label=Label(canvas,text="Departure ",font=("Arial",15))
    departure_entry=Entry(canvas,font=("Arial",15))
    departure_label.place(x=480, y=350)
    departure_entry.place(x=480, y=390, width=170, height=30)

    destination_label=Label(canvas,text="Destination ",font=("Arial",15))
    destination_entry=Entry(canvas,font=("Arial",15))
    destination_label.place(x=690, y=350)
    destination_entry.place(x=690, y=390, width=170, height=30)

    date_label=Label(canvas,text="Date ",font=("Arial",15))
    date_entry=Entry(canvas,font=("Arial",15))
    date_label.place(x=480, y=440)
    date_entry.place(x=480, y=480, width=170, height=30)

    seat_label=Label(canvas,text="Seat Number ",font=("Arial",15))
    seat_entry=Entry(canvas,font=("Arial",15))
    seat_label.place(x=690, y=440)
    seat_entry.place(x=690, y=480, width=170, height=30)

    # Clear form function
    def clear_form():
        name_entry.delete(0, END)
        flight_name_entry.delete(0, END)
        departure_entry.delete(0, END)
        destination_entry.delete(0, END)
        date_entry.delete(0, END)
        seat_entry.delete(0, END)


    # Book flight function
    def book_flight_btn():
        book_flight(
            name_entry.get(),
            flight_name_entry.get(),
            departure_entry.get(),
            destination_entry.get(),
            date_entry.get(),
            seat_entry.get()
        )

        clear_form()
        messagebox.showinfo("Flight Reserved", "Your flight has been booked successfully!")

    # Buttons
    cancel_btn=Button(canvas, text="Cancel", bg="#e7ecef", width=13,height=2,
           command=lambda: (canvas.pack_forget(), show_home_callback(), clear_form()))
    cancel_btn.place(x=770, y=540)
    book_btn=Button(canvas, text="Book Flight", bg="#3393ff", fg="white", width=13,height=2,
           command=book_flight_btn)
    book_btn.place(x=650,y=540)
    return canvas




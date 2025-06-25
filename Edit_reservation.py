from tkinter import *
from tkinter import messagebox
from database import edit_reservation
from PIL import Image, ImageTk

def edit_reservation_page(root, old_reservation_data, show_reservation_callback):
    screenwidth = root.winfo_screenwidth()
    screenheight = root.winfo_screenheight()
    editing_main_frame = Frame(root, width=screenwidth, height=screenheight, bg="#D3D3D3")
    editing_form_frame = Frame(editing_main_frame, width=400, height=500,bg="#f5eef8")
    editing_form_frame.place(anchor="center", x=screenwidth / 2, y=screenheight / 2)
    editing_main_frame.pack(fill="both", expand=True)

    # making the background
    bg_image = Image.open("images/background.jpg")
    bg_image = bg_image.resize((screenwidth, screenheight))
    bg_photo = ImageTk.PhotoImage(bg_image)

    bg_label = Label( editing_main_frame, image=bg_photo)
    bg_label.image = bg_photo
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    bg_label.lower()

    #old reservation data
    reservation_id=old_reservation_data[0]
    name_val=StringVar(value=old_reservation_data[1])
    flight_name_val=StringVar(value=old_reservation_data[2])
    departure_val=StringVar(value=old_reservation_data[3])
    destination_val=StringVar(value=old_reservation_data[4])
    date_val=StringVar(value=old_reservation_data[5])
    seat_val=StringVar(value=old_reservation_data[6])

    # the form

    form_title = Label(editing_form_frame, text="Edit Reservation", font=("Arial", 20, "bold"), fg="#1a5276")
    form_title.place(anchor="center", x=120, y=15)

    name_label = Label(editing_form_frame, text="Full Name", font=("Arial", 15))
    name_entry = Entry(editing_form_frame,textvariable=name_val,font=("Arial",15))
    name_label.place(x=10, y=50)
    name_entry.place(x=10, y=90, width=380, height=30)

    flight_name_label = Label(editing_form_frame, text="Flight Name", font=("Arial", 15))
    flight_name_entry = Entry(editing_form_frame,textvariable=flight_name_val,font=("Arial",15))
    flight_name_label.place(x=10, y=130)
    flight_name_entry.place(x=10, y=170, width=380, height=30)

    departure_label = Label(editing_form_frame, text="Departure ", font=("Arial", 15))
    departure_entry = Entry(editing_form_frame,textvariable=departure_val,font=("Arial",15))
    departure_label.place(x=10, y=210)
    departure_entry.place(x=10, y=250, width=170, height=30)

    destination_label = Label(editing_form_frame, text="Destination ", font=("Arial", 15))
    destination_entry = Entry(editing_form_frame,textvariable=destination_val,font=("Arial",15))
    destination_label.place(x=220, y=210)
    destination_entry.place(x=220, y=250, width=170, height=30)

    date_label = Label(editing_form_frame, text="Date ", font=("Arial", 15))
    date_entry = Entry(editing_form_frame,textvariable=date_val,font=("Arial",15))
    date_label.place(x=10, y=290)
    date_entry.place(x=10, y=330, width=170, height=30)

    seat_label = Label(editing_form_frame, text="Seat Number ", font=("Arial", 15))
    seat_entry = Entry(editing_form_frame,textvariable=seat_val,font=("Arial",15))
    seat_label.place(x=220, y=290)
    seat_entry.place(x=220, y=330, width=170, height=30)

    # function of buttons
    def update_flight_btn():
        updated_data = [name_val.get(), flight_name_val.get(), departure_val.get(), destination_val.get(),
                        date_val.get(), seat_val.get()]
        success=edit_reservation(reservation_id,updated_data)
        if success:
            messagebox.showinfo("Updated","Reservation updated successfully.")
            editing_main_frame.pack_forget()
            show_reservation_callback()

        else:
            messagebox.showerror("Error","Updated failed,please try again")

    #buttons
    cancel_button = Button( editing_form_frame, text="Cancel", bg="#e7ecef", command=lambda:
    ( editing_main_frame.pack_forget(), show_reservation_callback()))
    cancel_button.place(x=180, y=400, width=90, height=40)

    updated_button = Button( editing_form_frame, text="Update", bg="#3393ff", command=update_flight_btn)
    updated_button.place(x=300, y=400, width=90, height=40)

    return editing_main_frame
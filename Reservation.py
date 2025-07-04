from tkinter import *
from database import book_flight,delete_reservation
from database import view_reservation
from tkinter import ttk
from tkinter import messagebox
from Edit_reservation import edit_reservation_page
from PIL import Image, ImageTk
import os
import sys
def reservation (root):
    global tree
    screenwidth = root.winfo_screenwidth()
    screenheight = root.winfo_screenheight()
    reservation_main_frame = Frame(root, width=screenwidth - 60, height=screenheight - 150, bg="#e7ecef")

    # making the background

    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    image_path = os.path.join(base_path, "images", "background.jpg")

    bg_image = Image.open(image_path)
    bg_image = bg_image.resize((screenwidth, screenheight))
    bg_photo = ImageTk.PhotoImage(bg_image)
    bg_label = Label(reservation_main_frame, image=bg_photo)
    bg_label.image = bg_photo
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    bg_label.lower()

   #making the table
    columns=("no.reservation","name","flight number","departure","destination","date","seat number","time")
    tree=ttk.Treeview(reservation_main_frame,columns=columns,show="headings")
    for col in columns:
        tree.heading(col, text=col,anchor="center")
        tree.column(col, width=120,anchor="center")
    style = ttk.Style()
    style.configure("Treeview", font=("Arial", 11), rowheight=35)
    style.configure("Treeview.Heading", font=("Arial", 14, "bold"))
    data=view_reservation()
    for row in data:
        tree.insert("",END,values=row)


    tree.place(x=40,y=80,width=screenwidth-80,height=screenheight-260)
    edit_btn=Button(reservation_main_frame,text="edit reservation ",width=15,height=2,bg="#3393ff")
    delete_btn=Button(reservation_main_frame,text="delete reservation",width=15,height=2,bg="#3393ff")
    edit_btn.place(x=1050,y=600)
    delete_btn.place(x=1170,y=600)

    # function of the buttons
    def delete_selected():
        global tree
        selected=tree.focus()
        if selected:
            values=tree.item(selected,"values")
            reservation_id=values[0]
            success=delete_reservation(reservation_id)
            if success:
                messagebox.showinfo("Deleted", "Reservation deleted successfully!")
                refresh_table()
            else:
                messagebox.showerror("Error", "Failed to delete reservation.")

        else:
            messagebox.showwarning("No Selection", "Please select a reservation to delete.")



    def edit_selected():
        global tree
        selected = tree.focus()
        if selected:
            values=tree.item(selected,"values")
            edit_reservation_page(root,values,lambda :(reservation_main_frame.pack(fill="both", expand=True),refresh_table()))

            reservation_main_frame.pack_forget()

        else:
            messagebox.showwarning("No Selection", "Please select a reservation to edit.")

    # Buttons
    edit_btn = Button(reservation_main_frame, text="edit reservation ", width=15, height=2, bg="#85c1e9",command=edit_selected)
    delete_btn = Button(reservation_main_frame, text="delete reservation", width=15, height=2, bg="#85c1e9",command=delete_selected)
    edit_btn.place(x=1050, y=600)
    delete_btn.place(x=1170, y=600)

    return reservation_main_frame

# refresh function after editing
def refresh_table():
    global tree
    for row in tree.get_children():
        tree.delete(row)
    data=view_reservation()
    for row in data:
        tree.insert("",END,values=row)



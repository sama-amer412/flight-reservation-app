from tkinter import *
from Home import home

#the main frame
root=Tk()
screenwidth=root.winfo_screenwidth()
screenheight=root.winfo_screenheight()
root.state("zoomed")
root.title("FlySky Reservations")

#run the programme
home_main_frame=home(root,screenwidth,screenheight)
root.mainloop()

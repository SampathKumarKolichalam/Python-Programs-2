from tkinter import *
obj=Tk()
obj.geometry("300x300")
obj["bg"]="#51E1DC"
obj.title("Label GUI")
#Labels:-
#label=Label(obj,text="Hello Sampath Kumar").pack()
label=Label(obj,text="Hello Sampath Kumar").place(x=30,y=20)
obj.mainloop()

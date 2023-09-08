import time
from tkinter import *
from datetime import datetime

class Resize:
    def __init__(self,Master):

        Master.title("Current time")
        Master.geometry("400x150")
        Master.configure(bg="blue")

        def clock():
            hours = time.strftime("%H")
            minutes = time.strftime("%M")
            sec = time.strftime("%S")

            locate = time.strftime("%p")

            year = time.strftime("%Y")
            month = time.strftime("%B")
            day = time.strftime("%A")



            self.label_clock.config(text=hours+ ":" + minutes+":"+ sec+":"+locate)
            self.label_days_year_month.config(text=year+"-"+month+"-"+day)
            self.label_clock.after(1000,clock)




        self.label_main = Label(Master,text="",padx=50,pady=25,bg="blue")
        self.label_main.grid(row=1,columnspan=5 ,column=1)

        self.label_clock = Label(self.label_main,text="",padx=25,pady=12,font=("helvetica",40),bg="blue",fg="green2")
        self.label_clock.grid(row=1,column=1,columnspan=5)

        self.label_days_year_month = Label(self.label_main,text="",pady=12,padx=25,font=("helvetica",20),bg="blue",fg="green2")
        self.label_days_year_month.grid(row=2,column=1,columnspan=5)


        clock()


root = Tk()
resize_1 = Resize(root)
root.mainloop()
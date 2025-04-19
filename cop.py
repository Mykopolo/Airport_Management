import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import sqlite3  ##upto orignal imports and from AL
from tkinter import filedialog
from tkinter.filedialog import askopenfile
from PIL import Image, ImageTk
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 
import qrcode
import pathlib
from sqlalchemy import create_engine, Column, Integer, Float, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
#from sqlalchemy import create_engine

def open_dashboard():
    dashboard = tk.Tk()
    dashboard.title("Airline Management Dashboard")
    dashboard.geometry("900x600")
    dashboard.configure(bg="#283747")
    global filename, img
    

    def make_flight():
        made_flight = tk.Tk()
        made_flight.title("Make New Flight")
        made_flight.geometry("900x600")
        made_flight.configure(bg="#283747")

        def make_flight_save():
            return
        
        fdate1 = tk.Label(made_flight, text="Flight Date D/M/Y", font=("Arial", 14), fg="white", bg="#283747", anchor="w").place(x=10, y=50)
        Aircraft1 = tk.Label(made_flight, text="Aircraft", font=("Arial", 14), fg="white", bg="#283747", anchor="w").place(x=200, y=50)
        From1 = tk.Label(made_flight, text="From", font=("Arial", 14), fg="white", bg="#283747", anchor="w").place(x=390, y=50)
        To1 = tk.Label(made_flight, text="To", font=("Arial", 14), fg="white", bg="#283747", anchor="w").place(x=580, y=50)
        Dep_Time1 = tk.Label(made_flight, text="Depparture Time", font=("Arial", 14), fg="white", bg="#283747", anchor="w").place(x=10, y=100)
        Arr_Time1 = tk.Label(made_flight, text="Arrival Time", font=("Arial", 14), fg="white", bg="#283747", anchor="w").place(x=200, y=100)
        TFT1 = tk.Label(made_flight, text="Total Flight Time", font=("Arial", 14), fg="white", bg="#283747", anchor="w").place(x=390, y=100)
        Paxs1 = tk.Label(made_flight, text="Paxs On Board", font=("Arial", 14), fg="white", bg="#283747", anchor="w").place(x=10, y=150)
        Price_paxs1 = tk.Label(made_flight, text="Price per paxs", font=("Arial", 14), fg="white", bg="#283747", anchor="w").place(x=200, y=150)
        Total_Price1 = tk.Label(made_flight, text="Total Price", font=("Arial", 14), fg="white", bg="#283747", anchor="w").place(x=390, y=150)
        Cabin1 = tk.Label(made_flight, text="Cabin Crew", font=("Arial", 14), fg="white", bg="#283747", anchor="w").place(x=580, y=150)
        Rout_Distance1 = tk.Label(made_flight, text="Rout Distance", font=("Arial", 14), fg="white", bg="#283747", anchor="w").place(x=10, y=200)
        Dep_fuel2 = tk.Label(made_flight, text="Depparture Fuel Kg", font=("Arial", 14), fg="white", bg="#283747", anchor="w").place(x=200, y=200)
        Arr_fuel1 = tk.Label(made_flight, text="Arrival Fuel Kg", font=("Arial", 14), fg="white", bg="#283747", anchor="w").place(x=390, y=200)
        TFB1 = tk.Label(made_flight, text="Total Burned Fuel Kg", font=("Arial", 14), fg="white", bg="#283747", anchor="w").place(x=580, y=200)
        Captain1 = tk.Label(made_flight, text="Captain", font=("Arial", 14), fg="white", bg="#283747", anchor="w").place(x=10, y=250)
        Co_pilot1 = tk.Label(made_flight, text="Co-Pilot", font=("Arial", 14), fg="white", bg="#283747", anchor="w").place(x=200, y=250)
        Crew11 = tk.Label(made_flight, text="Cabin Crew 1", font=("Arial", 14), fg="white", bg="#283747", anchor="w").place(x=10, y=300)
        crew22 = tk.Label(made_flight, text="Cabin Crew 2", font=("Arial", 14), fg="white", bg="#283747", anchor="w").place(x=200, y=300)
        crew33 = tk.Label(made_flight, text="Cabin Crew 3", font=("Arial", 14), fg="white", bg="#283747", anchor="w").place(x=390, y=300)
        crew44 = tk.Label(made_flight, text="Cabin Crew 4", font=("Arial", 14), fg="white", bg="#283747", anchor="w").place(x=580, y=300)
        rout = tk.Label(made_flight, text="Route Code", font=("Arial", 14), fg="white", bg="#283747", anchor="w").place(x=770, y=400)
        
        fdate = tk.Entry(made_flight).place(x=10, y=75)
        Aircraft = ttk.Combobox(made_flight).place(x=200, y=75)
        From = ttk.Combobox(made_flight).place(x=390, y=75)
        To = ttk.Combobox(made_flight).place(x=580, y=75)
        Dep_Time = tk.Entry(made_flight).place(x=10, y=125)
        Arr_Time = tk.Entry(made_flight).place(x=200, y=125)
        TFT = tk.Entry(made_flight).place(x=390, y=125)
        Paxs = tk.Entry(made_flight).place(x=10, y=175)
        Price_paxs = tk.Entry(made_flight).place(x=200, y=175)
        Total_Price = tk.Entry(made_flight).place(x=390, y=175)
        Cabin = tk.Entry(made_flight).place(x=580, y=175)
        Rout_Distance = tk.Entry(made_flight).place(x=10, y=225)
        Dep_fuel = tk.Entry(made_flight).place(x=200, y=225)
        Arr_fuel = tk.Entry(made_flight).place(x=390, y=225)
        TFB = tk.Entry(made_flight).place(x=580, y=225)
        Captain = ttk.Combobox(made_flight).place(x=10, y=275)
        Co_pilot = ttk.Combobox(made_flight).place(x=200, y=275)
        Crew1 = ttk.Combobox(made_flight).place(x=10, y=325)
        crew2 = ttk.Combobox(made_flight).place(x=200, y=325)
        crew3 = ttk.Combobox(made_flight).place(x=390, y=325)
        crew4 = ttk.Combobox(made_flight).place(x=580, y=325)
        rout_code = ttk.Combobox(made_flight).place(x=580, y=425)
        make_flight_saveb = tk.Button(made_flight, text="Fly", font=("Arial", 20), bg="#2ECC71", fg="white", command=make_flight_save).place(x=10, y=370)
        made_flight.mainloop()

    def Add_Employee():
        Add_Employee = tk.Tk()
        Add_Employee.title("Recruit New Employee")
        Add_Employee.geometry("900x600")
        Add_Employee.configure(bg="#283747")

        def eimgs():
            return
        hdate = tk.Label(Add_Employee, text="Hire Date", font=("Arial", 14), fg="white", bg="#283747").place(x=350, y=50)
        Fname = tk.Label(Add_Employee, text="Full Name", font=("Arial", 14), fg="white", bg="#283747").place(x=450, y=50)
        job = tk.Label(Add_Employee, text="Job Position", font=("Arial", 14), fg="white", bg="#283747").place(x=600, y=50)
        ID = tk.Label(Add_Employee, text="Emloyement ID", font=("Arial", 14), fg="white", bg="#283747").place(x=800, y=50)
        Bsalary = tk.Label(Add_Employee, text="Basic Salary", font=("Arial", 14), fg="white", bg="#283747").place(x=350, y=150)
        Nationality = tk.Label(Add_Employee, text="Nationality", font=("Arial", 14), fg="white", bg="#283747").place(x=500, y=150)
        Age = tk.Label(Add_Employee, text="Age", font=("Arial", 14), fg="white", bg="#283747").place(x=600, y=150)
        epr = tk.Label(Add_Employee, text="Expriance", font=("Arial", 14), fg="white", bg="#283747").place(x=700, y=150)
        TFT = tk.Label(Add_Employee, text="Total Flight Time", font=("Arial", 14), fg="white", bg="#283747").place(x=350, y=250)
        Aircraft1 = tk.Label(Add_Employee, text="Aircraft 1", font=("Arial", 14), fg="white", bg="#283747").place(x=550, y=250)
        TFT1 = tk.Label(Add_Employee, text="Total Flight Time", font=("Arial", 14), fg="white", bg="#283747").place(x=750, y=250)
        Aircraft2 = tk.Label(Add_Employee, text="Aircraft 2", font=("Arial", 14), fg="white", bg="#283747").place(x=50, y=350)
        TFT2 = tk.Label(Add_Employee, text="Total Flight Time", font=("Arial", 14), fg="white", bg="#283747").place(x=250, y=350)
        Aircraft3 = tk.Label(Add_Employee, text="Aircraft 3", font=("Arial", 14), fg="white", bg="#283747").place(x=450, y=350)
        TFT3 = tk.Label(Add_Employee, text="Total Flight Time", font=("Arial", 14), fg="white", bg="#283747").place(x=650, y=350)
        Aircraft4 = tk.Label(Add_Employee, text="Aircraft 4", font=("Arial", 14), fg="white", bg="#283747").place(x=50, y=450)
        TFT4 = tk.Label(Add_Employee, text="Total Flight Time", font=("Arial", 14), fg="white", bg="#283747").place(x=250, y=450)
        Aircraft5 = tk.Label(Add_Employee, text="Aircraft 5", font=("Arial", 14), fg="white", bg="#283747").place(x=450, y=450)
        TFT5 = tk.Label(Add_Employee, text="Total Flight Time", font=("Arial", 14), fg="white", bg="#283747").place(x=650, y=450)
        eimg = tk.Button(Add_Employee, text="upload Employee Image", font=("Arial", 14), fg="white", bg="#283747", command=eimgs).place(x=50, y=300)

        hdate = tk.Entry(Add_Employee).place(x=350, y=100)
        Fname = tk.Entry(Add_Employee).place(x=450, y=100)
        job = tk.Entry(Add_Employee).place(x=600, y=100)
        ID = tk.Entry(Add_Employee).place(x=800, y=100)
        Bsalary = tk.Entry(Add_Employee).place(x=350, y=200)
        Nationality = tk.Entry(Add_Employee).place(x=500, y=200)
        age = tk.Entry(Add_Employee).place(x=600, y=200)
        epr = tk.Entry(Add_Employee).place(x=700, y=200)
        TFT = tk.Entry(Add_Employee).place(x=350, y=300)
        Aircraft1 = tk.Entry(Add_Employee).place(x=550, y=300)
        TFT1 = tk.Entry(Add_Employee).place(x=750, y=300)
        Aircraft2 = tk.Entry(Add_Employee).place(x=50, y=400)
        TFT2 = tk.Entry(Add_Employee).place(x=250, y=400)
        Aircraft3 = tk.Entry(Add_Employee).place(x=450, y=400)
        TFT3 = tk.Entry(Add_Employee).place(x=650, y=400)
        Aircraft4 = tk.Entry(Add_Employee).place(x=50, y=500)
        TFT4 = tk.Entry(Add_Employee).place(x=250, y=500)
        Aircraft5 = tk.Entry(Add_Employee).place(x=450, y=500)
        TFT5 = tk.Entry(Add_Employee).place(x=650, y=500)



        Add_Employee.mainloop()
        
    def in_out():
        in_out = tk.Tk()
        in_out.title("Buy and Sell")
        in_out.geometry("760x450") # first horizon second vertical
        in_out.configure(bg="#283747")

        def subsub():
            return

        tk.Label(in_out, text="Date", font=("Arial", 14), fg="white", bg="#283747").place(x=10, y=50)
        tk.Label(in_out, text="Home action", font=("Arial", 14), fg="white", bg="#283747").place(x=160, y=50)
        tk.Label(in_out, text="Reason", font=("Arial", 14), fg="white", bg="#283747").place(x=310, y=50)
        tk.Label(in_out, text="From", font=("Arial", 14), fg="white", bg="#283747").place(x=460, y=50)
        tk.Label(in_out, text="To", font=("Arial", 14), fg="white", bg="#283747").place(x=610, y=50)
        tk.Label(in_out, text="Total Paxs", font=("Arial", 14), fg="white", bg="#283747").place(x=10, y=150)
        tk.Label(in_out, text="Price/Paxs", font=("Arial", 14), fg="white", bg="#283747").place(x=160, y=150)
        tk.Label(in_out, text="Total Price", font=("Arial", 14), fg="white", bg="#283747").place(x=310, y=150)
        tk.Label(in_out, text="QTY", font=("Arial", 14), fg="white", bg="#283747").place(x=460, y=150)
        tk.Label(in_out, text="Unit Price", font=("Arial", 14), fg="white", bg="#283747").place(x=610, y=150)
        tk.Label(in_out, text="Total", font=("Arial", 14), fg="white", bg="#283747").place(x=10, y=250)
        tk.Label(in_out, text="Away Action", font=("Arial", 14), fg="white", bg="#283747").place(x=160, y=250)
        tk.Label(in_out, text="Legal Body", font=("Arial", 14), fg="white", bg="#283747").place(x=310, y=250)
        tk.Label(in_out, text="Transction ID", font=("Arial", 14), fg="white", bg="#283747").place(x=460, y=250)
        tk.Label(in_out, text="Total Asset", font=("Arial", 14), fg="white", bg="#283747").place(x=610, y=250)
        tk.Label(in_out, text="Total Expense", font=("Arial", 14), fg="white", bg="#283747").place(x=10, y=350)

        det= tk.Entry(in_out).place(x=10, y=100)   
        Homeact = ttk.Combobox(in_out).place(x=160, y=100)
        resn= tk.Entry(in_out).place(x=310, y=100)
        From = ttk.Combobox(in_out).place(x=460, y=100)
        TO = ttk.Combobox(in_out).place(x=610, y=100)
        totpaxs= tk.Entry(in_out).place(x=10, y=200)
        pppaxs= tk.Entry(in_out).place(x=160, y=200)
        tp= tk.Entry(in_out).place(x=310, y=200)
        qty1= tk.Entry(in_out).place(x=460, y=200)
        uprice= tk.Entry(in_out).place(x=610, y=200)
        tpi= tk.Entry(in_out).place(x=10, y=300)
        awayact = ttk.Combobox(in_out).place(x=160, y=300)
        legbody= tk.Entry(in_out).place(x=310, y=300)
        transid= tk.Entry(in_out).place(x=460, y=300)
        totasset= tk.Entry(in_out).place(x=610, y=300)
        totexpense= tk.Entry(in_out).place(x=10, y=400)

        sbmt= tk.Button(in_out, text="Submit", font=("Arial", 14), fg="white", bg="#283747", command=subsub).place(x=310, y=400)

        in_out.mainloop()

    def Grounded():
        return
    def Flight_List():
        return
    def buy_sell():
        buy_sell = tk.Tk()
        buy_sell.title("Buy and Sell")
        buy_sell.geometry("450x400") # first horizon second vertical
        buy_sell.configure(bg="#283747")

        def godata():
            return

        tk.Label(buy_sell, text="Date", font=("Arial", 14), fg="white", bg="#283747").place(x=10, y=50)
        tk.Label(buy_sell, text="Home Action", font=("Arial", 14), fg="white", bg="#283747").place(x=160, y=50)
        tk.Label(buy_sell, text="Reason", font=("Arial", 14), fg="white", bg="#283747").place(x=310, y=50)
        tk.Label(buy_sell, text="QTY", font=("Arial", 14), fg="white", bg="#283747").place(x=10, y=150)
        tk.Label(buy_sell, text="Unit Price", font=("Arial", 14), fg="white", bg="#283747").place(x=160, y=150)
        tk.Label(buy_sell, text="Total", font=("Arial", 14), fg="white", bg="#283747").place(x=310, y=150)
        tk.Label(buy_sell, text="Away Action", font=("Arial", 14), fg="white", bg="#283747").place(x=10, y=250)
        tk.Label(buy_sell, text="Legal Body", font=("Arial", 14), fg="white", bg="#283747").place(x=160, y=250)
        tk.Label(buy_sell, text="Transction ID", font=("Arial", 14), fg="white", bg="#283747").place(x=310, y=250)

        datesb = tk.Entry(buy_sell).place(x=10, y=100)
        Homeaction = tk.Entry(buy_sell).place(x=160, y=100)
        Reason = tk.Entry(buy_sell).place(x=310, y=100)
        qty = tk.Entry(buy_sell).place(x=10, y=200)
        Unitprice = tk.Entry(buy_sell).place(x=160, y=200)
        tot = tk.Entry(buy_sell).place(x=310, y=200)
        away = tk.Entry(buy_sell).place(x=10, y=300)
        Legal = tk.Entry(buy_sell).place(x=160, y=300)
        transid = tk.Entry(buy_sell).place(x=310, y=300)

        Buysellb = tk.Button(buy_sell, text="Submit", font=("Arial", 14), fg="white", bg="#283747", command=godata).place(x=150, y=350)

        buy_sell.mainloop()
    def op_aircraft():
        return
    def Add_aircraft():
        Add_aircraft = tk.Tk()
        Add_aircraft.title("Make New Flight")
        Add_aircraft.geometry("900x600")
        Add_aircraft.configure(bg="#283747")

        def upload_file():
            global filename, img
            f_types = [('Png files', '*.png'), ('Jpg Files', '*.jpg')]
            filename = filedialog.askopenfilename(filetypes=f_types)
            img = Image.open(filename)
            img_resized = img.resize((300, 300))
            img = ImageTk.PhotoImage(img_resized,file=filename)
            img_resized.save(Modele.get()+".png")
            img3=Image.open(Modele.get()+".png")
            img3_resized=img3.resize((400,400))
            img33=ImageTk.PhotoImage(img3_resized)
            leb=tk.Label(image=img33)
            leb.image=img33
            leb.place(x=20,y=50)

        pdate = tk.Label(Add_aircraft, text="Flight Date D/M/Y", font=("Arial", 14), fg="white", bg="#283747", anchor="w").place(x=500, y=50)
        Aircraft_name = tk.Label(Add_aircraft, text="Aircraft Name", font=("Arial", 14), fg="white", bg="#283747", anchor="w").place(x=500, y=100)
        Modele = tk.Label(Add_aircraft, text="Model", font=("Arial", 14), fg="white", bg="#283747", anchor="w").place(x=500, y=150)
        Aid = tk.Label(Add_aircraft, text="Aircraft ID", font=("Arial", 14), fg="white", bg="#283747", anchor="w").place(x=500, y=200)
        manufa = tk.Label(Add_aircraft, text="Manufacturer", font=("Arial", 14), fg="white", bg="#283747", anchor="w").place(x=500, y=250)
        manufad = tk.Label(Add_aircraft, text="Manufacturer Date", font=("Arial", 14), fg="white", bg="#283747", anchor="w").place(x=500, y=300)
        pp = tk.Label(Add_aircraft, text="Purchase Price", font=("Arial", 14), fg="white", bg="#283747", anchor="w").place(x=500, y=350)
        Expectedsy = tk.Label(Add_aircraft, text="Expected Service Year", font=("Arial", 14), fg="white", bg="#283747", anchor="w").place(x=500, y=400)
        mtime = tk.Label(Add_aircraft, text="Mentanance Time", font=("Arial", 14), fg="white", bg="#283747", anchor="w").place(x=500, y=450)
        uploadIMG = tk.Button(Add_aircraft, text='Upload Aircraft Image', width=20,command = lambda:upload_file()).place(x=500,y=500)


        pdatee = tk.Entry(Add_aircraft).place(x=500, y=75)
        Aircraft_namee = tk.Entry(Add_aircraft).place(x=500, y=125)
        Modele = tk.Entry(Add_aircraft)
        Modele.place(x=500, y=175)
        aide = tk.Entry(Add_aircraft).place(x=500, y=225)
        manufae = tk.Entry(Add_aircraft).place(x=500, y=275)
        manufade = tk.Entry(Add_aircraft).place(x=500, y=325)
        ppe = tk.Entry(Add_aircraft).place(x=500, y=375)
        Expectedsye = tk.Entry(Add_aircraft).place(x=500, y=425)
        mtimee = tk.Entry(Add_aircraft).place(x=500, y=475)


        Add_aircraft.mainloop()
    def Fuel_Management():
        return
    def Aircraft_Maintenance():
        return
    def setting():
        return
    Make_flight = tk.Button(dashboard, text="✈️ Make Flight", font=("Arial", 12), bg="#2ECC71", fg="white", command=make_flight).place(x=10, y=350)
    Add_Employee = tk.Button(dashboard, text="👨‍✈️ Add Employee", font=("Arial", 12), bg="#2ECC71", fg="white", command=Add_Employee).place(x=200, y=350)
    in_out = tk.Button(dashboard, text="💰 Income/Expense", font=("Arial", 12), bg="#2ECC71", fg="white", command=in_out).place(x=400, y=350)
    Grounded = tk.Button(dashboard, text="🏠 Grounded", font=("Arial", 12), bg="#2ECC71", fg="white", command=Grounded).place(x=600, y=350)
    Flight_List = tk.Button(dashboard, text="📜 Flight List", font=("Arial", 12), bg="#2ECC71", fg="white", command=Flight_List).place(x=10, y=400)
    buy_sell = tk.Button(dashboard, text="💵 Buy/Sell", font=("Arial", 12), bg="#2ECC71", fg="white", command=buy_sell).place(x=200, y=400)
    op_aircraft = tk.Button(dashboard, text="🛩️ Operational Aircraft List", font=("Arial", 12), bg="#2ECC71", fg="white", command=op_aircraft).place(x=400, y=400)
    Add_aircraft = tk.Button(dashboard, text="➕ Add Aircraft", font=("Arial", 12), bg="#2ECC71", fg="white", command=Add_aircraft).place(x=400, y=450)
    Fuel_Management = tk.Button(dashboard, text="⛽ Fuel Management", font=("Arial", 12), bg="#2ECC71", fg="white", command=Fuel_Management).place(x=10, y=450)
    Aircraft_Maintenance = tk.Button(dashboard, text="🔧 Aircraft Maintenance", font=("Arial", 12), bg="#2ECC71", fg="white", command=Aircraft_Maintenance).place(x=200, y=450)
    setting = tk.Button(dashboard, text="", font=("Arial", 12), bg="#2ECC71", fg="white", command=setting).place(x=15, y=500)
    
    dashboard.mainloop()

conn = sqlite3.connect("airline.db")
cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS users (password TEXT)")
cursor.execute("INSERT INTO users (password) VALUES ('121212')")
conn.commit()

# Function for login authentication
def login():
    cursor.execute("SELECT password FROM users WHERE rowid=1")
    stored_password = cursor.fetchone()[0]

    if entry_password.get() == stored_password:
        login_window.destroy()
        open_dashboard()
    else:
        messagebox.showerror("Login Failed", "Incorrect Password!")

# Function to open the Change Password window
def open_change_password():
    change_password_window = tk.Toplevel()
    change_password_window.title("Change Password")
    change_password_window.geometry("400x250")
    change_password_window.configure(bg="#1C2833")

    tk.Label(change_password_window, text="Change Password", font=("Arial", 18, "bold"), fg="white", bg="#1C2833").pack(pady=10)
    
    tk.Label(change_password_window, text="Old Password:", fg="white", bg="#1C2833").pack()
    entry_old_password = tk.Entry(change_password_window, show="*")
    entry_old_password.pack()

    tk.Label(change_password_window, text="New Password:", fg="white", bg="#1C2833").pack()
    entry_new_password = tk.Entry(change_password_window, show="*")
    entry_new_password.pack()

    def change_password():
        cursor.execute("SELECT password FROM users WHERE rowid=1")
        stored_password = cursor.fetchone()[0]

        if entry_old_password.get() == stored_password:
            cursor.execute("UPDATE users SET password=? WHERE rowid=1", (entry_new_password.get(),))
            conn.commit()
            messagebox.showinfo("Success", "Password changed successfully!")
            change_password_window.destroy()
        else:
            messagebox.showerror("Error", "Old password is incorrect!")

    tk.Button(change_password_window, text="Change Password", command=change_password, bg="#2ECC71", fg="white").pack(pady=10)

login_window = tk.Tk()
login_window.title("Login Page")
login_window.geometry("500x350")
login_window.configure(bg="#1C2833")
tk.Label(login_window, text="Well Come To Miki Ways Airlines Group", font=("Arial", 18, "bold"), fg="white", bg="#1C2833").pack(pady=10)
tk.Label(login_window, text="You Are On Safe Hands", font=("Arial", 14), fg="white", bg="#1C2833").pack()
tk.Label(login_window, text="Enter Password", fg="white", bg="#1C2833").pack(pady=5)
entry_password = tk.Entry(login_window, show="*", font=("Arial", 14))
entry_password.pack(pady=5)
tk.Button(login_window, text="Login", font=("Arial", 12), bg="#2ECC71", fg="white", command=login).pack(pady=10)
tk.Button(login_window, text="Change Password", font=("Arial", 12), bg="#E74C3C", fg="white", command=open_change_password).pack()
login_window.mainloop()


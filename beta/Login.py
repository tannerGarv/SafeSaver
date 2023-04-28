from tkinter import *
import sqlite3
import tkinter.messagebox
import hashlib

#def helloCallBack():
   #tkinter.messagebox.showinfo( "Hello Python", "Hello World")

def signup():
    screen = Tk()
    screen.title("Safekey")
    screen.geometry("340x440")
    entry = Tk.entry()
    
    Label(text = "Username", height = "2", width = "25").pack()
    Label(text = "").pack()
    Label(text = "Password", bg = 'grey', height = "2", width = "25").pack()
    Label(text = "").pack()
    
    user = Entry("Username: ")
    pwd = Entry("Password: ")

    enc = pwd.encode()
    enchash = hashlib.md5(enc).hexdigest()

    with open("database.txt", "w") as f:
        f.write(user + "\n")
        f.write(enchash)
    f.close()
    print ("Confirmed Registration")

def login_screen():
    screen = Tk()
    screen.title("Safekey")
    screen.geometry("340x440")

    Label(text = "Username", height = "2", width = "25").pack()
    Label(text = "").pack()
    Label(text = "Password", height = "2", width = "25").pack()
    Label(text = "").pack()

def login():
    user = input("Enter Username: ")
    pwd = input("Enter Password: ")

    auth = pwd.encode()
    auth_enchash = hashlib.md5(auth).hexdigest()
    
    with open("database.txt", "r") as f:
        user, pwd = f.read().split("\n2")
    f.close()

    if user == user and auth_enchash == pwd:
        print("Success!")
    else:
        print("Failed!")

def main_screen():
    screen = Tk()
    screen.geometry("340x440")
    screen.title("Safekey")

    Label(text = "Sign in", bg = 'grey', width = '300', height = '2', font = ('AniMe Matrix -MB_EN', 12)).pack()
    Label(text = "").pack()

    Button(text = "LOGIN", height = "2", width = "25", command = login_screen).pack()
    Label(text = "").pack()
    Button(text = "REGISTER", height = "2", width = "25", command = signup).pack()

    screen.mainloop()

main_screen()
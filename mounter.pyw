#!/usr/bin/env python2.7
#########################################################
#               Techknow Mounter 0.0.2                  #
#    Mounts Webdav Volumes for the Techknow Classes     #
#         By John Hass <john@techknow.io>               #
#             License GPLv2 no Warrantys!               #
# https://www.gnu.org/licenses/old-licenses/gpl-2.0.txt #
#########################################################
import Tkinter as tk
import os
import platform
from Tkinter import *
import tkMessageBox
import sys

def center(win):
    win.update_idletasks()
    width = win.winfo_width()
    height = win.winfo_height()

    if platform.system == "Windows":
        width=253
        height=75
    x = (win.winfo_screenwidth() // 2) - (width // 2)
    y = (win.winfo_screenheight() // 2) - (height // 2)
    win.geometry('{}x{}+{}+{}'.format(width, height, x, y))

def login(event=None):
    username = root.usernametxt.get().strip()
    password = root.passwordtxt.get().strip()
    if username == "" or password == "":
        tkMessageBox.showinfo("Error", "Username or Password Blank")
    #username and password aren't blank
    url = "https://" + username +":"+password+"@cloud.techknow.io"
    if platform.system() == "Darwin":
        print "/usr/bin/osascript -e 'mount volume "+url+"'"
        os.system("diskutil unmount /Volumes/cloud.techknow.io")
        output = os.system("/usr/bin/osascript -e 'mount volume \""+url+"\"'")
        if output != 0:
            tkMessageBox.showinfo("Error", "Username or Password Invalid")
            root.passwordtxt.delete(0, END)
        else:
            os.system("open /Volumes/cloud.techknow.io")
            tkMessageBox.showinfo("Volume Connected", "Your volume is now connected!")
            sys.exit(0)
    if platform.system() == "Windows":
        print "net use z: /delete"
        os.system("net use z: /delete")
        output = os.system("net use z: https://cloud.techknow.io /user:" + username + " " +password)
        if os.path.exists('z:') == False:
            tkMessageBox.showinfo("Error", "Username or Password Invalid")
            root.passwordtxt.delete(0, END)
        else:
            tkMessageBox.showinfo("Drive Connected", "Your Z Drive is now connected!")
            os.system('explorer /select,"z:\"')
            sys.exit(0)
def buildGUI():
    photo = """ R0lGODlhQABAAOZ/AI2Mjcvlpfq6aP7s1rS0tP3cs8TDxHt6ev79/RBttqWlpdPT0/vMkPBFaezs7PFWd/rG0fmlO/b29veZrJLIQs3NzZqZmb29vWVkZfiouW1rbDk5OPmsS5zD4fR2kZKRkUxMS9LosPq0XPm4xoSDhPn5+fmoQu0pUubm5oi22tra2fvKi/Ly8nRzc/iZIf7y4uXy0cXim3Kq1LvW6/u/c/zUo+z0+fvR2t7e3kFBQK2srfvDfP3iwNbquPvHhPqxVN3uxFNTU//69f79+f/58f716fzRnPr89cnJyazN5uHh4f3myaqpqf3i6P3fut3q9aXI5PP56l5dXqnUaVlZWKDG4v7w8vv8/O324f3ozWij0WhmaPzf5fzaroiHiGFfYJmXmfH452loaKysq5S+3ur129Lk8YB/f/ieK8/nrF1bXc/i8Hyw1/R+l5XKR5+fn+Ht9vb5/P74+f72+P/48Pq/y/7v3Pf78cvg72Kfz4+Oj+Tk5OwbR1xaXDMzMv///yH/C1hNUCBEYXRhWE1QPD94cGFja2V0IGJlZ2luPSLvu78iIGlkPSJXNU0wTXBDZWhpSHpyZVN6TlRjemtjOWQiPz4gPHg6eG1wbWV0YSB4bWxuczp4PSJhZG9iZTpuczptZXRhLyIgeDp4bXB0az0iQWRvYmUgWE1QIENvcmUgNS42LWMwNjcgNzkuMTU3NzQ3LCAyMDE1LzAzLzMwLTIzOjQwOjQyICAgICAgICAiPiA8cmRmOlJERiB4bWxuczpyZGY9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkvMDIvMjItcmRmLXN5bnRheC1ucyMiPiA8cmRmOkRlc2NyaXB0aW9uIHJkZjphYm91dD0iIiB4bWxuczp4bXBNTT0iaHR0cDovL25zLmFkb2JlLmNvbS94YXAvMS4wL21tLyIgeG1sbnM6c3RSZWY9Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC9zVHlwZS9SZXNvdXJjZVJlZiMiIHhtbG5zOnhtcD0iaHR0cDovL25zLmFkb2JlLmNvbS94YXAvMS4wLyIgeG1wTU06RG9jdW1lbnRJRD0ieG1wLmRpZDpDMThEMTc3QTgxRDMxMUU1QkNEM0U2Njk3NzNEQjQyMyIgeG1wTU06SW5zdGFuY2VJRD0ieG1w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 """
    photo = PhotoImage(data=photo)
    root.title("Techknow Webdav Connector")
    root.logolbl = tk.Label(root, image=photo, anchor=CENTER)

    root.logolbl.grid(row=0,column=3,rowspan=3,columnspan=1, sticky="e")
    root.usernamelbl = tk.Label(root, text="Username")
    root.usernamelbl.grid(row=0)
    root.usernametxt = tk.Entry(root)
    root.usernametxt.grid(row=0,column=1,sticky="nsew",columnspan=2)
    root.usernametxt.focus()
    root.passwordlbl = tk.Label(root, text="Password")
    root.passwordlbl.grid(row=1)
    root.passwordtxt = tk.Entry(root,show="*")
    root.passwordtxt.grid(row=1,column=1,sticky="nsew")

    root.loginButton = tk.Button(root, text='Login Now',command=login)
    root.loginButton.grid(row=2,column=1,sticky="nsew")

    root.bind('<Return>', login)
    center(root)
    root.lift()
    root.mainloop()

print platform.system()
print os.path.exists('z:')
root = tk.Tk()
if platform.system() == "Windows":
    root.attributes("-toolwindow", 1)

if platform.system() == "Darwin":
    os.system('''/usr/bin/osascript -e 'tell app "Finder" to set frontmost of process "Python" to true' ''')
    buildGUI()
if platform.system() == "Windows":
    buildGUI()

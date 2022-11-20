# import modules
from tkinter import *
import os


# user define function
def shutdown():
	return os.system("shutdown /s /t 1")

def restart():
	return os.system("shutdown /r /t 1")

def logout():
	return os.system("shutdown -l")


# crating tkinter object
master = Tk()

# background set to grey
master.configure(bg='light grey')

# creating a button using the widget
# Buttons that will call the submit function
Button(master, text="Shutdown", command=shutdown).grid(row=0)
Button(master, text="Restart", command=restart).grid(row=1)
Button(master, text="Log out", command=logout).grid(row=2)

mainloop()


'''
we can sut dwon our pc using py-command 

sutdown pc ------- > import os  os.system("shutdown /s/t 1")
restart pc ------ > import os   os.system("shutdown /r /t 1")
logout pc ------ > import os   os.system("shutdown -l")
'''

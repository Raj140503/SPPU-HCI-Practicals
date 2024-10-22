from tkinter import *
from functools import partial

def validateLogin(username, password):
	print("username entered :", username.get())
	print("password entered :", password.get())
	lognSucess = Label(tkWindow, text="Login Successfully!!!").grid(row=5, column=0)
	return

def clearLogin(username,password):
	usernameEntry.delete(0, 'end')
	passwordEntry.delete(0, 'end')
	return

#window
tkWindow = Tk()
tkWindow.geometry('400x150')
tkWindow.title('Welcome to Login Form ')

#username label and text entry box
usernameLabel = Label(tkWindow, text="User-Name").grid(row=0, column=0)
username = StringVar()
usernameEntry = Entry(tkWindow, textvariable=username).grid(row=0, column=1)

#password label and password entry box
passwordLabel = Label(tkWindow,text="Password").grid(row=1, column=0)
password = StringVar()
passwordEntry = Entry(tkWindow, textvariable=password, show='*').grid(row=1, column=1)

validateLogin = partial(validateLogin, username, password)
clearLogin = partial(clearLogin, username, password)

#login button
loginButton = Button(tkWindow, text="Login", command=validateLogin).grid(row=4, column=0)

cancelButton = Button(tkWindow, text="Clear", command=clearLogin).grid(row=4, column=1)


tkWindow.mainloop()
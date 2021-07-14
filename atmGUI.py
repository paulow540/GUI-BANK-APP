from tkinter import *
import tkinter.ttk as ttk
from tkinter.messagebox import *
import mysql.connector
import random
import time

class Atm():
	def __init__(self):
		self.root = Tk()
		# self.root.iconbitmap('icons8_Calculator.ico')
		self.root.title('ATM App')
		self.mainFrame = Frame(self.root)
		self.mainFrame.grid(row=1, column=0)
		self.main()
		self.connection()
		self.root.mainloop()

	def connection(self):
		self.mycon = mysql.connector.connect(host='localhost', passwd='', user='root', database='bank')
		self.mycursor = self.mycon.cursor()

	def main(self):
		self.screen = Text(self.mainFrame, width=53, height=5)
		self.screen.insert(1.0,'Welcome to my bank\n Press the register button to register or Enter your pin to continue transactions')
		self.screen.grid(row=1, column=0, columnspan=5)
		self.pinScreen = Entry(self.mainFrame, width=50, show='*')
		self.pinScreen.grid(row=2, column=0, columnspan=5)
		# self.screen.delete(1.0, 'end')
		# self.screen.insert(1.0, 'Enter your pin to continue transactions')
		Button(self.mainFrame, text='-', width=7, height=3, command=lambda: self.pin('-')).grid(row=4, column=0)
		Button(self.mainFrame, text='-', width=7, height=3, command=lambda: self.pin('-')).grid(row=5, column=0)
		Button(self.mainFrame, text='-', width=7, height=3, command=lambda: self.pin('-')).grid(row=6, column=0)

		Button(self.mainFrame, text=7, width=7, height=3, command=lambda: self.pin('7')).grid(row=4, column=1)
		Button(self.mainFrame, text=8, width=7, height=3, command=lambda: self.pin('8')).grid(row=4, column=2)
		Button(self.mainFrame, text=9, width=7, height=3, command=lambda: self.pin('9')).grid(row=4, column=3)

		Button(self.mainFrame, text=4, width=7, height=3, command=lambda: self.pin('4')).grid(row=5, column=1)
		Button(self.mainFrame, text=5, width=7, height=3, command=lambda: self.pin('5')).grid(row=5, column=2)
		Button(self.mainFrame, text=6, width=7, height=3, command=lambda: self.pin('6')).grid(row=5, column=3)

		Button(self.mainFrame, text=1, width=7, height=3, command=lambda: self.pin('1')).grid(row=6, column=1)
		Button(self.mainFrame, text=2, width=7, height=3, command=lambda: self.pin('2')).grid(row=6, column=2)
		Button(self.mainFrame, text=3, width=7, height=3, command=lambda: self.pin('3')).grid(row=6, column=3)

		Button(self.mainFrame, text='Enter', width=7, height=3, command=self.enter).grid(row=4, column=4)
		Button(self.mainFrame, text='Delete', width=7, height=3, command=self.delete).grid(row=5, column=4)
		Button(self.mainFrame, text='Cancel', width=7, height=3, command=lambda: self.cancel('')).grid(row=6, column=4)

		Button(self.mainFrame, text='Register', font=(20), width=50, height=5, command=self.register).grid(row=7, column=0, columnspan=5)

	def delete(self):
		self.onScreen = self.pinScreen.get()
		self.pinScreen.delete(0, len(self.pinScreen.get()))
		self.pinScreen.insert(0, self.onScreen[:-1])


	

me = Atm()
import threading
import paramiko
import subprocess
from tkinter import *
from main import *

class tampilan_gui():
	def tampilan():
		## Judul
		window = Tk( )
		window.title("Kiara Project")

		## Info
		tulis = StringVar( )
		label = Label(window, textvariable=tulis, relief=RAISED) 
		tulis.set("Login To Your Server \n Make sure Kiara running on your server") 
		label.pack(side=TOP)

		#Isi Data seperti Username dan Password 
		ip_address = Label(window, text="Ip Address") #.grid(column=2, row=2, sticky=W)
		ip_address.pack(side=LEFT)
		ip = Entry(window, bd=5)
		ip.pack(side=LEFT)

		port = Label(window, text="Port")
		port.pack(side=LEFT)

		port_isi = Entry(window, bd=5, width=6)
		port_isi.pack(side=LEFT)

		username = Label(window, text="username")
		username.pack(side=LEFT)
		usr = Entry(window, bd=5)
		usr.pack(side=LEFT)

		pasword = Label(window, text="Password")
		pasword.pack(side=LEFT)

		passwd = Entry(window, show="*",bd=5)
		passwd.pack(side=LEFT)

		kiara = Label(window, text="Kiara Project Version 1.0")
		kiara.pack(side=BOTTOM)
		
		kiara_Button = Button(window, text="Connect", command=gui)
		kiara_Button.pack()

	def ssh_command(ip, usr, passwd):
		client = paramiko.SSHClient()
		client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
		client.connect(ip, username=usr, password=passwd)
		ssh_session = client.get_transport().open_session()
		if ssh_session.active:
			print (ssh_session.recv(1024))
		return

		window.mainloop()
	tampilan()	

tampilan_gui()
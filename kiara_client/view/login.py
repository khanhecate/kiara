from tkinter import *
#from tkinter import messagebox

class tampilan_gui:
	def __init__(self, master):
		bingkai = Frame(master, width=500, height=500, bd=1)
		bingkai.pack()

		self.mbar = Frame(bingkai, relief= 'raised', bd=2 )
		self.mbar.pack(fill = X)

		bingkai_ip = Frame(bingkai, bd=2, relief=RIDGE)

		Label(bingkai_ip, text="Ip address", bd=5).pack(side=LEFT,padx=5)
		Entry(bingkai_ip, bd=5).pack(side=RIGHT, padx=5)

		bingkai_ip.pack(expand=1, fill= X, pady=10, padx=50)

		bingkai_port = Frame(bingkai, bd=2, relief=RIDGE)

		Label(bingkai_port, text="port", bd=5).pack(side=LEFT,padx=5)
		Entry(bingkai_port, bd=5).pack(side=RIGHT, padx=5)

		bingkai_port.pack(expand=1, fill= X, pady=20, padx=50)

		bingkai_usr = Frame(bingkai, bd=2, relief=RIDGE)

		Label(bingkai_usr, text="Username", bd=5).pack(side=LEFT,padx=5)
		Entry(bingkai_usr, bd=5).pack(side=RIGHT, padx=5)

		bingkai_usr.pack(expand=1, fill= X, pady=10, padx=50)

		bingkai_passwd = Frame(bingkai, bd=2, relief=GROOVE)

		Label(bingkai_passwd, text="Password", bd=5).pack(side=LEFT,padx=5)
		Entry(bingkai_passwd,show="*", bd=5).pack(side=RIGHT, padx=5)

		bingkai_passwd.pack(expand=1, fill= X, pady=20, padx=50)

		Ok = Button(bingkai, text="Connect", ).pack(side=TOP, padx=50)
		exit = Button(bingkai, text="exit", fg="red").pack(side=TOP, padx=50)


		
window = Tk()
window.title("Kiara")
tampil = tampilan_gui(window)
window.mainloop()

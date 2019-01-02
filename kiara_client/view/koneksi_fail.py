from tkinter import *

class cure:

	def __init__(self, master):

		self.frame = Frame(master, width=500, bd=2)
		self.frame.pack()

		self.ker = Frame(self.frame,relief=RAISED, bd=6)
		self.ker.pack(fill = X)

		label = Label(self.ker, justify=CENTER,text=" Wrong Username or Password or Ip Address or Port, Connection Fail ")
		label.pack(side=RIGHT)

		fail_army = Frame(frame, width=500, bd=5, relief=FLAT)
		fail_army.pack(fill = X)

		label_satu = Label(fail_army, text=" Please Make sure your username/password/ip address/port is correct including your Heart.", relief=FLAT)
		label_satu.pack(expand=1, fill= X,padx=10, pady=20)

		tryu = Button(fail_army, fg="blue", text="Try Again")
		tryu.pack(side=RIGHT)

		cancel = Button(fail_army, fg="Red", text="Cancel", command=quit )
		cancel.pack(side=RIGHT)

frame = Tk()
frame.title("Connection TimeOut")
inti = cure(frame)
frame.mainloop()

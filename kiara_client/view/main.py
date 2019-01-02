from tkinter import *
from tkinter import messagebox
class main:
	"""docstring for main"""
	def __init__(self, master):

		dicto = {
		 1 : "RED",2 : "GREEN",3 : "PINK",4 : "BLACK",5 : "YELLOW",6 : "GRAY",7 : "BLUE"
		}
		
		
		
		
		
		
		


		main_frame = Frame(master, width=500)
		main_frame.pack()

		self.bar = Frame(relief= RAISED, bd=2)
		self.bar.pack(fill= X)

		welcome = Label(self.bar, text="Hallo : ")
		welcome.pack(side=LEFT)
		
		child_frame = Frame(master, height=500, bd=5 )
		child_frame.pack(fill = X)


		### AUTO CONFIG MENU
		self.service_menu = Menubutton(child_frame, text="Services") 
		self.service_menu.pack(side=LEFT)

		### AUTO CONFIG MENU
		self.child_service_menu = Menu(self.service_menu, tearoff=0)
		self.service_menu ['menu'] = self.child_service_menu

		self.child_service_menu.add_command(label="Bind Auto")
		#####################

		### SET UP ACCOUNT etc
		self.system_menu = Menubutton(child_frame, text="System") 
		self.system_menu.pack(side=LEFT)

		### Child Menu System
		self.child_system_menu = Menu(self.system_menu, tearoff=0)
		self.system_menu ['menu'] = self.child_system_menu

		### Content Menu System
		self.child_system_menu.add_command(label="Username")
		self.child_system_menu.add_command(label="Password")


		### MANAGE STORAGE
		self.storage_menu = Menubutton(child_frame, text="Storage")
		self.storage_menu.pack(side=LEFT)

		### CHILD MANAGE STORAGE
		self.child_storage_menu = Menu(self.storage_menu, tearoff=0)
		self.storage_menu ['menu'] = self.child_storage_menu

		### Content Storage
		self.child_storage_menu.add_command(label="RAID")

		
		### TERMINAL 
		self.terminal_button = Button(child_frame, text="Terminal") 
		


		
		### Seting Kiara
		self.setting_kiara_menu = Menubutton(child_frame, text="Setting Kiara")
		self.setting_kiara_menu.pack(side=LEFT)

		### CHILD KIARA SETTING
		self.child_setting_kiara_menu = Menu(main_frame)
		self.grandchild_setting_kiara_menu = Menu(main_frame)

		self.child_setting_kiara_menu = Menu(self.setting_kiara_menu, tearoff=0)
		self.setting_kiara_menu ['menu'] = self.child_setting_kiara_menu

		### CONTENT KIARA SETTING
		def color():
			grandchild_setting_kiara_menu.add_command(command=dicto[0])	

		self.grandchild_setting_kiara_menu.add_radiobutton(label="red")
		self.grandchild_setting_kiara_menu.add_radiobutton(label="green")
		self.grandchild_setting_kiara_menu.add_radiobutton(label="pink")
		self.grandchild_setting_kiara_menu.add_radiobutton(label="black")
		self.grandchild_setting_kiara_menu.add_radiobutton(label="yellow")
		self.grandchild_setting_kiara_menu.add_radiobutton(label="gray")
		self.grandchild_setting_kiara_menu.add_radiobutton(label="blue")

		self.child_setting_kiara_menu.add_cascade(label="Background", menu=self.grandchild_setting_kiara_menu)
		

		### About
		def pesan():
			messagebox.showinfo("About", "Kiara Project, Hello There... Nice to meet you \n Kiara Version 1.0.0 ( BETA )")
		about_button = Button(child_frame, text="About", command=pesan, relief=FLAT)
		about_button.pack(side=LEFT)

		### WEB INTERFACES ###
		self.web_interfaces = Button(child_frame,text="Web Interfaces", relief=FLAT)
		self.web_interfaces.pack(side=LEFT)

main_frame = Tk()
main_frame.title("Welcome To Kiara")
main_tampil = main(main_frame)
main_frame.mainloop()

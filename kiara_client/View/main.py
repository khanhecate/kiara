import tkinter as tk
import os
import textwrap
from tkinter import messagebox
from tkinter import *

#### PENGHUBUNG #####

#ssh_command(ip, usr,passwd,cmd)

### SEMUA DEFINISI UNTUK AUTO CONFIG DISINI ###
def bdac():
	print("Waiting...")
	os.system("sudo chmod -R 755 bdac/*")
	os.system("cd bdac/")
	os.system("./bdac")
#################################

## Awalan ##
def gui():
	jendela = Tk()
	#frame = tk.Frame(jendela)
	#frame.pack()

	## Tengah ##
	jendela.title("Kiara Project")
	minta = tk.Button(jendela, text="Readme", fg="Black", command=pesan) .grid(column=1, row=1, sticky=W)  
	#Label (jendela, fg="Black") .grid(column=1, row=1, sticky=W)
	bdac_user = tk.Button(jendela, text="Bdac Configure", fg="Blue", command=komen) .grid(column=1, row=2, sticky=W) 
	#user_installl = tk.Button(jendela, text="Install", fg="Black", command=installl) 
	jendela.mainloop()

#### PENTING ########
def pesan():
	messagebox.showinfo("Readme", "Have you already install / download all of this \n 1.Python3.6 \n 2.python3.6-tk")
def installl():
	os.system("sudo apt-get update")

def komen():
	jendela = Tk()
	user_iya = tk.Button(jendela, text="YES", fg="black", command=bdac) 
	user_tidak = tk.Button(jendela, text="NO", fg="red", command=quit) 
######################
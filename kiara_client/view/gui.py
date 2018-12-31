#from tkinter import messagebox
#from tkinter import *
#import main as konfig


## Awalan ##
def gui():
	jendela = tk.Tk()
	frame = tk.Frame(jendela)
	frame.pack()

	## Tengah ##
	jendela.title("Kiara")
	minta = tk.Button(frame, text="Readme", fg="Black", command=pesan) .grid(column=1, row=3)
	bdac_user = tk.Button(frame, text="BDAC Configure", fg="Blue", command=komen) .grid(column=1, row=1)
	user_installl = tk.Button(frame, text="Install", fg="Black", command=installl) .grid(column=1, row=2)

	jendela.mainloop()
#### PENTING ########
def pesan():
	messagebox.showinfo("Readme", "Have you already install / download all of this \n 1.Python3.6 \n 2.python3.6-tk")
def installl():
	os.system("sudo apt-get update")

def komen():
	user_iya = tk.Button(frame, text="YES", fg="black", command=bdac) .grid(column=2, row=1)
	user_tidak = tk.Button(frame, text="NO", fg="red", command=quit) .grid(column=2, row=2)
######################
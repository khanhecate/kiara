from tkinter import *

class koneksi:
 	"""docstring for koneksi"""
 	def __init__(self, master):

 		main_frame = Frame(master, width=400, bd=5)
 		main_frame.pack()

 		self.frame_bar = Frame(main_frame, width=200, height=100, bd=4)
 		self.frame_bar.pack(fill = X)

 		self.label = Label(self.frame_bar, text="Please make sure your user is active/exist on your server...")
 		self.label.pack(expand=1, pady=20, padx=30)

 		self.tombol = Button(self.frame_bar, text="Try Again", fg="blue")
 		self.tombol.pack(side=RIGHT)

 		self.gagal = Button(self.frame_bar, fg="red",text="Cancel", command=quit)
 		self.gagal.pack(side=RIGHT)

tampil =Tk()
tampil.title("Connection Reject")
muncul = koneksi(tampil)
tampil.mainloop()

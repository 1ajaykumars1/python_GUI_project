from tkinter import *

window = Tk()
window.geometry("500x500")
window.title("python GUI program")
icon = PhotoImage(file="logo.png")
window.iconphoto(True, icon)
window.config(background="#4a9183")

window.mainloop()
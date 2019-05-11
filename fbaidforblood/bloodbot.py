#!/usr/bin/python
from tkinter import *;
window = Tk()
window.geometry('900x600')
window.configure(background='white')

window.title("BloodFinderBot")
window.iconbitmap('icon.ico')

app_title=Label(window, bg="white", text="Blood Finder Bot", fg="#0536BC")
msg_status = Label(window,bg="white",text="Bienvenue, vous n'etes pas connecté!", fg="#3E3E3E")
msg_instruction = Label(window,bg="white",text="Vous pouvez cliquer sur le bouton en bas pour le faire", fg="#3E3E3E")


app_title.configure(font=('Sitka',20, "bold"))
msg_status.configure(font=('Sitka',15))
msg_instruction.configure(font=('Skita',13,"bold"))
photo = PhotoImage(file='icon.png')
labelphoto = Label(window,image=photo)
labelphoto.place(x=10,y=10)
app_title.place(x=320,y=10)
msg_status.place(x=300,y=200)
msg_instruction.place(x=260, y=240)

btn_seconnecter = Button(window, text="Se connecter", bg="#F50707", fg="#FFFFFF")
btn_seconnecter.place(x=380,y=300)
btn_seconnecter.configure(height=2, width=15)
btn_seconnecter.config(font=('Skita', 13, "bold"))
window.resizable(False, False)
window.mainloop()

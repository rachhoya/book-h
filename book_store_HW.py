from tkinter import *

window=Tk()
window.geometry("400x350")
window.title("Book Inventory")
window.config(background="green")

title=Label(window,text="Book Title:",bg="dark grey",font=("Times",16,"bold"))
title.place(x=55,y=60)

entry_box=Entry(window,width=30)
entry_box.place(x=170,y=65)

author=Label(window,text="Author:",bg="dark grey",font=("Times",16,"bold"))
author.place(x=55,y=120)

entry_box2=Entry(window,width=30)
entry_box2.place(x=140,y=125)

price=Label(window,text="Price:",bg="dark grey",font=("Times",16,"bold"))
price.place(x=55,y=180)

entry_box3=Entry(window,width=30)
entry_box3.place(x=125,y=185)

save_book=Button(window,text="Save Book",command=window.destroy,bg="pink",border=2,width=10,font=("Times New Roman",15))
save_book.place(x=130,y=250)


window.mainloop()
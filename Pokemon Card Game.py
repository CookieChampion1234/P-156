from tkinter import*
from PIL import ImageTk, Image
root=Tk()

root.title("Pokemon Card Game")
root.geometry("600x400")

root.configure(background="green")

eevee=ImageTk.PhotoImage(Image.open("eevee.jpg"))
flareon=ImageTk.PhotoImage(Image.open("flareon.jpg"))
vaporeon=ImageTk.PhotoImage(Image.open("vaporeon.jpg"))
umbreon=ImageTk.PhotoImage(Image.open("umbreon.jpg"))
jolteon=ImageTk.PhotoImage(Image.open("jolteon.jpg"))
leafeon=ImageTk.PhotoImage(Image.open("leafeon.jpg"))
sylveon=ImageTk.PhotoImage(Image.open("sylveon.jpg"))
glaceon=ImageTk.PhotoImage(Image.open("glaceon.jpg"))
espeon=ImageTk.PhotoImage(Image.open("espeon.jpg"))

player1 = Label(root, text="Player 1", bg="light green", fg="dark green")
player1.place(relx=0.1, rely=0.3, anchor=CENTER)

player2 = Label(root, text="Player 2", bg="light green", fg="dark green")
player2.place(relx=0.9, rely=0.3, anchor=CENTER)

player1_score_label = Label(root, bg="light green", fg="dark green")
player1_score_label.place(relx=0.1, rely=0.4, anchor=CENTER)

player2_score_label = Label(root, bg="light green", fg="dark green")
player2_score_label.place(relx=0.9, rely=0.4, anchor=CENTER)


root.mainloop()

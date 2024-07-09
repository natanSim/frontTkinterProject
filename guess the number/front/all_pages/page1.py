from tkinter import *

window = Tk()

# region window properties
window.geometry('500x600')
window.resizable(False, False)
window.title("Guess The Number")
# endregion window properties

# region window elements
label_title = Label(master=window, text="Guess the random number", font=('Helvetica', 10))
label_title.place(x=165, y=15)

label_of_how_many_players = Label(master=window, text="How many players? ", font=('Helvetica', 22))
label_of_how_many_players.place(x=130, y=180)

text_box_of_how_many_players = Entry(master=window)
text_box_of_how_many_players.place(x=185, y=250)

button_continue = Button(master=window, text= "continue",  font=('Helvetica', 12))
button_continue.place(x=215, y=450)
# endregion window elements

window.mainloop()

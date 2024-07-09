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

label_of_player_name = Label(master=window, text="Insert your full name: ", font=('Helvetica', 22))
label_of_player_name.place(x=120, y=180)

text_box_of_player_name = Entry(master=window)
text_box_of_player_name.place(x=185, y=250)
# endregion window elements


window.mainloop()


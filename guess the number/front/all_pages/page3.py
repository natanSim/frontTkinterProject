from tkinter import *

# region window properties
window = Tk()
window.geometry('500x600')
window.resizable(False, False)
window.title("Guess The Number")
# endregion window properties

# region window elements
label_title = Label(master=window, text="Guess the random number", font=('Helvetica', 10))
label_title.place(x=165, y=15)

# region player details
label_name = Label(master=window, text="Name: natan", font=('Helvetica', 12))
label_name.place(x=30, y=70)

label_player_number = Label(master=window, text="Player number: 1", font=('Helvetica', 12))
label_player_number.place(x=190, y=70)

label_amount_of_guesses = Label(master=window, text="Guesses: 14", font=('Helvetica', 12))
label_amount_of_guesses.place(x=370, y=70)
# endregion player details

label_of_insert_number = Label(master=window, text="Insert number from 1 - 100:", font=('Helvetica', 22))
label_of_insert_number.place(x=75, y=200)

text_box_of_number = Entry(master=window)
text_box_of_number.place(x=185, y=270)
# endregion window elements


window.mainloop()



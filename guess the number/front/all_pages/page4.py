from tkinter import *

# region window properties
window = Tk()
window.geometry('500x600')
window.resizable(False, False)
window.title("Guess The Number")
# endregion window properties

# region window elements

label_of_winner = Label(master=window, text="The winner is:", font=('Helvetica', 24))
label_of_winner.place(x=155, y=220)

label_of_player_name = Label(master=window, text="Natan!", font=('Helvetica', 24))
label_of_player_name.place(x=195, y=260)
# endregion window elements

window.mainloop()

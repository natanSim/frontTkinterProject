from tkinter import *
from pages import *


def main():
    window = Tk()

    # region window properties
    window.geometry('500x600')
    window.resizable(False, False)
    window.title("Guess The Number")
    # endregion window properties

    label_title = Label(master=window, text="Guess the random number", font=('Helvetica', 24))
    label_title.place(x=65, y=15)

    open_first_page(window)

    window.mainloop()


if __name__ == '__main__':
    main()

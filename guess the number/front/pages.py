from tkinter import *


def clear_frame_from_window(window):
    for element in window.winfo_children():
        if type(element) is Frame:
            element.destroy()

    return window


def open_first_page(window):
    window_frame = Frame(master=window, width=500, height=500)

    label_of_how_many_players = Label(master=window_frame, text="How many players? ", font=('Helvetica', 22))
    label_of_how_many_players.place(x=120, y=130)

    text_box_of_how_many_players = Entry(master=window_frame)
    text_box_of_how_many_players.place(x=185, y=200)

    button_continue = Button(master=window_frame, text="continue",  font=('Helvetica', 12), command=lambda: open_second_page(window))
    button_continue.place(x=215, y=400)

    window_frame.place(x=0, y=80)

def open_second_page(window):
    clear_frame_from_window(window)

    window_frame = Frame(master=window, width=500, height=500)

    label_of_player_name = Label(master=window_frame, text="Insert your full name: ", font=('Helvetica', 22))
    label_of_player_name.place(x=120, y=130)

    text_box_of_player_name = Entry(master=window_frame)
    text_box_of_player_name.place(x=185, y=200)

    button_continue = Button(master=window_frame, text="continue", font=('Helvetica', 12), command=lambda: open_third_page(window))
    button_continue.place(x=215, y=400)

    window_frame.place(x=0, y=80)

def open_third_page(window):
    clear_frame_from_window(window)
    window_frame = Frame(master=window, width=500, height=500)

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

    button_continue = Button(master=window, text="continue", font=('Helvetica', 12), command=lambda: open_page_fourth(window))
    button_continue.place(x=215, y=480)

    window_frame.place(x=0, y=80)


def open_page_fourth(window):
    clear_frame_from_window(window)

    window_frame = Frame(master=window, width=500, height=500)

    label_of_winner = Label(master=window, text="The winner is:", font=('Helvetica', 24))
    label_of_winner.place(x=145, y=220)

    label_of_player_name = Label(master=window, text="Natan!", font=('Helvetica', 24))
    label_of_player_name.place(x=185, y=260)

    button_exit = Button(master=window, text="Exit", font=('Helvetica', 12), command=lambda: close_window(window))
    button_exit.place(x=225, y=480)

    window_frame.place(x=0, y=60)

def close_window(window):
    window.destroy()
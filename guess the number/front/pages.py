from tkinter import *


def get_entry_text(window):
    for element in window.winfo_children():
        if type(element) is Frame:
            for frame_element in element.winfo_children():
                if type(frame_element) is Entry:
                    print(f'frame_element.get() = {frame_element.get()}')
                    return frame_element.get()

    return None


def clear_frame_from_window(window):
    for element in window.winfo_children():
        if type(element) is Frame:
            element.destroy()

    return window


def is_entry_empty(entry_text):
    return entry_text == '' or entry_text is None


def is_number_in_range(number, minimum, maximum):
    return minimum <= number <= maximum


def contains_number(text):
    for i in text:
        if i.isdigit():
            return True
    return False


def is_ready_to_next_page(window, current_window_index):

    if current_window_index == 1:

        entry_text = get_entry_text(window)

        if is_entry_empty(entry_text):
            print("Stay as you are")
            return False

        if not entry_text.isdigit():
            print("Only numbers!!!")
            return False

        if not is_number_in_range(int(entry_text), 1, 5):
            print("Up to 5 players are allowed")
            return False

        clear_frame_from_window(window)

        return True

    elif current_window_index == 2:
        entry_text = get_entry_text(window)

        if is_entry_empty(entry_text):
            print("Stay as you are")
            return False

        if contains_number(entry_text):
            print("Enter a username without numbers")
            return False

        clear_frame_from_window(window)

        return True

    elif current_window_index == 3:
        entry_text = get_entry_text(window)

        if is_entry_empty(entry_text):
            print("Stay as you are")
            return False

        if not entry_text.isdigit():
            print("Only numbers!!!")
            return False

        if not is_number_in_range(int(entry_text), 1, 100):
            print("Up to 5 players are allowed")
            return False

        clear_frame_from_window(window)

        return True

    elif current_window_index == 4:
        close_window(window)

    else:
        return f"Natan fix that problem there is no exist page here"

    # TODO: Create validation and rules to move to the next page


def open_next_page(window, current_window_index):
    if current_window_index == 1 and is_ready_to_next_page(window, 1):
        clear_frame_from_window(window)
        open_second_page(window)

    elif current_window_index == 2 and is_ready_to_next_page(window, 2):
        clear_frame_from_window(window)
        open_third_page(window)

    elif current_window_index == 3 and is_ready_to_next_page(window, 3):
        clear_frame_from_window(window)
        open_fourth_page(window)

    elif current_window_index == 4 and is_ready_to_next_page(window, 4):
        clear_frame_from_window(window)
        close_window(window)


def open_first_page(window):
    window_frame = Frame(master=window, width=500, height=500)

    label_of_how_many_players = Label(master=window_frame, text="How many players? ", font=('Helvetica', 22))
    label_of_how_many_players.place(x=120, y=130)

    text_box_of_how_many_players = Entry(master=window_frame)
    text_box_of_how_many_players.place(x=185, y=200)

    button_continue = Button(master=window_frame, text="continue", font=('Helvetica', 12),
                             command=lambda: open_next_page(window, 1))
    button_continue.place(x=215, y=400)

    window_frame.place(x=0, y=80)


def open_second_page(window):
    window_frame = Frame(master=window, width=500, height=500)

    label_of_player_name = Label(master=window_frame, text="Insert your full name: ", font=('Helvetica', 22))
    label_of_player_name.place(x=120, y=130)

    text_box_of_player_name = Entry(master=window_frame)
    text_box_of_player_name.place(x=185, y=200)

    button_continue = Button(master=window_frame, text="continue", font=('Helvetica', 12),
                             command=lambda: open_next_page(window, 2))
    button_continue.place(x=215, y=400)

    window_frame.place(x=0, y=80)


def open_third_page(window):
    window_frame = Frame(master=window, width=500, height=500)

    # region player details
    label_name = Label(master=window, text="Name: natan", font=('Helvetica', 12))
    label_name.place(x=30, y=70)

    label_player_number = Label(master=window, text="Player number: 1", font=('Helvetica', 12))
    label_player_number.place(x=190, y=70)

    label_amount_of_guesses = Label(master=window, text="Guesses: 14", font=('Helvetica', 12))
    label_amount_of_guesses.place(x=370, y=70)
    # endregion player details

    label_of_insert_number = Label(master=window_frame, text="Insert number from 1 - 100:", font=('Helvetica', 22))
    label_of_insert_number.place(x=75, y=130)

    text_box_of_number = Entry(master=window_frame)
    text_box_of_number.place(x=185, y=200)

    button_continue = Button(master=window_frame, text="continue", font=('Helvetica', 12),
                             command=lambda: open_next_page(window, 3))
    button_continue.place(x=215, y=400)

    window_frame.place(x=0, y=80)


def open_fourth_page(window):
    window_frame = Frame(master=window, width=500, height=500)

    label_of_winner = Label(master=window, text="The winner is:", font=('Helvetica', 24))
    label_of_winner.place(x=145, y=220)

    label_of_player_name = Label(master=window, text="Natan!", font=('Helvetica', 24))
    label_of_player_name.place(x=185, y=260)

    button_exit = Button(master=window, text="Exit", font=('Helvetica', 12), command=lambda: open_next_page(window, 4))
    button_exit.place(x=225, y=480)

    window_frame.place(x=0, y=60)


def close_window(window):
    window.destroy()
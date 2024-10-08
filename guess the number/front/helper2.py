from tkinter import *
from random import randint
from tkinter import messagebox


class Player:
    """

    """
    def __init__(self, name, random_number, player_number):
        self.name = name
        self.random_number = random_number
        self.player_number = player_number

        self.amount_of_guesses = 0
        self.guesses_history = []
        print(self.random_number)

    def get_name(self):
        return self.name

    def get_amount_of_guesses(self):
        return self.amount_of_guesses

    def get_player_number(self):
        return self.player_number

    def is_guess_correct(self, guess):
        return self.random_number == guess

    def increment_user_guesses(self):
        self.amount_of_guesses += 1

    def update_guess_history(self, new_guess):
        self.guesses_history.append(new_guess)


def get_entry_text(window):
    for element in window.winfo_children():
        if type(element) is Frame:
            for frame_element in element.winfo_children():
                if type(frame_element) is Entry:
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


def is_contains_number(text):
    for i in text:
        if i.isdigit():
            return True
    return False


def open_pop_up_window(text):
    messagebox.showerror("ERROR", text)


def is_ready_to_next_page(window, current_window_index):

    if current_window_index == 1:

        entry_text = get_entry_text(window)

        if is_entry_empty(entry_text):
            open_pop_up_window("Field is empty")
            return False

        if not entry_text.isdigit():
            open_pop_up_window("Only numbers!!!")

            return False

        if not is_number_in_range(int(entry_text), 1, 5):
            open_pop_up_window("Up to 5 players are allowed")
            return False

        return True

    elif current_window_index == 2:
        entry_text = get_entry_text(window)

        if is_entry_empty(entry_text):
            open_pop_up_window("Stay as you are")
            return False

        if is_contains_number(entry_text):
            open_pop_up_window("Enter a username without numbers")
            return False

        return True

    elif current_window_index == 3:
        entry_text = get_entry_text(window)

        if is_entry_empty(entry_text):
            open_pop_up_window("Stay as you are")
            return False

        if not entry_text.isdigit():
            open_pop_up_window("Only numbers!!!")

            return False

        if not is_number_in_range(int(entry_text), 1, 100) or not get_random_number():
            open_pop_up_window("only numbers from 1 to 100!")
            return False
        return True

    elif current_window_index == 4:
        close_window(window)

    else:
        return f"Natan fix that problem there is no exist page here"


def is_all_players_played(wanted_amount_of_players, current_amount_of_players):
    return wanted_amount_of_players == current_amount_of_players


def get_amount_of_players(program_data):
    return program_data["amount_of_players"]


def get_current_amount_of_players(program_data):
    return len(program_data.keys()) - 1


def open_next_page(window, current_window_index, program_data, player_data=None):
    if current_window_index == 1 and is_ready_to_next_page(window, 1) is True:
        program_data['amount_of_players'] = int(get_entry_text(window))
        clear_frame_from_window(window)
        open_second_page(window, program_data)

    elif current_window_index == 2 and is_ready_to_next_page(window, 2):
        name = get_entry_text(window)
        random_number = get_random_number()
        player_number = len(program_data.keys())
        clear_frame_from_window(window)

        new_player = Player(name, random_number, player_number)
        open_third_page(window, program_data, new_player)

    elif current_window_index == 3 and is_ready_to_next_page(window, 3):
        guess = int(get_entry_text(window))
        player_data.increment_user_guesses()
        player_data.update_guess_history(guess)

        if not player_data.is_guess_correct(guess):
            open_pop_up_window("Wrong number try again!")
            clear_frame_from_window(window)
            open_third_page(window, program_data, player_data)
            return

        program_data[player_data.get_name()] = player_data
        amount_of_players = get_amount_of_players(program_data)
        current_amount_of_players = get_current_amount_of_players(program_data)

        if not is_all_players_played(amount_of_players, current_amount_of_players):
            clear_frame_from_window(window)
            open_second_page(window, program_data)
            return

        player_places = get_winner(program_data)
        get_player_winner = list(player_places.values())
        clear_frame_from_window(window)
        open_fourth_page(window, program_data, get_player_winner)

    elif current_window_index == 4 and is_ready_to_next_page(window, 4):
        clear_frame_from_window(window)
        close_window(window)


# region back
def get_random_number():
    """
    :return: randint(1, 100)
    The function returns a number in a range of 1 to 100
    """
    return randint(1, 100)


def get_names_list(program_data):
    names_list = []
    for key in program_data.keys():
        if key == 'amount_of_players':
            continue
        names_list.append(key)
    print(f"list {names_list}")
    return names_list


def get_group_players_with_same_guesses(program_data):
    result = {}
    names_list = get_names_list(program_data)

    for player in names_list:

        if program_data[player].get_amount_of_guesses() not in result.keys():
            result[program_data[player].get_amount_of_guesses()] = player
            continue

        if isinstance(result[program_data[player].get_amount_of_guesses()], str):
            result[program_data[player].get_amount_of_guesses()] =\
                [result[program_data[player].get_amount_of_guesses()], player]

        elif isinstance(result[program_data[player].get_amount_of_guesses()], list):
            result[program_data[player].get_amount_of_guesses()].append(player)

    # print(list(result.values()))
    return result


def sort_users_data(program_data):

    names_list = list(program_data.keys())
    new_users_data = {}

    for i in range(len(names_list)):
        for z in range(i, len(names_list)):
            if names_list[i] > names_list[z]:
                saved = names_list[i]
                names_list[i] = names_list[z]
                names_list[z] = saved
        new_users_data[names_list[i]] = program_data[names_list[i]]

    return new_users_data


def get_winner(program_data):

    players_with_same_guesses_group = get_group_players_with_same_guesses(program_data)
    sort_players_place = sort_users_data(players_with_same_guesses_group)
    print(f'end_of_the game: {sort_players_place}  ')
    return sort_players_place
# endregion back


def open_first_page(window, program_data):
    window_frame = Frame(master=window, width=500, height=500)

    label_of_how_many_players = Label(master=window_frame, text="How many players? ", font=('Helvetica', 22))
    label_of_how_many_players.place(x=120, y=130)

    text_box_of_how_many_players = Entry(master=window_frame)
    text_box_of_how_many_players.place(x=185, y=200)

    button_continue = Button(master=window_frame, text="continue", font=('Helvetica', 12),
                             command=lambda: open_next_page(window, 1, program_data))
    button_continue.place(x=215, y=400)

    window_frame.place(x=0, y=80)


def open_second_page(window, program_data):
    window_frame = Frame(master=window, width=500, height=500)

    label_of_player_name = Label(master=window_frame, text="Insert your full name: ", font=('Helvetica', 22))
    label_of_player_name.place(x=120, y=130)

    text_box_of_player_name = Entry(master=window_frame)
    text_box_of_player_name.place(x=185, y=200)

    button_continue = Button(master=window_frame, text="continue", font=('Helvetica', 12),
                             command=lambda: open_next_page(window, 2, program_data))
    button_continue.place(x=215, y=400)

    window_frame.place(x=0, y=80)


def open_third_page(window, program_data, new_player_data):
    window_frame = Frame(master=window, width=500, height=500)

    # region player details
    label_name = Label(master=window_frame, text=f"Name: {new_player_data.get_name()}", font=('Helvetica', 12))
    label_name.place(x=30, y=20)

    label_player_number = Label(master=window_frame, text=f"Player number:{new_player_data.get_player_number()}",
                                font=('Helvetica', 12))
    label_player_number.place(x=190, y=20)

    label_amount_of_guesses = Label(master=window_frame, text=f"Guesses: {new_player_data.get_amount_of_guesses()}",
                                    font=('Helvetica', 12))
    label_amount_of_guesses.place(x=370, y=20)
    # endregion player details

    label_of_insert_number = Label(master=window_frame, text="Insert number from 1 - 100:", font=('Helvetica', 22))
    label_of_insert_number.place(x=75, y=130)

    text_box_of_number = Entry(master=window_frame)
    text_box_of_number.place(x=185, y=200)

    button_continue = Button(master=window_frame, text="continue", font=('Helvetica', 12),
                             command=lambda: open_next_page(window, 3, program_data, new_player_data))
    button_continue.place(x=215, y=400)

    window_frame.place(x=0, y=80)


def open_fourth_page(window, program_data, winner):
    window_frame = Frame(master=window, width=500, height=500)

    label_of_winner = Label(master=window_frame, text="The winner is:", font=('Helvetica', 24))
    label_of_winner.place(x=150, y=130)

    label_of_player_name = Label(master=window_frame, text=winner[0], font=('Helvetica', 24))
    label_of_player_name.place(x=230, y=190)

    button_exit = Button(master=window_frame, text="Exit", font=('Helvetica', 12),
                         command=lambda: open_next_page(window, 4, program_data))
    button_exit.place(x=225, y=400)

    window_frame.place(x=0, y=80)


def close_window(window):
    window.destroy()

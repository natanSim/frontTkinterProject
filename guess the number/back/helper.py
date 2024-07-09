from random import randint


def show_welcome_message_to_user():
    """
    - without parameters
    -returns nothing
    :return:
    The function print message to user
    """
    print('Welcome to guess the random number')


def show_message_to_user():
    """
       - without parameters
       -returns nothing
       :return:
       The function print message to user
       """

    print('Good luck!')


def get_name_from_user():
    """
    - without parameters
    :return: name
    The function get the name of the user
    """
    name = get_input_from_user('string', 'To continue to guess the random number insert your full name: ')
    return name


def get_player_data(user_name, number_to_guess):
    """
    :param user_name:
    :param number_to_guess:
    :return: player_data

    The function get the user data
    """

    player_data = {'name': user_name, 'amount_of_guesses': number_to_guess}
    return player_data


def add_player_data_to_table(table, player_data):
    """
    :param table:
    :param player_data:
    :return: table

    The function adding player data to table
    """

    print(f'table = {table}')
    table[player_data['name']] = player_data
    return table


def show_player_data(user_guesses):
    """
    :param user_guesses:
    :return: nothing
    The function prints the user data after his game
    """
    for key, value in user_guesses.items():
        print(f'{key} - amount of guesses: {value}\n')


def is_user_wants_clue():
    """
    - without parameters
    :return: ask_for_clue == 'yes'
    The function checking if the user want a clue in his turn
    """

    while True:
        ask_for_clue = get_input_from_user('string', 'Do you want a "Bigger" and "Lower" clue ? (yes/no): ').lower()
        if ask_for_clue == 'yes' or ask_for_clue == 'no':
            break

        print('Insert "yes" or "no" ')

    return ask_for_clue == 'yes'


def show_clue_for_user(user_guess, correct_number):
    """

    :param user_guess:
    :param correct_number:
    :return: nothing
    the function show clue for user
    """
    if user_guess - correct_number > 0:
        print('Clue: Bigger')
    else:
        print('Clue: Lower')


def is_user_guess(user_guess, correct_number):
    """
    :param user_guess:
    :param correct_number:
    :return: user_guess == correct_number
    The function checking if is user guess correct
    """
    return user_guess == correct_number


def get_random_number():
    """
    :return: randint(1, 100)
    The function returns a number in a range of 1 to 100
    """
    return randint(1, 100)


def game(correct_number):
    """
    :param correct_number:
    :return: counter
    The function checks the number of guesses by the user
    """
    counter = 0
    clue_mode_flag = False

    while True:
        user_guess = get_input_from_user('int', 'Insert number from 1 - 100: ')
        counter += 1

        if is_user_guess(user_guess, correct_number) == True:
            if clue_mode_flag == True:
                counter += 1
            break

        if clue_mode_flag == False and counter == 2:
            clue_mode_flag = is_user_wants_clue()

        elif clue_mode_flag == True:
            show_clue_for_user(user_guess, correct_number)
            counter += 1

    return counter


def get_names_list(users_data):
    """
    :param users_data:
    :return: list(users_data.keys())
    The function return list of users name
    """
    return list(users_data.keys())


def group_players_with_same_guesses(data_base):
    """
    :param data_base:
    :return: result
    The function put players with the same guesses
    in the same group
    """
    result = {}
    names_list = get_names_list(data_base)

    for player in names_list:
        # print(f'result = {result}')
        if data_base[player]['amount_of_guesses'] not in result.keys():
            result[data_base[player]['amount_of_guesses']] = player
            continue

        if isinstance(result[data_base[player]['amount_of_guesses']], str):
            result[data_base[player]['amount_of_guesses']] = [result[data_base[player]['amount_of_guesses']], player]
        elif isinstance(result[data_base[player]['amount_of_guesses']], list):
            result[data_base[player]['amount_of_guesses']].append(player)

    # print(list(result.values()))
    return result


def sort_users_data(users_data):
    """
    :param users_data:
    :return: new_users_data
    The function sorting the places of all the players
    """
    names_list = list(users_data.keys())
    new_users_data = {}

    for i in range(len(names_list)):
        for z in range(i, len(names_list)):
            if names_list[i] > names_list[z]:
                saved = names_list[i]
                names_list[i] = names_list[z]
                names_list[z] = saved
        new_users_data[names_list[i]] = users_data[names_list[i]]

    return new_users_data


def get_winner(users_data):
    """
    :param users_data:
    :return: sort_players_place
    The function working like mini main that finding the guesses and places of all the user
    that calls to 2 function
    """
    players_with_same_guesses_group = group_players_with_same_guesses(users_data)
    sort_players_place = sort_users_data(players_with_same_guesses_group)

    return sort_players_place


def show_players_table(users_data):
    """
    :param users_data:
    :return:
    The function goes over the "copy_names_list" and
    prints the places of the users
    """
    place = 1

    print('    name:          |       guesses:       |     place:    ')

    for key, value in users_data.items():
        print(f'    {value}         |        {key}             |       {place}')

        place += 1


def get_input_from_user(type_of_input, massage_to_input):
    """
    :param type_of_input:
    :param massage_to_input:
    :return: user_input
    The programmer can choose what type of variable he wants
    when he calls the function and makes sure
    that there are no errors in the placement of the variable
    """
    while True:
        try:
            user_input = input(massage_to_input)

            if type_of_input == 'int':
                user_input = int(user_input)
            elif type_of_input == 'float':
                user_input = float(user_input)
            break

        except (UnboundLocalError, KeyError, ValueError) as error:
            print(f'We have a error-{error}')

        except Exception as error:
            print('---------------------------- New Error!!!!! ----------------------------')
            print(f'We have a error-{error}')

    return user_input


if __name__ == '__main__':
    database = {'A': {"name": "A", "amount_of_guesses": 12},
                'B': {"name": "B", "amount_of_guesses": 2},
                'C': {"name": "C", "amount_of_guesses": 4},
                'D': {"name": "C", "amount_of_guesses": 4}}

    players_place = get_winner(database)
    show_players_table(players_place)

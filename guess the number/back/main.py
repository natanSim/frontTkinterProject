from helper import show_welcome_message_to_user, show_message_to_user, get_name_from_user, game, get_input_from_user, get_player_data, \
    get_winner, add_player_data_to_table, show_player_data, show_players_table, get_random_number, Player


def main():
    players_table = {}
    show_welcome_message_to_user()

    number_of_player = get_input_from_user('int', 'How much players(maximum 10 players)? Insert "0" to exit : ')
    for i in range(number_of_player):
        name = get_name_from_user()
        number_to_guess = get_random_number()
        player_number = i + 1
        player_data = Player(name, number_to_guess, player_number)
        print(f'Player {i + 1}: {name} created!')

        show_message_to_user()
        player_data = game(player_data)
        player_data.show_player_data()
        players_table = add_player_data_to_table(players_table, player_data)

    print('Done\n')
    print(players_table)
    for player_name, player_data in players_table.items():
        print(f'{player_name}, {player_data.get_player_data()}')


    players_place = get_winner(players_table)
    show_players_table(players_place)


if __name__ == '__main__':
    main()





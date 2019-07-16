import constants
ALL_TEAM_NAMES = constants.TEAMS
all_players = constants.PLAYERS


def clean_guardians(list_of_players):
    for player in list_of_players:
        player.update({"guardians": player["guardians"].split(" and ")})
    return list_of_players


def clean_height(list_of_players):
    for player in list_of_players:
        player['height'] = player['height'].split()
        for item in player['height']:
            if item.isdigit():
                player['height'] = int(item)
    return list_of_players


def extract_experienced(list_of_players):
    experienced_list = []
    for player in list_of_players:
        if player['experience'] == 'YES':
            experienced_list.append(player)
    return experienced_list


def extract_inexperienced(list_of_players):
    inexperienced_list = []
    for player in list_of_players:
        if player['experience'] == 'NO':
            inexperienced_list.append(player)
    return inexperienced_list


def distribute_players(list_of_players):
    n = 0
    while n < len(list_of_players):
        for player in list_of_players:
            player['team'] = ALL_TEAM_NAMES[n % 3]
            n += 1


def populate_team_lists(list_of_players):
    for player in list_of_players:
        if player['team'] == 'Panthers':
            panthers.append(player)
        elif player['team'] == 'Bandits':
            bandits.append(player)
        elif player['team'] == 'Warriors':
            warriors.append(player)


def main_menu():
    while True:
        print('''
BASKETBALL TEAM STATS TOOL

---- MENU----
Here are your choices:
  1) Display Team Stats
  2) Quit
        ''')
        try:
            choice = int(input("Enter an option >  "))
        except ValueError:
            input("Please enter a number. Press Enter to continue.")
        else:
            if choice == 1:
                choose_team()
            elif choice == 2:
                print("Program terminating, bye :)\n")
                exit()
            else:
                print("Please enter 1 or 2\n")


def choose_team():
    while True:
        print("\nChoose a team:\n  1) Panthers\n  2) Bandits\n  3) Warriors")
        try:
            choice = int(input("\nEnter an option > "))
        except ValueError:
            input("Please enter a number. Press Enter to continue.\n")
        else:
            if choice == 1:
                show_stats(panthers)
                break
            elif choice == 2:
                show_stats(bandits)
                break
            elif choice == 3:
                show_stats(warriors)
                break
            else:
                input("Please enter 1, 2, or 3.\nPress Enter to continue\n")


def show_stats(team_name):
    # get player total
    player_total = len(team_name)

    # create a string that is all the players' names, comma-separated
    player_list = []
    for player in team_name:
        player_list.append(player['name'])
    player_string = ", ".join(player_list)

    # count the number of (in)experienced players on the team
    num_experienced = 0
    num_inexperienced = 0
    for player in team_name:
        if player['experience'] == 'YES':
            num_experienced += 1
        elif player['experience'] == 'NO':
            num_inexperienced += 1

    # calculate average height for players on the team
    avg_height = 0
    for player in team_name:
        avg_height += player['height']
    avg_height = round((avg_height / len(team_name)), ndigits=1)

    # create a string that is all the players' guardians, comma-separated
    guardian_list = []
    for player in team_name:
        guardian_list.extend(player['guardians'])
    guardian_string = ", ".join(guardian_list)

    # print the output prepared above
    print("\nStatistics for the {}:".format(team_name[0]['team'].upper()))
    print('''
    --------------------
    * Total players: {}
    * List of players on the team: {}
    * Number of experienced players on the team: {}
    * Number of inexperienced players on the team: {}
    * Average height of players on the team: {} inches
    * Guardians of the players on the team: {}
    '''.format(player_total, player_string, num_experienced, num_inexperienced, avg_height, guardian_string))

    input("Press Enter to return to Main Menu ")


if __name__ == "__main__":
    clean_guardians(all_players)
    clean_height(all_players)
    experienced_players = extract_experienced(all_players)
    inexperienced_players = extract_inexperienced(all_players)

    distribute_players(experienced_players)
    distribute_players(inexperienced_players)

    panthers = []
    bandits = []
    warriors = []

    populate_team_lists(experienced_players)
    populate_team_lists(inexperienced_players)

    main_menu()

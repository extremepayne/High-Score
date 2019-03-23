"""Save highscores to file via a command line interface."""
# HighScor program v1.3.3
# Idea & orignal code - Micheal Dawson. As shown in
# Python Programming for the Complete Beginner
# under name "High Scores 2.0"
# Modifications by Harrison Payne
# Commenced 11/6/17
# Last updated 12/11/17
# A progam to keep track of highscores


# pylint: disable=C0103
# pylint: disable=C1801
# ^If you're using pylint, those two are espically annoying.

# ---------------------------------------------------------------------

# Code

import shelve

try:
    games_file = shelve.open("scores.dat")
except IOError as error:
    print(
        'Unable to open the file "scores.dat" Ending program.\
\n',
        error,
    )
    input("\n\nPress the enter key to exit.")
    quit()

try:
    settings_file = shelve.open("highscorsettings.dat")
except IOError as error:
    print(
        'Unable to open the file "highscorsettings.dat" Ending program.\
\n',
        error,
    )
    input("\n\nPress the enter key to exit.")
    quit()
# ^Get files


games = {}
for game in games_file:
    games[game] = games_file[game]


settings = {}
for setting in settings_file:
    settings[setting] = settings_file[setting]
# ^Create vars


def list_scores(scores):
    """List all scores from a game."""
    if len(scores) > 0:  # If there are scores,
        print("\nScore\tName")  # (Heading)
        for entry in scores:
            print(entry[0], "\t", entry[1], sep="")
            # Print all the scores
    else:  # Otherwise, inform the user.
        print("No scores have been added.")
    print()  # Whitespace in display.


def list_players():
    """Print all players from all games."""
    rep = []
    for game in games:  # For each game
        for entry in games[game]:  # For each score
            if entry[1] not in rep:
                # If the player's name isn't
                # already in there, add it.
                rep.append(entry[1])
    if len(rep) > 0:
        for player in rep:
            print(player)
    else:
        print("No scores have been added.")


def get_players():
    """Return a list of all players from all games."""
    rep = []
    for game in games:  # For each game
        for entry in games[game]:  # For each score
            if entry[1].lower() not in rep:
                # If the player's name
                # isn't already in there, add it.
                rep.append(entry[1].lower())
    return rep


def list_player_scores(player):
    """Print all scores from all games for one player."""
    rep = []
    for game in games:  # For each game
        for entry in games[game]:  # For each score
            if entry[1].lower() == player:
                new_entry = (entry[0], game)  # format: score, game
                rep.append(new_entry)
    print("\nScore\tGame")  # (Heading)
    for entry in rep:
        print(entry[0], "\t", entry[1].title(), sep="")
        # Print all the scores
    print()


def save_and_exit():
    """Write local variables to the shelved files, then close the window."""
    for game in games:
        games_file[game] = games[game]
    for setting in settings:
        settings_file[setting] = settings[setting]
    games_file.sync()
    games_file.close()
    settings_file.sync()
    settings_file.close()

    input("\n\n Press enter to exit")
    import sys

    sys.exit()


def ask_yes_no(question):
    """Ask the user a yes or no question, return a boolean variable."""
    output = input(question)
    while output not in ("y", "n", "quit"):
        print('That is not "y" or "n"')
        output = input(question)
    if output == "y":
        rep = True
    elif output == "n":
        rep = False
    elif output == "quit":
        save_and_exit()
    else:  # Just in case
        rep = None
    return rep


# -----MAIN-----

print(
    'Welcome to HighScor v1.3.3!\nEnter "quit" at any prompt \
to save and exit.'
)


choice = None  # Sentry variable
while choice != "0":
    print(
        """
    HighScor
    v1.3.3

    Main Menu
    0 - Save and exit
    1 - Add a game"""
    )

    if len(games) > 0:
        # Best not to let the user access the games' files until
        # they've created some!
        print("    2 - Choose a game to manage")
        print("    3 - See all scores for a player")

    print("")  # add a blank line after the menu

    choice = input("Choice: ")  # Get the user's choice

    if choice in ("0", "quit"):
        save_and_exit()
        # ----------
    elif choice == "1":
        new_game = input("What is the name of this game? ")
        new_game = new_game.lower()
        while new_game == "" or new_game == "quit" or new_game in games:
            if new_game == "quit":
                save_and_exit()
            print(
                "That is an invalid name for a game.\nPossible issues:\n\
                - Didn't enter anything\n    - Name already taken"
            )
            new_game = input("What is the name of this game? ")
            new_game = new_game.lower()
        games[new_game] = []
        settings[new_game] = [5, True]
        input("Press enter to continue.")
        print("Returning to main menu.")
        # ----------
    elif choice == "2" and len(games) > 0:  # See line 233
        print(
            """
    HighScor
    v1.3.3

    Manage games and scores

    List of games
    """
        )

        for game in games:
            print("    -", game)
            # Show them all avaiable games by looping through the dictionary

        choose_game = input("Enter the name of a game to access that game: ")
        choose_game = choose_game.lower()
        # Get user input
        while choose_game not in games:
            if choose_game == "quit":
                save_and_exit()
            print("That game is not avaliable.")
            choose_game = input(
                "Enter the name of a game to access \
that game: "
            )
            choose_game = choose_game.lower()
            # Make sure that it's actually a saved game

        scores = games[choose_game]  # Create local var for easy access

        choice = None
        while choice != "back0":
            print(
                """
    HighScor
    v1.3.3
    """
            )
            print("   ", choose_game.title(), "Menu")
            print(
                """
    0 - Return to main menu
    1 - Display Scores
    2 - Add a score
    3 - Delete a score
    4 - Update a score
    5 - Delete this game
    6 - Edit game settings\n"""
            )
            choice = input("Choice: ")
            if choice == "0":
                choice = "back0"  # Break the while loop
                games[choose_game] = scores
                # Save scores to main dictionary
                # ----------
            elif choice == "quit":
                games[choose_game] = scores
                # Save scores to main dictionary
                save_and_exit()
                # ----------
            elif choice == "1":
                list_scores(scores)
                input("Press enter to continue.")
                # ----------
            elif choice == "2":
                score = input("What did the player get? ")
                # Get user input

                while (
                    score == ""
                    or score == "quit"
                    or ((not score.isdigit()) and settings[choose_game][1])
                ):
                    if score == "quit":
                        games[choose_game] = scores
                        # Save scores to main dictionary
                        save_and_exit()
                    print(
                        "That is an invalid score.\nPossible issues:\n    \
    - Didn't enter anything\n    - Wasn't a number"
                    )
                    score = input("What did the player get? ")

                name = input("Who scored this score? ")
                name = name.lower()
                # Get user input
                while name in ("", "quit"):
                    if name == "quit":
                        games[choose_game] = scores
                        # Save scores to main dictionary
                        save_and_exit()
                    print(
                        "That is an invalid name for a player.\n\
Possible issues:\n    - Didn't enter anything"
                    )
                    name = input("Who scored this score? ")
                    name = name.lower()

                done = False  # Sentry variable
                for entry in scores:
                    if entry[1].lower() == name:
                        done = True
                        break
                # ^Find out if player already has a score
                if done:  # And if he does, inform the user.
                    print(
                        name.title(),
                        "already has a score saved for this \
                    game. \nYou can update his score with option 4.",
                    )
                else:  # Otherwise, we save the score.
                    entry = (score, name)
                    scores.append(entry)
                    # Add the score.
                    scores.sort(reverse=True)
                    scores = scores[: settings[choose_game][0]]
                    # Each setting is a tuple, first element is the
                    # value we're after.
                    # Sort and truncate the scores.
                    print("Score has been added.")
                    # Inform the user.
                input("Press enter to continue.")
                # ----------
            elif choice == "3":
                if len(scores) > 0:  # If there are any scores
                    print("Listing scores:")
                    list_scores(scores)
                    name = input("Whose score would you like to delete? ")
                    name = name.lower()
                    # Get user input
                    if name == "quit":
                        games[choose_game] = scores
                        # Save scores to main dictionary
                        save_and_exit()
                    done = False
                    for entry in scores:
                        if entry[1] == name:
                            scores.remove(entry)
                            done = True
                            break
                    # ^ Attempt to delete score
                    if done:
                        print("Score removed.")
                    else:
                        print("Player not found.")
                    # ^ Inform them of the results
                else:  # If there aren't any scores:
                    print(
                        "No scores have been added. Add a score first \
to delete it."
                    )
                input("Press enter to continue.")
                # ----------
            elif choice == "4":
                if len(scores) > 0:  # If there are scores:
                    print("Listing scores:")
                    list_scores(scores)
                    done = False  # Sentry variable
                    while not done:
                        name = input("Whose score would you like to update? ")
                        name = name.lower()

                        if name == "quit":
                            games[choose_game] = scores
                            # Save scores to main dictionary
                            save_and_exit()

                        for entry in scores:  # for each score-name pair
                            if entry[1] == name:
                                # Check if entry belongs to the player
                                done = True
                        if not done:
                            print("Player not found.")
                    score = input("What is their new score? ")

                    while (score == "" or score == "quit") or (
                        (not score.isdigit()) and settings[choose_game][1]
                    ):
                        if score == "quit":
                            games[choose_game] = scores
                            # Save scores to main dictionary
                            save_and_exit()
                        print(
                            "That is an invalid score.\n\
Possible issues:\n    - Didn't enter anything\n    - \
Wasn't a number"
                        )
                        score = input("What did the player get? ")

                    new_entry = (score, name)
                    done = False  # Sentry variable
                    i = 0  # Counter var
                    for entry in scores:  # for each score-name pair
                        if entry[1] == name:
                            # Check if entry belongs to the player
                            scores[i] = new_entry
                            # and if so update the score
                            done = True
                            break
                            # and quit looping through the entries.
                        i += 1  # Update counter
                    scores.sort(reverse=True)
                    scores = scores[: settings[choose_game][0]]
                    # Sort and truncate the scores.
                    if done:
                        print("Score updated.")
                    else:
                        print("Player not found.")
                else:  # If there aren't any scores:
                    print(
                        "No scores have been added. Add a score first to\
update it."
                    )
                input("Press enter to continue.")
                # ----------
            elif choice == "5":
                sure = ask_yes_no("Are you sure? (y/n)")
                if sure:
                    choice = "back0"
                    del games[choose_game]
                    del settings[choose_game]
                    print("Game has been deleted.")
                    input("Press enter to continue.")
                # ----------
            elif choice == "6":
                choice = None
                while choice != "back1":
                    print(
                        """
    HighScor
    v1.3.3

    Edit Game Settings
    0 - Return to game menu
    1 - Number of scores to keep on table
    2 - Scores do or do not have to be numbers
    """
                    )
                    choice = input("Choice: ")
                    if choice == "1":
                        print("Current setting:", settings[choose_game][0])
                        done = False  # Sentry variable
                        while not done:
                            try:
                                setting = int(
                                    input(
                                        "How many scores should \
this game keep? "
                                    )
                                )
                                if setting == "quit":
                                    games[choose_game] = scores
                                    # Save scores to main dictionary
                                    save_and_exit()

                            except ValueError:
                                # Triggered if the string can't be converted
                                # into a number
                                print(
                                    "That is not a number. Please try \
again."
                                )
                            else:
                                done = True
                        settings[choose_game][0] = setting
                        scores = scores[: settings[choose_game][0]]
                        # Truncate scores
                        input("Press enter to continue.")
                    elif choice == "2":
                        print("Current setting:", settings[choose_game][1])
                        setting = ask_yes_no(
                            "Should all scores in this game \
have to be numbers? (y/n) "
                        )
                        if not setting:
                            print("Warning: The scores will not be sorted.")
                        settings[choose_game][1] = setting
                        input("Press enter to continue.")
                    elif choice == "0":
                        choice = "back1"
                    elif choice == "quit":
                        games[choose_game] = scores
                        # Save scores to main dictionary
                        save_and_exit()
                    else:
                        print("That is not a choice.")
                        input("Press enter to continue.")
                input("Press enter to return to the game menu.")
                # ----------
            else:  # Some unkown choice
                print("That is not a choice.")
                input("Press enter to continue.")
            # END of game editing
    elif choice == "3" and len(games) > 0:  # Player score listing feature
        print("Listing players.")
        players = get_players()  # gets a list of the player's names
        list_players()  # Printing out the list of all the players
        if len(players) > 0:
            choose_player = input(
                "Which player would you like to \
view? "
            )
            choose_player = choose_player.lower()
            while choose_player not in players:
                if choose_player == "quit":
                    save_and_exit()
                print("That player has no scores yet.")
                choose_player = input(
                    "Which player would you like to \
view? "
                )
            choose_player = choose_player.lower()
            list_player_scores(choose_player)
        input("Press enter to continue.")
    else:  # Back in the main menu, some unkown choice
        print("That is not a choice.")
        input("Press enter to continue.")

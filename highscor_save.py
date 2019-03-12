"""Module that allows games to save to the file used by highscor."""
import shelve


def save_files(games, settings):
    """
    Writes local variables back to the shelved files, then closes the window.
    """
    try:
        games_file = shelve.open("scores.dat")
    except IOError as error:
        print("Unable to open the file \"scores.dat\" Ending program.\
    \n", error)
        input("\n\nPress the enter key to exit.")
        quit()

    try:
        settings_file = shelve.open("highscorsettings.dat")
    except IOError as error:
        print("Unable to open the file \"highscorsettings.dat\" Ending program.\
    \n", error)
        input("\n\nPress the enter key to exit.")
        quit()
    #^Get files


    games = {}
    for game in games_file:
        games[game] = games_file[game]


    settings = {}
    for setting in settings_file:
        settings[setting] = settings_file[setting]
    for game in games:
        games_file[game] = games[game]
    for setting in settings:
        settings_file[setting] = settings[setting]
    games_file.sync()
    games_file.close()
    settings_file.sync()
    settings_file.close()

def load_files():
    """
    Returns two files that have the scores in them.
    """

    try:
        games_file = shelve.open("scores.dat")
    except IOError as error:
        print("Unable to open the file \"scores.dat\" Ending program.\
    \n", error)
        input("\n\nPress the enter key to exit.")
        quit()

    try:
        settings_file = shelve.open("highscorsettings.dat")
    except IOError as error:
        print("Unable to open the file \"highscorsettings.dat\" Ending program.\
    \n", error)
        input("\n\nPress the enter key to exit.")
        quit()
    #^Get files


    games = {}
    for game in games_file:
        games[game] = games_file[game]


    settings = {}
    for setting in settings_file:
        settings[setting] = settings_file[setting]

    return games, settings

def create_game_file(game_name, setting0, setting1):
    """
    Creates a file for a game to use.
    """
    games_file, settings_file = load_files()
    game_name = game_name.lower()
    if game_name in ("", "quit") or game_name in games_file:  # If the game is named "quit", this
                                                              # creates problems elsewhere.
        return "fail"
    games_file[game_name.lower()] = []
    settings_file[game_name.lower()] = [setting0, setting1]
    save_files(games_file, settings_file)
    return "success"


def write_score(game_name, player_name, score):
    """
    Writes a score to a game file. If player already has a score or game does
    not exist, return "fail".
    """
    games_file, settings_file = load_files()
    game_name = game_name.lower()
    if game_name in ("", "quit") or game_name in games_file:  # If the game is named "quit", this
                                                              # creates problems elsewhere.
        return "fail"
    if score == "" or score == "quit" or ((not score.isdigit()) and
                                          settings_file[game_name][1]):
        return "fail"
    if score in ("", "quit"):
        return "fail"
    if player_name in ("", "quit"):
        return "fail"
    save_files(games_file, settings_file)
    return "success"

def update_score(game_name, player_name, score):
    """
    Changes a player's score in a game file. If player or game doesn't exist, return "fail".
    """
    games_file, settings_file = load_files()
    game_name = game_name.lower()
    save_files(games_file, settings_file)
    return "success"










if __name__ == "__main__":
    print("This file was meant to be accessed as a module, not run on its own.")
    input("\n\nPress enter to exit.")
    quit()

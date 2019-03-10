"""Module that allows games to save to the file used by highscor."""
import shelve


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
    if game_name == "" or game_name in games_file:
        return "fail"
    games_file[game_name.lower()] = []
    settings_file[game_name.lower()] = [setting0, setting1]
    return "success"


def write_score(game_name, player_name, score):
    """
    Writes a score to a game file. If player already has a score or game does not exist, return "fail".
    """
    pass

def update_score(game_name, player_name, score):
    """
    Changes a player's score in a game file. If player or game doesn't exist, return "fail".
    """
    pass










if __name__ == "__main__":
    print("This file was meant to be accessed as a module, not run on its own.")
    input("\n\nPress enter to exit.")
    quit()

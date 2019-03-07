"""Module that allows games to save to the file used by highscor."""


def create_game_file(game_name, setting0, setting1):
    """
    Creates a file for a game to use.
    """
    pass

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


def load_game_file(game_name):
    pass







if __name__ == "__main__":
    print("This file was meant to be accessed as a module, not run on its own.")
    input("\n\nPress enter to exit.")
    quit()

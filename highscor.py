"""Module that allows games to save to the file used by highscor.

Functions:
create_game_file
write_score
update_score
"""
import shelve


def __save_files(games, settings):
    """Write local variables back to the shelved files."""
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
            'Unable to open the file "highscorsettings.dat" \
        Ending program.    \n',
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
    for game in games:
        games_file[game] = games[game]
    for setting in settings:
        settings_file[setting] = settings[setting]
    games_file.sync()
    games_file.close()
    settings_file.sync()
    settings_file.close()


def __load_files():
    """Return two dictionaries that have the score files in them."""
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
            'Unable to open the file "highscorsettings.dat" \
Ending program.    \n',
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

    return games, settings


def create_game_file(game_name, setting0, setting1):
    """Create a file for a game to use."""
    games_file, settings_file = __load_files()
    game_name = game_name.lower()
    if game_name in ("", "quit") or game_name in games_file:
        # If the game is named "quit", this creates problems elsewhere.
        return "fail"
    games_file[game_name.lower()] = []
    settings_file[game_name.lower()] = [setting0, setting1]
    __save_files(games_file, settings_file)
    return "success"


def new_score(game_name, player_name, score):
    """
    Add a score for a player that doesn't have one.

    If player already has a score or game does not exist, return "fail".
    """
    games_file, settings_file = __load_files()
    game_name = game_name.lower()
    player_name = player_name.lower()
    if game_name in ("", "quit") or game_name not in games_file:
        # If the game is named "quit", this creates problems elsewhere.
        return "fail"
    if score in ("", "quit"):
        # or (
        # (not score.isdigit()) and settings_file[game_name][1]
        # ):
        return "fail"
    if player_name in ("", "quit"):
        return "fail"
    scores = games_file[game_name]
    done = False
    for entry in scores:
        if entry[1].lower() == player_name:
            done = True
            break
    if done:
        return "fail"
    # At this point, there aren't any possible errors left.
    entry = (score, player_name)
    scores.append(entry)
    # Add the score.
    scores.sort(reverse=True)
    scores = scores[: settings_file[game_name][0]]
    # ^Each setting is a tuple, the first element is the value we're after.
    # Sort and truncate the scores.
    __save_files(games_file, settings_file)
    return "success"


def update_score(game_name, player_name, score):
    """
    Change a player's score in a game file.

    If player or game doesn't exist, return "fail".
    """
    games_file, settings_file = __load_files()
    game_name = game_name.lower()
    player_name = player_name.lower()
    if game_name in ("", "quit") or game_name in games_file:
        # If the game is named "quit", this creates problems elsewhere.
        return "fail"
    if score in ("", "quit"):
        # or (
        # (not score.isdigit()) and settings_file[game_name][1]
        # ):
        return "fail"
    if player_name in ("", "quit"):
        return "fail"
    scores = games_file[game_name]
    new_entry = (score, player_name)
    done = False
    i = 0
    for entry in scores:
        if entry[1].lower() == player_name:
            scores[i] = new_entry
            done = True
            break
    if not done:
        # Since were updating, we will throw an error if the player
        # doesn't exist.
        return "fail"
    # At this point there aren't any possible errors left.
    scores.sort(reverse=True)
    scores = scores[: settings_file[game_name][0]]
    # Each setting is a tuple, the first element is the value we're after.
    # Sort and truncate the scores.
    __save_files(games_file, settings_file)
    return "success"


def write_score(game_name, player_name, score):
    """
    Add or update a score.

    If game doesn't exist, return fail.
    """
    games_file, settings_file = __load_files()
    game_name = game_name.lower()
    player_name = player_name.lower()
    if game_name in ("", "quit") or game_name not in games_file:
        # If the game is named "quit", this creates problems elsewhere.
        return "fail"
    if score in ("", "quit"):
        # or (
        # (not score.isdigit()) and settings_file[game_name][1]
        # ):
        return "fail"
    if player_name in ("", "quit"):
        return "fail"
    scores = games_file[game_name]
    for entry in scores:
        if entry[1].lower() == player_name:
            entry[0] = score
            scores.sort(reverse=True)
            scores = scores[: settings_file[game_name][0]]
            games_file[game_name] = scores
            __save_files(games_file, settings_file)
            return "success"
    new_entry = (score, player_name)
    scores.append(new_entry)
    scores.sort(reverse=True)
    scores = scores[: settings_file[game_name][0]]
    games_file[game_name] = scores
    __save_files(games_file, settings_file)
    return "success"


def list_scores(game_name):
    games_file, settings_file = __load_files()
    if game_name in ("", "quit") or game_name not in games_file:
        # If the game is named "quit", this creates problems elsewhere.
        return "fail"
    scores = games_file[game_name]
    return scores


if __name__ == "__main__":
    print(
        "This file was meant to be accessed as a module, \
not run on its own."
    )
    input("\n\nPress enter to exit.")
    quit()

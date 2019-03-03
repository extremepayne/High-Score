#Highscores program v1.2
#Idea & orignal code - Micheal Dawson. As shown in
#Python Programming for the Complete Beginner
#under name "High Scores 2.0"
#Modifications by Harrison Payne
#Commenced 11/6/17
#Last updated 11/15/17
#A progam to keep track of highscores


#---------------------------------------------------------------------

#Coming Soon:

# Add more game settings (probably v1.3)
# User-friendly GUI (probably v2.0)

#---------------------------------------------------------------------


#Code

import shelve

try:
    games_file = shelve.open("scores.dat")
except IOError as e:
    print("Unable to open the file \"scores.dat\" Ending program.\
\n", e)
    input("\n\nPress the enter key to exit.")
    quit()

try:
    settings_file = shelve.open("highscorsettings.dat")
except IOError as e:
    print("Unable to open the file \"highscorsettings.dat\" Ending program.\
\n", e)
    input("\n\nPress the enter key to exit.")
    quit()
#^Get files


games = {}
for game in games_file:
    games[game] = games_file[game]


settings = {}
for setting in settings_file:
    settings[setting] = settings_file[setting]
#^Create vars

def list_scores(scores):
    if len(scores) > 0: # If there are scores,
        print("\nScore\tName") # (Heading)
        for entry in scores:
            print(entry[0], "\t", entry[1], sep = "")
            # Print all the scores
    else: # Otherwise, inform the user.
        print("No scores have been added.")
    print()

def list_players():
    rep = []
    for game in games: # For each game
        for entry in games[game]: # For each score
            if entry[1] not in rep: # If the player's name isn't
                                    # already in there, add it.
                rep.append(entry[1])
    if len(rep) > 0:
        for player in rep:
            print(player)
    else:
        print("No scores have been added.")

def get_players():
    rep = []
    for game in games: # For each game
        for entry in games[game]: # For each score
            if entry[1].lower() not in rep:# If the player's name
                                     # isn't already in there, add it.
                rep.append(entry[1].lower())
    return rep

def list_player_scores(player):
    rep = []
    for game in games:
        for entry in games[game]:
            if entry[1].lower() == player:
                new_entry = (entry[0], game) # format: score, game
                rep.append(new_entry)
    print("\nScore\tGame") # (Heading)
    for entry in rep:
        print(entry[0], "\t", entry[1].title(), sep = "")
        # Print all the scores
    print()


choice = None # Sentry variable
while choice != "0":
    print(
    """
    High Scores
    v1.2

    Main Menu
    0 - Save and quit
    1 - Add a game""")

    if len(games) > 0:
        # Best not to let the user access the games' files until
        # they've created some!
        print("    2 - Choose a game to manage")
        print("    3 - See all scores for a player")

    choice = input("Choice: ")# Get the user's choice

    if choice == "0":
        for game in games:
            games_file[game] = games[game]
        for setting in settings:
            settings_file[setting] = settings[setting]
        games_file.sync()
        games_file.close()
        settings_file.sync()
        settings_file.close()
        print("Goodbye.")# After this, the while loop will break, and
                         # the program will end.
        #----------
    elif choice == "1":
        new_game = input("What is the name of this game? ")
        while new_game == "" or new_game in games:
            print("That is an invalid name for a game.\nPossible \
issues:\n    - Didn't enter anything\n    - Name already taken")
            new_game = input("What is the name of this game? ")
        games[new_game.lower()] = []
        settings[new_game.lower()] = 5
        input("Press enter to continue.")
        print("Returning to main menu.")
        #----------
    elif choice == "2" and len(games) > 0: # See line 52
        print(
        """
    High Scores
    v1.2

    Manage games and scores

    List of games
    """)

        for game in games:
            print("    -", game)# Show them all avaiable games by
                                # looping through the dictionary

        choose_game = input("Enter the name of a game \
to access that game: ")# Get user input
        while choose_game.lower() not in games:
            print("That game is not avaliable.")
            choose_game = input("Enter the name of a game \
to access that game: ")# Make sure that it's actually a saved game

        scores = games[choose_game] # Create local var for easy access

        choice = None
        while choice != "quit":
            print(
    """
    High Scores
    v1.2
    """)
            print("   ", choose_game.title(), "Menu")
            print("""
    0 - Return to main menu
    1 - Display Scores
    2 - Add a score
    3 - Delete a score
    4 - Update a score
    5 - Delete this game
    6 - Edit game settings""")
            choice = input("Choose: ")
            if choice == "0":
                choice = "quit" # Break the while loop
                games[choose_game] = scores # Save scores to main
                                            # dictionary
                #----------
            elif choice == "1":
                list_scores(scores)
                input("Press enter to continue.")
                #----------
            elif choice == "2":
                score = input("What did the player get? ")# Get user
                                                          # input

                while score == "" or not score.isdigit():
                    print("That is an invalid score.\n\
Possible issues:\n    - Didn't enter anything\n    - \
Wasn't a number")
                    score = input("What did the player get? ")


                name = input("Who scored this score? ") # Get user
                                                        # input
                while name == "":
                    print("That is an invalid name for a player.\n\
Possible issues:\n    - Didn't enter anything")
                    name = input("Who scored this score? ")

                done = False # Sentry variable
                for entry in scores:
                    if entry[1].lower() == name.lower():
                        done = True
                        break
                # ^Find out if player already has a score
                if done: # And if he does, inform the user.
                    print(name.title(), "already has a score saved \
for this game. \nYou can update his score with option 4.")
                else: # Otherwise, we save the score.
                    entry = (score, name)
                    scores.append(entry)
                    # Add the score.
                    scores.sort(reverse = True)
                    scores = scores[:settings[game]]
                    # Sort and truncate the scores.
                    print("Score has been added.")
                    # Inform the user.
                input("Press enter to continue.")
                #----------
            elif choice == "3":
                if len(scores) > 0: # If there are any scores
                    print("Listing scores:")
                    list_scores(scores)
                    name = input("Whose score would you like \
to delete? ") # Get user input
                    done = False
                    for entry in scores:
                        if entry[1].lower() == name.lower():
                            scores.remove(entry)
                            done = True
                            break
                    # ^ Attempt to delete score
                    if done:
                        print("Score removed.")
                    else:
                        print("Player not found.")
                    # ^ Inform them of the results
                else: # If there aren't any scores:
                    print("No scores have been added. Add a score \
first to delete it.")
                input("Press enter to continue.")
                #----------
            elif choice == "4":
                if len(scores) > 0: # If there are scores:
                    print("Listing scores:")
                    list_scores(scores)
                    name = input("Whose score would you like to \
update? ")
                    score = input("What is their new score? ")

                    while score == "" or not score.isdigit():
                        print("That is an invalid score.\n\
Possible issues:\n    - Didn't enter anything\n    - \
Wasn't a number")
                        score = input("What did the player get? ")


                    new_entry = (score, name)
                    done = False # Sentry variable
                    i = 0 # Counter var
                    for entry in scores: # for each score-name pair
                        if entry[1].lower() == name.lower(): # Check
                                    # if entry belongs to the player
                            scores[i] = new_entry# and if so update
                                                 # the score
                            done = True
                            break # and quit looping through the
                                  # entries.
                        i+=1 # Update counter
                    scores.sort(reverse = True)
                    scores = scores[:settings[game]]
                    # Sort and truncate the scores.
                    if done:
                        print("Score updated.")
                    else:
                        print("Player not found.")
                else: # If there aren't any scores:
                    print("No scores have been added. Add a score \
first to update it.")
                input("Press enter to continue.")
                #----------
            elif choice == "5":
                choice = "quit"
                del games[choose_game]
                del settings[choose_game]
                print("Game has been deleted.")
                input("Press enter to continue.")
                #----------
            elif choice == "6":
                print("Edit Game Settings")
                done = False # Sentry variable
                while not done:
                    try:
                        setting = int(input("How many scores should \
this game keep? "))
                    except ValueError: # Triggered if the string can't
                                       # be converted into a number
                        print("That is not a number. Please try \
again.")
                    else:
                        done = True
                settings[choose_game] = setting
                scores = scores[:settings[game]] # Truncate scores
                input("Press enter to continue.")
                #----------
            else: # Some unkown choice
                print("That is not a choice.")
                input("Press enter to continue.")
            #END of game editing
    elif choice == "3" and len(games)>0:
        print("Listing players.")
        players = get_players()
        list_players()
        if len(players) > 0:
            choose_player = input("Which player would you like to \
view? ")
            while choose_player.lower() not in players:
                print("That player has no scores yet.")
                choose_player = input("Which player would you like to \
view? ")
            choose_player = choose_player.lower()
            list_player_scores(choose_player)
        input("Press enter to continue.")
    else: # Back in the main menu, some unkown choice
        print("That is not a choice.")
        input("Press enter to continue.")




input("\n\n Press enter to exit")

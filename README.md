# High-Score
Programs that save high scores to a file.

This program was created originally as a response to the fact that the games on my calculator didn't have a good way to save highscores, and the eventual hope is that it will be able to have games write highscores to it (while still allowing manual addition of scores).

The basic idea is that you add games, scores, and associate those scores with players. Additional functionality has also been added, including settings, viewing scores by player as well as by game, and so forth.
The program works by shelving files with the highscores in them and retrieving them when necessary (actually only once at the start of the program; they're re-shelved only when the user chooses "save and quit").

## Installation
You need [python 3.x downloaded on your computer](https://www.python.org/downloads/). Clone the project. If necessary, unzip it. Yep, that's it!

## Usage
Run the file marked `highscore1.3.py` however you [run python files](https://docs.python.org/3/faq/windows.html#id2). 
#### Running python files
The link provided is some docs on how to use the command line in windows to execute a script; there are several other options:
* Right-click the file, open with IDLE (comes pre-loaded with python) and press F5
* Download [atom](https://www.atom.io) and the [run python simply package](https://atom.io/packages/run-python-simply), open the file with atom, and press F5 (python must be in PATH)

#### Using the program
Alright, you're ready to save some scores! The program uses a command-line like interface, but never fear, there's no need to memorize any commands. Everything you need to know will be on a menu right before the prompt. There are a few types of prompts:
Regular menus:
```
    Main Menu
    0 - Save and exit
    1 - Add a game
Choice:
```
These ones are pretty self-explanatory, just enter the number that corresponds to the menu item you want, and then press enter.

Selection from a list/dictionary menus:
```
    List of games
    - 2048
    - t-rex game
Enter the name of a game to access that game: 
```
You have to enter one of the items on the list in order to access it. Entering anything but an item on the list will result in the program telling you it's not a valid option.  They might be case-sensitive (still working on that).

User input:
```
What is the name of this game?
```
These might be yes or no questions, requests for a name, or a number. The program should tell you if you enter an invalid value, and will otherwise proceed.

Enter-to-continue prompts:
```
Press enter to continue.
```
Just press enter to continue. These often occur right after printing output, to give you some time to look at the ouput before proceeding back to a menu.

And that's all you need to know to navigate the program! If you're still confused, you can check out the wiki on this repo's [Github page](https://github.com/extremepayne/High-Score).

## Versioning explanation
The project was originally programmed without git, so the opening comments still have some of the version history.
Also, version 2.0 was stopped in development and contains no changes to the code. The file marked v1.3 has the current version.

## License
Just a standard MIT license. Check `LICENSE.md` for more info.

## Contributions
More than welcome! Please check out the code, it really isn't that long of a program. Submit any thoughts or suggestions you have via the appropriate channels.

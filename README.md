# HighScor
<p align="center">
<a href "https://www.python.org/"><img alt="forthebadge made-with-python" src = "http://ForTheBadge.com/images/badges/made-with-python.svg">
</p>
    
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT) ![GitHub top language](https://img.shields.io/github/languages/top/extremepayne/HighScor.svg) [![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black) [![standard-readme compliant](https://img.shields.io/badge/readme%20style-standard-brightgreen.svg)](https://github.com/RichardLitt/standard-readme) [![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](http://makeapullrequest.com) [![Travis CI build status](https://travis-ci.org/extremepayne/HighScor.svg?branch=master)](https://travis-ci.org/extremepayne/HighScor) [![Coverage Status](https://coveralls.io/repos/github/extremepayne/HighScor/badge.svg)](https://coveralls.io/github/extremepayne/HighScor) [![BADGINATOR](https://badginator.herokuapp.com/extremepayne/highscor.svg)](https://github.com/defunctzombie/badginator)


> Programs that save high scores to a file.

The basic idea is that you add games, scores, and associate those scores with players. Additional functionality has also been added, including settings, viewing scores by player as well as by game, and so forth.
The program works by shelving files with the highscores in them and retrieving them when necessary (actually only once at the start of the program; they're re-shelved only when the user chooses "save and quit").

## Table of contents
- [Background](#background)
- [Install](#install)
- [Usage](#usage)
- [Versioning explanation](#versioning)
- [Contributing](#contributing)
- [License](#license)

## Background
This program was created originally as a response to the fact that the games on my calculator didn't have a good way to save highscores, and the eventual hope is that it will be able to have games write highscores to it (while still allowing manual addition of scores).


## Install
You need [python 3.x downloaded on your computer](https://www.python.org/downloads/). Clone the project. If necessary, unzip it. Yep, that's it!

## Usage
The project has two interfaces, currently only the CLI is working (API under development.)

Run the file marked `highscor_cmdline.py` however you run python files.
#### Running python files
If you're not familiar with python and don't know how to run a file, there are several options:
* [Use the command line in windows to execute a script](https://docs.python.org/3/faq/windows.html#id2)
* Right-click the file, open with IDLE (comes pre-loaded with python) and press F5
* Download [atom](https://www.atom.io) and the [run-python-simply package](https://atom.io/packages/run-python-simply), open the file (or clone the repo) with atom, and press F5 (python must be in PATH) (I don't recommend this method unless you already understand how programming works)

#### CLI
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
Just press enter to continue. These often occur right after printing output, to give you some time to look at the output before proceeding back to a menu.

And that's all you need to know to navigate the program! If you're still confused, you can check out the wiki on this repo's [Github page](https://github.com/extremepayne/HighScor).

## Versioning
The project was originally programmed without git, so the file marked `old_version_history` still has some of the version history.
The file included here has the current version (v1.3.3).

## Contributing
More than welcome! Please create issues/PRs for anything you think should be included that isn't. (Or bug/typo fixes, etc.)

Note: This repo conforms to the following styleguides; please comply: [standard-readme](https://github.com/RichardLitt/standard-readme) and [black](https://github.com/ambv/black).

## License
MIT License © Harrison Payne. See license in `LICENSE.md`

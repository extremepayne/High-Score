# High-Score
Programs that save high scores to a file. 

This program was created originally as a response to the fact that the games on my calculator didn't have a good way to save highscores, and the eventual hope is that it will be able to have games write higscores to it (while still allowing manual addition of scores).

The basic idea is that you add games, scores, and associate those scores with players. Additional functionality has also been added, including settings, viewing scores by player as well as by game, and so forth. 
The program works by shelving files with the highscores in them and retriving them when nessecary (actually only once at the start of the program; they're re-shelved only when the user chooses "save and quit").

## How To Use This
You need python 3.x downloaded on your computer, just the standard python.org distribution should work just fine, and really any distribution with the sys and shelve modules. Clone the project, and run the file marked `highscore1.3.py` however you run python files (via IDLE, command line, double-click the file in Windows File Explorer, etc.) It should run just fine if you left `scores.dat.db` and `highscoresettings.dat.db` in the same directory (sub-file) as the main program. You can now add games, add, edit, and delete scores, view game leaderboards, veiw all of one player's scores, edit game settings, etc. Don't forget to go back through each menu to the top menu and select `0` before exiting the program, otherwise the program won't save.

## Versioning explaination
The project was originally programmed without git, so the opening comments still have some of the version history. 
Also, version 2.0 was stopped in development and contains no changes to the code. The file marked v1.3 has the current version.

## License
Just a standard MIT liscence. Check `LICENSE.md` for more info.

## Contributions
More than welcome! Please check out the code, it really isn't that long of a program. Submit any thoughts or suggestions you have via the approriate channels.

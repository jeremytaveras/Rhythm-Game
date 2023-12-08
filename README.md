# Rhythm-Game
A simple two stage rhythm game.


Requires pygame. To download pygame, paste one of the following into the terminal:

python3 -m pip install -U pygame --user

py -m pip install -U pygame --user

pip3 install pygame

pip install pygame



The 2nd one is what worked for me but it may be different for you. Once pygame is installed, run the code and the game window will open.

Default keybinds: Left Shift, Z, /, Right Shift.
If you wish to change the keybinds, you can do so where I set the keys in the lines 86-89.

-Functions: load_stage1 defined on line 105 and called on line 162, load_stage2 defined on line 129 and called on line 165.

-Conditionals: line 51, line 169, line 177.

-List: key list created on line 86, added on lines 87-90, iterated over on line 203.

-Nested Loop: no nested loops I wrote, the one nested loop used in the code was from the source.

-Recursive Function: no recursive functions.

-Objects: button class on line 32, extra subclass on line 42 but no inheritance.

-GUI-Elements: 

-'Our team completed this project with code that we wrote ourselves. Any time we used code from a source outside the resources for this class, it was only a few lines and we cited that source in the code.' - Jeremy Taveras

The source provided below was used to help me load the notes (load function on line 67) and keys (if map_rect on line 189) into the game. And also help organize/format my code (as their code was generally better organized than mine was), such as placing the clock.tick in the game loop at the very bottom, and placing the mixer inside the load function (line 70).

Source: https://github.com/tested69420/rythm-gam-code/tree/main/tutorial

Music sources: https://www.youtube.com/watch?v=VIop055eJhU (stage 1), https://www.youtube.com/watch?v=ukRgBnTSYdo (stage 2)

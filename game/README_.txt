###########################################
########## ROCK, PAPER, SCISSORS ##########
###########################################
Rules:
User picks:
        r - Indicating Rock
        p - Indicating Paper
        s - Indicating Scissors
Winner is decided by:
        Rock wins by blunting Scissors
        Paper wins by covering Rock
        Scissors wins by cutting Paper
        Draw if both are the same

How to Play:
1. Open Command Prompt
2. In command line call: >>python.exe game.py
3. Enter your selection
4. Winner will be decided according to Rules.

Testing:
Currently supported for Windows 10 using Python version 2.7.15.
To run tests, in command line call: >>pytest test_game.py. The test script will run the test designed for the tool and determine if there are any issues.
Current Tests:
1. Check computer choices are in same range as users
2. Check set list of invalid character user entries. 
3. Check set list of invalid string user entries.
4. Check to see if Draw outcome can be achieved with entry: r.
5. Check to see if Draw outcome can be achieved with entry: p.
6. Check to see if Draw outcome can be achieved with entry: s.
7. Check to see if Lose outcome can be achieved with entry: r.
8. Check to see if Lose outcome can be achieved with entry: p.
9. Check to see if Lose outcome can be achieved with entry: s.
10. Check to see if Win outcome can be achieved with entry: r.
11. Check to see if Win outcome can be achieved with entry: p.
12. Check to see if Win outcome can be achieved with entry: s.
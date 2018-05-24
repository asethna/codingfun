from random import Random

def generate_random():
    '''
    Summary:    Generates a number between 0-2
    Input:      None
    Output:     Gives an output value that is generated from 0-2
    '''
    myRandom = Random()
    return myRandom.randint(0,2)

def compare(user_input):
    '''
    Summary:    Compares the user_input with the computer generate input
                to determine the winner
    Input:      User provides a character/string
    Output:     Following the rules defined:
                    Rock wins by blunting Scissors
                    Paper wins by covering Rock
                    Scissors wins by cutting Paper
                    Both are same it is a draw
                the winner will be determined.
    '''    
    game_input = ['r','p','s']
    if not(user_input in game_input):
        return "Invalid user input: %s" % user_input

    computer_input = game_input[generate_random()]

    print "Computer Picked: %s" % computer_input
    if user_input == computer_input:
        return "Draw!"
    else:
        if user_input == 'r':
            if computer_input == 'p':
                return "Paper covers rock\nComputer Wins!"
            else:
                return "Rock blunts scissors\nUser Wins!"
        elif user_input == 'p':
            if computer_input == 's':
                return "Scissors cut paper\nComputer Wins!"
            else:
                return "Paper covers rock\nUser Wins!"
        elif user_input == 's':
            if computer_input == 'r':
                return "Rock blunts scissors\nComputer Wins!"
            else:
                return "Scissors cut paper\nUser Wins!"
            
def main():
    print "###########################################"
    print "########## ROCK, PAPER, SCISSORS ##########"
    print "###########################################"
    print "Rules:\nUser picks:\n\tr - Indicating Rock"
    print "\tp - Indicating Paper\n\ts - Indicating Scissors"
    print "Winner is decided by:\n\tRock wins by blunting Scissors"
    print "\tPaper wins by covering Rock\n\tScissors wins by cutting Paper"
    print "\tDraw if both are the same\n\n"

    #Asks user for input
    user_input = raw_input("Please pick from (r,p,s):")
    print "User Picked: %s" % user_input
    print compare(user_input)
    
if __name__ == '__main__':
    main()

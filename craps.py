'''
craps.py - function that returns the amount won or lost from a single game of craps.

Inputs:
    bet - an amount bet on either the pass or don't pass line
    line - 1 for the pass line and 2 for the don't pass line

Outputs:
    winnings - the amount of money a player won/lost.  See note 2.

Notes:
    1.  I tried to order the various if/elif statements in the highest probabilty
        that they would occur so that the ones with the lowest probability of 
        occurring would be checked last.  In other words, I don't want to check
        for a 12 first when it is the least likey thing to be rolled (besides a two).

    2.  Right now the code is set for a player winning even money on a pass or don't
        pass line bet.  Working othe code to include taking/laying odds.

    3.  Comment out the print statements for large simulations.  The are included 
        here to allow the user to actually simulate playing craps.

'''

## Import needed modules
import random               # needed for the RNG
from random import randint  # needed for the RNG
import time                 # needed to pause after rollind die for effect
from os import system, name # needed to clear screen after each game.

## Define functions
# function to roll dice
def roll_die (num_die):    
    # Initialize variables
    die = [] # list to hold value for each die rolled
    # random.seed() # seed RNG with current system time    

    # for loop to roll each die
    for i in range(num_die):
        die.append(random.randint(1,6)) # roll ith die
    # end for

    # sum the dice and return the value
    total = sum(die)

    # return total
    return total
# end roll_die function

# function to keep rolling after a point is set
def keep_rolling(point):
   
    # Shooter rolls die
    new_roll = roll_die(2) # craps used two dice
    delay = randint(1,5) # randomly select a delay from 1 to 5 seconds.
    time.sleep(delay)           # pause game for 'delay' as shooter keeps rolling

    # Determine if shooter won or lost
    if (new_roll == point): # shooter wins
        win = True             # set win
        print("\nShooter rolled a", new_roll,"to win") # prints win to screen
        # Comment out print statement for large simulations

    elif (new_roll == 7): # shooter lost
        win = False            # set win
        print("\nShooter crapped out with a", new_roll)
    else: # neither point or crapping out
        print("\nShooter rolled", new_roll)
        win = keep_rolling(point)   # recursively call function as needed
    # end if, elif, else
    
    return win # return amount won/lost
# end function

# function to play game
def craps( bet, line, bank_roll):    
    # Establish point
    point = roll_die(2)            # roll dice
    print("\nThe comeout roll is a", point) # print point

    # Determine outcome of game
    if (point == 7 or point == 11): # shooter rolls 7 or 11 on come out roll
        if (line == 1):     # pass line win
            winnings = bet  # player wins bet
            print("\nPass line better wins with a",point) # print winner
        else: # don't pass line loser
            winnings = -bet # player loses bet
            print("\nDon't pass line better loses with a",point) # print loser
        # end if, else

    elif (point == 2 or point == 3): # shooter rolls 2 or 3 on come out roll
        if (line == 1): # pass line lose
            winnings = -bet # player loses bet
            print("\nPass line shooter loses with a", point) # print lose
        else: # don't pass line win
            winnings = bet  # player wins bet
            print("\nDon't pass line shooter loses with a", point) # print win
        # end if, else

    elif(point == 12):
        if (line == 1): # pass line lose
            winnings = -bet # player loses bet
            print("\nPass line better loses with a", point) # print lose
        else: # don't pass line push
            winnings = 0    # player niether wins or loses bet
            print("\nDon't pass line better pushes with a", point) # print push
        # end if, else

    else:
        # Ask player if they want to place an odds bet
        odds = float(input("\nEnter 1 to place an Odds bet and 2 to not place an Odds bet.\n"))
        odds = int(odds)
        odds_bet = 6 * bet
        if(odds == 1 and odds_bet > bank_roll):
            print('\nOdds bet larger than bank roll, odds bet not allowed.  Continuing without odds bet')
            odds = 2
        # end if

        winnings = keep_rolling(point) # determine win/loss after point established

        if(winnings == True):
            if(odds == 1 and line == 1):    # pass line bet with odds
                winnings = 6 * bet
            elif(odds != 1 and line == 1):  # pass line bet with no odds
                winnings = bet
            elif(odds != 1 and line != 1):  # don't pass line bet with no odds
                winnings = -bet
            else: # don't pass line bet with odds
                winnings = -7 * bet
            # end if, elif, elif, else
        elif(winnings == False):
            if(odds != 1 and line != 1):    # don't pass line bet with no odds
                winnings = bet
            elif(odds != 1 and line == 1):  # pass line bet with no odds
                winnings = -bet
            elif(odds != 1 and line == 1):  # pass line bet with odds
                if(point == 6 or point == 8):
                    winnings = -6 * bet
                elif(point == 5 or point == 9):
                    winnings = -5 * bet
                elif(point == 4 or point == 10):
                    winnings = -4 * bet
                else:
                    print('Error 1')
                # end if, elif, else
            else: # don't pass line bet with odds
                if(point == 6 or point == 8):
                    winnings = 6 * bet
                elif(point == 5 or point == 9):
                    winnings = 5 * bet
                elif(point == 4 or point == 10):
                    winnings = 4 * bet
                else:
                    print('Error 2')
                # end if, elif, else
            # end if, elif, elif, else
        else:
            print('Error 3')
        # end if, elif, else
        
        # Update and print bankroll
        bank_roll = bank_roll + winnings 

    return winnings # return winnings

# end function

# function to clear the screen after each game.
def clear_screen():
    
    # Windows
    if (name == 'nt'):
        _ = system('cls')

    # for Mac and Linux
    else:
        _ = system('clear')
    #end if, else

    return None
# end function

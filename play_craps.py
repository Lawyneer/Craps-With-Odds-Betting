'''
play_craps.py - script to allow a user to play a simple texted based game of craps.

Inputs:
    bet - user input bet amount
    line - user input to select a pass or don't pass line bet
    
Outputs:
    Print if the player wins, loses, pushes, and how much was won/lost.
    Other functions called from within print out rolls as shooter rolls

Notes:
    This has been run and tested on linux and Mac machines.
    
'''


# Import needed packages
import craps as crps    # function to play craps

# Initialize variables
bank_roll = 500     # starting bankroll
keep_playing = 1    # termination condition

while(keep_playing == 1 and bank_roll > 0):
    
    # Clear screen from last game
    crps.clear_screen()    
        
    # Prompt user for a bet
    print("\nThe current bankroll is", bank_roll)
    bet = float(input("\nPlease enter a bet.\n")) # accept any number
    bet = int(bet)	# round down to nearest whole dollar amount

    # Make sure bankroll covers bet
    if(bet > bank_roll):
    	keep_betting = True
    	while keep_betting == True:
    		print("\nBet too high.  Max bet is: ",bank_roll)
    		bet = float(input("\nPlease enter a bet.\n")) # accept any number
    		bet = int(bet)	# round down to nearest whole dollar amount
    		if bet <= bank_roll:
    			keep_betting = False
    		# end if
    	# end while
    # end if
    
    # Prompt user to line
    line = float(input("\nEnter 1 for a pass line bet and 2 for a don't pass line bet.\n"))
    line = int(line) # round float down to nearest integer.  Anything other than 1
    				 # in craps game will default to don't pass line.

    # Play the game
    win = crps.craps(bet, line, bank_roll)
    
    # Print results
    if(win < 0): # print lose
        print("\nPlayer lost -$",abs(win))
    elif(win > 0): # print win
        print("\nPlayer won $", win)
    else: # print push
        print("\nThe player pushes")
    # end if, elif, else
    
    # Update and print bankroll
    bank_roll = bank_roll + win
    print("\nCurrent bankroll is $",bank_roll)
    
    # Determine if play continues
    if(bank_roll <= 0): # Check if player busted
        print("\nPlayer busts.  Please try again.")
    else: # prompt user to keep playing
        keep_playing = float(input("\nEnter 1 to keep playing or 0 to quit.\n"))
        keep_playing = int(keep_playing) # round down to nearest integer
        if(keep_playing < 0 or keep_playing > 1):
            print("\nInput error.\n")
            keep_playing = int(input("\nEnter 1 to keep playing or 0 to quit.\n"))
        # end if
    # end if, else

# end while loop

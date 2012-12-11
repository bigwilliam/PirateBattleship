from __future__ import print_function # makes the print() function compatible with older versions of python
import boat
import gameboard
import player

########################### 
#      introduction
###########################
print("Yarr Pirate Battleship matey!")
player1 = player.Player(raw_input("What be yer name? "))
#theBoardSize = int(raw_input("How large a board? (recommend 10)"))
theBoardSize = 10 # right now the board size must be 10 to keep 'coordinateReference' simple
numBoats = int(raw_input("How many boats? (recommend 3)"))

###########################
#     create elements
###########################

# create a dictionary for referencing coordinates from the player to the computer
coordinateReference = { 'A':0, 'B':1, 'C':2,'D':3, 'E':4, 'F':5, 'G':6, 'H':7, 'I':8, 'J':9 }

# create the board
board = gameboard.GameBoard(theBoardSize)

# create the boats. Boat coordinates are dictionaries with tuples as the coordinates and 'o' as the initial values (when hit, value changes to 'x')
boatList = []
for num in range(numBoats):
    #make sure the boats don't overlap (eventually, not right now)
    #
    #
    boatList.append(boat.Boat(boardSize=theBoardSize))

###########################
#     Play the game!
###########################
def clearScreen():
    for i in range(50):
        print()

while numBoats > 0:
    #clearScreen()
    board.draw()
    #TEST
    print("The boat list is:")
    for boat in boatList:
        print(boat.getCoordinates())
    move = raw_input("Arrgh, make yer move " + player1.name() + "! (example: C,4)")
    # convert move to int format (note x and y coords are reversed cuz in Battleship the letter is the row, yadda yadda, oops)
    y = int(coordinateReference[move[0].upper()])
    x = int(move[2])

    #TEST
    print("x is " + str(x))
    print("y is " + str(y))
    print("Now checking if boat is in boatList...")

    for boat in boatList:
        if (x,y) in boat.getCoordinates():
            print(boat.isHit(x,y))
            board.updateHit(x,y)
            print("Boat was hit!")
            break
    else:
        board.updateMiss(x,y)
        print("Miss")
        
    # check to see if any boats are sunk, and lower numBoats accordingly
    # doing it later





"""
1. The game starts, the user sees an intro screen (hits enter)
2. The board is created and boats positions randomly generated
3. asks for user name
4. Screen displays board and asks for input
5. input is checked for validity 
6. compare input with boat values
7. if found, update boat and board to 'x', run the "hit" screen for the user to see
8. if miss, update board to 'o', run the 'miss' screen
9. ask for next input
"""


"""
def showBoard():
	''' 
	Just displays what the board is supposed to look like
	'''
	print("  0 1 2 3 4 5 6 7 8 9")
	print("A . . . . . . . . . .")
	print("B . . . . . . . . . .")
	print("C . . . . . . . . . .")
	print("D . . . . . . . . . .")
	print("E . . . . . . . . . .")
	print("F . . . . . . . . . .")
	print("G . . . . . . . . . .")
	print("H . . . . . . . . . .")
	print("I . . . . . . . . . .")
	print("J . . . . . . . . . .")
#showBoard()
"""

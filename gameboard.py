from __future__ import print_function # lets us use the newer print function on older versions of python
import string # lets us do some formatting for the draw method

class GameBoard:
    """ 
    Create a square grid as a list of lists. Default is 10x10 with '.' as initial values. 
    NOTE: Because the board stores values in the order of row then column (y then x), 
    the x and y coordinates are switched to match. 
    Outside this class everything is considered to be x,y (col, row). This also assumes that
    we receive all coordinates as x,y. In other words, inside here the world is y,x but outside
    it's x,y. See notes at the bottom of readme.txt for more on this.
    """
    
    def __init__(self, boardSize=10, setMark='.'):
        self.size = boardSize
        self.defaultMark = setMark 

        ### This creates the board matrix ###
        self.grid = [ [ self.defaultMark for row in range(self.size) ] for col in range(self.size) ] 

    def draw(self): # Draws the board for the user to see. The most commonly used method of this class.
        rowLabels = "ABCDEFGHIJ" # will be used as a reference for the player to see

        print("  0 1 2 3 4 5 6 7 8 9") # references for the columns
        for rowLabel, row in zip(rowLabels, self.grid): # zip lets us iterate through two variables at the same time
            print(rowLabel,end=" ") # print rowLabel but don't start a newline, yet.
            for col in row:
                print('{0:1}'.format(col), end=" ") # print each board coordinate and keep it evenly spaced
            print() # now that we printed a row completely, start a newline

    def hasAlreadyBeenPlayed(self, xCoord, yCoord):
        # returns True if the user has already made a move at (xCoord,yCoord)
        return not self.grid[yCoord][xCoord] == self.defaultMark

    def countSpacesNotPlayed(self):
        count = 0
        for row in self.grid:
            for space in row:
                if self.defaultMark in space:
                    count = count + 1
        return count

    def updateHit(self, xCoord, yCoord, hitMark='x'):
            self.grid[yCoord][xCoord] = hitMark
            
    def updateMiss(self, xCoord, yCoord, missMark='o'):
            self.grid[yCoord][xCoord] = missMark

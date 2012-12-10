from random import randint
class Boat:
    """Create a boat object with specified length. Default length is 3. ASSUMES that boardSize is > boatLength"""
    
    def __init__(self, boatLength=3, boardSize=10):
        self.length = boatLength
        self.matrixLimit = boardSize
        self.coordinates = {}
        self.hitMark = 'x'
        self.notHitMark = 'o'
        # randomly choose coordinates where the boat will start from
        x = randint(0, self.matrixLimit - 1)
        y = randint(0, self.matrixLimit - 1)       
        
        # Choose a direction the boat will be facing, and check to make sure it doesn't run off the board
        def setDirection():
            d = randint(0,3)  # 0 = north, 1 = east, 2 = south, 3 = west
            if (d == 0 and y-(self.length-1) < 0) or (d == 1 and x+(self.length-1) > 9) or (d == 2 and y+(self.length-1) > 9) or (d == 3 and x-(self.length-1) < 0):
                setDirection()
            return d
        direction = setDirection()

        # Now create the boat based on what direction it is facing
        if direction == 0: # if facing NORTH
            for i in range(self.length):
                self.coordinates[(x,y)] = self.notHitMark
                y = y - 1
        if direction == 1: # if facing EAST
            for i in range(self.length):
                self.coordinates[(x,y)] = self.notHitMark
                x = x + 1
        if direction == 2: # if facing SOUTH
            for i in range(self.length):
                self.coordinates[(x,y)] = self.notHitMark
                y = y + 1
        if direction == 3: # if facing WEST
            for i in range(self.length):
                self.coordinates[(x,y)] = self.notHitMark
                x = x - 1
        
    def getCoordinates(self):
        return self.coordinates
    
    def isHit(self, x, y):
        #returns true and updates boat value if coordinates given is a hit, false if miss or coordinate already played
        if (x,y) not in self.coordinates:
            return False
        elif self.coordinates[(x,y)] == self.hitMark:
            return False
        else:
            self.coordinates[(x,y)] = self.hitMark
            return True
        
    def isSunk(self):
        #returns true if the boat is sunk (all coordinates have been hit)
        return not (self.notHitMark in self.coordinates.values())
    
    def numberNotHit(self):
        # returns how many coords have not been hit yet
        count = 0
        for key in self.coordinates:
            if self.coordinates[key] == self.notHitMark:
                count = count + 1
        return count

    def numberOfHits(self):
        # returns how many hits the boat has taken
        count = 0
        for key in self.coordinates:
            if self.coordinates[key] == self.hitMark:
                count = count + 1
        return count

""" FOR TESTING PURPOSES """
#boat1 = Boat(3)
#print(boat1.getCoordinates())
#boat2 = Boat(4)
#print(boat2.getCoordinates())
#boat3 = Boat(5)
#print(boat3.getCoordinates())


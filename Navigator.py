class Navigator:
    # the constructor
    def __init__(self, yPos, xPos, speed, plugTime, available):
        self.xPos = xPos
        self.yPos = yPos
        self.speed = speed
        self.plugTime = plugTime
        self.available = available
    
    def pickup(self, batt):
        xDelta = abs(batt.xPos - self.xPos)
        yDelta = abs(batt.yPos - self.yPos)
        print("The xPos of this navigator is: " + str(self.xPos))
        print("The xPos of this battery is: " + str(batt.xPos))
        # time passed to pickup battery is the (distance along x + 
        # distance along y) times the rate of travel
        tDelta = (xDelta + yDelta) * self.speed
        # moves the navigator to the battery module
        self.xPos = batt.xPos
        self.yPos = batt.yPos
        print("this task took " + str(tDelta) + " seconds")
        return tDelta

    def reportStats(self):
        print("REPORTING STATUS: " + "my current pos is " + str(self.xPos) + ", " + str(self.yPos))
    
    def moveTo(self, obj):
        xDelta = abs(obj.xPos - self.xPos)
        yDelta = abs(obj.yPos - self.yPos)
        tDelta = (xDelta + yDelta) * self.speed
        self.xPos = obj.xPos
        self.yPos = obj.yPos

        print("moving there took " + str(tDelta) + " time")
        return tDelta

class Navigator:
    # Constructor
    def __init__(self, yPos, xPos, speed, plugTime, available):
        self.xPos = xPos
        self.yPos = yPos
        self.speed = speed
        self.plugTime = plugTime
        self.available = available
    
    # Methods
    
    # moves navigator to the battery it wants
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
    
    # 
    def moveTo(self, obj):
        xDelta = abs(obj.xPos - self.xPos)
        yDelta = abs(obj.yPos - self.yPos)
        # time passed to move to obj is the (distance along x + 
        # distance along y) times the rate of travel
        tDelta = (xDelta + yDelta) * self.speed
        # moves the navigator to the object
        self.xPos = obj.xPos
        self.yPos = obj.yPos

        print("moving there took " + str(tDelta) + " time")
        return tDelta

    def goHome(self):
        xDelta = abs(self.xPos)
        yDelta = abs(self.yPos)
        # time passed to move to obj is the (distance along x + 
        # distance along y) times the rate of travel
        tDelta = (xDelta + yDelta) * self.speed
        # moves the navigator to the object
        self.xPos = 0
        self.yPos = 0

        print("moving there took " + str(tDelta) + " time")
        return tDelta


    def useArm(self):
        tDelta = self.plugTime  #(assume it takes 3 min to plug in or out)
        return tDelta
    
    # NEED TO CREATE DICTIONARY OF ALL NAVIGATORS BUSY/NOT BUSY AND FOR HOW LONG
    #def updateAvailability(self):
    #        if t <= self.plugTime >= self.chargingThreshold:
    #            self.available = True
    #        else:
    #            self.available = False
    #        print("Availability of Navigator has been updated.")
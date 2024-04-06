class Navigator:
    # Constructor
    def __init__(self, yPos, xPos, xSpeed, ySpeed, plugTime, available):
        self.xPos = xPos
        self.yPos = yPos
        self.xSpeed = xSpeed
        self.ySpeed = ySpeed
        self.plugTime = plugTime
        self.available = available

    def reportStats(self):
        print("REPORTING STATUS: " + "my current pos is " + str(self.xPos) + ", " + str(self.yPos))
    
    # 
    def moveTo(self, obj):
        xDelta = abs(obj.xPos - self.xPos)
        yDelta = abs(obj.yPos - self.yPos)
        # time passed to move to obj is the (distance along x + 
        # distance along y) / the rates of travel

        print("----DEBUGGING MOVETO------"+
              "\nObj pos:" + str(obj.xPos) + "," + str(obj.yPos) +
              "\nNav pos:" + str(self.xPos) + "," + str(self.yPos) +
              "\nxDelta = " + str(xDelta) +
              "\nyDelta = " + str(yDelta) +
              "\nxSpeed = " + str(self.xSpeed) +
              "\nySpeed = " + str(self.ySpeed))
        
        tDelta = (xDelta / self.xSpeed) + (yDelta / self.ySpeed)
        # moves the navigator to the object
        self.xPos = obj.xPos
        self.yPos = obj.yPos

        # print("moving there took " + str(tDelta) + " time")
        return tDelta

    def goHome(self):
        xDelta = abs(self.xPos)
        yDelta = abs(self.yPos)
        # time passed to move to obj is the (distance along x + 
        # distance along y) / the rates of travel
        tDelta = (xDelta / self.xSpeed) + (yDelta / self.ySpeed)
        # moves the navigator to the object
        self.xPos = 0
        self.yPos = 0

        # print("moving there took " + str(tDelta) + " time")
        return tDelta


    def useArm(self):
        tDelta = self.plugTime
        return tDelta
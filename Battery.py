import Car

class Battery:
    # Constructor
    # chargeRate = time unit takes to charge by 1%. assume all cars have same max charge amount
    def __init__(self, xPos, yPos, chargeLevel, chargeRate, available):
        self.xPos = xPos
        self.yPos = yPos
        self.chargeLevel = chargeLevel
        self.chargeRate = chargeRate
        self.available = available

    # Variables
    chargingThreshold = 100 # the charging level at which the battery can go charge a car

    # Methods
    def updateAvailability(self):
        if self.chargeLevel >= self.chargingThreshold:
            self.available = True
        else:
            self.available = False
        print("Availability of Battery has been updated.")

    def chargeUp(self):
        self.xPos = 0
        self.yPos = 0
        diff = 100 - self.chargeLevel
        self.chargeLevel = 100
        self. available = True
        tDelta = diff * self.chargeRate
        return tDelta
    

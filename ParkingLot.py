import Car
import random

class ParkingLot:
    # constuctor
    def __init__(self, xSize, ySize):
        self.xSize = xSize
        self.ySize = ySize

    # make sure bots don't go out of bounds
    #def outOfBounds(a, b):
    #    if a > self.xSize or  b > self.ySize:
    #        print("WARNING: out of bounds.")
    
    # populate lot with random num cars in random places
    # can index the new cars using myCars[]
    def populate(self, numCars):
      ranX = random.randrange(0, self.xSize, 1)
      ranY = random.randrange(0, self.ySize, 1)
      ranDesiredLevel = random.randrange(0, 100, 1) #fix. must be larger than current
      ranCurrentLevel = random.randrange(0, 100, 1)
      # make a bunch of cars with locations
      myCars = {k: Car.Car(ranX, ranY, ranDesiredLevel, ranCurrentLevel) for k in numCars}
      print(str(numCars) + "have entered this lot.")
      return myCars
      #for k in lst}
    #STILL NEED TO TEST ^


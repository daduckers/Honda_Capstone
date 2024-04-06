import Car
import random
import Battery
import Navigator
import hashlib

class ParkingLot:
  # constuctor
  def __init__(self, xSize, ySize):
      self.xSize = xSize
      self.ySize = ySize
      self.numCars = 0
      self.cars = []
      self.navigators = []
      self.batteries = []
      print(">> CREATED A LOT OF SIZE " + str(self.xSize) + ", " + str(self.ySize))

  # creates and adds a battery to the parkinglot's list of battery objects
  def buyBattery(self, xPos, yPos, chargeLevel, chargeRate, available):
    newBattery = Battery.Battery(xPos, yPos, chargeLevel, chargeRate, available)
    self.batteries.append(newBattery)

  def buyBatteries(self, numBatts, xPos, yPos, chargeLevel, chargeRate, available):
    for i in range(numBatts):
      self.buyBattery(xPos, yPos, chargeLevel, chargeRate, available)
    print("Just bought " + str(numBatts) + " batteries")

  # creates and adds a navigator to the parkinglot's list of navigator objects
  def buyNavigator(self, yPos, xPos, xSpeed, ySpeed, plugTime, available):
    newNavigator = Navigator.Navigator(yPos, xPos, xSpeed, ySpeed, plugTime, available)
    self.navigators.append(newNavigator)

  def buyNavigators(self, numNavs, yPos, xPos, xSpeed, ySpeed, plugTime, available):
      for i in range(numNavs):
        self.buyNavigator(yPos, xPos, xSpeed, ySpeed, plugTime, available)
      print("Just bought " + str(numNavs) + " navigators.")

  # populate lot with random num cars in random places. can index the new cars using myCars[]
  def populate(self, numCars):
    self.numCars = numCars
    for i in range(numCars):
      ranX = random.randrange(0, self.xSize, 1)
      ranY = random.randrange(0, self.ySize, 1)
      ranChargeLevel = random.randrange(0, 99, 1) # I wrote this so the present charge level would never be greater than the desired charge level
      lowerLimit = ranChargeLevel + 1
      ranDesiredCharge = random.randrange(lowerLimit, 100, 1) 

      print("Car #" + str(i) + " needs " + str(ranDesiredCharge - ranChargeLevel) + " percent charge, and is at " + str(ranX) + "," + str(ranY) + ".")

      # this part is now irrelavant, but I keep it just for reassurance
      if ranDesiredCharge >= ranChargeLevel:
        available = True
      else:
        available = False

      theCar = Car.Car(ranX, ranY, ranChargeLevel, ranDesiredCharge, available)
      #print("THE CAR DETAILS:" + str(theCar.xPos) + "," + str(theCar.yPos) + "," + str(theCar.chargeLevel) + "," + str(theCar.desiredCharge) + "," + str(theCar.available))
      self.cars.append(theCar)
    print(">> POPULATED THE LOT WITH " + str(numCars) +" CARS")
    return
    
  # meant for updating the availability status of all the cars in the lot, called from findAvailableCars
  def updateCarAvailability(self):
    for i in range(len(self.cars)):
      theCar = self.cars[i]
      if (theCar.desiredCharge > theCar.chargeLevel):
        theCar.availability = True
      else:
        theCar.availability = False
    return

  # find all available cars in the lot where "cars" is an array of all the car objects in the lot. called from main
  def findAvailableCars(self):    # SOEMTHING WRONG
    availableCars = []
    self.updateCarAvailability()
    for i in range(len(self.cars)):
      thisCar = self.cars[i]
      if thisCar.available == True:
        availableCars.append(thisCar)
      else:
        pass
    #print("A LIST OF AVAILABLE CARS:" + str(availableCars))
    print(">> MADE A LIST OF THE AVAILABLE CARS IN THE LOT")
    return availableCars

  # charge a singular car
  def chargeCar(self, theCar, theBatt):
    if theCar.desiredCharge > theCar.chargeLevel:
      # charge the car the amount it wants
      chargeDiff = abs(theCar.desiredCharge - theCar.chargeLevel)
      theCar.chargeLevel = theCar.desiredCharge
      # set the battery to not available and reduce its charge amount
      theBatt.chargeLevel -= chargeDiff # (assume its one to one)
      theBatt.available = False
      # count the time it took to charge
      t = theBatt.chargeRate * chargeDiff
      #print('the t value for this chargeCar() method is:' + str(t))
      return t
    else:
      print("ERROR: The Car's desired charge level may be lower than the current charge level. Could not charge this car.")
  
  # search for and return a navigator that is at home (the central station, aka (0,0))
  def findNavAtHome(self):
    for k in range(len(self.navigators)):
      if ((self.navigators[k].xPos == 0) and (self.navigators[k].yPos == 0)): # assume all the navs at home are available
        navAtHome = self.navigators[k]
        print("The navAtHome lives at " + str(navAtHome.xPos) + "," + str(navAtHome.yPos))
        return navAtHome
      else:
        pass
    return navAtHome

  # search for and return a battery that is at home (the central station, aka (0,0))
  def findBattAtHome(self):
    for k in range(len(self.batteries)):
      if ((self.batteries[k].xPos == 0) and (self.batteries[k].yPos == 0)): # assume all the batts at home are available
        battAtHome = self.batteries[k]
        return battAtHome
      else:
        pass
    return battAtHome
    
  # return the object of the navigator thats the closest to the car
  def findClosestNav(self, theCar):
    # create a list of all available navigators, and fill it with those navigators using a loop. this renews for every car
    availableNavs = [] 
    for l in range(len(self.navigators)):
      if (self.navigators[l].available == True):
        availableNavs.append(self.navigators[l])
      else:
        pass
    print("The available navs are " + str(availableNavs))

    # create a list of how far away each available navigator is from the car in question. this renews for every car
    # first find a navigator that is the closest and available
    # go thru every available navigator in the lot
    navDistances = []
    for j in range(len(availableNavs)):
      xDelta = abs(theCar.xPos - availableNavs[j].xPos)
      yDelta = abs(theCar.yPos - availableNavs[j].yPos)
      distanceAway = yDelta + xDelta #how far away is the navigator from the car
      navDistances.append(distanceAway) #add how far away the navigator is from the car to a list
    print("the navDistances are: " + str(navDistances))

    # in the list that details how far away each available nav in the lot is, find the index value of the shortest distance
    chosen = navDistances.index(min(navDistances)) #chosen is an index value for a list
    closestNav = self.navigators[chosen]
    print("The chosen nav is in pos" + str(chosen) + "in that list, and is at pos " + str(closestNav.xPos) + "," + str(closestNav.yPos) + ".")

    return closestNav


  # charge all cars in lot. must populate before using chargeCars
  def chargeCars(self, availableCars):
    if len(availableCars)>0: # only charge if populated with cars
      totalTime = []
      #loop thru the list of available car objects
      for i in range(len(availableCars)):
        theCar = availableCars[i] #the car in question
        # find and move a navigator and battery at the central station to the car (assume all navs and batts at the central station are at the same location 0,0)
        navAtHome = self.findNavAtHome()
        battAtHome = self.findBattAtHome()
        movingTime = navAtHome.moveTo(theCar) # move navigator to the car in question. returns a time
        print("MOVING NAV & BATT TO THE CAR TOOK " + str(movingTime) + "min.")
        battAtHome.xPos = navAtHome.xPos
        battAtHome.yPos = navAtHome.yPos # set battery pos equal to nav pos (assume this took no time, ie the navigator moves just as fast with as without the batt)
        plugBattTime = navAtHome.useArm() #returns time it took to plug the battery into the car
        print("PLUGGING BATTERY IN TOOK " + str(plugBattTime) + "min.")
        theBatt = battAtHome #because the battery is no longer at the central station, we rename it
        chargingTime = self.chargeCar(theCar, theBatt) # charges theCar with theBatt. returns a time
        print("CHARGING CAR TOOK " + str(chargingTime) + "min.")
        # pretend navigator we used is somewhere completely diff now. it's unavailable. see README file for a footnote on this
        navAtHome.available = False
        # grab the navigator that's closest to the car
        closestNav = self.findClosestNav(theCar)
        # move the closest navigator to the now much depleted battery, unplug the battery, then go home
        movingTime2 = closestNav.moveTo(theBatt)
        print("The chosen nav is at pos " + str(closestNav.xPos) + "," + str(closestNav.yPos) + ".")
        print("MOVING NEW NAV TO DONECAR TOOK " + str(movingTime2) + "min.")
        # print("just moved the closest nav to the now depleted batt")
        unplugBattTime = navAtHome.useArm() #returns a time
        print("UNPLUGGING BATTERY IN TOOK " + str(unplugBattTime) + "min.")
        movingTime3 = closestNav.goHome()
        print("MOVING THE NEW NAV & THE BATT HOME TOOK " + str(movingTime2) + "min.")
        # print("unplugged batt and nav went home")
        # sets batt location to 0,0 and charges up to 100%
        #chargingTime2 = theBatt.chargeUp() #actually, don't use this cause the active user doesn't see this time. i'd need to be able to move two batts at once to use this
        # print("batt went home and charged up")
        # make the original navigator available again
        navAtHome.available = True
        chargeCarTime = movingTime + plugBattTime + chargingTime + movingTime2 + unplugBattTime + movingTime3 #+ chargingTime2
        totalTime.append(chargeCarTime)
        print("------done charging that car------")
      print(">> CHARGED ALL AVAILABLE CARS")
      print("The time it took to charge all the available cars in the lot was:" + str(totalTime) + ". \nThat's equal to " + 
            str(sum(totalTime)) + " minutes, or " + str(sum(totalTime)/60) + " hours.")
      return totalTime
    else:
      print("ERROR: There might not be cars in this lot that need charging. Could not charge these cars.")
      
  
    


  # make sure bots don't go out of bounds
  #def outOfBounds(a, b):
  #    if a > self.xSize or  b > self.ySize:
  #        print("WARNING: out of bounds.")
  
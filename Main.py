import ParkingLot
import Navigator
import Battery
import Car

class Main:

    # make a parking lot
    parkingLot1 = ParkingLot.ParkingLot(25, 25)

    # fill it with cars
    parkingLot1.populate(5)
    print("JUST POPULATED")
    parkingLot1.buyBattery(0, 0, 100, 1, True)
    parkingLot1.buyBattery(0, 0, 100, 1, True)
    parkingLot1.buyNavigator(0, 0, 1, 3, True)
    parkingLot1.buyNavigator(0, 0, 1, 3, True)
    parkingLot1.buyNavigator(0, 0, 1, 3, True)
    parkingLot1.buyNavigator(0, 0, 1, 3, True)
    #print("BOUGHT THESE NAVS:" + str(parkingLot1.navigators))
    #print("BOUGHT THESE BATTS:" + str(parkingLot1.batteries))

    # figure out what cars in the lot need to be charged
    availableCars = parkingLot1.findAvailableCars() #returns a list of the available cars
    print("findAvailableCars = success")
    
    # charge all the available cars in the lot
    time = parkingLot1.chargeCars(availableCars)
    print("the time it took to charge all the available cars in the lot was:" + str(time))
    # figure out which are priority
    # priorityCars = priority(cars)

    
    
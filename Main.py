import ParkingLot
import Navigator
import Battery
import Car

class Main:

    print("_________________________________________________________________________\n"+
          "                            STARTING PROGRAM                               \n"+
          "_________________________________________________________________________\n")
    # make a parking lot
    parkingLot1 = ParkingLot.ParkingLot(5, 5)
    # fill it with cars
    parkingLot1.populate(2)
    parkingLot1.buyBatteries(2, 0, 0, 100, 1.6, True) #buy 5 batteries for the lot
    parkingLot1.buyNavigators(3, 0, 0, 31.05, 14.67, 3, True) #buy 3 navs for the lot

    # figure out what cars in the lot need to be charged
    availableCars = parkingLot1.findAvailableCars() #returns a list of the available cars

    # charge all the available cars in the lot
    parkingLot1.chargeCars(availableCars)



    print("_________________________NEW PARKING LOT_____________________________\n")

    
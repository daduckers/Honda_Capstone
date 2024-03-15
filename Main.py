import ParkingLot
import Navigator
import Battery
import Car

class Main:
    car1 = Car.Car(8, 8, 50, 80)
    car2 = Car.Car(5, 5, 80, 100)
    car3 = Car.Car(2, 2, 20, 80)
    navigator1 = Navigator.Navigator(0, 0, 1, 3, True)
    battery1 = Battery.Battery(0, 0, 100, True)
    
    t = 0
    t += navigator1.pickup(battery1)
    navigator1.reportStats()
    t += navigator1.moveTo(car1)
    navigator1.reportStats()
    print(t)

    # make a parking lot
    parkingLot1 = ParkingLot.ParkingLot(32, 32)

    # fill it with cars
    parkingLot1.populate(5)

    # charge the cars
    
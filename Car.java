public class Car {
    Integer chargeLevel;
    Integer xPos;
    Integer yPos;
    Integer desiredCharge;

    // constructor makes a new instance of a Car
    public Car(Integer xPos, Integer yPos, Integer chargeLevel, Integer desiredCharge) {
        this.xPos = xPos;
        this.yPos = yPos;
        this.chargeLevel = chargeLevel;
        this.desiredCharge = desiredCharge;
    }
}

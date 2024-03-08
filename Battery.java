public class Battery {
    Integer xPos;
    Integer yPos;
    Integer chargeLevel;
    boolean availability;

    public Battery(Integer xPos, Integer yPos, Integer chargeLevel, boolean availability){
        this.yPos = yPos;
        this.xPos = xPos;
        this.chargeLevel = chargeLevel;
        this.availability = availability;
    }
}

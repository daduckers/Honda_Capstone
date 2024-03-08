import java.lang.Math;

public class Navigator {

    Integer xPos;
    Integer yPos;
    Integer baseSpeed;
    Integer plugTime;
    boolean availability;

    public Navigator(Integer xPos, Integer yPos, Integer baseSpeed, 
                    Integer plugTime, boolean availability){
        this.xPos = xPos;
        this.yPos = yPos;
        this.baseSpeed = baseSpeed;
        this.plugTime = plugTime;
        this.availability = availability;
    }

    //goes to battery
    public Integer pickup(Battery batt){
        int xDelta = Math.abs(batt.xPos - this.xPos);
        int yDelta = Math.abs(batt.yPos - this.yPos);
        System.out.println("the x pos is: " + this.xPos);
        System.out.println("the x pos of the batt is: " + batt.xPos);
        // amount of time passed to pickup battery is the distance it takes to get there
        // (it travels along the x first, then the y), times the rate of travel
        Integer tDelta = (xDelta + yDelta) * this.baseSpeed;
        //moves the navigator to the battery module
        this.xPos = batt.xPos;
        this.yPos = batt.yPos;

        //prints the time it took for debugging
        System.out.println("the change in time is: " + tDelta);
        //returns the time that action took the system
        return tDelta;
    }

    public void reportStats(){
        System.out.println("REPORTING STATUS: " + "My current position is:  " + this.xPos + ", " + this.yPos);
    }

    //similar to pickup but for getting to the car with the new battery
    public Integer moveTo(Car c) {
        int xDelta = Math.abs(c.xPos - this.xPos);
        int yDelta = Math.abs(c.yPos - this.yPos);
        Integer tDelta = (xDelta + yDelta) * this.baseSpeed;
        this.xPos = c.xPos;
        this.yPos = c.yPos;

        //prints the time it took for debugging
        System.out.println("the change in time is: " + tDelta);
        //returns the time that action took the system
        return tDelta;
    }
}

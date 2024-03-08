public class Main {

    public static void main(String[] args) {
        Car car1 = new Car(8, 8, 50, 80);
        //Car car2 = new Car(3, 4, 30, 80);
        //Car car3 = new Car(7, 5, 20, 50);
        Navigator navigator1 = new Navigator(0, 0, 1, 3, true);
        Battery battery1 = new Battery(4, 4, 100, true);

        int t=0;
        t += navigator1.pickup(battery1);
        navigator1.reportStats();
        t += navigator1.moveTo(car1);
        navigator1.reportStats();
        System.out.println(t);
    }
}
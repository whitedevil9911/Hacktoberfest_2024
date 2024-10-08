import java.util.Scanner;

class Circle {
    double radius;
    
    Circle(double r) {
        this.radius = r;
    }
    
    double calculateArea() {
        return Math.PI * radius * radius;
    }
}

public class AreaOfCircle {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter the radius of the circle: ");
        double radius = sc.nextDouble();
        
        Circle circle = new Circle(radius);
        double area = circle.calculateArea();
        
        System.out.println("Area of the circle: " + area);
    }
}

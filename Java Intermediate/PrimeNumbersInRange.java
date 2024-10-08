import java.util.Scanner;

public class PrimeNumbersInRange {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter the lower bound: ");
        int low = sc.nextInt();
        System.out.print("Enter the upper bound: ");
        int high = sc.nextInt();

        for (int i = low; i <= high; i++) {
            if (isPrime(i)) {
                System.out.println(i + " is a prime number.");
            }
        }
    }

    public static boolean isPrime(int num) {
        if (num <= 1) return false;
        for (int i = 2; i <= Math.sqrt(num); i++) {
            if (num % i == 0) return false;
        }
        return true;
    }
}

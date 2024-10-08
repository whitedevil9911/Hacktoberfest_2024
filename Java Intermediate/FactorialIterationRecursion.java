import java.util.Scanner;

public class FactorialIterationRecursion {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter a number: ");
        int num = sc.nextInt();
        
        System.out.println("Factorial using iteration: " + factorialIterative(num));
        System.out.println("Factorial using recursion: " + factorialRecursive(num));
    }

    public static int factorialIterative(int n) {
        int result = 1;
        for (int i = 1; i <= n; i++) {
            result *= i;
        }
        return result;
    }

    public static int factorialRecursive(int n) {
        if (n == 0) return 1;
        return n * factorialRecursive(n - 1);
    }
}

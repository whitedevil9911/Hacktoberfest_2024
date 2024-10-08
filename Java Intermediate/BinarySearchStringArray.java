import java.util.Arrays;
import java.util.Scanner;

public class BinarySearchStringArray {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the size of the string array: ");
        int n = sc.nextInt();
        sc.nextLine();
        
        String[] arr = new String[n];
        System.out.println("Enter sorted strings:");
        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextLine();
        }
        
        System.out.print("Enter the string to search for: ");
        String key = sc.nextLine();
        
        int result = Arrays.binarySearch(arr, key);
        
        if (result >= 0) {
            System.out.println("String found at index: " + result);
        } else {
            System.out.println("String not found.");
        }
    }
}

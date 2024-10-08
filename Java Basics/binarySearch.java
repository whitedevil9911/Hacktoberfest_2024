import java.util.Scanner;

public class BinarySearch {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter the size of the array: ");
        int n = sc.nextInt();
        
        int[] arr = new int[n];
        System.out.println("Enter " + n + " sorted array elements:");
        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }
        
        System.out.print("Enter the element to search: ");
        int key = sc.nextInt();
        
        int result = binarySearch(arr, 0, n - 1, key);
        
        if (result == -1) {
            System.out.println("Element not found.");
        } else {
            System.out.println("Element found at index: " + result);
        }
    }
    
    public static int binarySearch(int[] arr, int low, int high, int key) {
        if (high >= low) {
            int mid = low + (high - low) / 2;
            
            // If the element is present at the middle
            if (arr[mid] == key) {
                return mid;
            }
            
            // If the element is smaller than mid, search the left subarray
            if (arr[mid] > key) {
                return binarySearch(arr, low, mid - 1, key);
            }
            
            // Else search the right subarray
            return binarySearch(arr, mid + 1, high, key);
        }
        
        // If the element is not present in the array
        return -1;
    }
}

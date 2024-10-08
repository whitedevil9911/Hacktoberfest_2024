import java.util.Scanner;

public class BubbleSortWithSwaps {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter the size of the array: ");
        int n = sc.nextInt();
        
        int[] arr = new int[n];
        System.out.println("Enter array elements:");
        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }
        
        int swaps = bubbleSort(arr);
        System.out.print("Sorted array: ");
        for (int i : arr) {
            System.out.print(i + " ");
        }
        System.out.println("\nNumber of swaps: " + swaps);
    }
    
    public static int bubbleSort(int[] arr) {
        int swaps = 0;
        for (int i = 0; i < arr.length - 1; i++) {
            for (int j = 0; j < arr.length - i - 1; j++) {
                if (arr[j] > arr[j + 1]) {
                    int temp = arr[j];
                    arr[j] = arr[j + 1];
                    arr[j + 1] = temp;
                    swaps++;
                }
            }
        }
        return swaps;
    }
}

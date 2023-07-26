import java.util.Scanner;

/**
 * LinearSearch
 */
public class LinearSearch {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int arr[] = { 1, 2, 4, 6, 11, 25, 34, 67, 69, 84 };
        System.out.println("Enter the number to be searched");
        int key = sc.nextInt();
        sc.close();
        int indx = linearSearch(arr, key);
        if (indx != -1) {
            System.out.println("Element found at index " + indx);
        } else {
            System.out.println("Element not found");
        }
    }

    static int linearSearch(int arr[], int key) {
        for (int i = 0; i <= arr.length; i++) {
            if (arr[i] == key) {
                return i;
            }
        }
        return -1;
    }
}
import java.util.Scanner;
public class BinarySearch {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int arr[] = { 1, 2, 4, 6, 11, 25, 34, 67, 69, 84 };
        System.out.println("Enter the number to be searched");
        int key = sc.nextInt();
        sc.close();
        int indx = binarySearch(arr, key);
        if (indx != -1) {
            System.out.println("Element found at index " + indx);
        } else {
            System.out.println("Element not found");
        }
    }

    static int binarySearch(int[] arr, int key) {
        int low = 0, highest = arr.length - 1, indx = 0;
        boolean flag = false;
        while (low <= highest) {
            int mid = (low + highest) / 2;
            if (arr[mid] < key) {
                low = mid + 1;
            } else if (arr[mid] > key) {
                highest = mid - 1;
            } else{
                flag = true;
                indx = mid;
                break;
            }
            if (!flag) {
                indx = -1;
            }
        }
        return indx;

    }
}

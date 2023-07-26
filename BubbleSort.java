public class BubbleSort {
    public static void main(String[] args) {
        int[] arr = { 1, 2, 34, 6, 46, 7, 56, 4, 1, 34, 64, 3, 4, 64, 7, 6, 4, 64, 7, 1, 3, 45, 67, 97, 46, 4, 4, 4, 3,
                6, 54, 5 };
        bubbleSort(arr);
        for (int k = 0; k < arr.length; k++) {
            System.out.println(arr[k]);
        }

    }

    static int[] bubbleSort(int[] arr) {
        for (int i = 0; i < arr.length; i++) {
            boolean sorted = true;
            for (int j = 0; j < arr.length - i - 1; j++) {

                if (arr[j] > arr[j + 1]) {
                    int temp = arr[j];
                    arr[j] = arr[j + 1];
                    arr[j + 1] = temp;
                    sorted = false;
                }
            }
            if (sorted) {
                break;
            }
        }
        return arr;

    }
}

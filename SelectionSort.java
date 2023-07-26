public class SelectionSort {
    public static void main(String[] args) {
        int[] arr = { 1, 2, 34, 6, 46, 7, 56, 4, 1, 34, 64, 3, 4, 64, 7, 6, 4, 64, 7, 1, 3, 45, 67, 97, 46, 4, 4, 4, 3,
                6, 54, 5 };
        selectionSort(arr);
        for (int k = 0; k < arr.length; k++) {
            System.out.print(arr[k] + " ");
        }
    }    
    public static int[] selectionSort(int[] arr) {
        int smallest = 0;
        for (int i = 0; i < arr.length-1; i++) {
            int index = i;
            for (int j = i+1; j < arr.length; j++) {
                if (arr[j] < arr[index]) {
                    index = j;
                }
            }
            smallest = arr[index];
            arr[index] = arr[i];
            arr[i] = smallest;
        }
        return arr;
    }
}

package Algorithms;
// find kth largest element in an array

import java.util.Arrays;

public class FindKthLargest {
    public static void main(String[] args) {
        int[] arr = { 1, 2, 3, 4, 5, 6, 7, 8 };
        int k = 3;
        System.out.println(kthLargest(arr, k));
    }

    public static int kthLargest(int[] arr, int k) {
        Arrays.sort(arr);
        return arr[arr.length - k];
    }
}
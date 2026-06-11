

import java.util.HashSet;

// Solution Class
class Solution {
    // Method to find the length of the longest common prefix among all pairs
    public int longestCommonPrefix(int[] arr1, int[] arr2) {
        // Initialize the hashset for the keeping the values
        HashSet<Integer> set = new HashSet<>();

        // Iterate over the arr1 to fill the set array
        for (int i = 0; i < arr1.length; i++) {
            // Add all the prefix of the current index of the arr1 untill it become zero
            while (arr1[i] != 0) {
                // If arr1[i] is in the set then break out of the loop
                if (set.contains(arr1[i])) {
                    break;
                }

                // Add the value to the set
                set.add(arr1[i]);

                // Update the number
                arr1[i] /= 10;
            }
        }

        // Initialize the longest common prefix varaible
        int longestCommonPrefix = 0;

        // Iterate over the arr2 to get the longest common prefix
        for (int i = 0; i < arr2.length; i++) {
            // Check all the prefix of teh current index of the arr2 untill it become zero
            while (arr2[i] != 0) {
                // If arr2[i] is in the set then check the length of the prefix and break out of
                // the loop
                if (set.contains(arr2[i])) {
                    // Initialize the length variable
                    int length = 0;

                    // Get the length of the arr2[i]
                    while (arr2[i] != 0) {
                        // Update the number
                        arr2[i] /= 10;

                        // Increment the length value
                        length++;
                    }

                    // Update the longest common prefix varaible
                    longestCommonPrefix = Math.max(longestCommonPrefix, length);

                    // Break out of the loop
                    break;
                }

                // Update the number
                arr2[i] /= 10;
            }
        }

        // Return the longest common prefix
        return longestCommonPrefix;
    }
}

public class _3043_Find_the_Length_of_the_Longest_Common_Prefix {
    // Main method to test longestCommonPrefix
    public static void main(String[] args) {
        int[] arr1 = new int[] { 1, 10, 100 };
        int[] arr2 = new int[] { 1000 };

        int result = new Solution().longestCommonPrefix(arr1, arr2);

        System.out.println("The length of the longest common prefix among all pairs is : " + result);
    }
}
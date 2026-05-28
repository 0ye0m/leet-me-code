class Solution {

    int[] dp;

    private int helper(int[] arr, int i, int d) {

        if (dp[i] != 0)
            return dp[i];

        int curr = 1;

        for (int j = i - 1; j >= Math.max(0, i - d); j--) {

            if (arr[j] >= arr[i])
                break;

            curr = Math.max(curr, 1 + helper(arr, j, d));
        }

        for (int j = i + 1; j <= Math.min(arr.length - 1, i + d); j++) {
            if (arr[j] >= arr[i])
                break;

            curr = Math.max(curr, 1 + helper(arr, j, d));
        }

        dp[i] = curr;

        return curr;
    }

    public int maxJumps(int[] arr, int d) {

        int n = arr.length;

        dp = new int[n];

        int result = 1;

        for (int i = 0; i < n; i++) {
            result = Math.max(result, helper(arr, i, d));
        }

        return result;
    }
}
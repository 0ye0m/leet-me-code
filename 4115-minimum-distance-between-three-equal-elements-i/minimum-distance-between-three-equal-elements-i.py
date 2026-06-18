class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        n=len(nums)
        dis=float('inf')
        for i in range(n-2):
            for j in range(i+1,n-1):
                if nums[i] != nums[j]:
                    continue
                for k in range(j+1,n):
                    if nums[i]==nums[j]==nums[k]:
                        dis=min((abs(i - j) + abs(j - k) + abs(k - i)),dis)
        if dis==float('inf'):
            return -1
        else:
            return dis                  



        
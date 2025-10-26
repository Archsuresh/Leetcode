class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        total_sum= int(n * (n+1)/2)
        list_sum=0
        for i in nums:
            list_sum +=i
        return total_sum - list_sum
        
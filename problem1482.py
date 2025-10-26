class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        if len(nums)<1:
            return []
        sum=0
        final_list=[]
        for i in range(len(nums)):
            sum=sum+nums[i]
            final_list.append(sum)
        return final_list
from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums)<1:
            return False
        aux_dict={}
        
        for i in range(len(nums)):
            if nums[i] in aux_dict:
                return aux_dict[nums[i]],i
            else:
                aux_dict[target-nums[i]]=i
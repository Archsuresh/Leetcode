from typing import List
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        merged_interval = []
        
        for interval in intervals:
            if not merged_interval or merged_interval[-1][1] < interval[0]:
                merged_interval.append(interval)
            else:
                merged_interval[-1][1] = max(merged_interval[-1][1],interval[1])
        return merged_interval
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        map={} #value:index

        for i,n in enumerate(nums):
            need= target-n

            if need in map:
                return [map[need],i]

            else:
                map[n]=i
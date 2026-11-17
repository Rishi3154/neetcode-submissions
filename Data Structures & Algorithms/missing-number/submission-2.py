class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        n =len(nums)
        actual=0

        expected = n*(n+1)//2
        
        for i in range(n):
            actual += nums[i]
        return expected-actual
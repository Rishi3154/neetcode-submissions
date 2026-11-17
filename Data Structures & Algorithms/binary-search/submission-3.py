class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left,right = 0,len(nums)-1

        while left<=right:
            mid = (right+left)//2
            if target==nums[mid]:
                return mid
            elif target>nums[mid]:
                left+=1
            else:
                right-=1
        return -1

        
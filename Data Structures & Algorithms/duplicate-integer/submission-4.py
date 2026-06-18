class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        hashset = set()

        for n in nums:

            if n in hashset:
                return True
            hashset.add(n)

        return False

        # check if the number is present in the created hash set, if yes 
        # then return true it contains duplicate else add that number to 
        # set.


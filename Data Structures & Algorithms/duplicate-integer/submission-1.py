class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #Brute force
        # nums.sort()
        # for i in range(len(nums) -1):
        #     if nums[i] == nums[i+1]:
        #         return True
        # return False   
        #You can't get both O(n) time and O(1) space for this problem.
        #Unordered set method 
        s=set() #Extra o(n) space
        for i in range(len(nums)):
            if nums[i] in s:
                return True
            else:
                s.add(nums[i])           
        return False
        
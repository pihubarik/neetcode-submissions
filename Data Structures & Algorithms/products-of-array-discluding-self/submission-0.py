class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        # res=[]
        # for i in range(n):
        #     prod=1
        #     for j in range(n):
        #         if i != j:
        #             prod *= nums[j]
        #     res.append(prod) 
        # return res    
        left = [1]*n
        right = [1]*n
        result= [1]*n
        for i in range(1,n):
            left[i] = left[i-1] * nums[i-1]
        for i in range(n-2,-1,-1):
            right[i]= right[i+1] * nums[i+1]
        for i in range(n):
            result[i] = left[i] * right[i]    
        return result                  

        
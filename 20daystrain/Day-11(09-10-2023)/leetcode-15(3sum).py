class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        tar=0
        res=[]
        nums.sort()
        for i in range(len(nums)):
            left=i+1
            right=len(nums)-1
            while left<right:
                if (nums[i]+nums[left]+nums[right])==tar and ([nums[i],nums[left],nums[right]]) not in res:
                    res.append([nums[i],nums[left],nums[right]])
                if (nums[i]+nums[left]+nums[right])<tar:
                    left+=1
                else:
                    right-=1
        return res

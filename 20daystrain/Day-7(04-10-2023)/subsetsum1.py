#Check subset sum by mam
def check_subset(nums,target):
    def backtrack(start,sum):
        if sum==target:
            return True
        if sum>target or start==len(nums):
            return False
        if backtrack(start+1,sum+nums[start]):
            subset.append(nums[start])
            return True
        return backtrack(start+1,sum)
    subset=[]
    if backtrack(0,0):
        return True, subset
    else:
        return False,[]
nums=[1,2,3,4,5]
target_sum=0
bool, subset=check_subset(nums,target_sum)
if bool:
    print("target sum exists")
else:
    print("target sum not exists")
    

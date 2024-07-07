nums = [1,6142,8192,10239]
target = 18431

def twoSum(nums, target):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i]+nums[j] == target:
                return [i,j]


print(twoSum(nums, target))
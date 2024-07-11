#SEE https://leetcode.com/problems/rearrange-array-elements-by-sign/

def rearrangeArray(nums):
    negative = []
    i = 0
    while len(negative) != len(nums):
        if nums[i] < 0:
            negative.append(nums[i])
            nums.pop(i)
            i -= 1
        i += 1
    for i in range(0, len(nums)*2, 2):
        nums.insert(i+1, negative[int(i/2)])
    return nums

def rearrangeArray2(nums):
    list1 = []
    list2 = []
    for i in nums:
        if i > 0:
            list1.append(i)
        else:
            list2.append(i)
    nums.clear()
    for i in range(0, len(list1)):
        nums.append(list1[i])
        nums.append(list2[i])
    return nums

nums = [-1,1]
print(rearrangeArray(nums))

#[3,-2,1,-5,2,-4]
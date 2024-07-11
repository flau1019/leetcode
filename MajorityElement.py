# SEE:https://leetcode.com/problems/majority-element/

def majorityElement(nums):
    #nums.sort()
    #return nums[int(len(nums)/2)]
    nums.sort()
    uniquenum = set(nums)
    numunique = []
    numunique2 = []
    for i in uniquenum:
        counter = 0
        for j in nums:
            if i == j:
                counter += 1
        numunique2.append(i)
        numunique.append(counter)  
    return numunique2[numunique.index(max(numunique))]  

print(majorityElement([3,2,3]))

def majorityElement2(nums: list) -> int:
    elements = {}
    for i in nums:
        if  i not in elements:
            elements[ i ] = 0
        elements[ i ] += 1
    s = 0
    i = 0
    for e in elements:
        if  elements[ e ] > s:
            s = elements[ e ]
            i = e
    return i

print( majorityElement2 ( [ 3, 2, 3 ] ) )

def test_majorityElement():
    assert majorityElement2([3,2,3]) == 3
    assert majorityElement2([2,2,1,1,1,2,2]) == 2

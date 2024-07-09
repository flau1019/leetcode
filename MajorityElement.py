def majorityElement(nums):
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
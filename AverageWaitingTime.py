# SEE: https://leetcode.com/problems/average-waiting-time/

def averageWaitingTime(customers) -> float:
    FinishTime = customers[0][0]
    TimeWaiting = []
    for i in customers:
        if i[0] > FinishTime:
            FinishTime = i[0] + i[1]
            TimeWaiting.append(i[1])
        else:
            FinishTime = FinishTime + i[1]
            TimeWaiting.append(FinishTime-i[0])    
    return sum(TimeWaiting)/len(TimeWaiting)

print(averageWaitingTime([[5,2],[5,4],[10,3],[20,1]]))
print(averageWaitingTime([[2,3],[6,3],[7,5],[11,3],[15,2],[18,1]]))
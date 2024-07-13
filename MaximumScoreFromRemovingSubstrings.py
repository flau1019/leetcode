def maximumGain(s, x, y):
    if y > x:
        s = s[::-1] 
    else:
        x, y = y, x
    temp = s
    while temp.count("ab") > 0:
        temp = temp.replace("ab", "")
    score = (len(s) - len(temp))//2 *y
    s = temp
    while temp.count("ba") > 0:
        temp = temp.replace("ba", "")
    score += (len(s) - len(temp))//2 *x
    return score

def maximumGain2(s, x, y):
    temp = s
    s1 = temp.count('ab')*x + temp.replace('ab', '').count('ba')*y
    s2 = temp.count('ba')*y + temp.replace('ba', '').count('ab')*x
    if s1 > s2:
        return s1
    else:
        return s2

print(maximumGain2("cdbcbbaaabab", 4, 5))
print(maximumGain2("aabbaaxyaabbb", 5, 4))
print(maximumGain2("aabbabkbbbfvybssbtaobaaaabataaadabbbmakgabbaoapbbbbobaabvqhbbzbbkapabaavbbeghacabamdpaaqbqabbjbababmbakbaabajabasaabbwabrbbaabbafubayaazbbbaababbaaha", 1926, 4320))

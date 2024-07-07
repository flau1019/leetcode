
def ispalindrome(x):
    x = list(str(x))
    for i in range(len(str(x))):
        if x[i] != x[len(str(x))-i-1]:
            return False
    return True

x = 0
print(ispalindrome(x))
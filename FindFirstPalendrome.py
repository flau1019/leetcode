# SEE: https://leetcode.com/problems/find-first-palindromic-string-in-the-array/

def firstPalindrome(words) -> str:
    for i in words:
        if i == i[::-1]:
            return i
    return ""

print( firstPalindrome(["abc","car","ada","racecar","cool"]))
print( firstPalindrome(["abc","car","racecar","ada","cool"]))
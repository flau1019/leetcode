def firstPalindrome(words) -> str:
    for i in words:
        if i == i[::-1]:
            return i
    return ""

print(firstPalindrome(["def","ghi"]))
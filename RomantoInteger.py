def romanToInt(s):
    roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    s = list(s)
    Total = 0
    i = 0
    while i < (len(s)):
        if i+1 < len(s) and roman[s[i+1]] > roman[s[i]]:
            Total += roman[s[i+1]]-roman[s[i]]
            i += 2  
        else:
            Total += roman[s[i]]
            i += 1
    return Total

print(romanToInt("MCMXCIV"))
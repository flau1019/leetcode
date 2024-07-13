# SEE: https://leetcode.com/problems/reverse-substrings-between-each-pair-of-parentheses/

def reverseParentheses(s):
    while s.count(")") > 0:
        position = 0
        for i in range(s.index(")")): 
            if s[s.index(")")-i-1] == "(":
                position = s.index(")")-i-1
                break
        s = s[0:position] + s[s.index(")")-1:position:-1] + s[s.index(")")+1:]
    return s

s = "(u(love)i)"
print(reverseParentheses(s))
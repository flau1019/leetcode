def isValid(s: str) -> bool:
    grid = []
    i = 0
    counter = 0
    while i < len(s):
        if s[i] == "(" or s[i] == "[" or s[i] == "{":   # s[i] in {'(', '[', '{'}:
            grid.append(s[i])
            i += 1
        elif s[i] == ")" or s[i] == "]" or s[i] == "}": # s[i] in {')', ']', '}'}:
            if len(grid) == 0:
                return False
            else:
                if grid[len(grid)-1] == "(" and s[i] == ")":
                    grid.pop(len(grid)-1)
                    i += 1
                    counter += 1
                elif grid[len(grid)-1] == "[" and s[i] == "]":
                    grid.pop(len(grid)-1)
                    i += 1            
                    counter += 1   
                elif grid[len(grid)-1] == "{" and s[i] == "}":
                    grid.pop(len(grid)-1)
                    i += 1    
                    counter += 1
                else:
                    return False
    if counter == len(s)/2:
        return True
    else: 
        return False

def is_valid(s: str) -> bool:
    stack: list[str] = []

    for c in s:
        if  c   in "({[":
            stack.append( c )
        elif  c   in ")}]":
            if  len(stack) == 0:
                return False
            else:
                d = stack.pop()
                if  c == ')' and not d == '(':
                    return False
                elif  c == ']' and not d == '[':
                    return False
                elif  c == '}' and not d == '{':
                    return False
    return  len(stack) == 0

s = "(([]){})"
print(isValid(s))


def test_is_valid():
    assert is_valid("()")           == True
    assert is_valid("[]")           == True
    assert is_valid("{}")           == True
    assert is_valid("{[]}")         == True
    assert is_valid("()[]{}")       == True
    assert is_valid("({[]})")       == True
    assert is_valid("[({})]")       == True
    assert is_valid("{[()]}")       == True
    assert is_valid("{a[b(c)d]e}")  == True
    
    assert is_valid("(]")     == False
    assert is_valid("([)]")   == False
    assert is_valid("]")      == False
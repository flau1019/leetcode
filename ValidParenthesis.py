def isValid(s: str) -> bool:
    grid = []
    i = 0
    j = 0 
    counter = 0
    while i < len(s):
        if s[i] == "(" or s[i] == "[" or s[i] == "{":
            grid.append(s[i])
            i += 1
        elif s[i] == ")" or s[i] == "]" or s[i] == "}":
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

s = "(([]){})"
print(isValid(s))

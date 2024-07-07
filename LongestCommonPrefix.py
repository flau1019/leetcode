def longestCommonPrefix(strs):
    min_len = min([len(e) for e in strs])
    prefix = ''
    for i in range(0, min_len):
        prev = None
        for e in strs:
            if prev:
                if prev[i] != e[i]:
                    return prefix
            else:
                prev = e
        prefix += prev[i]
    return prefix

s = [""]
print(longestCommonPrefix(s))
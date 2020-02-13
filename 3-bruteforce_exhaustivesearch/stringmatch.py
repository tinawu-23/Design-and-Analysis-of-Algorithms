## String Pattern Matching ##

# Time: O(mn) worst case; O(m+n) avg case
# Space: O(1) 

def match(text, pattern):
    for i in range(0, len(text)-len(pattern)):
        j = 0
        while j < len(pattern) and text[i+j]==pattern[j]:
            j += 1
        if j == len(pattern):
            return i
    return -1

print(match('somebirdsarenotmeanttobecaged', 'bird'))
print(match('somebirdsarenotmeanttobecaged', 'meag'))

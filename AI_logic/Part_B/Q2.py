"""
Given two strings s and t, return the shortest contiguous substring of s that contains all characters of t including duplicates.
If no such substring exists, return an empty string "". The answer is guaranteed to be unique when it exists.
"""

from collections import Counter
def minWindow(s:str, t:str):
    if not s or not t or len(s) < len(t):
        return ""
    
    # maintain count of all unique char in t 
    dict_t = Counter(t)
    required = len(dict_t)

    # dict to count char in current window
    window_count = {}
    formed = 0 
    ans = float('inf'), None,  None
    left =0
    for right in range(len(s)):
        character = s[right]
        window_count[character] = window_count.get(character, 0) +1

        #if freq of current char match with required freq 
        if character in dict_t and window_count[character] == dict_t[character]:
            formed +=1
        
        while left <= right and formed== required:
            character = s[left]
            
            if right - left +1 < ans[0]:
                ans = (right - left + 1, left, right)
            
            # check char at the left pointer 
            window_count[character] -=1
            if character in dict_t and window_count[character] < dict_t[character]:
                formed -=1

            left += 1
    return "" if ans[0] == float('inf') else s[ans[1]:ans[2] + 1]




# Open Test Cases 

s1 = "ADOBECODEBANC" # combinations = ADOBEC, DOBECODEBA, OBECODEBA, BECODEBA, ECODEBAN, CODEBA, ODEBANC, DEBANC, EBANC, BANC(sortest)
t1 = "ABC"            #Output: "BANC"
 
s2 = "a"  
t2 = "a"     # Output: "a"

print(minWindow(s1, t1))
print(minWindow(s2, t2))
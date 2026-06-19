"""
Given a string s of distinct lowercase characters, return a list of all possible permutations of s.
You must implement the permutation generation from scratch using backtracking.
Use of any built-in permutation library functions (e.g., itertools.permutations) is NOT allowed.
The output list may be returned in any order.
"""

def permutations(s):
    result = []
    
    # defining helper fucntion 
    def backtrack(current, pending):
        if not pending:
          result.append(current)
          return

        # checking each char
        for i in range(len(pending)):
             backtrack(current+ pending[i], pending[:i]+ pending[i+1:])
    backtrack("", s)
    return result



# Open test cases 
s1 = "abc"
s2 = "ab"

print(permutations(s1))
print(permutations(s2))
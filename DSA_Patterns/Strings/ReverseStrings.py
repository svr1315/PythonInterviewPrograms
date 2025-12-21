"""Write a function that reverses a string. The input string is given as an array of characters s.
You must do this by modifying the input array in-place with O(1) extra memory.
Example 1:
Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]

Example 2:
Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
"""
"""Time Complexity-O(n), Space Complexity-O(1)"""
class ReverseString:
    def revStr(self, s:list[int])->None:
        l=0
        r=len(s)-1
        while l<r:
            s[l],s[r]=s[r],s[l]
            l+=1
            r-=1
        return s
rs=ReverseString()
print(rs.revStr(["h","e","l","l","o"]))
print(rs.revStr(["H","a","n","n","a","h"]))
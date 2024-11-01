"""verifying whether a string is substring of another string"""
"""Time complexity-O(n), Space complexity-O(1)"""

class Solution:
    def isSubsequence(self, smallerString: str, largerString:str) -> bool:
        i,j=0,0
        while i<len(smallerString) and j<len(largerString):
            if(smallerString[i]==largerString[j]):
                i+=1;
                j+=1;
            j+=1
        return True if i==len(smallerString) else False 
    
s=Solution()
print(s.isSubsequence("abc", "adbfc"))
print(s.isSubsequence("axc", "adbfc"))
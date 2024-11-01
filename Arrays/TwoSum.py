
"""If any two numbers in the input array sum up to the target sum, 
below function should return those numbers in a array"""
"""Time complexity-O(n), Space complexity-O(n)"""

def twoNumberSum(array, targetSum):
   hashMap={}
   for i, n in enumerate(array):
       diff=targetSum-n
       if diff in hashMap:
           return [diff, n]
       hashMap[n]=i
   return []

print(twoNumberSum([3, 5, -4, 8, 11, 1, -1, 6],10))
print(twoNumberSum([],10))
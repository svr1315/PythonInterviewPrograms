"""Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order"""
#time complexity->O(n),space complexity-O(n)
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen={}
        for i, num in enumerate(nums):
            complement=target-num
            if complement in seen:
                return [seen[complement], i]
            seen[num]=i
        return []

s=Solution()
print(s.twoSum([1,2,5,7],6))
print(s.twoSum([2,7,11,15], 9))
print(s.twoSum([3,2,4], 6))
print(s.twoSum([3,3], 6))
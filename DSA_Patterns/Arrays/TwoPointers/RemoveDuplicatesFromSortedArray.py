#26. Remove Duplicates from Sorted Array
"""Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same.
Then return the number of unique elements in nums."""
# time complexity-O(n), space compleity-O(1)
class Solution:
    def removeDuplicates(self, nums:list[int])->int:
        l=1
        for r in range(1,len(nums)):
            if nums[r]!=nums[r-1]:
                nums[l]=nums[r]
                l+=1
        return l
s=Solution()
print(s.removeDuplicates([1,1,2]))
print(s.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))
print(s.removeDuplicates([1,2,3]))
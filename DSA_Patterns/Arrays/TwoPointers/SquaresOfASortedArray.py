"""leetcode #977 : Given an integer array nums sorted
in non-decreasing order, return an array of the
squares of each number sorted in non-decreasing order."""
# time complexity-O(n), space compleity-O(n)
class Solution:
    def sortedSquares(self, nums: list[int])-> list[int]:
        result=[]
        l,r=0,len(nums)-1
        while l<=r:
            if nums[l]*nums[l]>nums[r]*nums[r]:
                result.append(nums[l]*nums[l])
                l+=1
            else:
                result.append(nums[r] * nums[r])
                r-=1
        return result[::-1] #reverse
s=Solution()
print(s.sortedSquares([-4,-1,0,3,10]))
print(s.sortedSquares([-7,-3,2,3,11]))
print(s.sortedSquares([-5,-4,-2,-1]))
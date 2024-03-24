class Solution(object):
    def removeDuplicates(self, nums):
        counter = 0
        i = 0 
        while i < len(nums)-2:           

            if nums[i] != nums[i+2]:
                i = i + 1
            else:
                del nums[i+1]
                counter +=1 
class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums)
        for i in range(len(nums)):
            if target == nums[i]:
                return 1
        
        binary = 1
        mid = len(nums)//2 
        first = 0
        last = len(nums)-1
        while binary == 1 :
            if first+2 == last :
                binary = 0
                closest = first
            if target > nums[mid] : 
                first = nums[mid] 
            else :
                last = mid 
            mid = (last+first)//2
            print(f"{first},{mid},{last}")
        
list = [2,3,1,2,4,3]
list-s =[1,2,2,3,3,4]
targ = 7
s = Solution()
s.minSubArrayLen(targ,list)


        
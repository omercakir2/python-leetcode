class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        res = len(nums)+1
        currentSum = 0
        l = 0 
        for index,value in enumerate(nums):
            currentSum += value
            while currentSum >= target:
                res = min(res,index-l+1)
                currentSum -= nums[l]
                l +=1

        returnval = res % (len(nums)+1)
        return returnval
list = [2,3,1,2,4,3]
lists =[1,2,2,3,3,4]
targ = 7
s = Solution()
s.minSubArrayLen(targ,list)


        
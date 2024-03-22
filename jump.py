class Solution(object):
    def canJump(self,nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        result = self.helper(self,0,len(nums)-1,nums)
        print(result)
        return result
    def helper(self,i,j,nums):
        if i + nums[i] >= j :
            return True
        else:
            #k = i
            for k in range(i+1,nums[i]+i,1) :
                if self.helper(self,i,k,nums) and self.helper(self,k,j,nums):
                    return True
            return False
        


#list1 = [3,2,1,0,4]
list2 = [2,3,1,1,4]
list3 = [1,2,3]
s = Solution
Solution.canJump(s,list2)
#Solution.canJump(list2)

        

            

# using recursive , some cases it's not efficient
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
            for k in range(i+1,nums[i]+i+1,1) :
                if self.helper(self,i,k,nums) and self.helper(self,k,j,nums):
                    return True
            return False
        


list1 = [3,2,1,0,4]
list2 = [2,3,1,1,4]
list3 = [2,0,6,9,8,4,5,0,8,9,1,2,9,6,8,8,0,6,3,1,2,2,1,2,6,5,3,1,2,2,6,4,2,4,3,0,0,0,3,8,2,4,0,1,2,0,1,4,6,5,8,0,7,9,3,4,6,6,5,8,9,3,4,3,7,0,4,9,0,9,8,4,3,0,7,7,1,9,1,9,4,9,0,1,9,5,7,7,1,5,8,2,8,2,6,8,2,2,7,5,1,7,9,6]
s = Solution
Solution.canJump(s,list3)
#Solution.canJump(list2)

        

            

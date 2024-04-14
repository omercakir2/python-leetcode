class Solution(object):    
    def recurs(self,lst,start,counter):
        if start == 0 :
            return counter
        stp = start
        for i in range(start,-1,-1):
            if lst[i] >= start-i:
                stp = i 
        start = stp
        counter +=1 
        return self.recurs(lst,start,counter)
    def jump(self, nums):
        cnt = 0
        return self.recurs(nums,len(nums)-1,cnt)
        
    


list=[
    2,3,1,1,4,3
]
s = Solution()
print(s.jump(list))
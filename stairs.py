class Solution:
    # How many different ways there are to reach the top of the stairs 
    def climbStairs(self,target : int):
        res = []
        options = [1,2,3] # List of options the person take 1,2,or 3 steps
        def _climbStairs(arr : list):   
            if sum(arr)==target:
                res.append(arr[:])
                return
            elif sum(arr) > target:
                return

            for i in options:
                arr.append(i)
                _climbStairs(arr)
                arr.pop()
        _climbStairs([])
        return res
s = Solution()
res = s.climbStairs(5)
print(res)
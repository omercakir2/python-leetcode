class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        cursub,maxsub = "" , ""
        x , y = 0 , 1
        while y < len(s)-1:
            for i in range(0,len(cursub),1):
                if s[y] == cursub[i]:
                    x = i + 1
                    if len(cursub) > len(maxsub):
                        maxsub = cursub
                        cursub = ""
                else : 
                    cursub += y
            y +=1 
        return len(maxsub)

    
                

        

a = 'abcabccsdd'
s = Solution()
s.lengthOfLongestSubstring(a)
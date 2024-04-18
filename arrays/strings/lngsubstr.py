class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        cursub = ""
        maxsub = ""
        x,y = 0, 0 
        
        for index,char in enumerate(s):
            cursub += char
            if char in cursub:
                if len(cursub) > len(maxsub):
                    maxsub = cursub

                cursub = cursub.replace(char,'')
        return len(maxsub)
                

        

a = 'abcabccsdd'
s = Solution()
s.lengthOfLongestSubstring(a)
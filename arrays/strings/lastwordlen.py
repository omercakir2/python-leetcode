class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        leng = len(s)
        x = 0
        for i in range(leng-1,-1,-1):
            if s[i]!=' ':
                for k in range(i,-1,-1):
                    if s[k]==' ':
                        break
                    else:
                        x+=1
                break
        return x



            
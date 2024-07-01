# Assuming that lenght of s and t are the same 

class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dicti={}
        for i in range(0,len(s),1):
            if s[i] in dicti:
                if dicti[s[i]]!=t[i]:
                    return False
            else:
                if t[i] not in dicti.values():
                    dicti[s[i]]=t[i]
                else:
                    return False
        return True

        
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        minlen = 200
        if len(strs)==1:
            return (strs[0])
        for k in range(len(strs)):
            if (strs[k])=="":
                return ""
            else:
                if len((strs)[k])<minlen:
                    minlen= len((strs)[k])
        returnval=""
        for i in range(minlen): # This "i" indicates which index is going to be checked
            x = (strs[0])[i]
            for j in range(1,len(strs),1):# This "j" is gonna represent which string is going to be checked         
                
                if (strs[j])[i]!=x:
                    return returnval
                    
            returnval+=x
        return returnval
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        hash1={}
        hash2={}
        for i in range(0,len(s),1):
            if s[i] in hash1:
                hash1[s[i]] += 1
            else:
                hash1[s[i]] = 1
        for k in range(0,len(t),1):
            if t[k] in hash2:
                hash2[t[k]] += 1
            else:
                hash2[t[k]] = 1
        if len(hash1)!=len(hash2):
            return False         
        for j in hash1.keys():
            if hash1.get(j)!=hash2.get(j):
                return False
        return True
                 
        
fstr="omer"
sstr="emre"
s = Solution()
x =s.isAnagram(fstr,sstr)
print(x)
class Solution(object):
    def canConstruct(self,ransomNote,magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        :checks whether first string can be constructed from
        the letters in string2 
        """
        hash_map1 = {}
        hash_map2 = {}
        for char in ransomNote:
            hash_map1[char] = hash_map1.get(char, 0) + 1
        #print(hash_map1)
        for cchar in magazine:
            hash_map2[char] = hash_map2.get(cchar,0) + 1

         


str1 ="bg"            
str2 = "bfaassbbdsc"
sol = Solution()
sol.canConstruct(str1,str2)


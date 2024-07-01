class Solution(object):
    def get_words(self, s):
        """
        :type s: str
        :rtype: list
        """
        arr=[]
        element=''
        for i in range(len(s)):
            if s[i]==' ' :
                arr.append(element)
                element=''
            else:
                element+=s[i]
        arr.append(element)
        return arr
    def wordPattern(self,pattern,s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool 
        """
        elements = self.get_words(s)
        if len(elements) != len(pattern):
            return False
        hashmap={}
        for i in range(len(elements)):
            if pattern[i] in hashmap:
                if hashmap[pattern[i]]!=elements[i]:
                    return False
            else:
                if elements[i] not in hashmap.values():
                    hashmap[pattern[i]]=elements[i]
                else:
                    return False
        return True
        
patt = "abba"        
t = "dog cat cat fish"
s = Solution()
result = s.wordPattern(patt,t)
print(result)



        
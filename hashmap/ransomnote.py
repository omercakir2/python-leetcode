class Solution(object):
    def canConstruct(self,ransomNote,magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        :checks whether first string can be constructed from
        the letters in string2 
        """
        var = 0
        pointer = 0
        founded = []
        for i in range(len(ransomNote)):
            while pointer < len(magazine):
                if magazine[pointer] == ransomNote[i] and pointer not in founded:
                    var +=1
                    founded.append(pointer)
                    break
                pointer+=1
                
            pointer = 0
                    
        if var == len(ransomNote):
            print("True")
            return True
        print("False")
        return False
str1 , str2 = "bg" , "efjbdfbdgfjhhaiigfhbaejahgfbbgbjagbddfgdiaigdadhcfcj"
s = Solution()
s.canConstruct(str1,str2)


    
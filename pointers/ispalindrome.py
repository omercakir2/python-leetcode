# if a text doesnt change when you reading it from th end , it is a palindrome
class Solution(object):
    def isPalindrome(self, s):
        return Solution.test(self,Solution.lower_and_stick(self,s))
    def lower_and_stick(self,string):
        lowercase_version , sticked_vers, finalvers = "" ,"",""
        
        for char in string:
            if 'A' <= char <= 'Z': # if a char is uppercase , we change it this way
                lowercase_char = chr(ord(char)+32)
            else:
                lowercase_char = char
            lowercase_version += lowercase_char

        for char in lowercase_version:
            if char != ' ':
                sticked_vers += char 
        for char in sticked_vers:
            if char.isalnum():
                finalvers += char

        return finalvers
    def test(self,arr):
        palindrome = True
        if arr == " ":
            return palindrome
        for i, j in zip(range(0, len(arr) - 1, 1), range(len(arr) - 1, -1, -1)):
            if arr[i] != arr[j]:
                palindrome = False
        print(palindrome)
        return palindrome
            
text = "A man, a plan, a canal: Panama"
Solution.isPalindrome(Solution,text)
            

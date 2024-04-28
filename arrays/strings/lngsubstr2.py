#This is the version powered by chatgpt , 
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        if len(s) < 1:
            return 0
        
        char_index = {}  # Dictionary to store the index of each character
        max_len = 0
        start = 0
        
        for end in range(len(s)):
            if s[end] in char_index and char_index[s[end]] >= start:
                start = char_index[s[end]] + 1
                
            char_index[s[end]] = end
            max_len = max(max_len, end - start + 1)
        
        return max_len

ss = Solution()
a = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~ abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
print(ss.lengthOfLongestSubstring(a))

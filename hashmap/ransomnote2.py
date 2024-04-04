class Solution(object):
    def canConstruct(self, ransomNote, magazine):
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
            hash_map1[char] = hash_map1.get(char, 0) + 1 # mapping the letter in a dic

        for cchar in magazine:
            hash_map2[cchar] = hash_map2.get(cchar, 0) + 1

        for k in ransomNote:
            if hash_map1[k] > hash_map2.get(k, 0):  # Use get() to avoid KeyError
                return False

        return True  # Return True after checking all characters

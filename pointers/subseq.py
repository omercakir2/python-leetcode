class Solution(object):
    def isSubsequence(self,s,t):
        var = 0
        note = -1
        for i in range(len(s)):
            for j in range(len(t)):
                if s[i] == t[j] and note < j:
                    var +=1 
                    note = j
                    break

        if len(s) == var :
            return True
        else:
            return False

a , b = "ab" , "baab"
print(Solution.isSubsequence(Solution,a,b))

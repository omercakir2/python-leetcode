# we're using a last in first out method here
# because we have to check the last index of the array each time 
class Solution(object):
    def isValid(self,s):
        stack = list() #note to myself ; it's same with stack = []
        # we're gonna record every open bracket onto stack
        for i in s:
            if i in '([{': 
                stack.append(i)
            else: #that means we encounter a closing bracket and we need to check if it has its openning or not
                if not stack or \
                    (i==')' and stack[-1]!='(') or\
                    (i==']' and stack[-1]!='[') or\
                    (i=='}' and stack[-1]!='{'):
                    return False # if it has no openning at the end of the list that means this bracket cant be closed
                stack.pop() 
        return not stack



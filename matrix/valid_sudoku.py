class Solution(object):
    def has_unique_numbers(self,lst):
        for i in range(len(lst)):
            for j in range(i + 1, len(lst)):
                if lst[i] == lst[j] and lst[i] != "." and lst[j] != ".":
                    return False
        return True
    def isValidSudoku(self,board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        check1 , check2 , check3 = False ,False ,False
        for i in range(9):
            arr = list(board[i])
            if self.has_unique_numbers(arr) == False:
                print("it's not valid")
                return False
        check1 = True
            
        for j in range (9):
            for m in range(9):
                verticallist = []
                verticallist.append((board[m])[j])
                if self.has_unique_numbers(verticallist) == False:
                    print("it's not valid")
                    return False
            verticallist = []
        check2 = True
        for k in range(0,9,3):
            for h in range(0,9,3):
                if self.has_unique_numbers((board[j])[m]) == False:
                    print("it's not valid")
                    return False
        check3 = True
        if check1 and check2 and check3 == True:
            print("its valid")
            return True
        else:
            print("it's not valid")
            return False



board1 = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
Solution.isValidSudoku(Solution,board1)
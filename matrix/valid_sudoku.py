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
        #check1 , check2 , check3 = False ,False ,False
        for i in range(9):
            arr = list(board[i])
            if self.has_unique_numbers(arr) == False:
                print("it's not valid")
                return False
            
        for j in range (9):
            verticallist = []
            for m in range(9):
                verticallist.append((board[m])[j])
            if self.has_unique_numbers(verticallist) == False:
                print("it's not valid")
                return False
        print("its valid")
        return True
            
        
        



board1 = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
solution_instance = Solution()  # Create an instance of Solution
solution_instance.isValidSudoku(board1)
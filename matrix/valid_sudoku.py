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
        for i in range(9): # checking the list from left to right (horizontaly)
            arr = list(board[i])
            if self.has_unique_numbers(arr) == False:
                print("it's not valid")
                return False
            
        for j in range (9): # checking the list from top to bottom (verticaly)
            verticallist = []
            for m in range(9):
                verticallist.append((board[m])[j])
            if self.has_unique_numbers(verticallist) == False:
                print("it's not valid")
                return False
        for hor in range(0,7,3):
            for ver in range(0,7,3):
                liste = []
                for hora in range(hor,hor+3,1):
                    for vert in range(ver,ver+3,1):
                        liste.append((board[hora])[vert])
                if self.has_unique_numbers(liste) == False:
                    print("its not valid")
                    return False
                    



        print("its valid")
        return True
    
            
        
        



board1 = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
solution_instance = Solution()  # Create an instance of Solution
solution_instance.isValidSudoku(board1)
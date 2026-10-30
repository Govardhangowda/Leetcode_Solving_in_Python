class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        
        for i in range(9):
            row=set();
            for j in range(9):
                if(board[i][j]=="."):
                    continue;
                if(board[i][j] in row):
                    return False;
                else:
                    row.add(board[i][j]);

        for k in range(9):
            column=set();
            for l in range(9):
                if(board[l][k]=="."):
                    continue;
                if(board[l][k] in column):
                    return False;
                else:
                    column.add(board[l][k]);

        for box_row in range(0,9,3):
            for box_column in range(0,9,3):
                box=set();
                for r in range(box_row,box_row + 3):
                    for c in range(box_column, box_column+3):
                        if(board[r][c]=="."):
                            continue;
                        if(board[r][c] in box):
                            return False;
                        box.add(board[r][c]);
            

        return True;
                

def generate_possible_moves(board:[str,str], player: str):
    
    empty_array = []
    b_array = []
    w_array = []

    
    for i,valuei in enumerate(board):
        for j, valuej in enumerate(valuei):
            if valuej == "W":
                cor = [i,j]
                w_array.append(cor)
            if valuej == "B":
                cor = [i,j]
                b_array.append(cor)  
            if valuej == ".":
                cor = [i,j]
                empty_array.append(cor) 
    moves = []

    for each in empty_array:
        if player=="B":
            if afxazuri(w_array, each):
                moves.append([each[0],each[1]]) 
        else:
            if afxazuri2(b_array,each):
                moves.append([each[0],each[1]])   
                
    return moves

    
def afxazuri(w_array: [int,int], each: []):
    if [each[0]+1,each[1]+1] in w_array or [each[0], each[1]+1] in w_array or [each[0]+1,each[1]] in w_array or [each[0]-1,each[1]] in w_array or [each[0],each[1]-1] in w_array or [each[0]+1,each[1]-1] in w_array or [each[0]-1,each[1]+1] in w_array or [each[0]-1,each[1]-1] in w_array:
        return True      
def afxazuri2(b_array: [int,int], each: []):
    if [each[0]+1,each[1]+1] in b_array or [each[0], each[1]+1] in b_array or [each[0],each[1]-1] in b_array or [each[0]+1,each[1]] in b_array or [each[0]+1,each[1]-1] in b_array or [each[0]-1,each[1]] in b_array or [each[0]-1,each[1]+1] in b_array or [each[0]-1,each[1]-1] in b_array or [each[0]+1,each[1]+1] in b_array:           
            return True
def file_info (filename:str):
    with open(filename, 'r', encoding='utf8') as f:
        data = f.read()
        d = data.split()
        horiz = len((data.partition('\n')[0]).split())
        vertic = int(len(d)/horiz)
        array = []
        for i in range(len(d)):
            if i %horiz == 0:
                sub = d[i:i+horiz]
                lst = []
                for j in sub:
                    lst.append(j)
                array.append(lst)     
        dimension = [horiz, vertic]        
         
    return array, dimension

def dumbothello(filename : str) -> tuple[int,int,int]:
    
    tree = []
    array, dimension = file_info(filename)
    list = generate_game_tree(dimension, array, tree, "B")
   
    countw = 0
    countb = 0
    countww = 0
    countbw = 0
    countpre = 0
    for i in range(len(list)):
        for j in range(len(list[i])):
            countw += list[i][j].count('W')
            countb += list[i][j].count('B')

        if countw > countb:
            countww +=1
        if countw < countb:
            countbw += 1
        if countw == countb:
            countpre += 1
        countw = 0
        countb = 0
    return (countbw,countww,countpre)
    pass

def generate_game_tree(dimension: [int], board:[str,str], game_tree: [str,str], player: str) -> [str,str]:

    array = generate_possible_moves(board, player)
    if not array:
        game_tree.append(board)
        return game_tree

    valid_moves = []
    for i in range(len(board)):
        for j in range(len(board[0])):
            if [i,j] in array:
                valid_moves.append((i, j))
                


    for move in valid_moves:

        new_board = [row[:] for row in board]

        make_move(dimension,new_board, move[0], move[1], player)

        generate_game_tree(dimension, new_board, game_tree, 'B' if player == 'W' else 'W')

    return game_tree


def capture_in_direction(dimension: [int], board: [str,str], row: int, col: int, player: str, row_offset: int, col_offset: int) -> [[str,str]]:

    curr_row = row + row_offset
    curr_col = col + col_offset

    
    if curr_row < 0 or curr_row >= dimension[1] or curr_col < 0 or curr_col >= dimension[0] or board[curr_row][curr_col] == '.':
        return board

    if board[curr_row][curr_col] != player:
        
        board[curr_row][curr_col] = player
    
    return 
    
        
def make_move(dimension: [int], board: [str,str], row: int, col: int, player: str) -> None:
    

    board[row][col] = player
    capture_in_direction(dimension,board, row, col, player, -1, -1)
    capture_in_direction(dimension,board, row, col, player, -1, 0)
    capture_in_direction(dimension,board, row, col, player, -1, 1)
    capture_in_direction(dimension,board, row, col, player, 0, -1)
    capture_in_direction(dimension,board, row, col, player, 0, 1)
    capture_in_direction(dimension,board, row, col, player, 1, -1)
    capture_in_direction(dimension,board, row, col, player, 1, 0)
    capture_in_direction(dimension,board, row, col, player, 1, 1)

    return 





# LeetCode: 1275. Find Winner on a Tic Tac Toe Game

def tictactoe(moves: [[int]]) -> str:
    
    player = ''
    board = [['' for _ in range(3)] for _ in range(3)]
    st = set()
    pflag = False

    for i in range(len(moves)):
        if i%2 == 0:
            player = 'A'
        else:
            player = 'B'
        
        r = moves[i][0]
        c = moves[i][1]

        board[r][c] = player
    
    for r in board:
        print(r)

    #-- check all rows
    for r in board:
        st = set(r)
        if '' in st:
            pflag = True
        elif len(st) == 1:
            return st.pop()
     
    #-- check all columns
    for j in range(len(board)):
        c = [board[i][j] for i in range(len(board))]
        st = set(c)
        if '' in st:
            pflag = True
        elif len(st) == 1:
            return st.pop()
    
    #-- check forward diag
    d = [board[i][i] for i in range(len(board))]
    st = set(d)
    if '' in st:
        pflag = True
    elif len(st) == 1:
        return st.pop()

    d.clear()

    #-- check backward diag
    i = len(board) - 1
    for j in range(len(board)):  #-- check all columns
        d.append(board[i][j])
        i -= 1
    st = set(d)
    if '' in st:
        pflag = True
    elif len(st) == 1:
        return st.pop()

    if pflag:
        return 'Pending'

    return 'Draw'

moves = [[0,0],[2,0],[1,1],[2,1],[2,2]]
#moves = [[0,0],[1,1],[0,1],[0,2],[1,0],[2,0]]
#moves = [[0,0],[1,1],[2,0],[1,0],[1,2],[2,1],[0,1],[0,2],[2,2]]
moves = [[0,0],[1,1]]
print(tictactoe(moves))

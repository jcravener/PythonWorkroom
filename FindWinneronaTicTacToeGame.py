

# LeetCode: 1275. Find Winner on a Tic Tac Toe Game

def tictactoe(moves: [[int]]) -> str:
    
    player = ''
    board = [['' for _ in range(3)] for _ in range(3)]

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

    return None

moves = [[0,0],[2,0],[1,1],[2,1],[2,2]]
moves = [[0,0],[1,1],[0,1],[0,2],[1,0],[2,0]]
moves = [[0,0],[1,1],[2,0],[1,0],[1,2],[2,1],[0,1],[0,2],[2,2]]
print(tictactoe(moves))

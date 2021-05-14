"""
Tic Tac Toe Player
"""

import math
import copy
X = "X"
O = "O"
EMPTY = None

def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """

    x_plays = 0
    o_plays = 0
    for row in board:
        for cell in row:
            x_plays += 1 if cell == X else 0
            o_plays += 1 if cell == O else 0

    if x_plays > o_plays:
        return O
    return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """

    possible_actions = set()
    for row_index in range(0, 3):
        for column_index in range(0, 3):
            try:
                if board[row_index][column_index] == EMPTY:
                    if board[row_index][column_index] == []:
                        raise Exception("Bug here!")
                    possible_actions.add((row_index, column_index))
            except:
                pass
    return possible_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """

    turn = player(board)
    if terminal(board):
        return utility(board)
    if board[action[0]][action[1]]  != EMPTY:
        print(action)
        raise Exception("Invalid action!\nThis cell has already been taken!")

    d_b = copy.deepcopy(board)

    d_b[action[0]][action[1]] = player(board)

    return d_b

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    row1_column1 = board[0][0]
    row1_column2 = board[0][1]
    row1_column3 = board[0][2]

    row2_column1 = board[1][0]
    row2_column2 = board[1][1]
    row2_column3 = board[1][2]

    row3_column1 = board[2][0]
    row3_column2 = board[2][1]
    row3_column3 = board[2][2]

    if row1_column1 == X:
        if row1_column2 == X and row1_column3 == X:
            return X
        if row2_column1 == X and row3_column1 == X:
            return X
        if row2_column2 == X and row3_column3 == X:
            return X
        else:
            pass
    else:
        pass
    if row1_column2 == X:
        if row2_column2 == X and row3_column2 == X:
            return X
        else:
            pass
    else:
        pass
        
    if row1_column3 == X:
        if row2_column3 == X and row3_column3 == X:
            return X
        if row2_column2 == X and row3_column1 == X:
            return X
        else:
            pass
    else:
        pass
        
    if row2_column1 == X:
        if row2_column2 == X and row2_column3 == X:
            return X

    if row3_column1 == X:
        if row3_column2 == X and row3_column3 == X:
            return X
        else:
            pass
    else:
        pass

    
    if row1_column1 == O:
        if row1_column2 == O and row1_column3 == O:
            return O
        if row2_column1 == O and row3_column1 == O:
            return O
        if row2_column2 == O and row3_column3 == O:
            return O
        else:
            pass
    else:
        pass
        
    if row1_column2 == O:
        if row2_column2 == O and row3_column2 == O:
            return O
        
    if row1_column3 == O:
        if row2_column3 == O and row3_column3 == O:
            return O
        if row2_column2 == O and row3_column1 == O:
            return O
        else:
            pass
    else:
        pass
    if row2_column1 == O:
        if row2_column2 == O and row2_column3 == O:
            return O
        else:
            pass
    else:
        pass

    if row3_column1 == O:
        if row3_column2 == O and row3_column3 == O:
            return O
        else:
            pass
    else:
        pass
    
    return None

def terminal(board):
    if winner(board) != None:
        return True
    if board == [[EMPTY, EMPTY, EMPTY],
                [EMPTY, EMPTY, EMPTY],
                [EMPTY, EMPTY, EMPTY]]:
                return False
    empty_counter = 0
    for row in board:
        for column in row:
            if column == EMPTY:
                empty_counter += 1
                break
    if empty_counter == 0:
        return True
    return False

def utility(board):
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0

def min_val(board):
    if terminal(board):
        return utility(board)
    v = 2
    for action in actions(board):
        v = min(v, max_val(result(board, action)))
    return v

def max_val(board):
    if terminal(board):
        return utility(board)
    v = -2
    for action in actions(board):
        v = max(v, min_val(result(board, action)))
    return v

def num_columns_filled(board):
    counter = 0
    for row in board:
        for column in row:
            if column != EMPTY:
                counter += 1
    return counter

def minimax(board):
    if terminal(board):
        return None

    if player(board) == O:
        best_move = []
        moves = actions(board)
        smallest = 2
        if board[1][1] == EMPTY:
            return (1, 1)




        for action in moves:
            d_b = result(board, action)

            if terminal(d_b):
                return action


            for act in actions(d_b):
                sub_d_b = result(d_b, act)

                if terminal(sub_d_b):
                    return act

            mini_val = min_val(board)

            if mini_val <= smallest:
                best_move = action
                smallest = mini_val
        return best_move
    else:
        best_move = []
        moves = actions(board)
        smallest = -2


        if board[1][1] == EMPTY:
            return (1, 1)



        for action in moves:
            d_b = result(board, action)

            if terminal(d_b):
                return action

            for act in actions(d_b):
                sub_d_b = result(d_b, act)

                if terminal(sub_d_b):
                    return act

            mini_val = max_val(board)

            if mini_val >= smallest:
                best_move = action
                smallest = mini_val
        return best_move


"""
def initial_state():
    #Returns starting state of the board.
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    #Returns player who has the next turn on a board.
    
    x_plays = 0
    o_plays = 0
    for row in board:
        for cell in row:
            if cell == X:
                x_plays += 1
            if cell == O:
                o_plays += 1
    if x_plays == o_plays:
        return X
    else:
        return O


def actions(board):
    #Returns set of all possible actions (i, j) available on the board.
    
    moves = []
    row_index = 0
    for row in board:
        column_index = 0
        for cell in row:
            if cell == EMPTY:
                moves.append([row_index, column_index])
            column_index += 1
        row_index += 1
    return moves


def result(boardk, action):
    #Returns the board that results from making move (i, j) on the board.
    
    turn = player(boardk)
    m = copy.deepcopy(boardk)
    if turn == X:
        m[action[0]][action[1]] = X
    else:
        m[action[0]][action[1]] = O
    return m

def winner(board):
    #Returns the winner of the game, if there is one.
    raise NotImplementedError


def who_win(board):
    row1_column1 = board[0][0]
    row1_column2 = board[0][1]
    row1_column3 = board[0][2]

    row2_column1 = board[1][0]
    row2_column2 = board[1][1]
    row2_column3 = board[1][2]

    row3_column1 = board[2][0]
    row3_column2 = board[2][1]
    row3_column3 = board[2][2]

    if row1_column1 == X:
        if row1_column2 == X and row1_column3 == X:
            return 1
        if row2_column1 == X and row3_column1 == X:
            return 1
        if row2_column2 == X and row3_column3 == X:
            return 1
        else:
            pass
    else:
        pass
    if row1_column2 == X:
        if row2_column2 == X and row3_column2 == X:
            return 1
        else:
            pass
    else:
        pass
        
    if row1_column3 == X:
        if row2_column3 == X and row3_column3 == X:
            return 1
        if row2_column2 == X and row3_column1 == X:
            return 1
        else:
            pass
    else:
        pass
        
    if row2_column1 == X:
        if row2_column2 == X and row2_column3 == X:
            return 1

    if row3_column1 == X:
        if row3_column2 == X and row3_column3 == X:
            return 1
        else:
            pass
    else:
        pass

    
    if row1_column1 == O:
        if row1_column2 == O and row1_column3 == O:
            return -1
        if row2_column1 == O and row3_column1 == O:
            return -1
        if row2_column2 == O and row3_column3 == O:
            return -1
        else:
            pass
    else:
        pass
        
    if row1_column2 == O:
        if row2_column2 == O and row3_column2 == O:
            return -1
        
    if row1_column3 == O:
        if row2_column3 == O and row3_column3 == O:
            return -1
        if row2_column2 == O and row3_column1 == O:
            return -1
        else:
            pass
    else:
        pass
    if row2_column1 == O:
        if row2_column2 == O and row2_column3 == O:
            return -1
        else:
            pass
    else:
        pass

    if row3_column1 == O:
        if row3_column2 == O and row3_column3 == O:
            return -1
        else:
            pass
    else:
        pass
    
    return 0

def terminal(board):
    #Returns True if game is over, False otherwise.
   
    win = who_win(board)
    if win == 1 or win == -1:
        return True
    return False


def utility(board):
    #Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    
    return who_win(board)

def max_val(board):
    if terminal(board):
        return utility(board)
    v = -2
    for action in actions(board):
        v = max(v, min_val(result(board, action)))
    return v

def min_val(board):
    if terminal(board):
        return utility(board)
    v = 2
    for action in actions(board):
        v = min(v, max_val(result(board, action)))
    return v

def minimax(b):
    #Returns the optimal action for the current player on the board.

    best_action = max_val(b)
    print("move:", best_action[0])
    return best_action[0]


    possibilities = actions(b)
    action_value = []
    for action in possibilities:
        d_b = copy.deepcopy(result(b, action))
        min_v = max_val(d_b)
        action_value.append([action, min_v])
    print(action_value)
    
    best_move = action_value[0][0]
    greatest = action_value[0][1]
    for p in action_value:
        if p[1] < greatest:
            greatest = p[1]
            best_move = p[0]
    print(best_move)
    raise NotImplementedError
"""
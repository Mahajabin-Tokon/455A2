# Cmput 455 sample code
# Boolean Negamax
# Written by Martin Mueller

import time
#from game_basics import colorAsString, isBlackWhite, opponent
# import gtp_connection
from board_util import GoBoardUtil 
from board import GoBoard 
from gtp_connection import GtpConnection

def negamaxBoolean(self):
    if self.endOfGame():
        return self.staticallyEvaluateForToPlay()
    legal_moves = GoBoardUtil.generate_legal_moves(self.board, self.board.current_player)
    board_copy: GoBoard = self.board.copy()
    for m in legal_moves:
        can_play_move = board_copy.play_move(m, self.board.current_player)
        if can_play_move:
            success = not negamaxBoolean(board_copy)
        # board_copy.undoMove()
        if success:
            return True
    return False

def negamaxBooleanSolveAll(self):
    if self.endOfGame():
        return self.staticallyEvaluateForToPlay()
    wins = []
    legal_moves = GoBoardUtil.generate_legal_moves(self.board, self.board.current_player)
    board_copy: GoBoard = self.board.copy()
    for m in legal_moves:
        can_play_move = board_copy.play_move(m, self.board.current_player)
        if can_play_move:
            success = not negamaxBoolean(board_copy)
        #  board_copy.undoMove()
        if success:
            wins.append(m)
    return wins

def solveForColor(self, color): 
# use for 3-outcome games such as TicTacToe
    #assert isBlackWhite(color)
    #saveOldDrawWinner = state.drawWinner
    # to check if color can win, count all draws as win for opponent
    #state.setDrawWinner(opponent(color)) 
    # start = time.process_time()
    winForToPlay = negamaxBoolean()
    # timeUsed = time.process_time() - start
    #state.setDrawWinner(saveOldDrawWinner)
    winForColor = winForToPlay == (color == self.board.current_player)
    return winForColor # timeUsed

# def solveForBlack(self): 
#     # Need to check the time used here
#     win = False
#     start = time.process_time()
#     if self.board.current_player == BLACK:
#         win = minimaxBooleanOR()
#     else:
#         win = minimaxBooleanAND()
#     # timeUsed = time.process_time() - start
#     return win, timeUsed

def timed_solve(state): 
    start = time.process_time()
    wins = negamaxBooleanSolveAll(state)
    timeUsed = time.process_time() - start
    return wins, timeUsed

# def solveForWinLossDraw(state):
#     winBlack, timeBlack = solveForColor(state, self.bo)
#     if winBlack:
#         return BLACK, (timeBlack, -1)
#     else:
#         winner = EMPTY
#         winWhite, timeWhite = solveForColor(state, WHITE)
#         if winWhite:
#             winner = WHITE
#         return winner, (timeBlack, timeWhite)
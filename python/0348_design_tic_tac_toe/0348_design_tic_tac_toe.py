from typing import List, Optional

"""
LeetCode Design Tic-Tac-Toe

Problem from LeetCode: https://leetcode.com/problems/design-tic-tac-toe/

Description:
Design a Tic-tac-toe game that is played between two players on an n x n grid.
You may assume the following rules:
1. A move is guaranteed to be valid and is placed on an empty block.
2. Once a winning condition is reached, no more moves are allowed.
3. A player who succeeds in placing n of their marks in a horizontal, vertical, or diagonal row wins the game.

Example:
Input: ["TicTacToe", "move", "move", "move", "move", "move", "move", "move"]
[[3], [0, 0, 1], [0, 2, 2], [2, 2, 1], [1, 1, 2], [2, 0, 1], [1, 0, 2], [2, 1, 1]]
Output: [null, 0, 0, 0, 0, 0, 0, 1]

Explanation:
TicTacToe ticTacToe = new TicTacToe(3);
ticTacToe.move(0, 0, 1); // return 0 (no one wins)
ticTacToe.move(0, 2, 2); // return 0 (no one wins)
ticTacToe.move(2, 2, 1); // return 0 (no one wins)
ticTacToe.move(1, 1, 2); // return 0 (no one wins)
ticTacToe.move(2, 0, 1); // return 0 (no one wins)
ticTacToe.move(1, 0, 2); // return 0 (no one wins)
ticTacToe.move(2, 1, 1); // return 1 (player 1 wins)

Constraints:
- 2 <= n <= 100
- player is 1 or 2
- 0 <= row, col < n
- (row, col) are unique for each different call to move.
- At most n^2 calls will be made to move.

Follow-up: Could you do better than O(n^2) per move() operation?
"""

class TicTacToe:
    """
    Design a Tic-tac-toe game that is played between two players on an n x n grid.
    
    The game should be optimized for constant-time win checking, without 
    requiring checking the entire board after each move.
    """

    def __init__(self, n: int):
        """
        Initialize the TicTacToe game with an n x n board.
        
        Args:
            n: Size of the board (n x n)
        """
        self.rows = [0] * n
        self.cols = [0] * n
        self.diagonal = 0
        self.anti_diagonal = 0
        self.size = n

    def move(self, row: int, col: int, player: int) ->int:
        """
        Player makes a move at position (row, col).
        
        Args:
            row: The row of the board (0-indexed)
            col: The column of the board (0-indexed)
            player: The player, can be either 1 or 2
            
        Returns:
            int: The current winning condition:
                 0: No one wins
                 1: Player 1 wins
                 2: Player 2 wins
        """
        player_value = 1 if player == 1 else -1
        self.rows[row] += player_value
        self.cols[col] += player_value
        if row == col:
            self.diagonal += player_value
        if row + col == self.size - 1:
            self.anti_diagonal += player_value
        if abs(self.rows[row]) == self.size or abs(self.cols[col]
            ) == self.size or abs(self.diagonal) == self.size or abs(self.
            anti_diagonal) == self.size:
            return player
        return 0


    class TicTacToeGrid:

        def __init__(self, n: int):
            self.n = n
            self.board = [([0] * n) for _ in range(n)]

        def move(self, row: int, col: int, player: int) ->int:
            self.board[row][col] = player
            if all(self.board[row][j] == player for j in range(self.n)):
                return player
            if all(self.board[i][col] == player for i in range(self.n)):
                return player
            if row == col and all(self.board[i][i] == player for i in range
                (self.n)):
                return player
            if row + col == self.n - 1 and all(self.board[i][self.n - 1 - i
                ] == player for i in range(self.n)):
                return player
            return 0

if __name__ == '__main__':
    # Example usage based on LeetCode sample
    ticTacToe = TicTacToe(3)
    
    # Simulate a game
    moves = [
        (0, 0, 1),  # Player 1 at (0,0)
        (0, 2, 2),  # Player 2 at (0,2)
        (2, 2, 1),  # Player 1 at (2,2)
        (1, 1, 2),  # Player 2 at (1,1)
        (2, 0, 1),  # Player 1 at (2,0)
        (1, 0, 2),  # Player 2 at (1,0)
        (2, 1, 1),  # Player 1 at (2,1) - should win
    ]
    
    print("TicTacToe Game with 3x3 board:")
    for i, (row, col, player) in enumerate(moves):
        result = ticTacToe.move(row, col, player)
        print(f"Move {i+1}: Player {player} at ({row},{col}) - Result: {result}")
        if result != 0:
            print(f"Player {result} wins!")
            break

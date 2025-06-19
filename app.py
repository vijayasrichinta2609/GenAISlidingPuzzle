from flask import Flask, render_template, jsonify, request
import random
import json

app = Flask(__name__)

class SlidingPuzzle:
    def __init__(self, size=3):
        self.size = size
        self.board = self.create_solved_board()
        self.empty_pos = (size - 1, size - 1)  # Bottom right corner
        
    def create_solved_board(self):
        """Create a solved puzzle board"""
        board = []
        num = 1
        for i in range(self.size):
            row = []
            for j in range(self.size):
                if i == self.size - 1 and j == self.size - 1:
                    row.append(0)  # Empty space
                else:
                    row.append(num)
                    num += 1
            board.append(row)
        return board
    
    def shuffle(self, moves=100):
        """Shuffle the puzzle by making random valid moves"""
        for _ in range(moves):
            possible_moves = self.get_possible_moves()
            if possible_moves:
                move = random.choice(possible_moves)
                self.move_tile(move[0], move[1])
    
    def get_possible_moves(self):
        """Get all possible moves (adjacent tiles to empty space)"""
        empty_row, empty_col = self.empty_pos
        moves = []
        
        # Check all four directions
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for dr, dc in directions:
            new_row, new_col = empty_row + dr, empty_col + dc
            if 0 <= new_row < self.size and 0 <= new_col < self.size:
                moves.append((new_row, new_col))
        
        return moves
    
    def move_tile(self, row, col):
        """Move a tile to the empty space if possible"""
        empty_row, empty_col = self.empty_pos
        
        # Check if the tile is adjacent to empty space
        if abs(row - empty_row) + abs(col - empty_col) == 1:
            # Swap tile with empty space
            self.board[empty_row][empty_col] = self.board[row][col]
            self.board[row][col] = 0
            self.empty_pos = (row, col)
            return True
        return False
    
    def is_solved(self):
        """Check if the puzzle is solved"""
        solved_board = self.create_solved_board()
        return self.board == solved_board
    
    def get_board_state(self):
        """Get current board state"""
        return {
            'board': self.board,
            'empty_pos': self.empty_pos,
            'is_solved': self.is_solved(),
            'size': self.size
        }

# Global puzzle instance
puzzle = SlidingPuzzle(3)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/new_game', methods=['POST'])
def new_game():
    global puzzle
    data = request.get_json()
    size = data.get('size', 3)
    puzzle = SlidingPuzzle(size)
    puzzle.shuffle()
    return jsonify(puzzle.get_board_state())

@app.route('/api/move', methods=['POST'])
def move_tile():
    global puzzle
    data = request.get_json()
    row = data.get('row')
    col = data.get('col')
    
    if puzzle.move_tile(row, col):
        return jsonify({
            'success': True,
            'board_state': puzzle.get_board_state()
        })
    else:
        return jsonify({
            'success': False,
            'message': 'Invalid move'
        })

@app.route('/api/state')
def get_state():
    return jsonify(puzzle.get_board_state())

if __name__ == '__main__':
    puzzle.shuffle()  # Start with a shuffled puzzle
    app.run(debug=True, port=5000)

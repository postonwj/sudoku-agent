import random
import copy
import sys

class SudokuAgent:
    def __init__(self):
        self.size = 9
        self.box_size = 3

    def generate_full_solution(self):
        """Generates a full board with randomized valid structure."""
        base = 3
        side = base * base
        
        def pattern(r, c): return (base * (r % base) + r // base + c) % side
        def shuffle(s): return random.sample(s, len(s))
        
        r_base = range(base)
        rows = [g * base + r for g in shuffle(r_base) for r in shuffle(r_base)]
        cols = [g * base + c for g in shuffle(r_base) for c in shuffle(r_base)]
        nums = shuffle(range(1, side + 1))
        
        board = [[nums[pattern(r, c)] for c in cols] for r in rows]
        return board


    def is_valid(self, board, row, col, num):
        for i in range(9):
            if board[row][i] == num or board[i][col] == num:
                return False

        box_row = row - row % 3
        box_col = col - col % 3

        for i in range(3):
            for j in range(3):
                if board[box_row + i][box_col + j] == num:
                    return False

        return True

    def solve(self, board):
        """Standard backtracking solver."""
        for row in range(9):
            for col in range(9):
                if board[row][col] == 0:
                    for num in range(1, 10):
                        if self.is_valid(board, row, col, num):
                            board[row][col] = num
                            if self.solve(board):
                                return True
                            board[row][col] = 0
                    return False
        return True

    def count_solutions(self, board, limit=2):
        """Backtracking-based solution counter (stops early if > limit)."""
        def _count(board, count):
            if count[0] >= limit:
                return
            for row in range(9):
                for col in range(9):
                    if board[row][col] == 0:
                        for num in range(1, 10):
                            if self.is_valid(board, row, col, num):
                                board[row][col] = num
                                _count(board, count)
                                board[row][col] = 0
                        return
            count[0] += 1

        count = [0]
        _count(copy.deepcopy(board), count)
        return count[0]

    def generate_unique_puzzle(self, difficulty='medium'):
        full_board = self.generate_full_solution()
        puzzle = copy.deepcopy(full_board)

        # Difficulty presets
        target_empty = {
            'easy': 36,
            'medium': 46,
            'hard': 56
        }.get(difficulty, 46)

        # Coordinates of all cells, shuffled
        positions = [(r, c) for r in range(9) for c in range(9)]
        random.shuffle(positions)

        removed = 0
        for row, col in positions:
            if removed >= target_empty:
                break

            backup = puzzle[row][col]
            puzzle[row][col] = 0

            # Check uniqueness
            solutions = self.count_solutions(puzzle, limit=2)
            if solutions != 1:
                puzzle[row][col] = backup
            else:
                removed += 1

        return puzzle, full_board

    def display_board(self, board):
        for i, row in enumerate(board):
            print(' '.join(str(num) if num != 0 else '.' for num in row))
            if i in [2, 5]:
                print("-" * 17)

if __name__ == "__main__":
    agent = SudokuAgent()
    diff = input("Choose difficulty (easy, medium, hard): ").strip().lower()
    puzzle, solution = agent.generate_unique_puzzle(diff)

    print("\nGenerated Puzzle:\n")
    agent.display_board(puzzle)

    view = input("\nShow solution? (y/n): ").strip().lower()
    if view == 'y':
        print("\nSolution:\n")
        agent.display_board(solution)

    save_pdf = input("\nSave puzzle to PDF? (y/n): ").strip().lower()
    if save_pdf == 'y':
        from render_pdf import render_puzzle_to_pdf
        render_puzzle_to_pdf(puzzle)


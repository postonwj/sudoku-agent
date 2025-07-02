from sudoku_agent import SudokuAgent
from batch_render import render_puzzles_to_pdf

agent = SudokuAgent()
count = 12  # you can set to 60, 120, etc.
difficulty = 'medium'

puzzles = []
for _ in range(count):
    puzzle, _ = agent.generate_unique_puzzle(difficulty)
    puzzles.append(puzzle)

render_puzzles_to_pdf(puzzles, difficulty_label=difficulty.capitalize())


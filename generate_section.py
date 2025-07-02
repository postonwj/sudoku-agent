import sys
from sudoku_agent import SudokuAgent
from batch_render import render_booklet, render_puzzles_to_pdf

def main():
    if len(sys.argv) == 4:
        try:
            pages = int(sys.argv[1])
        except ValueError:
            print("Error: number of pages must be an integer.")
            sys.exit(1)
        difficulty = sys.argv[2].lower()
        if difficulty not in ('easy', 'medium', 'hard'):
            print("Error: difficulty must be 'easy', 'medium', or 'hard'.")
            sys.exit(1)
        include_solutions = sys.argv[3].lower() == 'y'
    else:
        pages = int(input("Enter number of pages to generate: "))
        difficulty = input("Enter difficulty (easy, medium, hard): ").lower()
        include_solutions = input("Include solutions? (y/n): ").lower() == 'y'

    total_puzzles = pages * 6  # 6 puzzles per page
    print(f"Generating {total_puzzles} {difficulty} puzzles...")

    agent = SudokuAgent()
    puzzles = []
    solutions = []

    for i in range(total_puzzles):
        puzzle, solution = agent.generate_unique_puzzle(difficulty)
        puzzles.append(puzzle)
        solutions.append(solution)
        if (i + 1) % 6 == 0:
            print(f"Generated {(i + 1) // 6} pages so far...")

    filename = f"sudoku_{difficulty}_section.pdf"
    if include_solutions:
        print("Rendering puzzles and solutions to PDF...")
        render_booklet(puzzles, solutions, filename=filename, difficulty_label=difficulty.capitalize())
    else:
        print("Rendering puzzles to PDF...")
        render_puzzles_to_pdf(puzzles, filename=filename, difficulty_label=difficulty.capitalize())

    print("Done!")

if __name__ == "__main__":
    main()

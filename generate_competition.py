from sudoku_agent import SudokuAgent
from render_competition import render_competition_sheet

def main():
    agent = SudokuAgent()

    difficulty = input("Difficulty? (easy, medium, hard): ").strip().lower()
    label = input("Label for header (e.g. 'Challenge 3'): ").strip()
    filename = f"sudoku_challenge_{label.lower().replace(' ', '_')}.pdf"

    print("Generating puzzle...")
    puzzle, solution = agent.generate_unique_puzzle(difficulty)

    print("Rendering PDF...")
    render_competition_sheet(puzzle, solution, filename=filename, label=label)

if __name__ == "__main__":
    main()

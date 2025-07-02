import subprocess
import sys

def generate_section(pages, difficulty, include_solutions):
    # Adjust total puzzles = pages * 6 puzzles per page
    total_puzzles = pages * 6
    cmd = [
        sys.executable,
        "generate_section.py",
        str(pages),
        difficulty,
        "y" if include_solutions else "n"
    ]
    print(f"Running command: {' '.join(cmd)}")
    result = subprocess.run(cmd, capture_output=True, text=True)
    print(result.stdout)
    if result.returncode != 0:
        print("Error:", result.stderr)
    else:
        print("Puzzle generation complete.")

if __name__ == "__main__":
    # For manual testing
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("pages", type=int)
    parser.add_argument("difficulty", type=str)
    parser.add_argument("solutions", type=str)
    args = parser.parse_args()
    generate_section(args.pages, args.difficulty, args.solutions.lower() == "y")

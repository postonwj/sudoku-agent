from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

CELL_SIZE = 40
GRID_SIZE = CELL_SIZE * 9
MARGIN = 50

def draw_sudoku_board(c, puzzle, x_offset, y_offset):
    # Draw cells and numbers
    for row in range(9):
        for col in range(9):
            x = x_offset + col * CELL_SIZE
            y = y_offset + (8 - row) * CELL_SIZE

            c.setStrokeColor(colors.black)
            c.setLineWidth(0.5)
            c.rect(x, y, CELL_SIZE, CELL_SIZE)

            num = puzzle[row][col]
            if num != 0:
                c.setFont("Helvetica", 14)
                c.drawCentredString(x + CELL_SIZE/2, y + CELL_SIZE/2 - 5, str(num))

    # Draw thicker lines every 3 boxes (internal 3x3 box grid)
    c.setLineWidth(2)
    for i in range(0, 10):
        line_x = x_offset + i * CELL_SIZE
        line_y = y_offset + i * CELL_SIZE

        if i % 3 == 0:
            # Vertical thick lines
            c.line(line_x, y_offset, line_x, y_offset + GRID_SIZE)
            # Horizontal thick lines
            c.line(x_offset, y_offset + i * CELL_SIZE, x_offset + GRID_SIZE, y_offset + i * CELL_SIZE)

    # Bold outer border
    c.setLineWidth(4)
    c.rect(x_offset, y_offset, GRID_SIZE, GRID_SIZE)

def render_puzzle_to_pdf(puzzle, output_path="sudoku_puzzle.pdf"):
    c = canvas.Canvas(output_path, pagesize=letter)
    page_width, page_height = letter

    x_offset = (page_width - GRID_SIZE) / 2
    y_offset = (page_height - GRID_SIZE) / 2

    draw_sudoku_board(c, puzzle, x_offset, y_offset)
    c.save()

    print(f"✅ Puzzle saved to: {output_path}")

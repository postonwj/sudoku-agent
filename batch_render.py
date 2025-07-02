from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

CELL_SIZE = 25
GRID_SIZE = CELL_SIZE * 9
PADDING = 20
MARGIN_X = 36
MARGIN_Y = 36
from reportlab.lib.pagesizes import letter

def draw_board(c, puzzle, x_offset, y_offset):
    for row in range(9):
        for col in range(9):
            x = x_offset + col * CELL_SIZE
            y = y_offset + (8 - row) * CELL_SIZE

            c.setLineWidth(0.5)
            c.rect(x, y, CELL_SIZE, CELL_SIZE)

            num = puzzle[row][col]
            if num != 0:
                c.setFont("Helvetica-Bold", 10)
                c.drawCentredString(x + CELL_SIZE/2, y + CELL_SIZE/2 - 3, str(num))

    c.setLineWidth(1.5)
    for i in range(10):
        if i % 3 == 0:
            c.line(x_offset + i*CELL_SIZE, y_offset, x_offset + i*CELL_SIZE, y_offset + GRID_SIZE)
            c.line(x_offset, y_offset + i*CELL_SIZE, x_offset + GRID_SIZE, y_offset + i*CELL_SIZE)

    c.setLineWidth(3)
    c.rect(x_offset, y_offset, GRID_SIZE, GRID_SIZE)

def layout_puzzles(c, puzzles, difficulty_label):
    page_width, page_height = letter

    # Calculate width of puzzle area (2 grids + 1 padding space)
    puzzle_area_width = (2 * GRID_SIZE) + PADDING
    puzzle_area_start_x = MARGIN_X

    # Center the label within the puzzle grid area
    center_x = puzzle_area_start_x + puzzle_area_width / 2
    c.setFont("Helvetica-Bold", 16)
    c.drawCentredString(center_x, page_height - 30, difficulty_label)

    positions = [
        (0, 2),
        (1, 2),
        (0, 1),
        (1, 1),
        (0, 0),
        (1, 0),
    ]

    for i, puzzle in enumerate(puzzles):
        col, row = positions[i]
        x = MARGIN_X + col * (GRID_SIZE + PADDING)
        y = MARGIN_Y + row * (GRID_SIZE + PADDING)
        draw_board(c, puzzle, x, y)


def render_puzzles_to_pdf(puzzles, filename="puzzles.pdf", difficulty_label="Medium"):
    c = canvas.Canvas(filename, pagesize=letter)

    for i in range(0, len(puzzles), 6):
        batch = puzzles[i:i+6]
        layout_puzzles(c, batch, difficulty_label)
        c.showPage()

    c.save()
    print(f"✅ Saved {len(puzzles)} puzzles to {filename}")

def render_booklet(puzzles, solutions, filename="booklet.pdf", difficulty_label="Medium"):
    c = canvas.Canvas(filename, pagesize=letter)

    # Render puzzles
    for i in range(0, len(puzzles), 6):
        batch = puzzles[i:i+6]
        layout_puzzles(c, batch, difficulty_label)
        c.showPage()

    # Render solutions
    for i in range(0, len(solutions), 6):
        batch = solutions[i:i+6]
        layout_puzzles(c, batch, difficulty_label + " Solutions")
        c.showPage()

    c.save()
    print(f"✅ Saved booklet to {filename}")



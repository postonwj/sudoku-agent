from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

from render_pdf import draw_board  # reuse existing draw_board logic

def render_competition_sheet(puzzle, solution, filename="competition_sheet.pdf", label="Sudoku Challenge"):
    page_width, page_height = letter
    c = canvas.Canvas(filename, pagesize=letter)

    positions = [
        (36, 450),       # top-left
        (310, 450),      # top-right
        (36, 60),        # bottom-left
        (310, 60),       # bottom-right
    ]

    # Front side: 4 identical puzzles
    c.setFont("Helvetica-Bold", 16)
    c.drawCentredString(page_width / 2, page_height - 40, label)

    for x, y in positions:
        draw_board(c, puzzle, x, y)

    c.showPage()

    # Back side: 4 identical solutions
    c.setFont("Helvetica-Bold", 16)
    c.drawCentredString(page_width / 2, page_height - 40, label + " — Solution")

    for x, y in positions:
        draw_board(c, solution, x, y)

    c.save()
    print(f"✅ Competition sheet saved to {filename}")

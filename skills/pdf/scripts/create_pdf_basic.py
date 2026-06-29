import sys

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas


def main():
    if len(sys.argv) != 2:
        print("Usage: create_pdf_basic.py <output.pdf>")
        sys.exit(1)
    c = canvas.Canvas(sys.argv[1], pagesize=letter)
    width, height = letter
    c.drawString(100, height - 100, "Hello World!")
    c.drawString(100, height - 120, "This is a PDF created with reportlab")
    c.line(100, height - 140, 400, height - 140)
    c.save()
    print(f"Created {sys.argv[1]}")


if __name__ == "__main__":
    main()

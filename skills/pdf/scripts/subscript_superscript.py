import sys

from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph, SimpleDocTemplate


def main():
    if len(sys.argv) != 2:
        print("Usage: subscript_superscript.py <output.pdf>")
        sys.exit(1)
    doc = SimpleDocTemplate(sys.argv[1], pagesize=letter)
    styles = getSampleStyleSheet()
    story = []
    chemical = Paragraph("H<sub>2</sub>O", styles['Normal'])
    story.append(chemical)
    squared = Paragraph("x<super>2</super> + y<super>2</super>", styles['Normal'])
    story.append(squared)
    doc.build(story)
    print(f"Created {sys.argv[1]} with subscript/superscript")


if __name__ == "__main__":
    main()

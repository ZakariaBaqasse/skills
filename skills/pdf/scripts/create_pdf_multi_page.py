import sys

from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak


def main():
    if len(sys.argv) != 2:
        print("Usage: create_pdf_multi_page.py <output.pdf>")
        sys.exit(1)
    doc = SimpleDocTemplate(sys.argv[1], pagesize=letter)
    styles = getSampleStyleSheet()
    story = []
    title = Paragraph("Report Title", styles['Title'])
    story.append(title)
    story.append(Spacer(1, 12))
    body = Paragraph("This is the body of the report. " * 20, styles['Normal'])
    story.append(body)
    story.append(PageBreak())
    story.append(Paragraph("Page 2", styles['Heading1']))
    story.append(Paragraph("Content for page 2", styles['Normal']))
    doc.build(story)
    print(f"Created multi-page PDF {sys.argv[1]}")


if __name__ == "__main__":
    main()

import sys
from pypdf import PdfWriter, PdfReader


def main():
    if len(sys.argv) < 3:
        print("Usage: merge_pdfs.py <output.pdf> <input1.pdf> [input2.pdf ...]")
        sys.exit(1)
    writer = PdfWriter()
    for pdf_file in sys.argv[2:]:
        reader = PdfReader(pdf_file)
        for page in reader.pages:
            writer.add_page(page)
    with open(sys.argv[1], "wb") as output:
        writer.write(output)
    print(f"Merged {len(sys.argv) - 2} PDFs into {sys.argv[1]}")


if __name__ == "__main__":
    main()

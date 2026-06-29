import sys
from pypdf import PdfReader, PdfWriter


def main():
    if len(sys.argv) != 2:
        print("Usage: split_pdf.py <input.pdf>")
        sys.exit(1)
    reader = PdfReader(sys.argv[1])
    for i, page in enumerate(reader.pages):
        writer = PdfWriter()
        writer.add_page(page)
        with open(f"page_{i+1}.pdf", "wb") as output:
            writer.write(output)
    print(f"Split {sys.argv[1]} into {len(reader.pages)} pages")


if __name__ == "__main__":
    main()

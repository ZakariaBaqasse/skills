import sys
from pypdf import PdfReader, PdfWriter


def main():
    if len(sys.argv) != 4:
        print("Usage: add_watermark.py <input.pdf> <watermark.pdf> <output.pdf>")
        sys.exit(1)
    watermark = PdfReader(sys.argv[2]).pages[0]
    reader = PdfReader(sys.argv[1])
    writer = PdfWriter()
    for page in reader.pages:
        page.merge_page(watermark)
        writer.add_page(page)
    with open(sys.argv[3], "wb") as output:
        writer.write(output)
    print(f"Added watermark to {sys.argv[1]}, saved as {sys.argv[3]}")


if __name__ == "__main__":
    main()

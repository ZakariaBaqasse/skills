import sys
from pypdf import PdfReader, PdfWriter


def main():
    if len(sys.argv) != 4:
        print("Usage: rotate_pages.py <input.pdf> <output.pdf> <degrees>")
        sys.exit(1)
    reader = PdfReader(sys.argv[1])
    writer = PdfWriter()
    degrees = int(sys.argv[3])
    for page in reader.pages:
        page.rotate(degrees)
        writer.add_page(page)
    with open(sys.argv[2], "wb") as output:
        writer.write(output)
    print(f"Rotated all pages by {degrees} degrees")


if __name__ == "__main__":
    main()

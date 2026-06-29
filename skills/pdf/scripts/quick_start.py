import sys
from pypdf import PdfReader


def main():
    if len(sys.argv) != 2:
        print("Usage: quick_start.py <input.pdf>")
        sys.exit(1)
    reader = PdfReader(sys.argv[1])
    print(f"Pages: {len(reader.pages)}")
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    print(text)


if __name__ == "__main__":
    main()

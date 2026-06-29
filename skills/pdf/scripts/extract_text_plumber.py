import sys

import pdfplumber


def main():
    if len(sys.argv) != 2:
        print("Usage: extract_text_plumber.py <input.pdf>")
        sys.exit(1)
    with pdfplumber.open(sys.argv[1]) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            print(text)


if __name__ == "__main__":
    main()

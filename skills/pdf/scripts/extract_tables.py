import sys

import pdfplumber


def main():
    if len(sys.argv) != 2:
        print("Usage: extract_tables.py <input.pdf>")
        sys.exit(1)
    with pdfplumber.open(sys.argv[1]) as pdf:
        for i, page in enumerate(pdf.pages):
            tables = page.extract_tables()
            for j, table in enumerate(tables):
                print(f"Table {j+1} on page {i+1}:")
                for row in table:
                    print(row)


if __name__ == "__main__":
    main()

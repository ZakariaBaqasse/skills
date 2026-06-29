import sys
from pypdf import PdfReader


def main():
    if len(sys.argv) != 2:
        print("Usage: extract_metadata.py <input.pdf>")
        sys.exit(1)
    reader = PdfReader(sys.argv[1])
    meta = reader.metadata
    print(f"Title: {meta.title}")
    print(f"Author: {meta.author}")
    print(f"Subject: {meta.subject}")
    print(f"Creator: {meta.creator}")


if __name__ == "__main__":
    main()

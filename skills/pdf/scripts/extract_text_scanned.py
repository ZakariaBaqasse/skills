import sys

import pytesseract
from pdf2image import convert_from_path


def main():
    if len(sys.argv) != 2:
        print("Usage: extract_text_scanned.py <scanned.pdf>")
        sys.exit(1)
    images = convert_from_path(sys.argv[1])
    text = ""
    for i, image in enumerate(images):
        text += f"Page {i+1}:\n"
        text += pytesseract.image_to_string(image)
        text += "\n\n"
    print(text)


if __name__ == "__main__":
    main()

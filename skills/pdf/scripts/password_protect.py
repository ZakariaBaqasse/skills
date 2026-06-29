import sys
from pypdf import PdfReader, PdfWriter


def main():
    if len(sys.argv) != 4:
        print("Usage: password_protect.py <input.pdf> <user_password> <owner_password>")
        sys.exit(1)
    reader = PdfReader(sys.argv[1])
    writer = PdfWriter()
    for page in reader.pages:
        writer.add_page(page)
    writer.encrypt(sys.argv[2], sys.argv[3])
    output_path = "encrypted.pdf"
    with open(output_path, "wb") as output:
        writer.write(output)
    print(f"Encrypted {sys.argv[1]} as {output_path}")


if __name__ == "__main__":
    main()

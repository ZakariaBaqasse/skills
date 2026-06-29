import sys

import pandas as pd
import pdfplumber


def main():
    if len(sys.argv) != 3:
        print("Usage: extract_tables_to_excel.py <input.pdf> <output.xlsx>")
        sys.exit(1)
    with pdfplumber.open(sys.argv[1]) as pdf:
        all_tables = []
        for page in pdf.pages:
            tables = page.extract_tables()
            for table in tables:
                if table:
                    df = pd.DataFrame(table[1:], columns=table[0])
                    all_tables.append(df)
    if all_tables:
        combined_df = pd.concat(all_tables, ignore_index=True)
        combined_df.to_excel(sys.argv[2], index=False)
        print(f"Saved {len(combined_df)} rows to {sys.argv[2]}")
    else:
        print("No tables found")


if __name__ == "__main__":
    main()

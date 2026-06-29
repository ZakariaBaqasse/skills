---
name: pdf
description: Use this skill whenever the user wants to do anything with PDF files. This includes reading or extracting text/tables from PDFs, combining or merging multiple PDFs into one, splitting PDFs apart, rotating pages, adding watermarks, creating new PDFs, filling PDF forms, encrypting/decrypting PDFs, extracting images, and OCR on scanned PDFs to make them searchable. If the user mentions a .pdf file or asks to produce one, use this skill.
license: Proprietary. LICENSE.txt has complete terms
---

# PDF Processing Guide

## Overview

This guide covers essential PDF processing operations using Python libraries and command-line tools. For advanced features, JavaScript libraries, and detailed examples, see REFERENCE.md. If you need to fill out a PDF form, read FORMS.md and follow its instructions.

## Quick Start

```bash
python scripts/quick_start.py document.pdf
```

## Python Libraries

### pypdf - Basic Operations

#### Merge PDFs

```bash
python scripts/merge_pdfs.py merged.pdf doc1.pdf doc2.pdf doc3.pdf
```

#### Split PDF

```bash
python scripts/split_pdf.py input.pdf
```

#### Extract Metadata

```bash
python scripts/extract_metadata.py document.pdf
```

#### Rotate Pages

```bash
python scripts/rotate_pages.py input.pdf rotated.pdf 90
```

### pdfplumber - Text and Table Extraction

#### Extract Text with Layout

```bash
python scripts/extract_text_plumber.py document.pdf
```

#### Extract Tables

```bash
python scripts/extract_tables.py document.pdf
```

#### Advanced Table Extraction

```bash
python scripts/extract_tables_to_excel.py document.pdf extracted_tables.xlsx
```

### reportlab - Create PDFs

#### Basic PDF Creation

```bash
python scripts/create_pdf_basic.py hello.pdf
```

#### Create PDF with Multiple Pages

```bash
python scripts/create_pdf_multi_page.py report.pdf
```

#### Subscripts and Superscripts

**IMPORTANT**: Never use Unicode subscript/superscript characters (₀₁₂₃₄₅₆₇₈₉, ⁰¹²³⁴⁵⁶⁷⁸⁹) in ReportLab PDFs. The built-in fonts do not include these glyphs, causing them to render as solid black boxes.

Instead, use ReportLab's XML markup tags in Paragraph objects:

```bash
python scripts/subscript_superscript.py output.pdf
```

The script demonstrates `H<sub>2</sub>O` for subscripts and `x<super>2</super> + y<super>2</super>` for superscripts.

For canvas-drawn text (not Paragraph objects), manually adjust font the size and position rather than using Unicode subscripts/superscripts.

## Command-Line Tools

### pdftotext (poppler-utils)

```bash
# Extract text
scripts/pdftotext_extract.sh input.pdf output.txt

# Extract text preserving layout
scripts/pdftotext_extract.sh -l input.pdf output.txt

# Extract specific pages (1-5)
scripts/pdftotext_extract.sh -f 1 -L 5 input.pdf output.txt
```

### qpdf

```bash
# Merge PDFs
scripts/qpdf_operations.sh merge merged.pdf file1.pdf file2.pdf

# Split pages 1-5
scripts/qpdf_operations.sh split input.pdf 1-5 pages1-5.pdf

# Rotate page 1 by 90 degrees
scripts/qpdf_operations.sh rotate input.pdf output.pdf +90:1

# Remove password
scripts/qpdf_operations.sh decrypt encrypted.pdf mypassword decrypted.pdf
```

### pdftk (if available)

```bash
# Merge
scripts/pdftk_operations.sh merge merged.pdf file1.pdf file2.pdf

# Split
scripts/pdftk_operations.sh split input.pdf

# Rotate
scripts/pdftk_operations.sh rotate input.pdf rotated.pdf 1east
```

## Common Tasks

### Extract Text from Scanned PDFs

Requires: `pip install pytesseract pdf2image`

```bash
python scripts/extract_text_scanned.py scanned.pdf
```

### Add Watermark

```bash
python scripts/add_watermark.py document.pdf watermark.pdf watermarked.pdf
```

### Extract Images

```bash
scripts/extract_images.sh input.pdf output_prefix
```

This extracts all images as `output_prefix-000.jpg`, `output_prefix-001.jpg`, etc.

### Password Protection

```bash
python scripts/password_protect.py input.pdf userpassword ownerpassword
```

## Quick Reference

| Task | Best Tool | Command/Code |
|------|-----------|--------------|
| Merge PDFs | pypdf | `writer.add_page(page)` |
| Split PDFs | pypdf | One page per file |
| Extract text | pdfplumber | `page.extract_text()` |
| Extract tables | pdfplumber | `page.extract_tables()` |
| Create PDFs | reportlab | Canvas or Platypus |
| Command line merge | qpdf | `qpdf --empty --pages ...` |
| OCR scanned PDFs | pytesseract | Convert to image first |
| Fill PDF forms | pdf-lib or pypdf (see FORMS.md) | See FORMS.md |

## Next Steps

- For advanced pypdfium2 usage, see REFERENCE.md
- For JavaScript libraries (pdf-lib), see REFERENCE.md
- If you need to fill out a PDF form, follow the instructions in FORMS.md
- For troubleshooting guides, see REFERENCE.md

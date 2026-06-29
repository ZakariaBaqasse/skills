#!/usr/bin/env bash
set -euo pipefail

usage() {
    echo "Usage: $0 <input.pdf> [output_prefix]"
    echo ""
    echo "Extracts all images from a PDF using pdfimages (poppler-utils)."
    echo "Output is saved as <prefix>-NNN.jpg (or .png)."
    exit 1
}

[ $# -lt 1 ] && usage

input="$1"
prefix="${2:-${input%.pdf}_img}"

pdfimages -j "$input" "$prefix"
echo "Extracted images with prefix: $prefix"

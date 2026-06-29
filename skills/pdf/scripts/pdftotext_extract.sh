#!/usr/bin/env bash
set -euo pipefail

usage() {
    echo "Usage: $0 [options] <input.pdf> [output.txt]"
    echo "Options:"
    echo "  -l        Preserve layout"
    echo "  -f <n>    First page to extract (1-indexed)"
    echo "  -L <n>    Last page to extract"
    exit 1
}

layout=""
first=""
last=""

while getopts "lf:L:" opt; do
    case $opt in
        l) layout="-layout" ;;
        f) first="-f $OPTARG" ;;
        L) last="-l $OPTARG" ;;
        *) usage ;;
    esac
done
shift $((OPTIND-1))

[ $# -lt 1 ] && usage

input="$1"
output="${2:-${input%.pdf}.txt}"

pdftotext $layout $first $last "$input" "$output"
echo "Extracted text to $output"

#!/usr/bin/env bash
set -euo pipefail

usage() {
    echo "Usage: $0 <command> [args...]"
    echo ""
    echo "Commands:"
    echo "  merge <out.pdf> <in1.pdf> [in2.pdf ...]"
    echo "  split <in.pdf>"
    echo "  rotate <in.pdf> <out.pdf> <rotation>"
    echo ""
    echo "Examples:"
    echo "  pdftk_operations.sh merge merged.pdf a.pdf b.pdf"
    echo "  pdftk_operations.sh split input.pdf"
    echo "  pdftk_operations.sh rotate input.pdf output.pdf 1east"
    exit 1
}

[ $# -lt 1 ] && usage

cmd="$1"
shift

case "$cmd" in
    merge)
        out="${1:?Missing output}"
        shift
        pdftk "$@" cat output "$out"
        echo "Merged into $out"
        ;;
    split)
        inp="${1:?Missing input}"
        pdftk "$inp" burst
        echo "Split $inp into individual pages"
        ;;
    rotate)
        inp="${1:?Missing input}"
        out="${2:?Missing output}"
        rot="${3:?Missing rotation (e.g. 1east)}"
        pdftk "$inp" rotate "$rot" output "$out"
        echo "Rotated $inp -> $out"
        ;;
    *)
        usage
        ;;
esac

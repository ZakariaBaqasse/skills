#!/usr/bin/env bash
set -euo pipefail

usage() {
    echo "Usage: $0 <command> [args...]"
    echo ""
    echo "Commands:"
    echo "  merge <out.pdf> <in1.pdf> [in2.pdf ...]"
    echo "  split <in.pdf> <first_page>-<last_page> <out.pdf>"
    echo "  rotate <in.pdf> <out.pdf> <degrees>:<pages>"
    echo "  decrypt <in.pdf> <password> <out.pdf>"
    exit 1
}

[ $# -lt 1 ] && usage

cmd="$1"
shift

case "$cmd" in
    merge)
        out="${1:?Missing output}"
        shift
        qpdf --empty --pages "$@" -- "$out"
        echo "Merged into $out"
        ;;
    split)
        inp="${1:?Missing input}"
        pages="${2:?Missing page range (e.g. 1-5)}"
        out="${3:?Missing output}"
        qpdf "$inp" --pages . "$pages" -- "$out"
        echo "Split pages $pages into $out"
        ;;
    rotate)
        inp="${1:?Missing input}"
        out="${2:?Missing output}"
        rot="${3:?Missing rotation (e.g. +90:1)}"
        qpdf "$inp" "$out" --rotate="$rot"
        echo "Rotated $inp -> $out"
        ;;
    decrypt)
        inp="${1:?Missing input}"
        pass="${2:?Missing password}"
        out="${3:?Missing output}"
        qpdf --password="$pass" --decrypt "$inp" "$out"
        echo "Decrypted $inp -> $out"
        ;;
    *)
        usage
        ;;
esac

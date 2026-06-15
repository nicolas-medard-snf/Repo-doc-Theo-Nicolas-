#!/usr/bin/env bash
# md-to-pdf converter — uses pandoc + xelatex
# Usage:
#   ./convert.sh path/to/file.md              → outputs file.pdf next to the source
#   ./convert.sh path/to/directory/           → converts all *.md files in directory
#   ./convert.sh path/to/directory/ --outdir /tmp/pdfs   → custom output directory

set -euo pipefail

TARGET="${1:-}"
OUTDIR=""

if [[ -z "$TARGET" ]]; then
  echo "Usage: $0 <file.md|directory> [--outdir /path/to/output]" >&2
  exit 1
fi

shift
while [[ $# -gt 0 ]]; do
  case "$1" in
    --outdir) OUTDIR="$2"; shift 2 ;;
    *) echo "Unknown argument: $1" >&2; exit 1 ;;
  esac
done

PANDOC_OPTS=(
  --pdf-engine=xelatex
  -V "geometry:margin=2.5cm"
  -V "fontsize=11pt"
  -V "linestretch=1.4"
  -V "mainfont=Georgia"
  -V "colorlinks=true"
  -V "linkcolor=NavyBlue"
  --standalone
  -f markdown-yaml_metadata_block
)

convert_file() {
  local src="$1"
  local out_pdf

  if [[ -n "$OUTDIR" ]]; then
    mkdir -p "$OUTDIR"
    out_pdf="${OUTDIR}/$(basename "${src%.md}").pdf"
  else
    out_pdf="${src%.md}.pdf"
  fi

  echo "-> Converting: $(basename "$src")"
  if pandoc "$src" -o "$out_pdf" "${PANDOC_OPTS[@]}" 2>/dev/null; then
    echo "   OK: $(basename "$out_pdf")"
  else
    echo "   FAILED: $(basename "$src")" >&2
    return 1
  fi
}

if [[ -f "$TARGET" ]]; then
  convert_file "$TARGET"
elif [[ -d "$TARGET" ]]; then
  shopt -s nullglob
  files=("$TARGET"/*.md)
  if [[ ${#files[@]} -eq 0 ]]; then
    echo "No .md files found in: $TARGET" >&2
    exit 1
  fi
  echo "Converting ${#files[@]} files from: $TARGET"
  ok=0; fail=0
  for f in "${files[@]}"; do
    if convert_file "$f"; then
      ((ok++)) || true
    else
      ((fail++)) || true
    fi
  done
  echo ""
  echo "Done - ${ok} converted, ${fail} failed."
else
  echo "Error: '$TARGET' is not a file or directory." >&2
  exit 1
fi

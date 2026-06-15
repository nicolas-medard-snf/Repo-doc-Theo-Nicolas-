"""
PDF Semantic Annotator

Applies structured, color-coded highlights to scientific PDFs based on four
knowledge tiers aligned with the paper reading strategy:

  - CRITICAL (red):    Must Know Absolutely — core facts, definitions, essential findings
  - DEEP (green):      Must Understand Deeply — mechanisms, methodology, complex reasoning
  - INSIGHT (yellow):  Where Insights Are — novel ideas, surprising results, interpretations
  - GAP (pink):        Where Gaps Are — limitations, open questions, missing evidence

Usage:
    python pdf_annotator.py <input_pdf> <annotations_json> [--output <output_pdf>]
"""

import json
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional

import fitz  # PyMuPDF


@dataclass
class AnnotationTier:
    name: str
    color: tuple  # RGB 0-1 float
    opacity: float = 0.35

TIERS = {
    "critical": AnnotationTier("Critical Knowledge", (1.0, 0.3, 0.3), 0.35),
    "deep":     AnnotationTier("Deep Understanding", (0.3, 0.8, 0.4), 0.30),
    "insight":  AnnotationTier("Key Insight",        (1.0, 0.9, 0.3), 0.35),
    "gap":      AnnotationTier("Knowledge Gap",      (1.0, 0.5, 0.7), 0.35),
}


@dataclass
class Annotation:
    tier: str
    text: str
    note: str = ""
    page: Optional[int] = None  # None = search all pages


def load_annotations(json_path: str) -> list[Annotation]:
    with open(json_path) as f:
        data = json.load(f)
    annotations = []
    for item in data:
        annotations.append(Annotation(
            tier=item["tier"],
            text=item["text"],
            note=item.get("note", ""),
            page=item.get("page"),
        ))
    return annotations


def highlight_text(
    doc: fitz.Document,
    annotation: Annotation,
    tier: AnnotationTier,
    stats: dict,
) -> int:
    """Search for text in the PDF and apply a highlight annotation.
    Returns number of highlights applied.
    """
    count = 0
    pages = [doc[annotation.page - 1]] if annotation.page else doc

    for page in pages:
        text_instances = page.search_for(annotation.text, quads=True)
        if not text_instances:
            continue

        quads = text_instances
        highlight = page.add_highlight_annot(quads)
        highlight.set_colors(stroke=tier.color)
        highlight.set_opacity(tier.opacity)

        info_text = f"[{tier.name}]"
        if annotation.note:
            info_text += f" {annotation.note}"
        highlight.set_info(content=info_text, title=tier.name)
        highlight.update()
        count += 1

    if count == 0:
        stats["missed"].append(annotation.text[:80])
    else:
        stats["applied"] += count

    return count


def add_legend(doc: fitz.Document):
    """Insert a legend on the first page showing the color scheme."""
    page = doc[0]
    legend_y = 30
    legend_x = page.rect.width - 200

    legend_items = [
        ("CRITICAL — Must Know", TIERS["critical"].color),
        ("DEEP — Must Understand", TIERS["deep"].color),
        ("INSIGHT — Novel Ideas", TIERS["insight"].color),
        ("GAP — Limitations", TIERS["gap"].color),
    ]

    for i, (label, color) in enumerate(legend_items):
        y = legend_y + i * 12
        rect = fitz.Rect(legend_x, y, legend_x + 10, y + 8)
        page.draw_rect(rect, color=color, fill=color)
        page.insert_text(
            fitz.Point(legend_x + 14, y + 7),
            label,
            fontsize=6,
            color=(0.2, 0.2, 0.2),
        )


def annotate_pdf(
    input_path: str,
    annotations: list[Annotation],
    output_path: str,
    add_legend_box: bool = True,
) -> dict:
    doc = fitz.open(input_path)
    stats = {"applied": 0, "missed": [], "total": len(annotations)}

    for ann in annotations:
        tier = TIERS.get(ann.tier)
        if tier is None:
            print(f"  WARNING: Unknown tier '{ann.tier}' — skipping")
            continue
        highlight_text(doc, ann, tier, stats)

    if add_legend_box:
        add_legend(doc)

    doc.save(output_path)
    doc.close()
    return stats


def main():
    if len(sys.argv) < 3:
        print(__doc__)
        sys.exit(1)

    input_pdf = sys.argv[1]
    annotations_json = sys.argv[2]
    output_pdf = sys.argv[3] if len(sys.argv) > 3 else None

    if output_pdf is None:
        p = Path(input_pdf)
        output_pdf = str(p.with_stem(p.stem + "_annotated"))

    annotations = load_annotations(annotations_json)
    stats = annotate_pdf(input_pdf, annotations, output_pdf)

    print(f"\nAnnotation Summary:")
    print(f"  Total targets:  {stats['total']}")
    print(f"  Applied:        {stats['applied']}")
    print(f"  Missed:         {len(stats['missed'])}")
    if stats["missed"]:
        print(f"\n  Missed snippets:")
        for m in stats["missed"]:
            print(f"    - {m}")
    print(f"\n  Output: {output_pdf}")


if __name__ == "__main__":
    main()

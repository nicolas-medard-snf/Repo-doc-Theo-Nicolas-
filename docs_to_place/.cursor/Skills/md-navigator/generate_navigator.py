#!/usr/bin/env python3
"""
Lab Markdown Navigator Generator
==================================
Walks the MMintegration2 project tree, collects all .md files and writes
a self-contained lab_navigator.html to the project root.

Usage (from project root):
    python .cursor/Skills/md-navigator/generate_navigator.py [options]

Options:
    --no-corpus         Exclude per-paper corpus article summaries
                        (by default they ARE included)

    --export <dir>      Mirror all referenced .md files + the HTML into <dir>,
                        preserving the folder structure. The result is a
                        fully self-contained bundle you can share with anyone:
                        they just open a local server from <dir> and browse.

    --snapshot-parent   Also write a versioned bundle next to the project folder
                        (parent of PROJECT_ROOT): a directory named
                        lab_navigator_YYYY-MM-DD/ containing all mirrored .md
                        files plus lab_navigator_YYYY-MM-DD.html (today's date).

Examples:
    # Default: all files including corpus articles
    python .cursor/Skills/md-navigator/generate_navigator.py

    # Without corpus article summaries
    python .cursor/Skills/md-navigator/generate_navigator.py --no-corpus

    # Full export bundle (corpus included)
    python .cursor/Skills/md-navigator/generate_navigator.py --export ~/Users/U1029063/Documents/Codes/lab_navigator

    # Export without corpus
    python .cursor/Skills/md-navigator/generate_navigator.py --no-corpus --export ~/Users/U1029063/Documents/Codes/MMintegration2

    # Versioned snapshot (parent of project): ../lab_navigator_YYYY-MM-DD/ + dated HTML
    python .cursor/Skills/md-navigator/generate_navigator.py --snapshot-parent

Then serve (from project root or from the export dir):
    python -m http.server 8765
    # open http://localhost:8765/lab_navigator.html
"""

import json
import shutil
import sys
from datetime import date
from pathlib import Path

# ── Configuration ────────────────────────────────────────────────────────────

# Resolve project root: this script lives at .cursor/Skills/md-navigator/
SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SCRIPT_DIR.parents[2]  # up 3 levels: md-navigator → Skills → .cursor → root
OUTPUT_FILE = PROJECT_ROOT / "lab_navigator.html"

# Corpus folders where we exclude deep article summaries.
# Auto-discovered: every immediate subdirectory of Doc/Corpus (except those
# starting with "_") is treated as a corpus article root, so this works for
# any project's corpora without editing the script.
def _discover_corpus_roots():
    base = PROJECT_ROOT / "Doc" / "Corpus"
    if not base.is_dir():
        return []
    return [
        f"Doc/Corpus/{p.name}"
        for p in sorted(base.iterdir())
        if p.is_dir() and not p.name.startswith("_")
    ]

CORPUS_ARTICLE_ROOTS = _discover_corpus_roots()

# Files to always INCLUDE even inside corpus article roots (by filename)
CORPUS_ALWAYS_INCLUDE = {
    "CROSS_REFERENCE_INDEX.md",
    "README.md",
    "HOW_TO_ADD_PAPERS.md",
    "PAPER_TEMPLATE_GENERAL.md",
}

# Directories to skip entirely
SKIP_DIRS = {
    ".git", "__pycache__", "node_modules", ".venv", "venv",
    "external",   # read-only reference implementations
    "data",       # gitignored data
}

# ── Exclusion logic ───────────────────────────────────────────────────────────

def is_corpus_article(rel_path: str) -> bool:
    """
    Returns True if this file is a per-paper summary inside one of the three
    scientific corpora (i.e. more than 1 level deep inside the corpus root,
    and not in the always-include set).
    """
    p = Path(rel_path)
    for corpus_root in CORPUS_ARTICLE_ROOTS:
        try:
            relative = p.relative_to(corpus_root)
            if len(relative.parts) >= 2 and p.name not in CORPUS_ALWAYS_INCLUDE:
                return True
        except ValueError:
            continue
    return False


# ── Filesystem walker ─────────────────────────────────────────────────────────

def build_tree(root: Path, include_corpus: bool = True) -> dict:
    """
    Recursively builds a nested dict representing the file tree.
    Each node is either:
      { "type": "file",   "name": str, "path": str (relative, posix) }
      { "type": "folder", "name": str, "path": str, "children": [...] }

    include_corpus: if False, per-paper corpus article summaries are skipped.
    """
    def walk(current: Path, rel: Path) -> list:
        entries = []
        try:
            items = sorted(current.iterdir(), key=lambda p: (p.is_file(), p.name.lower()))
        except PermissionError:
            return entries

        for item in items:
            item_rel = rel / item.name

            if item.is_dir():
                # Allow .cursor explicitly; skip all other dot-folders and SKIP_DIRS
                if item.name in SKIP_DIRS:
                    continue
                if item.name.startswith(".") and item.name != ".cursor":
                    continue
                children = walk(item, item_rel)
                if children:  # only include non-empty folders
                    entries.append({
                        "type": "folder",
                        "name": item.name,
                        "path": item_rel.as_posix(),
                        "children": children,
                    })
            elif item.is_file() and item.suffix == ".md":
                rel_posix = item_rel.as_posix()
                if not include_corpus and is_corpus_article(rel_posix):
                    continue
                entries.append({
                    "type": "file",
                    "name": item.name,
                    "path": rel_posix,
                })
        return entries

    root_children = walk(root, Path(""))
    return {
        "type": "folder",
        "name": root.name,
        "path": "",
        "children": root_children,
    }


# ── HTML generation ───────────────────────────────────────────────────────────

HTML_TEMPLATE = r"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
<title>Lab Navigator — MMintegration2</title>
<style>
  /* ── Reset & base ── */
  *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

  :root {
    --bg:            #0a1024;
    --surface:       #121a38;
    --surface2:      #18224a;
    --border:        #2a3d72;
    --border-blue:   #3d5a9e;
    --border-pink:   #8b4a7a;
    --accent:        #5b9fff;
    --accent2:       #f472b6;
    --accent-yellow: #fde047;
    --accent-warm:   #fbcfe8;
    --text:          #e2e8ff;
    --text-dim:      #8b9fd4;
    --text-bright:   #fff7ed;
    --folder:        #fde047;
    --file:          #7ec8ff;
    --hover:         rgba(91, 159, 255, 0.12);
    --active:        rgba(244, 114, 182, 0.18);
    --active-left:   rgba(91, 159, 255, 0.22);
    --radius:        6px;
    --mono:          'JetBrains Mono', 'Fira Code', 'Cascadia Code', monospace;
    --sans:          'Inter', system-ui, sans-serif;
  }

  html, body { height: 100%; overflow: hidden; }

  body {
    font-family: var(--sans);
    background: radial-gradient(ellipse 120% 80% at 10% 0%, rgba(91, 159, 255, 0.08), transparent 50%),
                radial-gradient(ellipse 100% 60% at 100% 100%, rgba(244, 114, 182, 0.07), transparent 45%),
                var(--bg);
    color: var(--text);
    display: flex;
    flex-direction: column;
  }

  /* ── Header ── */
  header {
    display: flex;
    align-items: center;
    gap: 16px;
    padding: 12px 20px;
    background: linear-gradient(90deg, var(--surface) 0%, #1a1f45 50%, var(--surface) 100%);
    border-bottom: 1px solid var(--border-blue);
    flex-shrink: 0;
  }

  header .logo {
    font-family: var(--mono);
    font-size: 13px;
    font-weight: 600;
    color: var(--accent);
    letter-spacing: 0.04em;
    white-space: nowrap;
  }

  header .logo span { color: var(--accent-yellow); }

  #search {
    flex: 1;
    max-width: 360px;
    background: var(--surface2);
    border: 1px solid var(--border);
    border-radius: var(--radius);
    color: var(--text);
    padding: 7px 12px 7px 32px;
    font-size: 13px;
    outline: none;
    background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='14' height='14' viewBox='0 0 24 24' fill='none' stroke='%23f472b6' stroke-width='2'%3E%3Ccircle cx='11' cy='11' r='8'/%3E%3Cpath d='m21 21-4.35-4.35'/%3E%3C/svg%3E");
    background-repeat: no-repeat;
    background-position: 10px center;
    transition: border-color 0.2s, box-shadow 0.2s;
  }
  #search:focus { border-color: var(--accent2); box-shadow: 0 0 0 2px rgba(244, 114, 182, 0.2); }
  #search::placeholder { color: var(--text-dim); }

  .stat { font-size: 11px; color: var(--text-dim); margin-left: auto; white-space: nowrap; }

  /* ── Layout: two symmetric columns (tree | viewer | tree | viewer) ── */
  .layout {
    display: flex;
    flex: 1;
    overflow: hidden;
    min-height: 0;
  }

  .dual-pane {
    flex: 1;
    display: flex;
    min-width: 0;
    overflow: hidden;
    flex-direction: row;
  }

  .dual-pane.pane-left {
    border-right: 2px solid var(--border-pink);
    background: linear-gradient(180deg, rgba(91, 159, 255, 0.07) 0%, transparent 35%);
  }

  .dual-pane.pane-right {
    background: linear-gradient(180deg, rgba(244, 114, 182, 0.06) 0%, transparent 35%);
  }

  /* ── Sidebars / tree ── */
  .sidebar {
    width: 200px;
    min-width: 120px;
    max-width: 300px;
    background: var(--surface);
    overflow-y: auto;
    overflow-x: hidden;
    flex-shrink: 0;
    padding: 8px 0;
    resize: horizontal;
  }

  #sidebar-left {
    border-right: 1px solid var(--border-blue);
  }

  #sidebar-right {
    border-right: 1px solid var(--border-pink);
  }

  .sidebar::-webkit-scrollbar { width: 6px; }
  .sidebar::-webkit-scrollbar-track { background: transparent; }
  .sidebar::-webkit-scrollbar-thumb { background: var(--border); border-radius: 3px; }

  .tree-node { user-select: none; }

  .tree-row {
    display: flex;
    align-items: center;
    gap: 6px;
    padding: 4px 8px;
    cursor: pointer;
    border-radius: 4px;
    margin: 1px 4px;
    font-size: 12.5px;
    color: var(--text);
    transition: background 0.1s;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
  }
  .tree-row:hover { background: var(--hover); }

  .pane-left .tree-row.active { background: var(--active-left); color: var(--text-bright); }
  .pane-right .tree-row.active { background: var(--active); color: var(--text-bright); }

  .tree-row .icon {
    width: 16px;
    flex-shrink: 0;
    font-size: 12px;
    text-align: center;
  }
  .tree-row.folder-row .icon { color: var(--folder); }
  .tree-row.file-row .icon   { color: var(--file); }

  .tree-row .label {
    overflow: hidden;
    text-overflow: ellipsis;
    flex: 1;
  }

  .tree-row.hidden { display: none; }

  .tree-row mark {
    background: rgba(253, 224, 71, 0.35);
    color: var(--text-bright);
    border-radius: 2px;
    padding: 0 1px;
  }

  /* ── Content pane ── */
  .content-pane {
    flex: 1;
    display: flex;
    flex-direction: column;
    overflow: hidden;
    min-width: 0;
    background: var(--bg);
  }

  .toolbar {
    display: flex;
    align-items: center;
    gap: 10px;
    padding: 10px 16px;
    background: var(--surface);
    border-bottom: 1px solid var(--border);
    flex-shrink: 0;
    min-height: 44px;
  }

  .pane-left .toolbar { border-bottom-color: var(--border-blue); }
  .pane-right .toolbar { border-bottom-color: var(--border-pink); }

  .btn-back {
    background: var(--surface2);
    border: 1px solid var(--border);
    color: var(--text-dim);
    border-radius: var(--radius);
    padding: 5px 12px;
    font-size: 12px;
    cursor: pointer;
    display: flex;
    align-items: center;
    gap: 5px;
    transition: all 0.15s;
    white-space: nowrap;
  }
  .btn-back:hover:not(:disabled) { border-color: var(--accent2); color: var(--accent-yellow); }
  .btn-back:disabled { opacity: 0.3; cursor: default; }

  .breadcrumb {
    font-family: var(--mono);
    font-size: 11.5px;
    color: var(--text-dim);
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
  }
  .breadcrumb .crumb { color: var(--text-dim); }
  .breadcrumb .crumb-sep { margin: 0 4px; color: var(--border); }
  .pane-left .breadcrumb .crumb-last { color: var(--accent); }
  .pane-right .breadcrumb .crumb-last { color: var(--accent2); }

  .btn-copy {
    margin-left: auto;
    background: transparent;
    border: 1px solid var(--border);
    color: var(--text-dim);
    border-radius: var(--radius);
    padding: 4px 10px;
    font-size: 11px;
    cursor: pointer;
    transition: all 0.15s;
    white-space: nowrap;
  }
  .btn-copy:hover { border-color: var(--accent-yellow); color: var(--accent-yellow); }
  .btn-copy.copied { color: #86efac; border-color: #86efac; }

  .viewer {
    flex: 1;
    overflow-y: auto;
    padding: 24px 28px;
  }
  .viewer::-webkit-scrollbar { width: 8px; }
  .viewer::-webkit-scrollbar-track { background: transparent; }
  .viewer::-webkit-scrollbar-thumb { background: var(--border); border-radius: 4px; }

  .welcome {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    height: 100%;
    gap: 16px;
    color: var(--text-dim);
  }
  .welcome .big { font-size: 48px; }
  .welcome h2 { font-size: 18px; color: var(--text); font-weight: 500; }
  .welcome p { font-size: 13px; max-width: 320px; text-align: center; line-height: 1.6; }
  .welcome kbd {
    background: var(--surface2);
    border: 1px solid var(--border);
    border-radius: 4px;
    padding: 2px 6px;
    font-family: var(--mono);
    font-size: 11px;
    color: var(--accent-yellow);
  }

  /* ── Markdown rendered styles ── */
  .md-body {
    max-width: 100%;
    margin: 0 auto;
    line-height: 1.7;
    color: var(--text);
    font-size: 14.5px;
  }

  .md-body h1 { font-size: 26px; color: var(--text-bright); margin: 0 0 20px; padding-bottom: 10px; border-bottom: 1px solid var(--border-blue); font-weight: 700; }
  .md-body h2 { font-size: 19px; color: var(--text-bright); margin: 32px 0 12px; padding-bottom: 6px; border-bottom: 1px solid var(--border); font-weight: 600; }
  .md-body h3 { font-size: 15px; color: var(--accent2); margin: 24px 0 8px; font-weight: 600; }
  .md-body h4 { font-size: 13.5px; color: var(--accent); margin: 18px 0 6px; font-weight: 600; text-transform: uppercase; letter-spacing: 0.05em; }

  .md-body p { margin: 10px 0; }

  .md-body a { color: var(--accent); text-decoration: none; border-bottom: 1px solid transparent; transition: border-color 0.15s; }
  .md-body a:hover { border-bottom-color: var(--accent); }

  .md-body a.internal-link { color: var(--accent2); cursor: pointer; }
  .md-body a.internal-link:hover { border-bottom-color: var(--accent2); }

  .md-body code {
    background: var(--surface2);
    border: 1px solid var(--border);
    border-radius: 3px;
    padding: 1px 5px;
    font-family: var(--mono);
    font-size: 12.5px;
    color: var(--accent-warm);
  }

  .md-body pre {
    background: var(--surface2);
    border: 1px solid var(--border-blue);
    border-radius: var(--radius);
    padding: 16px 20px;
    overflow-x: auto;
    margin: 16px 0;
    white-space: pre;
    font-family: var(--mono);
    font-size: 12.5px;
    line-height: 1.45;
    letter-spacing: normal;
    word-spacing: normal;
    text-align: left;
  }
  .md-body pre code {
    background: none;
    border: none;
    padding: 0;
    color: #bae6fd;
    font-size: inherit;
    line-height: inherit;
    font-family: inherit;
    white-space: pre;
    letter-spacing: normal;
    word-spacing: normal;
  }

  .md-body blockquote {
    border-left: 3px solid var(--accent-yellow);
    margin: 16px 0;
    padding: 8px 16px;
    background: rgba(253, 224, 71, 0.06);
    border-radius: 0 var(--radius) var(--radius) 0;
    color: var(--text-dim);
    font-style: italic;
  }

  .md-body ul, .md-body ol { margin: 10px 0 10px 24px; }
  .md-body li { margin: 4px 0; }
  .md-body li > ul, .md-body li > ol { margin: 4px 0 4px 18px; }

  .md-body table {
    border-collapse: collapse;
    width: 100%;
    margin: 16px 0;
    font-size: 13px;
  }
  .md-body th {
    background: var(--surface2);
    border: 1px solid var(--border);
    padding: 8px 12px;
    color: var(--accent-yellow);
    font-weight: 600;
    text-align: left;
  }
  .md-body td {
    border: 1px solid var(--border);
    padding: 7px 12px;
  }
  .md-body tr:hover td { background: var(--hover); }

  .md-body hr {
    border: none;
    border-top: 1px solid var(--border-pink);
    margin: 24px 0;
  }

  .md-body strong { color: var(--text-bright); font-weight: 600; }
  .md-body em { color: var(--accent2); }

  .loading {
    display: flex;
    align-items: center;
    justify-content: center;
    height: 200px;
    color: var(--text-dim);
    font-size: 13px;
    gap: 10px;
  }
  .spinner {
    width: 18px; height: 18px;
    border: 2px solid var(--border);
    border-top-color: var(--accent2);
    border-radius: 50%;
    animation: spin 0.7s linear infinite;
  }
  @keyframes spin { to { transform: rotate(360deg); } }

  .error-box {
    background: rgba(244, 114, 182, 0.08);
    border: 1px solid rgba(244, 114, 182, 0.35);
    border-radius: var(--radius);
    padding: 16px 20px;
    color: #fda4af;
    font-size: 13px;
    margin: 20px 0;
  }

  .badge {
    background: var(--surface2);
    border: 1px solid var(--border);
    border-radius: 10px;
    padding: 1px 7px;
    font-size: 10px;
    color: var(--text-dim);
    margin-left: 6px;
    flex-shrink: 0;
  }
</style>
</head>
<body>

<header>
  <div class="logo">🧬 <span>MMintegration2</span> · Lab Navigator</div>
  <input id="search" type="text" placeholder="Search files…" autocomplete="off" spellcheck="false"/>
  <div class="stat" id="stat"></div>
</header>

<div class="layout">
  <div class="dual-pane pane-left">
    <div id="sidebar-left" class="sidebar" aria-label="File tree A"></div>
    <div class="content-pane">
      <div class="toolbar">
        <button type="button" class="btn-back" id="btn-back-left" disabled>← Back</button>
        <div class="breadcrumb" id="breadcrumb-left"><span class="crumb-last">Pane A — select a file</span></div>
        <button type="button" class="btn-copy" id="btn-copy-left" style="display:none">Copy path</button>
      </div>
      <div class="viewer" id="viewer-left">
        <div class="welcome" id="welcome-left">
          <div class="big">📘</div>
          <h2>Left pane</h2>
          <p>Use the tree on the left to open a markdown file here. The right side has the same tree so you can open a second file at once.</p>
        </div>
      </div>
    </div>
  </div>
  <div class="dual-pane pane-right">
    <div id="sidebar-right" class="sidebar" aria-label="File tree B"></div>
    <div class="content-pane">
      <div class="toolbar">
        <button type="button" class="btn-back" id="btn-back-right" disabled>← Back</button>
        <div class="breadcrumb" id="breadcrumb-right"><span class="crumb-last">Pane B — select a file</span></div>
        <button type="button" class="btn-copy" id="btn-copy-right" style="display:none">Copy path</button>
      </div>
      <div class="viewer" id="viewer-right">
        <div class="welcome" id="welcome-right">
          <div class="big">📕</div>
          <h2>Right pane</h2>
          <p>Use the tree on the right to open another <kbd>.md</kbd> here. Search filters both trees.</p>
        </div>
      </div>
    </div>
  </div>
</div>

<script>
// ── Data injected by generator ─────────────────────────────────────────────
const TREE = __TREE_JSON__;
const TOTAL_FILES = __FILE_COUNT__;

// ── State (independent per pane) ───────────────────────────────────────────
const PANES = ['left', 'right'];

let historyLeft = [];
let historyRight = [];
let currentPathLeft = null;
let currentPathRight = null;
let expandedFoldersLeft = new Set();
let expandedFoldersRight = new Set();

// ── DOM refs ────────────────────────────────────────────────────────────────
const els = {
  left: {
    sidebar: document.getElementById('sidebar-left'),
    viewer: document.getElementById('viewer-left'),
    btnBack: document.getElementById('btn-back-left'),
    btnCopy: document.getElementById('btn-copy-left'),
    breadcrumb: document.getElementById('breadcrumb-left'),
  },
  right: {
    sidebar: document.getElementById('sidebar-right'),
    viewer: document.getElementById('viewer-right'),
    btnBack: document.getElementById('btn-back-right'),
    btnCopy: document.getElementById('btn-copy-right'),
    breadcrumb: document.getElementById('breadcrumb-right'),
  },
};

const searchEl = document.getElementById('search');
const statEl = document.getElementById('stat');

statEl.textContent = `${TOTAL_FILES} files indexed`;

function expandedSet(pane) {
  return pane === 'left' ? expandedFoldersLeft : expandedFoldersRight;
}

function getSidebar(pane) {
  return pane === 'left' ? els.left.sidebar : els.right.sidebar;
}

// ── Tree rendering ─────────────────────────────────────────────────────────
function renderTree(node, depth, pane) {
  const expanded = expandedSet(pane);
  const el = document.createElement('div');
  el.className = 'tree-node';
  el.dataset.path = node.path;
  el.dataset.type = node.type;
  el.dataset.pane = pane;

  const row = document.createElement('div');
  row.className = `tree-row ${node.type === 'folder' ? 'folder-row' : 'file-row'}`;
  row.style.paddingLeft = `${8 + depth * 14}px`;

  const icon = document.createElement('span');
  icon.className = 'icon';
  const label = document.createElement('span');
  label.className = 'label';
  label.dataset.rawName = node.name;
  label.textContent = node.name;

  if (node.type === 'folder') {
    icon.textContent = expanded.has(node.path) ? '▾' : '▸';
    row.appendChild(icon);
    row.appendChild(label);

    const childrenEl = document.createElement('div');
    childrenEl.className = 'tree-children';
    childrenEl.style.display = expanded.has(node.path) ? 'block' : 'none';

    row.addEventListener('click', (e) => {
      e.stopPropagation();
      const open = expanded.has(node.path);
      if (open) {
        expanded.delete(node.path);
        icon.textContent = '▸';
        childrenEl.style.display = 'none';
      } else {
        expanded.add(node.path);
        icon.textContent = '▾';
        childrenEl.style.display = 'block';
      }
    });

    if (node.children) {
      node.children.forEach((child) => childrenEl.appendChild(renderTree(child, depth + 1, pane)));
    }

    el.appendChild(row);
    el.appendChild(childrenEl);
  } else {
    icon.textContent = '📄';
    row.appendChild(icon);
    row.appendChild(label);
    row.addEventListener('click', () => navigateTo(node.path, pane));
    el.appendChild(row);
  }
  return el;
}

function buildSidebar(pane) {
  const sb = getSidebar(pane);
  sb.innerHTML = '';
  TREE.children.forEach((child) => sb.appendChild(renderTree(child, 0, pane)));
}

// ── Navigation ─────────────────────────────────────────────────────────────
async function navigateTo(path, pane) {
  if (pane === 'left') {
    if (currentPathLeft) historyLeft.push(currentPathLeft);
    currentPathLeft = path;
    els.left.btnBack.disabled = historyLeft.length === 0;
    els.left.btnCopy.style.display = 'inline-flex';
  } else {
    if (currentPathRight) historyRight.push(currentPathRight);
    currentPathRight = path;
    els.right.btnBack.disabled = historyRight.length === 0;
    els.right.btnCopy.style.display = 'inline-flex';
  }
  updateBreadcrumb(path, pane);
  highlightActive(path, pane);
  await loadFile(path, pane);
}

function goBack(pane) {
  const history = pane === 'left' ? historyLeft : historyRight;
  if (!history.length) return;
  const prev = history.pop();
  if (pane === 'left') {
    currentPathLeft = prev;
    els.left.btnBack.disabled = historyLeft.length === 0;
  } else {
    currentPathRight = prev;
    els.right.btnBack.disabled = historyRight.length === 0;
  }
  if (prev) {
    updateBreadcrumb(prev, pane);
    highlightActive(prev, pane);
    loadFile(prev, pane);
  } else {
    showWelcome(pane);
  }
}

els.left.btnBack.addEventListener('click', () => goBack('left'));
els.right.btnBack.addEventListener('click', () => goBack('right'));

function wireCopy(btn, pane) {
  btn.addEventListener('click', () => {
    const path = pane === 'left' ? currentPathLeft : currentPathRight;
    if (!path) return;
    navigator.clipboard.writeText(path).then(() => {
      btn.textContent = '✓ Copied';
      btn.classList.add('copied');
      setTimeout(() => {
        btn.textContent = 'Copy path';
        btn.classList.remove('copied');
      }, 1500);
    });
  });
}
wireCopy(els.left.btnCopy, 'left');
wireCopy(els.right.btnCopy, 'right');

function updateBreadcrumb(path, pane) {
  const bc = pane === 'left' ? els.left.breadcrumb : els.right.breadcrumb;
  const parts = path.split('/').filter(Boolean);
  if (!parts.length) {
    bc.innerHTML = '';
    return;
  }
  let html = '';
  parts.forEach((p, i) => {
    if (i > 0) html += `<span class="crumb-sep">/</span>`;
    if (i === parts.length - 1) html += `<span class="crumb-last">${p}</span>`;
    else html += `<span class="crumb">${p}</span>`;
  });
  bc.innerHTML = html;
}

function highlightActive(path, pane) {
  const sb = getSidebar(pane);
  sb.querySelectorAll('.tree-row.active').forEach((r) => r.classList.remove('active'));
  sb.querySelectorAll(`.tree-node[data-path="${CSS.escape(path)}"] > .tree-row`).forEach((r) =>
    r.classList.add('active')
  );
  autoExpand(path, pane);
}

function autoExpand(filePath, pane) {
  const expanded = expandedSet(pane);
  const sb = getSidebar(pane);
  const parts = filePath.split('/');
  let cumPath = '';
  for (let i = 0; i < parts.length - 1; i++) {
    cumPath = cumPath ? cumPath + '/' + parts[i] : parts[i];
    if (!expanded.has(cumPath)) {
      expanded.add(cumPath);
      const folderNode = sb.querySelector(`[data-path="${CSS.escape(cumPath)}"]`);
      if (folderNode) {
        const icon = folderNode.querySelector('.icon');
        const children = folderNode.querySelector('.tree-children');
        if (icon) icon.textContent = '▾';
        if (children) children.style.display = 'block';
      }
    }
  }
}

function welcomeHtml(pane) {
  if (pane === 'left') {
    return `
    <div class="welcome">
      <div class="big">📘</div>
      <h2>Left pane</h2>
      <p>Use the tree on the left to open a markdown file here.</p>
    </div>`;
  }
  return `
    <div class="welcome">
      <div class="big">📕</div>
      <h2>Right pane</h2>
      <p>Use the tree on the right to open another <kbd>.md</kbd> here.</p>
    </div>`;
}

function showWelcome(pane) {
  const viewer = pane === 'left' ? els.left.viewer : els.right.viewer;
  const bc = pane === 'left' ? els.left.breadcrumb : els.right.breadcrumb;
  const btnCopy = pane === 'left' ? els.left.btnCopy : els.right.btnCopy;
  const btnBack = pane === 'left' ? els.left.btnBack : els.right.btnBack;

  if (pane === 'left') {
    currentPathLeft = null;
    historyLeft = [];
  } else {
    currentPathRight = null;
    historyRight = [];
  }

  btnCopy.style.display = 'none';
  btnBack.disabled = true;
  bc.innerHTML =
    pane === 'left'
      ? '<span class="crumb-last">Pane A — select a file</span>'
      : '<span class="crumb-last">Pane B — select a file</span>';
  viewer.innerHTML = welcomeHtml(pane);
}

// ── File loading ───────────────────────────────────────────────────────────
async function loadFile(path, pane) {
  const viewer = pane === 'left' ? els.left.viewer : els.right.viewer;
  viewer.innerHTML = `<div class="loading"><div class="spinner"></div> Loading ${path}…</div>`;
  try {
    const response = await fetch(path);
    if (!response.ok) throw new Error(`HTTP ${response.status}`);
    const text = await response.text();
    const html = markdownToHtml(text, path);
    viewer.innerHTML = `<div class="md-body">${html}</div>`;
    viewer.scrollTop = 0;
    viewer.querySelectorAll('a.internal-link').forEach((a) => {
      a.addEventListener('click', (e) => {
        e.preventDefault();
        navigateTo(a.dataset.target, pane);
      });
    });
  } catch (err) {
    viewer.innerHTML = `
      <div class="md-body">
        <div class="error-box">
          <strong>Could not load file:</strong> ${path}<br/>
          <small>${err.message}</small><br/><br/>
          Make sure you're serving this HTML via a local server:<br/>
          <code>python -m http.server 8765</code>
        </div>
      </div>`;
  }
}

// ── Markdown parser (lightweight, no external deps) ────────────────────────
function markdownToHtml(md, filePath) {
  const baseDir = filePath.includes('/') ? filePath.substring(0, filePath.lastIndexOf('/')) : '';

  let html = md
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/```(\w*)\n([\s\S]*?)```/g, (_, lang, code) =>
      `<pre><code class="lang-${lang}">${code.replace(/&lt;/g, '<').replace(/&gt;/g, '>')}</code></pre>`
    );

  // Isolate <pre> blocks so later line-based rules (lists, paragraphs) cannot touch ASCII diagrams
  const preBlocks = [];
  html = html.replace(/<pre><code[^>]*>[\s\S]*?<\/code><\/pre>/g, (match) => {
    const i = preBlocks.length;
    preBlocks.push(match);
    return `<span class="md-pre-hold" data-i="${i}"></span>`;
  });

  html = html
    .replace(/^###### (.+)$/gm, '<h6>$1</h6>')
    .replace(/^##### (.+)$/gm, '<h5>$1</h5>')
    .replace(/^#### (.+)$/gm, '<h4>$1</h4>')
    .replace(/^### (.+)$/gm, '<h3>$1</h3>')
    .replace(/^## (.+)$/gm, '<h2>$1</h2>')
    .replace(/^# (.+)$/gm, '<h1>$1</h1>')
    .replace(/^---+$/gm, '<hr/>')
    .replace(/^&gt; (.+)$/gm, '<blockquote>$1</blockquote>')
    .replace(/\*\*\*(.+?)\*\*\*/g, '<strong><em>$1</em></strong>')
    .replace(/\*\*(.+?)\*\*/g, '<strong>$1</strong>')
    .replace(/\*(.+?)\*/g, '<em>$1</em>')
    .replace(/__(.+?)__/g, '<strong>$1</strong>')
    .replace(/_(.+?)_/g, '<em>$1</em>')
    .replace(/`([^`]+)`/g, '<code>$1</code>')
    .replace(/!\[([^\]]*)\]\(([^)]+)\)/g, '<img alt="$1" src="$2" style="max-width:100%;border-radius:4px;"/>')
    .replace(/\[([^\]]+)\]\(([^)]+)\)/g, (_, text, href) => {
      if (href.endsWith('.md') && !href.startsWith('http')) {
        let target = href;
        if (!href.startsWith('/')) {
          target = baseDir ? baseDir + '/' + href : href;
        }
        target = resolvePath(target);
        return `<a class="internal-link" data-target="${target}" href="#">${text}</a>`;
      }
      return `<a href="${href}" target="_blank" rel="noopener">${text}</a>`;
    })
    .replace(/\|(.+)\|\n\|[-| :]+\|\n((?:\|.+\|\n?)+)/g, (_, header, rows) => {
      const ths = header
        .split('|')
        .filter((c) => c.trim())
        .map((c) => `<th>${c.trim()}</th>`)
        .join('');
      const trs = rows
        .trim()
        .split('\n')
        .map((row) => {
          const tds = row
            .split('|')
            .filter((c) => c.trim())
            .map((c) => `<td>${c.trim()}</td>`)
            .join('');
          return `<tr>${tds}</tr>`;
        })
        .join('');
      return `<table><thead><tr>${ths}</tr></thead><tbody>${trs}</tbody></table>`;
    })
    .replace(/((?:^[ \t]*[-*+] .+\n?)+)/gm, (block) => {
      const items = block
        .trim()
        .split('\n')
        .map((line) => `<li>${line.replace(/^[ \t]*[-*+] /, '')}</li>`)
        .join('');
      return `<ul>${items}</ul>`;
    })
    .replace(/((?:^[ \t]*\d+\. .+\n?)+)/gm, (block) => {
      const items = block
        .trim()
        .split('\n')
        .map((line) => `<li>${line.replace(/^[ \t]*\d+\. /, '')}</li>`)
        .join('');
      return `<ol>${items}</ol>`;
    })
    .replace(/^(?!<[a-z]|$)(.+)$/gm, '<p>$1</p>');

  preBlocks.forEach((block, i) => {
    html = html.replace(`<span class="md-pre-hold" data-i="${i}"></span>`, block);
  });

  return html;
}

function resolvePath(path) {
  const parts = path.split('/');
  const resolved = [];
  for (const p of parts) {
    if (p === '..') resolved.pop();
    else if (p !== '.') resolved.push(p);
  }
  return resolved.join('/');
}

// ── Search (both sidebars) ─────────────────────────────────────────────────
let searchQuery = '';

searchEl.addEventListener('input', () => {
  searchQuery = searchEl.value.trim().toLowerCase();
  applySearch();
});

function applySearchForSidebar(sidebar, expanded) {
  const allNodes = sidebar.querySelectorAll('.tree-node');
  if (!searchQuery) {
    allNodes.forEach((node) => {
      node.querySelector('.tree-row').classList.remove('hidden');
      const label = node.querySelector('.label');
      if (label) label.innerHTML = label.dataset.rawName;
    });
    sidebar.querySelectorAll('.tree-children').forEach((c) => {
      const parentPath = c.parentElement.dataset.path;
      c.style.display = expanded.has(parentPath) ? 'block' : 'none';
    });
    return;
  }

  sidebar.querySelectorAll('.tree-children').forEach((c) => (c.style.display = 'block'));
  sidebar.querySelectorAll('.icon').forEach((ic) => {
    if (ic.textContent === '▸') ic.textContent = '▾';
  });

  allNodes.forEach((node) => {
    const row = node.querySelector('.tree-row');
    const label = row.querySelector('.label');
    if (!label) return;
    const name = label.dataset.rawName.toLowerCase();
    if (node.dataset.type === 'file') {
      if (name.includes(searchQuery)) {
        row.classList.remove('hidden');
        label.innerHTML = highlightMatch(label.dataset.rawName, searchQuery);
      } else {
        row.classList.add('hidden');
      }
    } else {
      const hasMatch = [...node.querySelectorAll('[data-type="file"] .label')].some((l) =>
        l.dataset.rawName.toLowerCase().includes(searchQuery)
      );
      row.classList.toggle('hidden', !hasMatch && !name.includes(searchQuery));
      label.innerHTML = highlightMatch(label.dataset.rawName, searchQuery);
    }
  });
}

function applySearch() {
  applySearchForSidebar(els.left.sidebar, expandedFoldersLeft);
  applySearchForSidebar(els.right.sidebar, expandedFoldersRight);
}

function highlightMatch(name, query) {
  const idx = name.toLowerCase().indexOf(query);
  if (idx < 0) return name;
  return (
    name.slice(0, idx) +
    `<mark>${name.slice(idx, idx + query.length)}</mark>` +
    name.slice(idx + query.length)
  );
}

// ── Keyboard shortcuts ─────────────────────────────────────────────────────
document.addEventListener('keydown', (e) => {
  if (e.key === 'Backspace' && e.altKey && e.shiftKey) goBack('right');
  else if (e.key === 'Backspace' && e.altKey) goBack('left');
  if ((e.metaKey || e.ctrlKey) && e.key === 'f') {
    e.preventDefault();
    searchEl.focus();
    searchEl.select();
  }
});

// ── Init ───────────────────────────────────────────────────────────────────
TREE.children.forEach((c) => {
  if (c.type === 'folder') {
    expandedFoldersLeft.add(c.path);
    expandedFoldersRight.add(c.path);
  }
});
buildSidebar('left');
buildSidebar('right');
</script>
</body>
</html>
"""

# ── Helpers ───────────────────────────────────────────────────────────────────

def count_files(node: dict) -> int:
    if node["type"] == "file":
        return 1
    return sum(count_files(c) for c in node.get("children", []))


def collect_paths(node: dict) -> list[str]:
    """Return a flat list of all file paths referenced in the tree."""
    if node["type"] == "file":
        return [node["path"]]
    paths = []
    for child in node.get("children", []):
        paths.extend(collect_paths(child))
    return paths


def copy_md_mirror(tree: dict, project_root: Path, dest_dir: Path) -> tuple[int, int]:
    """Copy every .md path in the tree into dest_dir, preserving layout."""
    dest_dir.mkdir(parents=True, exist_ok=True)
    paths = collect_paths(tree)
    copied = 0
    skipped = 0
    for rel_posix in paths:
        src = project_root / rel_posix
        dst = dest_dir / rel_posix
        if not src.exists():
            print(f"  ⚠️  Not found, skipping: {rel_posix}")
            skipped += 1
            continue
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dst)
        copied += 1
    return copied, skipped


def export_bundle(tree: dict, project_root: Path, export_dir: Path, html: str) -> None:
    """
    Copy all referenced .md files into export_dir, mirroring the folder
    structure relative to project_root, then write lab_navigator.html there.
    """
    copied, skipped = copy_md_mirror(tree, project_root, export_dir)
    html_dst = export_dir / "lab_navigator.html"
    html_dst.write_text(html, encoding="utf-8")

    print(f"  ✅ Copied {copied} .md files ({skipped} missing/skipped)")
    print(f"  ✅ Written lab_navigator.html")
    print()
    print(f"  📦 Bundle ready at: {export_dir}")
    print(f"  Share the entire folder, then the recipient runs:")
    print(f"     cd \"{export_dir}\"")
    print(f"     python -m http.server 8765")
    print(f"     # open http://localhost:8765/lab_navigator.html")



    print(f"     # open http://localhost:8765/lab_navigator_2026-05-02.html")


def export_snapshot_parent(tree: dict, project_root: Path, html: str, date_str: str) -> Path:
    """
    Write a versioned bundle in the parent directory of the project:
    <parent>/lab_navigator_YYYY-MM-DD/ with all .md files mirrored and
    lab_navigator_YYYY-MM-DD.html inside.
    """
    parent = project_root.parent
    bundle_dir = parent / f"lab_navigator_{date_str}"
    bundle_dir.mkdir(parents=True, exist_ok=True)
    copied, skipped = copy_md_mirror(tree, project_root, bundle_dir)
    html_name = f"lab_navigator_{date_str}.html"
    html_path = bundle_dir / html_name
    html_path.write_text(html, encoding="utf-8")

    print(f"  ✅ Snapshot: {copied} .md files ({skipped} missing/skipped)")
    print(f"  ✅ Written {html_name}")
    print()
    print(f"  📦 Versioned bundle: {bundle_dir}")
    print(f"     cd \"{bundle_dir}\"")
    print(f"     python -m http.server 8765")
    print(f"     # open http://localhost:8765/{html_name}")
    return bundle_dir


# ── Main ─────────────────────────────────────────────────────────────────────

def main():
    args = sys.argv[1:]

    # Parse --no-corpus
    include_corpus = True
    if "--no-corpus" in args:
        include_corpus = False
        args.remove("--no-corpus")

    # Parse --export <dir>
    export_dir: Path | None = None
    if "--export" in args:
        idx = args.index("--export")
        if idx + 1 >= len(args):
            print("❌ --export requires a directory argument")
            sys.exit(1)
        export_dir = Path(args[idx + 1]).expanduser().resolve()
        args.pop(idx); args.pop(idx)  # remove flag + value

    snapshot_parent = False
    if "--snapshot-parent" in args:
        snapshot_parent = True
        args.remove("--snapshot-parent")

    if args:
        print(f"❌ Unknown arguments: {args}")
        print(
            "   Usage: generate_navigator.py [--no-corpus] [--export <dir>] [--snapshot-parent]"
        )
        sys.exit(1)

    print(f"📂 Project root : {PROJECT_ROOT}")
    print(f"📄 Output       : {OUTPUT_FILE}")
    print(f"🧬 Corpus articles: {'included' if include_corpus else 'excluded (--no-corpus)'}")
    if export_dir:
        print(f"📦 Export bundle: {export_dir}")
    if snapshot_parent:
        snap_hint = PROJECT_ROOT.parent / f"lab_navigator_{date.today().isoformat()}"
        print(f"📸 Versioned snapshot will be written under: {snap_hint}")
    print()

    print("🔍 Walking filesystem…")
    tree = build_tree(PROJECT_ROOT, include_corpus=include_corpus)
    total = count_files(tree)
    corpus_note = "" if include_corpus else " (corpus articles excluded)"
    print(f"✅ Found {total} markdown files{corpus_note}")

    tree_json = json.dumps(tree, ensure_ascii=False, indent=None)
    html = HTML_TEMPLATE.replace("__TREE_JSON__", tree_json).replace("__FILE_COUNT__", str(total))

    # Always write to project root
    OUTPUT_FILE.write_text(html, encoding="utf-8")
    size_kb = OUTPUT_FILE.stat().st_size // 1024
    print(f"✅ Written {size_kb} KB → {OUTPUT_FILE.name}")

    if export_dir:
        print()
        print("📦 Building export bundle…")
        export_bundle(tree, PROJECT_ROOT, export_dir, html)

    if snapshot_parent:
        print()
        print("📸 Building versioned snapshot (parent of project folder)…")
        today = date.today().isoformat()
        export_snapshot_parent(tree, PROJECT_ROOT, html, today)

    if not export_dir:
        print()
        print("🚀 To open:")
        print(f"   cd {PROJECT_ROOT}")
        print(f"   python -m http.server 8765")
        print(f"   # then open http://localhost:8765/lab_navigator.html")


if __name__ == "__main__":
    main()

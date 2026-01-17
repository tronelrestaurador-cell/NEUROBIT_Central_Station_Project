#!/usr/bin/env python3
"""Simple Flask server to receive a text file, fragment it and write parts
into the local `fragments/` directory with headers following README format.

Usage:
  python3 scripts/fragment_server.py

POST /fragment
  form-data: file=@<file>, title=<optional>, author=<optional>, max_chars=<optional int>

Returns JSON: { created: <n>, files: [names...] }
"""
from flask import Flask, request, jsonify
import os
import re
from pathlib import Path

app = Flask(__name__)
BASE_DIR = Path(__file__).resolve().parent.parent
FRAGMENTS_DIR = BASE_DIR / 'fragments'
FRAGMENTS_DIR.mkdir(parents=True, exist_ok=True)


def split_paragraphs(text):
    # Robust split: one or more blank lines (allow spaces)
    parts = re.split(r'\n\s*\n+', text)
    return [p.strip() for p in parts if p.strip()]


def split_long_paragraph(p, max_chars):
    # Split paragraph by words to ensure no fragment exceeds max_chars
    words = re.split(r'\s+', p)
    chunks = []
    cur = ''
    for w in words:
        if cur:
            candidate = cur + ' ' + w
        else:
            candidate = w
        if len(candidate) > max_chars:
            if cur:
                chunks.append(cur)
            # If single word longer than max, force-split the word
            if len(w) > max_chars:
                # break word in parts
                for i in range(0, len(w), max_chars):
                    chunks.append(w[i:i+max_chars])
                cur = ''
            else:
                cur = w
        else:
            cur = candidate
    if cur:
        chunks.append(cur)
    return chunks


def build_header(idx, title, author, source):
    return (f"[FRAGMENT_ID]: {idx}\n"
            f"[TITLE]: \"{title or ''}\"\n"
            f"[AUTHOR]: {author or ''}\n"
            f"[SOURCE]: {source}\n"
            f"[CONTENT]:\n")


def next_index(prefix='parte_'):
    # scan existing files matching prefix and extract numeric suffix
    max_n = 0
    pattern = re.compile(rf"^{re.escape(prefix)}(\d+)\.txt$")
    for p in FRAGMENTS_DIR.iterdir():
        if p.is_file():
            m = pattern.match(p.name)
            if m:
                try:
                    n = int(m.group(1))
                    if n > max_n:
                        max_n = n
                except ValueError:
                    continue
    return max_n + 1


@app.route('/fragment', methods=['POST'])
def fragment_endpoint():
    if 'file' not in request.files:
        return jsonify({'error': 'no file provided'}), 400
    f = request.files['file']
    try:
        content = f.read().decode('utf-8')
    except Exception:
        # attempt with latin1 fallback
        content = f.read().decode('latin-1')

    title = request.form.get('title', '').strip()
    author = request.form.get('author', '').strip()
    max_chars = int(request.form.get('max_chars') or 5000)
    prefix = request.form.get('prefix') or 'parte_'

    paragraphs = split_paragraphs(content)
    fragments = []
    current = ''
    for p in paragraphs:
        if len(p) > max_chars:
            # break paragraph into safe chunks
            pieces = split_long_paragraph(p, max_chars)
            for piece in pieces:
                if current:
                    fragments.append(current)
                    current = ''
                fragments.append(piece)
        else:
            if current:
                if len(current) + 2 + len(p) <= max_chars:
                    current = current + '\n\n' + p
                else:
                    fragments.append(current)
                    current = p
            else:
                current = p
    if current:
        fragments.append(current)

    # starting index
    start = next_index(prefix=prefix)
    created = []
    pad = max(3, len(str(start + len(fragments))))
    for i, piece in enumerate(fragments, start=start):
        idx = str(i).zfill(pad)
        name = f"{prefix}{idx}.txt"
        header = build_header(idx, title, author, f.filename)
        path = FRAGMENTS_DIR / name
        with open(path, 'w', encoding='utf-8') as out:
            out.write(header + '\n' + piece + '\n')
        created.append(name)

    return jsonify({'created': len(created), 'files': created})


if __name__ == '__main__':
    # Run in development mode on 127.0.0.1:5000
    app.run(host='127.0.0.1', port=5000)

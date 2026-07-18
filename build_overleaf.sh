#!/bin/bash

# Directory for the Overleaf package
RELEASE_DIR="overleaf_release"

echo "Building Overleaf drag-and-drop folder..."
rm -rf "$RELEASE_DIR"
mkdir -p "$RELEASE_DIR"

# Copy the core style files
cp harvard-warwick.bbx "$RELEASE_DIR/"
cp harvard-warwick.cbx "$RELEASE_DIR/"

# Create a sample main.tex file for Overleaf users
cat << 'EOF' > "$RELEASE_DIR/main.tex"
\documentclass{article}
\usepackage[utf8]{inputenc}
\usepackage[style=harvard-warwick, backend=biber]{biblatex}
\addbibresource{references.bib}

\title{Sample Overleaf Document}
\author{Author Name}
\date{\today}

\begin{document}
\maketitle

This is a sample document using the Harvard Warwick citation style \parencite{sample}.

\printbibliography

\end{document}
EOF

# Create a sample references.bib file
cat << 'EOF' > "$RELEASE_DIR/references.bib"
@article{sample,
  author = {Smith, John},
  title = {A Sample Article},
  journaltitle = {Journal of Examples},
  year = {2024},
  volume = {1},
  number = {1},
  pages = {1--10}
}
EOF

echo "Done! You can now drag and drop the contents of the '$RELEASE_DIR' folder into your Overleaf project."

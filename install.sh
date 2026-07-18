#!/bin/bash

# Determine texmf directory
if [ "$(uname)" == "Darwin" ]; then
    TEXMF_DIR="$HOME/Library/texmf/tex/latex/biblatex-harvard-warwick"
else
    TEXMF_DIR="$HOME/texmf/tex/latex/biblatex-harvard-warwick"
fi

echo "Installing to $TEXMF_DIR..."
mkdir -p "$TEXMF_DIR"
cp harvard-warwick.bbx "$TEXMF_DIR/"
cp harvard-warwick.cbx "$TEXMF_DIR/"

# Update texhash if mktexlsr is available
if command -v mktexlsr >/dev/null 2>&1; then
    echo "Updating TeX tree..."
    mktexlsr "$HOME/Library/texmf" 2>/dev/null || mktexlsr "$HOME/texmf" 2>/dev/null || true
fi

echo "Installation complete!"

# Warwick & Cite Them Right `biblatex` Styles

This repository provides two highly accurate `biblatex` referencing styles:
1. **Harvard - Cite Them Right 13th Edition** (`harvard-ctr`)
2. **Harvard - University of Warwick Economics** (`harvard-warwick`)

Both styles support a unified `v12=true` package option, allowing you to easily downgrade to the 12th Edition formatting rules without needing to maintain parallel codebases.

## Downloads & Releases

This repository provides two different types of releases for your convenience:

* **CTAN-Style Release (`warwickbib-ctan.zip`)**: A complete archive containing the raw `.dtx` engines, manuals, `Makefile`, and the generated engine files. Ideal for local developers and system-wide TeX installations.
* **Overleaf-Ready Release (`warwickbib-overleaf.zip`)**: A streamlined, minimal archive containing *only* the compiled engine files (`.bbx`, `.cbx`, `.lbx`). This is perfect for drag-and-dropping directly into an Overleaf project or a local project folder.

## Installation

### 1. Online Editors (e.g., Overleaf)
The easiest way to use these styles is per-project.
1. Download the `warwickbib-overleaf.zip` archive from the Releases page.
2. Unzip the contents directly into the root folder of your Overleaf project (or local LaTeX project).
3. Ensure the `.bbx`, `.cbx`, and `.lbx` files are alongside your main `.tex` file.

### 2. Local Installation (Mac / Linux)
To install the package system-wide so it is available to all local projects:
1. Download the `warwickbib-ctan.zip` archive.
2. Locate your local `texmf` tree (you can find it by running `kpsewhich -var-value=TEXMFHOME` in your terminal).
3. Copy the `.bbx`, `.cbx`, and `.lbx` files into `~/Library/texmf/tex/latex/warwickbib/` (Mac) or `~/texmf/tex/latex/warwickbib/` (Linux).
4. Run `texhash` in your terminal.

### 3. Local Installation (Windows / MiKTeX)
1. Download the `warwickbib-ctan.zip` archive.
2. Find your local `texmf` directory (usually `C:\Users\<Name>\AppData\Local\MiKTeX\texmf`).
3. Place the `.bbx`, `.cbx`, and `.lbx` files into `\tex\latex\warwickbib\`.
4. Open the MiKTeX Console, go to **Tasks**, and click **Refresh file name database**.

## Usage

Load the package in your preamble. To use the Cite Them Right standard:

```latex
\usepackage[style=harvard-ctr, backend=biber]{biblatex}
```

To use the Warwick Economics adaptation:

```latex
\usepackage[style=harvard-warwick, backend=biber]{biblatex}
```

### 12th Edition Backward Compatibility
If your institution still strictly requires the older 12th edition of Cite Them Right, you can easily toggle it using the native `v12` option:

```latex
\usepackage[style=harvard-warwick, backend=biber, v12=true]{biblatex}
```

## Compilation

These packages use `biblatex` and require **Biber** to compile the bibliography.
Standard compilation sequence:
1. `lualatex main.tex`
2. `biber main`
3. `lualatex main.tex`

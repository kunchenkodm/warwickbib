# Cite Them Right / Warwick Harvard Referencing Styles

This repository contains robust, programmatic implementations of the **Harvard Referencing Style** based on the *Cite Them Right* (CTR) standards, with specific overrides for the University of Warwick (Economics) style.

Implementations are provided for both **LaTeX (BibLaTeX/Biber)** and **Citation Style Language (CSL)** (used by Zotero, Mendeley, and Word).

## Available Versions and Releases

We maintain four distinct versions of the style to ensure strict compliance depending on your target guidelines. All packages are pre-compiled and available on the [GitHub Releases](../../releases) page:

1. **Cite Them Right 13th Edition (Warwick Economics)**
   * Based on the CTR 13th edition.
   * Includes Warwick strict overrides (e.g., retains publisher location for books, uses `Available at:` URL labels).
   * **[Download v13.0.0-warwick](../../releases/tag/v13.0.0-warwick)**

2. **Cite Them Right 13th Edition (Standard)**
   * Pure CTR 13th edition compliance (non-Warwick).
   * Drops publisher location for books, drops `Available at:` URL labels.
   * **[Download v13.0.0-standard](../../releases/tag/v13.0.0-standard)**

3. **Cite Them Right 12th Edition (Warwick Economics)**
   * Based on the older CTR 12th edition standard.
   * Includes Warwick overrides.
   * **[Download v12.0.0-warwick](../../releases/tag/v12.0.0-warwick)**

4. **Cite Them Right 12th Edition (Standard)**
   * Pure CTR 12th edition compliance.
   * **[Download v12.0.0-standard](../../releases/tag/v12.0.0-standard)**

---

## Installation & Quick Start

Each GitHub Release contains two ZIP files depending on your workflow:

### 1. Overleaf / LaTeX Users (`overleaf-package-*.zip`)
If you are writing in LaTeX (e.g., Overleaf) and just want to use the style:
1. Download the `overleaf-package-*.zip` from your desired release.
2. Extract and drag-and-drop the `.bbx` and `.cbx` files directly into your Overleaf project's root directory.
3. Import the style in your `main.tex` using:
   ```latex
   \usepackage[style=harvard-warwick, backend=biber]{biblatex}
   % (Use style=harvard-ctr if you downloaded the Standard edition)
   ```
4. Compile your document using Biber!

### 2. Zotero / Mendeley / Word Users (`biblatex-csl-package-*.zip`)
If you are using a reference manager:
1. Download the `biblatex-csl-package-*.zip` from your desired release.
2. Inside the `csl/` folder, you will find the `.csl` style file.
3. Import this `.csl` file into Zotero, Mendeley, or Microsoft Word to automatically format your citations according to the exact guidelines.

---

## Technical Details
This repository uses programmatic patching (via Python scripts and Biber sourcemaps) to automatically clean up dirty metadata exports. For example, it will automatically strip redundant issue numbers when a publisher erroneously outputs `OnlineFirst` as a volume, and suppresses redundant URLs when a DOI is provided. You do *not* need to manually clean your `.bib` files.

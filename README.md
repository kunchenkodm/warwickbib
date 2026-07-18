# Programmatic implementations of the University of Warwick (Economics) Harvard referencing style

## BibTeX and biblatex styles

This repository contains a LaTeX implementation of the
[Harvard referencing style][warwick-harvard] recommended by the University of Warwick Library and Economics Department.
It is based on the *Cite Them Right* 13th edition standards with the necessary Warwick overrides (such as retaining the place of publication for books and single quoting journal article titles).

  + `harvard-warwick.bbx` and `harvard-warwick.cbx`
    contains the implementation for use with [biblatex] and [Biber].

[warwick-harvard]: https://warwick.ac.uk/services/library/students/referencing/referencing-styles/harvard/
[biblatex]: https://ctan.org/pkg/biblatex
[Biber]: https://ctan.org/pkg/biber


## Citation Style Language (CSL)

This repository also contains a [CSL implementation](csl/) for maintaining the Warwick Harvard style in [Citation Style Language] (used by tools like Zotero and Mendeley).

You can find the standard CSL file at `csl/harvard-warwick.csl`.

[Citation Style Language]: http://docs.citationstyles.org/en/stable/


## Quick Start (Overleaf / LaTeX)

1. Run the included `./build_overleaf.sh` script to automatically generate a pre-packaged `overleaf_release` directory.
2. Drag and drop the `harvard-warwick.bbx` and `harvard-warwick.cbx` files into your Overleaf project's root folder.
3. Import the style in your `main.tex` using:
   ```latex
   \usepackage[style=harvard-warwick, backend=biber]{biblatex}
   ```
4. Compile with Biber and you are good to go!

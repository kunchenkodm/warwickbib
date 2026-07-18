WW_NAME=harvard-warwick
CTR_NAME=harvard-ctr

all: source $(WW_NAME).pdf $(CTR_NAME).pdf
	@echo "All outputs generated successfully."

source: $(WW_NAME).dtx $(CTR_NAME).dtx
	luatex -interaction=batchmode $(CTR_NAME).dtx >/dev/null
	luatex -interaction=batchmode $(WW_NAME).dtx >/dev/null

$(CTR_NAME).pdf: $(CTR_NAME).dtx source
	latexmk -silent -lualatex -interaction=batchmode $< >/dev/null
	@echo "Compilation of $(CTR_NAME) complete."

$(WW_NAME).pdf: $(WW_NAME).dtx source
	latexmk -silent -lualatex -interaction=batchmode $< >/dev/null
	@echo "Compilation of $(WW_NAME) complete."

test: source
	latexmk -silent -pdflatex -interaction=batchmode test_run.tex >/dev/null

release:
	python3 release_automation.py

distclean: clean
	rm -f $(CTR_NAME).{pdf,bib,ins,bbx,cbx} english-ctr.lbx british-ctr.lbx
	rm -f $(WW_NAME).{pdf,bib,ins,bbx,cbx} english-warwick.lbx british-warwick.lbx
	rm -f *-release.zip

clean:
	rm -f $(CTR_NAME).aux $(CTR_NAME).bbl $(CTR_NAME).bcf $(CTR_NAME).blg $(CTR_NAME).fdb_latexmk $(CTR_NAME).fls $(CTR_NAME).listing $(CTR_NAME).log $(CTR_NAME).out $(CTR_NAME).run.xml \
	      $(WW_NAME).aux $(WW_NAME).bbl $(WW_NAME).bcf $(WW_NAME).blg $(WW_NAME).fdb_latexmk $(WW_NAME).fls $(WW_NAME).listing $(WW_NAME).log $(WW_NAME).out $(WW_NAME).run.xml \
	      test_run.aux test_run.bbl test_run.bcf test_run.blg test_run.fdb_latexmk test_run.fls test_run.listing test_run.log test_run.out test_run.run.xml

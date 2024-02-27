##
# LaTeX numerical presentation
#
# @file
# @version 0.1

ALGORITHMS = algorithms/algorithms.py

ORIGCSV = tables/bisection.csv tables/newton.csv tables/secant.csv
PROCESSCSV = tables/bisectionrel.csv tables/newtonrel.csv tables/secantrel.csv
PLOTS = plots/bisectionrel.png plots/newtonrel.png plots/secantrel.png plots/ffp.png plots/ffull.png

TEXFILES = $(wildcard *.tex)
PDFFILES = $(TEXFILES:.tex=.pdf)

all: $(ORIGCSV) $(PROCESSCSV) $(PLOTS) $(PDFFILES)

$(ORIGCSV): $(ALGORITHMS)
	python3 -m algorithms.algorithms

$(PROCESSCSV): $(ORIGCSV)
	python3 -m tables.process

$(PLOTS): $(PROCESSCSV)
	python3 -m plots.plots

%.pdf: %.tex $(PLOTS)
	pdflatex -shell-escape $<

clean:
	rm -f *.aux *.log *.fdb_latexmk *.fls *.dvi
	rm -rf _minted-*
	rm -rf *.synctex.gz


# end

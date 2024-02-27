From the root directory, run

`python -m algorithms.algorithms`

`python -m plots.plots`

`python -m tables.process`

The order matters, `tables.process` modifies the .csv files in-place to format for printing.

Then, to compile the LaTeX, run

`latexmk -pdf -pvc -shell-escape FILENAME.tex`

for each .tex file.

Alternatively, run

`make` to regenerate all pdfs, and `make clean` to clean up latex build files.
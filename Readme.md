**Spring 2024 $\LaTeX$ Workshop**
---

In this workshop, learn good practices for communicating numerical results through LaTeX. Attendees will become familiar with popular LaTeX packages for writing algorithms/pseudocode, presenting and formatting source code, organizing and managing their plots, and presenting numerical results in a table alongside.

While attendees are expected to have a working knowledge of LaTeX, all materials will be provided through Overleaf, a free-to-use LaTeX editor. Participants have the option to either log in to Overleaf and follow along or observe through Zoom. Everyone will be given a copy of the LaTeX files in advance.

If you do not have an account already, you may create one via https://www.overleaf.com/register.

Link to complete project on Overleaf: https://www.overleaf.com/read/djprbvswgxmj#437502

Link to participant project on Overleaf: https://www.overleaf.com/read/ycxywkgbpzfk#c52172

Usage
---

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

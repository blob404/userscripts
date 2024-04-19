#!/usr/bin/env python3

import os
import sys
import pdf2bib

pdfname = sys.argv[1] # get filename from first argument
bib = pdf2bib.pdf2bib(pdfname)

home_folder = os.getenv("HOME")

# append bibtex to file
bib_filepath = os.getenv("ORG_BIB_FILEPATH", os.path.join(home_folder, "/tmp/hazel.bib"))
with open(bib_filepath, "a") as f:
    f.write(bib['bibtex'] + "\n\n")

# set filename in same format as pdf2bib article index
firstauthor = bib['metadata']['author'][0]['family']
year = bib['metadata']['year']
title = bib['metadata']['title'].split()[0] # first word
fname = '%s%s%s.pdf' % (firstauthor, year, title)
fname = fname.lower()

# move file
pdf_current_path = os.path.abspath(pdfname)
pdf_target_path = os.getenv("ORG_PDF_FILEPATH", os.path.join(home_folder, "/tmp/papers"))
os.rename(pdf_current_path, os.path.join(pdf_target_path, fname))

#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

# combinePdfs.py - Combines all the PDFs in the current working directory into a single PDF

import PyPDF2, os

# Get all the PDF filenames
from PyPDF2.utils import PdfReadError

pdfFiles = []
for filename in os.listdir('.'):
    if filename.endswith('.pdf'):
        pdfFiles.append(filename)

pdfFiles.sort(key=str.lower)

pdfWriter = PyPDF2.PdfFileWriter()

# Loop through all the PDF files
for filename in pdfFiles:
    pdfFileObj = open(filename, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    if pdfReader.isEncrypted:
        continue
    # Loop through all the pages (except the first) and add them
    for pageNum in range(1, pdfReader.numPages):
        try:
            pageObj = pdfReader.getPage(pageNum)
            pdfWriter.addPage(pageObj)
        except RuntimeError as e:
            continue
# TODO: Save the resulting PDF to a file.
pdfOutput = open('allminutes.pdf', 'wb')
pdfWriter.write(pdfOutput)
pdfOutput.close()

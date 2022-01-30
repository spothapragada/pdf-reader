import pandas as pd
import numpy as np
import requests
import PyPDF2

if '__name__' == '__main__':
    # Import and read the pdf file
    pdfFileObj = open('Home Inspection.pdf', 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    num_pages = pdfReader.numPages
    count = 0
    text = ""
    while count < num_pages:
        pageObj = pdfReader.getPage(count)
        count += 1
        text += pageObj.extractText()
    # print(text)
    # Split the text into lines
    lines = text.split('\n')
    # Create a dataframe with the lines
    df = pd.DataFrame(lines)
    # Remove the empty lines
    df = df[df.columns[0] != '']


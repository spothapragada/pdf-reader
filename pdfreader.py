import PyPDF2
import pandas as pd
import logging

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')


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

    print("I found the following lines:")
    print(df)



    try:
        # Create a csv file with the dataframe
        df.to_csv('Home Inspection.csv', index=False)
    except Exception as e:
        print(e)
        count
    
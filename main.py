import pdfplumber

text = ''

file = open("dupa.txt", "r+")

with pdfplumber.open('statement.pdf') as pdf:
    # iterate over each page
    for page in pdf.pages:
        # extract text
        text += page.extract_text()

print(text)

file.write(text)
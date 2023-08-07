import pdfplumber
import re
from datetime import datetime

text = ''

file = open("dupa.txt", "r+")

with pdfplumber.open('statement.pdf') as pdf:
    # iterate over each page
    for page in pdf.pages:
        # extract text
        text += page.extract_text()

print(text)

file.write(text)

match_str = re.search(r"\d{1,2}\.\d{1,2}\.\d{2,4} \d{1,2}\.\d{1,2}\.\d{2,4}", text)

print(match_str)

# for element in text:
#     if element 
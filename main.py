import pdfplumber
import re
from datetime import datetime
import openai

openai.api_key = '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'

messages = [ {"role": "system", "content": 
              "You are a intelligent assistant."} ]

text = ''

file = open("dupa.txt", "r+")

with pdfplumber.open('statement.pdf') as pdf:
    # iterate over each page
    for page in pdf.pages:
        # extract text
        text += page.extract_text()

file.write(text)

match_str = re.search(r"-?\d+,\d+ \d+ \d+,\d+", text)
match_pos = match_str.span()[1]


# for element in text:
#     if element 
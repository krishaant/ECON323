import pdfplumber
import re 
import pandas as pd 
import json 
import unicodedata

pdf_path = "/Users/krishaantpathmanathan/ECON323 final projext/financial_info/FY21-UBC-Statement-of-Financial-Information.pdf"

with pdfplumber.open(pdf_path) as pdf: 
        text = "\n".join([page.extract_text() for page in pdf.pages if page.extract_text()])

pattern = r'([A-Za-z]+,\s[A-Za-z]+)\s+([\d,]+)' # I asked GPT for help with this 

matches = re.findall(pattern, text)

for match in matches : 
    name, salary = match    
    print(f'Name : {Name}, Salary : {Salary}')

data = pd.DataFrame(matches, columns = ["Name", "Salary"])

data.to_csv("UBC_Professor_Salaries.csv", index = False)

print("done")


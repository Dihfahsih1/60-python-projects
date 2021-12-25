import pdfplumber

with pdfplumber.open("pdf1.pdf") as pdf:
    first_page = pdf.pages[0]
    print(first_page.chars[0])
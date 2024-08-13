import PyPDF2
# PDF = Portable Document Format

f = open("Working_Business_Proposal.pdf", mode="rb") # Read Binary
pdf_reader =PyPDF2.PdfReader(f)
print(len(pdf_reader.pages))

page_one_text = pdf_reader.pages[0].extract_text()

f.close()

f = open("Working_Business_Proposal.pdf", mode="rb")

pdf_reader = PyPDF2.PdfReader(f)
first_page = pdf_reader.pages[0]

pdf_writer = PyPDF2.PdfWriter()
pdf_writer.add_page(first_page)

pdf_output = open("Some_BrandNew_Doc.pdf", "wb")
pdf_writer.write(pdf_output)

f.close()
pdf_output.close()
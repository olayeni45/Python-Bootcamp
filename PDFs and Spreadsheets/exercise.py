import csv, requests, re, PyPDF2

csv_filestream = open("Exercise_Files\\find_the_link.csv", encoding="utf-8")
csv_data = csv.reader(csv_filestream)
data_lines = list(csv_data)

n = 0
link_list = []

for line in data_lines:
    link_list.append(data_lines[n][n]) # Diagonal
    n += 1

link = ''.join(link_list)
id_regex = re.search(r"id=\w*", link)
id = id_regex.group().replace("id=", "")

download_link = f"https://drive.google.com/uc?export=download&id={id}"
print(download_link)

download = requests.get(download_link)
print(download)

with open("tempdata.pdf", "wb") as f:
    f.write(download.content)

csv_filestream.close()

# PDF
phone_pattern = r"\d{3}\W\d{3}\W\d{4}"

with open("tempdata.pdf", "rb") as f:
    pdf_reader = PyPDF2.PdfReader(f)
    for page in range(len(pdf_reader.pages)):
        page_text = pdf_reader.pages[page].extract_text()

        phone_number = re.search(phone_pattern, page_text)
        if(phone_number):
            print(phone_number.group())

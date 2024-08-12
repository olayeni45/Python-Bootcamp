import shutil, os, re

#shutil.unpack_archive("unzip_me_for_instructions.zip", "", "zip")
folder_path = f"{os.getcwd()}\\extracted_content"
phone_pattern = r'\d{3}-\d{3}-\d{4}'

def search(file, pattern=r'\d{3}-\d{3}-\d{4}'):
    f = open(file, "r")
    text = f.read()

    if re.search(pattern, text):
        return re.search(pattern, text)
    else:
        return ""
    
results = []

for folder, sub_folders, files in os.walk(folder_path):

    for file in files:
        full_path = f"{folder}\\{file}"
        results.append(search(full_path))

for r in results:
    if (r != ''):
        print(r.group())

# with open('extracted_content/Instructions.txt') as f:
#     content = f.read()
#     print(content)

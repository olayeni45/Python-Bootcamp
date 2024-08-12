import zipfile, shutil

f = open("fileone.txt", 'w+')
f.write("ONE File, File One")
f.close()

f = open("filetwo.txt", 'w+')
f.write("Two File, File Two")
f.close()

compressed_file = zipfile.ZipFile("comp_file.zip", 'w')
compressed_file.write("fileone.txt", compress_type=zipfile.ZIP_DEFLATED)
compressed_file.write("filetwo.txt", compress_type=zipfile.ZIP_DEFLATED)
compressed_file.close()

zip_obj = zipfile.ZipFile("comp_file.zip", 'r')
zip_obj.extractall("extracted_content")

dir_to_zip = "extracted_content"
output_file_name = "example"

shutil.make_archive(output_file_name, "zip", dir_to_zip) # Preferrable method
shutil.unpack_archive("example.zip", "final_unzip", "zip")
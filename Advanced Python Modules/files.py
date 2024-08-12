import os, shutil, send2trash

print(os.getcwd())

print(os.listdir())

f = open("practice.txt", "w+")
f.write("This is a test string")
f.close()

#shutil.move("practice.txt", "C:\\Users\\tils")
#send2trash.send2trash("practice.txt")

for folder, sub_folders, files in os.walk(os.getcwd()):
    print(f"Currently looking at {folder}")
    print("\n")

    print("The subfolders are: ")
    for sub_fold in sub_folders:
        print(f"Subfolder: {sub_fold}")
        for f in files:
            print(f"File: {f}")
    
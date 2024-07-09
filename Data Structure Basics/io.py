textFile = "test.txt"

#Reading, Writing, Appending Modes
# mode='r' is read only
# mode='w' is write only (will overwrite files or create new)
# mode='a' is append only (will add on to files)
# mode='r+' is reading and writing
# mode='w+' us writing and reading (overwrites existing files or creates a new file)

#Reading files
myfile = open(textFile)
myfile.seek(0) #To bring the cursor back to the beginning of the text

print(myfile.read())
print(myfile.readlines())
myfile.close()

with open(textFile) as fileStream:
    contents = fileStream.read()
    print(contents)

#Writing files
newTextFile = "New_Test.txt"

with open(newTextFile, mode="w") as fileStream:
    fileStream.write("Four on the fourth")


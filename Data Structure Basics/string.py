mystring = "abcdefghijk"

#to get the first n characters (abc)
# n (up to the index but not including)
print(mystring[:3])

#to get the characters after a specific point (cdefghijk)
print(mystring[2:])

print(mystring[3:6]) #def

print(mystring[6:9]) #ghi

#6:9 start and include the character at index 6, end and don't include the character at index 9

print(mystring[::2]) #jump 2 characters (acegik)

#reverse a string
print(mystring[::-1])

#String Interpolation
print("This is a string {}".format('INSERTED'))

print("The {} {} {}".format("quick", "brown", "fox"))
print("The {2} {0} {1}".format("quick", "brown", "fox"))

name = "Jose"
print(f"Hello, his name is {name}")
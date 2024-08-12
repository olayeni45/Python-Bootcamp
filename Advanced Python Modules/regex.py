import re

text = "The agent's phone number is 408-555-1234. Call soon!"
pattern = "phone"
match = re.search(pattern, text)
matches = re.findall(pattern, text)

print(matches)

for match in re.finditer(pattern, text):
    print(match.group())

# Character Identifiers
# \d => Digits
# \w => Alphanumeric
# \s => Whitespace
# \D => Non-Digit
# \W => Non-Alphanumeric
# \S => Non-Whitespace

# Quantifiers
# + => occurs one or more times
# {3} => occurs exactly 3 times
# {2,4} => occurs 2 to 4 times
# {3,} => occurs 3 or more
# * => occurs zero or more times
# ? => once or none

phone = re.search(r"\d{3}-\d{3}-\d{4}", text) # Add 'r' before the string to tell python it's a regex
print(phone.group()) # to grab the phone num

phone_pattern = re.compile(r'(\d{3})-(\d{3})-(\d{4})')
results = re.search(phone_pattern, text)
print(results.group())
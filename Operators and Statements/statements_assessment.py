# Task 1
st = "Print only the words that start with s in this sentence"
for word in st.split(" "):
    if word.lower().startswith("s"):
        print(word)

# Task 2
evenNumbers = list(range(0, 11, 2))
print(evenNumbers)

# Task 3
divisbleBy3 = [num for num in range(1,51) if num%3 == 0]
print(divisbleBy3)

# Task 4
st = "Print every word in this sentence that has an even number of letters"
for word in st.split(" "):
    if len(word) %2 == 0:
        print(f"Even! Word = {word}")

# Task 5
nums = list(range(1, 101))
for num in nums:
    if (num%3 == 0) and (num%5==0):
        print(f"FizzBuzz: {num}")
    elif num%3 == 0:
        print(f"Fizz {num}")
    elif num%5 == 0:
        print(f"Buzz {num}")

# Task 6
st = "Create a list of the first letters of every word in this string"
# words = [word for word in st.split(" ")]
firstLetters = [word[0] for word in st.split(" ")]
print(firstLetters)
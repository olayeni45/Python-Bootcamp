import string

print("---Rad---")
def vol(rad):
    return (4/3) * 3.14 * (rad**3)

print(vol(2))

print("---Given range---")
def ran_check(num, low, high):
   # return num in range(low, high+1)
    for x in range(low, high+1):
        if x == num:
            return True
    
    return False

print(ran_check(5,2,7))

print("---Upper and Lower---")
def up_low(s):
    upperList = []
    lowerList=[]

    for char in s:
        if(str(char).isupper()):
            upperList.append(char)
        elif (str(char).islower()):
            lowerList.append(char)

    print(f"Original String: {s}")
    print(f"No. of Upper case characters: {len(upperList)}")
    print(f"No. of lower case characters: {len(lowerList)}")

up_low('Hello Mr. Rogers, how are you this fine Tuesday?')

print("---Unique elements---")
def unique_list(lst):
    return list(set(lst))

print(unique_list([1,1,1,1,1,2,3,3,3,4,3,3,5,5]))

print('---Multiply all numbers---')
def multiply(numbers):
    sum = 1
    for num in numbers:
        sum *= num
    
    return sum
print(multiply([1,2,3,-4]))

print("---Palindrome---")
def palindrome(s):
    s = str(s).replace(" ", "")
    reversedString = s[::-1]
    return reversedString == s

print(palindrome("nurses run"))

print("---Pangram---")
def isPangram(str1, alphabet=string.ascii_lowercase):
    str1 = str(str1).replace(" ", "").lower()
    stringIndexes = []

    for char in str1:
        index = alphabet.find(char)
        stringIndexes.append(index)
    
    uniqueIndexes = list(set(stringIndexes))
    return len(uniqueIndexes) == 26

print(isPangram("The quick brown fox jumps over the lazy dog"))
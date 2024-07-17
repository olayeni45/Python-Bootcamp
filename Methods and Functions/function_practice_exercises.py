# Warm Up Section
print("---Lesser of Two Evens---")
def lesser_of_two_evens(a,b):
    if (a%2 == 0) and (b%2 == 0):
        return min(a,b)
    else:
        return max(a,b)

print(lesser_of_two_evens(2,4))
print(lesser_of_two_evens(2,5))

# Animal Crackers
print("---Animal Crackers---")
def animal_crackers(text):
    textList = str(text).split(" ")
    firstWord = textList[0]
    secondWord = textList[1]

    return firstWord[0].lower() == secondWord[0].lower()

print(animal_crackers("Levelheaded Llama"))
print(animal_crackers("Crazy Kangaroo"))

# Makes Twenty
print("---Makes Twenty---")
def makes_twenty(n1, n2):
    numberSum = n1+n2
    if numberSum==20 or n1==20 or n2==20:
        return True
    else:
        return False

print(makes_twenty(20,10))
print(makes_twenty(12,8))
print(makes_twenty(2,3))

#Level 1 Problems
print("---Old Macdonald")
def old_macdonald(word):
    result = ""

    for index,letter in enumerate(word):
        if index == 0 or index == 3:
            result += str(letter).upper()
        else:
            result+= str(letter)

    return result

print(old_macdonald("macdonald"))

print("---Master Yoda")
def master_yoda(text):
    words = str(text).split(" ")
    result = []

    for word in reversed(words):
        result.append(word)
    
    return " ".join(result)

print(master_yoda("I am home"))
print(master_yoda("We are ready"))

print("---Almost There---")
def almost_there(n):
    is100 = abs(100-n) >= 0 and abs(100-n) <= 10
    is200 = abs(200-n) >= 0 and abs(200-n) <= 10

    return is100 or is200

print(almost_there(90))
print(almost_there(104))
print(almost_there(150))
print(almost_there(209))

# Level 2 Problems
print("---Find 33----")
def has_33(numList = []):
    for i, num in enumerate(numList):
        if i != len(numList) - 1:
            if(numList[i] == 3 and numList[i+1] == 3):
                return True
            else:
                pass
    
    return False

print(has_33([1,3,3]))
print(has_33([1,3,1,3]))
print(has_33([3,1,3]))

print("---Paper Doll---")
def paper_doll(text):
    result = ""

    for letter in text:
        for i in range(0,3):
            result += letter

    return result

print(paper_doll("Hello"))
print(paper_doll("Mississippi"))

print("---Black Jack---")
def blackjack(a,b,c):
    numSum = a+b+c
    result = 0
    #and (a==11 or b==11 or c==11)

    if numSum <= 21:
        result = numSum
    elif numSum > 21 and (a==11 or b==11 or c==11) :
        result = numSum - 10   
    
    if result > 21:
        return "BUST"
    
    return result
    
print(blackjack(5,6,7))
print(blackjack(9,9,9))
print(blackjack(9,9,11))

print("---Summer of 69---")
def summer_69(numList):
    numSum = 0
    numList = list(numList)

    for i, num in enumerate(numList):
        if 6 in numList and 9 in numList:
            index_six = numList.index(6)
            index_nine = numList.index(9)

            if i >= index_six and i <= index_nine:
                pass
            else:
                numSum += num
            
        else:
            numSum += num

    return numSum

print(summer_69([1,3,5]))
print(summer_69([4,5,6,7,8,9]))
print(summer_69([2,1,6,9,11]))
    

# Challenging Problems
print("---Spy Game---")
def spy_game(numList):
   result = ""

   for num in numList:
       if num == 0 or (num==0 and result=="0"):
           result += str(num)
       elif num==7 and result=="00":
           result += str(num)

   return result == "007"    

print(spy_game([1,2,4,0,0,7,5]))
print(spy_game([1,0,2,4,0,5,7]))
print(spy_game([1,7,2,0,4,5,0]))

print("---Count Prime---")
def count_primes(num):
    if num < 2:
        return 0
    
    primes = [2]
    x = 3

    while x <= num:
        for y in range(3,x,2):
            if x%y==0:
                x+=2
                break
        else:
            primes.append(x)
            x+= 2
    
    print(primes)
    return len(primes)

print(count_primes(100))
print("--Task 1--")
try:
    for i in ['a', 'b', 'c']:
        print(i**2)
except:
    print("Exception occured")

print("--Task 2--")
try:
    x=5
    y=0
    z = x/y
except:
    print("Error occured")
finally:
    print("All Done")

print("--Task 3--")
def ask():
    while True:
        try:
            result = int(input("Input an integer: "))            
        except:
            print("An error occured! Please try again")
            continue
        else:
            print(f"Thank you, your number squared is: {result**2}")
            break
ask()
term=int(input("Enter a number: "))
try:
    if term%2==0:
        print("Number is even")
    else:
        print("Number is odd")
except:
    print("Number is neither odd nor even")
lowestValue = int(input("Enter the lowest number to be included in this Fizz Buzz program:"))
highestValue = int(input("Enter the highest number to be included in this Fizz Buzz program:"))
highestValue += 1
multipleOne = int(input("Enter the first multiple to indicate Fizz/Buzz/FizzBuzz:"))
multipleTwo = int(input("Enter the second multiple to indicate Fizz/Buzz/FizzBuzz:"))

for i in range(lowestValue,highestValue): #Outputs numbers from lowestValue to highestValue, depending on the conditions below.
    if i%multipleOne and i%multipleTwo != 0: #If number is neither Fizz or Buzz.
        print(i) #Return the number.
    elif i%multipleOne == 0: #Else if the number is a multiple of multipleOne:
        if i%multipleTwo == 0: #And if it's a multiple of multipleTwo:
            print("FizzBuzz") #Output "FizzBuzz"
        else: #Otherwise:
            print("Fizz") #Return "Fizz" (Multiple of multipleOne).
    elif i%multipleTwo == 0: #If the number is a multiple of multipleTwo:
        if i%multipleOne == 0: #And if it's a multiple of multipleOne:
            print("FizzBuzz") #Output "FizzBuzz".
        else: #Otherwise:
            print("Buzz") #Return "Buzz" (Multiple of multipleTwo).
        

'''
#Notes:
Conditions:     
#i % 3
#i % 5
#(i % 3) and (i % 5)

for i in range(1,101):
    if (i % 3) == 0:
        if (i % 5) == 0:
            print("FizzBuzz")
        else:
            print("Fizz")
    if (i % 5) == 0:
        print("Buzz")
    else:
        print(i)

3 and 5 are the default values for multiples however I've changed them to variables to avoid hardcoding.
'''

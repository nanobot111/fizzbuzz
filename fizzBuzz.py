n = input("Give me a number: ")

def fizzBuzz(n):
    i = 0
    while i > 0 and i <= n:
        if (i%3 != 0) and (i%5 != 0):
            print (i)
            i += 1
        if (i%3 == 0) and (i%5 != 0):
            print ("Fizz")
            i += 1
        if (i%3 != 0) and (i%5 == 0):
            print ("Buzz")
            i += 1
        if (i%3 == 0) and (i%5 == 0):
            print ("FizzBuzz")
            i += 1

fizzBuzz(n)

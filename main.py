#WRITE YOUR CODE IN THIS FILE

#define factorial
def factorial(x):

    #define temp variable
    total = 1
    
    #for loop
    for i in range(1,x+1):
        total = total * i
    return total
print(factorial(5))
#
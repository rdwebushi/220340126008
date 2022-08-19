number = int(input('Enter a number'))
# Define a function to factorial
def factorial(num):
     return 1 if (num==1 or num==0) else num * factorial(num - 1);
 
# print the output
print("Square of ",number, "is ", factorial(number))

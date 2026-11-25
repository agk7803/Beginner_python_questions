# Create a function called is_prime(num) that:
# - Accepts an integer.
# - Checks whether it is prime.
# - Returns True if prime, otherwise False.



def is_prime(num):

 if num <=1:
    return False
 
 for i in range(2,num):
    if num % i ==0:
        return False

    else:
       return True

print(is_prime(num = int(input("Enter an integer: "))))
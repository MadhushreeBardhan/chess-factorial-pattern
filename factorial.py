#quetion-2 Assignment-1
def factorial(n): 
       
    if n == 0: 
        return 1
      
    return n * factorial(n-1)
factorial(int(input("enter number to find factorial")))
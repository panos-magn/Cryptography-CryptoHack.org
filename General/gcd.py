def GCD(x, y): 
  
   while(y): 
       x, y = y, x % y 
  
   return x

a = 66528
b = 52920
print ("The gcd of 66528 and 52920 is : ",end="") 
print (GCD(a,b))
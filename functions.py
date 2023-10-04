def hello():
   "Hello this is Hello fuction"
   print ("Hello World")
   return
hello()


# Function definition is here
def printme( str ):
   "This prints a passed string into this function"
   print (str)
   return;
# Now you can call printme function
printme("Sairaj Gad")
printme("Bharat is Best")



def add(x,y):
   z=x+y
   return z

a=10
b=20
result = add(a,b)
print ("a = {} b = {} a+b = {}".format(a, b, result))
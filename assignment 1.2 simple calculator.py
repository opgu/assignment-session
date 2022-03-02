def addition(num1,num2):
    result = num1 + num2
    print ("{0} + {1} = {2}".format(num1,num2,result))

def subtraction(num1,num2):
    result = num1 - num2
    print("{0} - {1} = {2}".format(num1,num2,result))
    

print("what do u want to do?")
print("1 addition")
print("2 subtraction")


choice = input("enter the choice : ")

num1 = float(input("enter the first number : "))
num2 = float(input("enter the second number : "))

if choice == '1':
    addition (num1,num2)
elif choice == '2':
    subtraction(num1,num2)
else:
    print("invaild choice")


    
    
    
    

def add(a, b):
    return a+b
def mul(a, b):
    return a*b
def sub(a, b):
    if a>b :
        return a-b
    else :
        return b-a
def div(a, b):
    return a/b

print ("select options: \n 1 For addition \n 2 for multiply \n 3 for substraction \n 4 for divition")
choice = int(input("Enter Your Choices :- 1,2,3,4"))
num1 = float(input("Enter First number: "))
num2 = float(input("Enter Second number: "))

if choice == 1:
    print("addition of {0} and {1} is {2}".format(num1, num2, add(num1,num2)))
elif choice == 2:
    print("multiplication of {0} and {1} is {2}".format(num1, num2, mul(num1,num2)))
elif choice == 3:
    print("subtraction of {0} and {1} is {2}".format(num1, num2, sub(num1,num2)))
elif choice == 4:
    print("division of {0} and {1} is {2}".format(num1, num2, div(num1,num2)))
else:
    print("----invalid input----- ")
        
        
            
    

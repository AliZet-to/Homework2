#Data input
first_number = a = float(input("Please input any 1st number \n"))
second_number = b = float(input("Please input any 2nd number \n"))
third_number = c = float(input("Please input any 3rd number \n"))

#Calculation workflow
if (a >= b) and (a >= c):
    print("The biggest number is ", a)
elif (b >= a) and (b >= c):
    print("The biggest number is ", b)
else:
    print("The biggest number is ", c)

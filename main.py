print("Select the operation:")
print("1.Addition \n"
      "2.Subtraction \n"
      "3.Multiplication \n"
      "4.Division")
opt = int(input("Enter the number for your operation: "))
num1 = int(input("Enter your First Number: "))
num2 = int(input("Enter your Second Number: "))
output = 0
if opt == 1 :
    output += num1 + num2 

elif opt == 2 :
    output += num1 - num2

elif opt == 3 :
    output += num1*num2

elif opt == 4 :
    output += num1/num2
print(output)
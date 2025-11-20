day_of_week = input("Enter the days of week: ").lower() # converting lowercase
print(day_of_week)

if day_of_week == "saturday" or day_of_week == "sunday":  #true
    print("I will learn Devops")
else:  #false
    print("I will practice DevOps")  

num1 = int(input("Enter First number: ")) #str -> int Type Casting
num2 = int(input("Enter Second number: "))

choice = input("Enter the operation: (Options + , - , * , / , %)")

if choice == "+":
    sum_of_num = num1 + num2
    print("addition ",sum_of_num)
elif choice == "-":
    diff_of_num = num1 - num2
    print("subtraction ",diff_of_num)
elif choice == "*":
    prod_of_num = num1 * num2
    print("multipplaction: ",prod_of_num)
elif choice == "/":
    div_of_num = num1 /num2
    print("division ",div_of_num)
elif choice == "%":
    rem_of_num = num1 % num2
    print("remainder ",rem_of_num)
else:
    print("Invalid choice")                
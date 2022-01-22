valueA = int(input("Enter the value A: "))
valueB = int(input("Enter the value B: "))
opr = input("Enter the Operator: ")

print("====================")
if opr == '+':
    print('The Addition is', valueA + valueB)
elif opr == '-':
    print('The subtraction is: ', valueA - valueB)
elif opr == '*':
    print('The multiplication is: ', valueA * valueB)
elif opr == '/':
    print('The divide is: ', valueA / valueB)
elif opr == '%':
    print('The modular is: ', valueA % valueB)
elif opr == '**':
    print('The rank is: ', valueA ** valueB)
else:
    print('Operator your input not found in the system')
print("====================")
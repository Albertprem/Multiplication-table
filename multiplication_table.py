#Python program to print the multiplication table of the given number

number = int(input("Enter the number: "))

for m in range(1, 11):
    print(number, 'x', m, '=', number*m)

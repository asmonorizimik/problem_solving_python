# Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'. Once 'done' is entered, print out the largest and smallest of the numbers. If the user enters anything other than a valid number catch it with a try/except and put out an appropriate message and ignore the number. Enter 7, 2, bob, 10, and 4 and match the output below.




# largest = 0
# smallest = 1000
# while True:
#     num = input("Enter a number: ")
#     if num == "done":
#         break
#     try:
#         num1=float(num)
#     except:
#         print("invalid number")
#         continue
#     if num1>largest:
#         largest=num1
#     if num1<smallest:
#         smallest=num1
# print("Maximum", largest)
# print("Minimum", smallest)



largest = None
smallest = None
while True:
    num = input('Enter a number: ')
    if num == "done":
        break
    try:
        num1=int(num)
    except:
        print('Invalid input')
        continue
    if largest is None or largest<num1:
        largest=num1
    if smallest is None or smallest>num1:
        smallest=num1

print("Maximum is", smallest)
print("Minimum is", largest)
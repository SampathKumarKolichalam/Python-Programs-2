#Program to check number is prime number or not:-
#Using FOR loop:-
no=int(input("Enter your number:"))
for i in range(2,no):
    if no%i==0:
        print("Not a prime  number!!!")
        break
else:
    print("Prime number!!!")
#using while loop:-
no=int(input("Enter your number:"))
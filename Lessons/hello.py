# print("Hello World!");

# a = 26;
# b = 23;
# print(a+b);

# name = input("What is your name?: ")
# print("hello " + name)

# print(f"Hello, {name}");

try:
    n = int(input("Enter in a number: "))
    if n > 0:
        print("n is positive")
    elif n < 0:
        print("n is negative")
    else:
        print("n is zero")
except:
    print("Number not valid")
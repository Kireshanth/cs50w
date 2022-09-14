# library allows us to end the program by using sys.exit(1)
import sys 

# try/exceptions allow us to react to errors during runtime
try:
    x = int(input("x: "))
    y = int(input("y: "))
except ValueError:
    print("Invalid input")
    sys.exit(1)

try:
    result = x / y
except ZeroDivisionError:
    print("Error: Cannot divide by 0.")
    sys.exit(1)

print(f"{x} / {y} = {result}")
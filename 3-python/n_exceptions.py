import sys

try:
    x = int(input("x: "))
    y = int(input("y: "))
    result = x / y
    print(f"{x}/{y} is: {result}")

except ZeroDivisionError as e:
    print("Error: Cannot divide by zero.")

except ValueError as e:
    print("Error: Cannot convert input to integer.")
except Exception as e:
    sys.exit(1)  # 1 means something went wrong

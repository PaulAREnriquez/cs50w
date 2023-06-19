# importing a function from another file
# inside the same directory
from i_functions import square

num = float(input("Your number: "))
print(f"The square of {num} is {square(num)}.")

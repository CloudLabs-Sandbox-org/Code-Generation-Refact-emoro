# A refactored example of a program in Python.
# It prompts the user for the number of elements to sum,
# takes those integers as input, and handles basic error cases.

MAX = 100

def calculate_sum(arr):
   """Calculate the sum of a list of integers."""
   return sum(arr)

def get_integer_input(prompt):
   """Prompt the user for an integer input and handle invalid input."""
   while True:
      try:
         return int(input(prompt))
      except ValueError:
         print("Invalid input. Please enter a valid integer.")

def main():
   """Main function to execute the program."""
   try:
      n = get_integer_input("Enter the number of elements (1-100): ")
      if not 1 <= n <= MAX:
         print("Invalid input. Please provide a number ranging from 1 to 100.")
         return

      arr = []
      print(f"Enter {n} integers:")
      for _ in range(n):
         arr.append(get_integer_input(""))

      total = calculate_sum(arr)
      print("Sum of the numbers:", total)

   except KeyboardInterrupt:
      print("\nProgram terminated by user.")

if __name__ == "__main__":
   main()

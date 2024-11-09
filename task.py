
def operationlist() :
      print("The available operations are:")
      print("1 - Palindrome: Check if the input is palindrome")
      print("2 - Lower: Check if all characters in the input are lowercase")
      print("3 - Digit: Check if all characters in the input are digits")
      print("4 - Long: Check if the input length is longer than 15")
      print("5 - Empty: Check if the input is empty")
      print("6 - Exit: Exit successfully from the application")


def is_palindrome(inputpr)  :
       return inputpr == inputpr[::-1]

def is_lower(inputpr):
    v=str(inputpr)
    return v.islower()

def is_digit(inputpr):
    v=str(inputpr)
    return v.isdigit()

def is_long(inputpr,threshold=15):
    v = str(inputpr)
    return len(v)>threshold

def is_empty(inputpr):
    v = str(inputpr)
    return v==""


def main():
    while True:
     operationlist()
     try:
         operation_op=int(input("Please enter the number of the operation you choose:"))

         if operation_op==6:
             print("exit successfully")
             break

         input_pr=input("Enter an input:")

         if operation_op==1:
             print("The answer is","True"if is_palindrome(input_pr) else "False")
         elif operation_op == 2:
             print("The answer is","True" if is_lower(input_pr) else "False")
         elif operation_op == 3:
             print("The answer is","True" if is_digit(input_pr) else "False")
         elif operation_op == 4:
            threshold = int(input("Enter the length threshold: "))
            print("The answer is","True" if is_long(input_pr,threshold) else "False")
         elif operation_op==5:
            print("The answer is","True" if is_empty(input_pr) else "False")
         else:
             print("Invalid selection. Please try again.")
     except ValueError:
             print("Error: Please enter a valid number.")


if __name__ == "__main__":
    main()






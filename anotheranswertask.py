def operationlist():
    print("\nThe available operations are:")
    print("1 - Palindrome: Check if the input is palindrome")
    print("2 - Lower: Check if all characters in the input are lowercase")
    print("3 - Digit: Check if all characters in the input are digits")
    print("4 - Long: Check if the input length is longer than a threshold")
    print("5 - Empty: Check if the input is empty")
    print("6 - Exit: Exit successfully from the application")


def is_palindrome(inputpr):
    return inputpr == inputpr[::-1]


def is_lower(inputpr):
    return inputpr.islower()


def is_digit(inputpr):
    return inputpr.isdigit()


def is_long(inputpr, threshold=15):
    return len(inputpr) > threshold


def is_empty(inputpr):
    return inputpr == ""


def main():
    while True:
        operationlist()
        try:
            operation_op = int(input("Please enter the number of the operation you choose: "))

            # Use match-case instead of if-elif chain
            match operation_op:
                case 1:
                    input_pr = input("Enter an input: ")
                    print("The answer is", "True" if is_palindrome(input_pr) else "False")
                case 2:
                    input_pr = input("Enter an input: ")
                    print("The answer is", "True" if is_lower(input_pr) else "False")
                case 3:
                    input_pr = input("Enter an input: ")
                    print("The answer is", "True" if is_digit(input_pr) else "False")
                case 4:
                    input_pr = input("Enter an input: ")
                    threshold = int(input("Enter the length threshold: "))
                    print("The answer is", "True" if is_long(input_pr, threshold) else "False")
                case 5:
                    input_pr = input("Enter an input: ")
                    print("The answer is", "True" if is_empty(input_pr) else "False")
                case 6:
                    print("Exiting successfully.")
                    break
                case _:
                    print("Invalid selection. Please try again.")

        except ValueError:
            print("Error: Please enter a valid number.")


if __name__ == "__main__":
    main()

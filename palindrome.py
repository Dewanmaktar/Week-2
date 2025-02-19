def check_palindrome():
    user_input = input("Enter a string to check if it is a palindrome: ")
    if is_palindrome(user_input):
        print("The string is a palindrome.")
    else:
        print("The string is not a palindrome.")

def is_palindrome(s):
    s = s.replace(" ", "").lower()
    return s == s[::-1]

def main():
    check_palindrome()

if __name__ == "__main__":
    main()
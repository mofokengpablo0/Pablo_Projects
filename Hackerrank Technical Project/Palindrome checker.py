def is_palindrome(s):
    # Normalize the string.
    # remove non-alphanumeric characters and convert it to lowercase
    clean_s = "".join(char.lower() for char in s if char.isalnum())

    # compare the string with its reverse using slicing
    return clean_s == clean_s[::-1]


print(is_palindrome("racecar"))  # True
print(is_palindrome("hello"))  # False
print(is_palindrome("A man, a plan, a canal: Panama"))  # True

def is_palindrome(string: str) -> bool:
    string = string.replace(" ", "").lower()

    return string == string[::-1] # reverse the string :: (iterable)

def run():
    word = 1000

    print(is_palindrome(word))


# In order to check the static types we need to run:
# mypy palindome.py --check-untyped-defs
""" ON CONSOLE:
palindrome.py:10: error: Argument 1 to "is_palindrome" has incompatible type "int"; expected "str"
Found 1 error in 1 file (checked 1 source file)
"""

if __name__ == '__main__':
    run()

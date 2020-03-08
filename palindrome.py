def is_palindrome(value: str) -> bool:
    """
    This function determines if a word or phrase is a palindrome

    :param value: A string
    :return: A boolean
    """

    if (value ==value[::-1]):
        return print("is palindrome")
    else:
        return print("not palindrome")

is_palindrome("rotator")

def is_anagram(first_string: str, second_string: str) -> bool:
    """
    Given two strings, this functions determines if they are an anagram of one another.
    """
    pass  # remove pass statement and implement me

    first_string = sorted(first_string)
    second_string = sorted(second_string)
    if first_string == second_string:
        print("anagram")
    else:
        print("not anagram")
first_string = "dormitory"
second_string = "dirtyroom"
is_anagram(first_string, second_string)
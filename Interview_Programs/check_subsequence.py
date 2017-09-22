

"""
The idea is simple, we traverse both strings from one side to other side
(say from rightmost character to leftmost). If we find a matching character,
we move ahead in both strings. Otherwise we move ahead only in Bigger one.
"""
def is_Subsequence(string1, string2, len1, len2):
    if len2 == 0:  # this means that all the elements of smaller string are present in bigger one.
        return True
    if len1 == 0:   # this means that we have exhausted all the elements of bigger string but still can find one or more characters in the bigger one.
        return False

    if string1[len1-1] == string2[len2-1]:
        return is_Subsequence(string1, string2, len1-1, len2-1)
    return is_Subsequence(string1, string2, len1-1, len2)


if __name__ == '__main__':
    string1 = 'abcdef'
    string2 = 'dfe'
    # check if string2 is a substring of string1
    sub_check = is_Subsequence(string1, string2, len(string1), len(string2))
    print(sub_check)

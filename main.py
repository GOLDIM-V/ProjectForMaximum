def testz_palindrome(word):
    if len(word) == 1:
        return True
    elif len(word) == 2 and word[0] == word[1]:
        return True
    elif word[0] == word[-1]:
        return testz_palindrome(word[1:-1])
    else:
        return False
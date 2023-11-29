def is_palindrome_iterative(word):
    if not word:
        return False

    size = len(word)
    mid = size // 2
    for i in range(0, mid):
        if word[i] != word[size - 1 - i]:
            return False
    return True

def ispalindrome(self, s: str) -> bool:
    strs = []
    for char in s:
        if char.isalnum:
            strs.append(char.lower())

    # define that palindrome
    while len(strs) > 1:
        if strs.pop(0) != strs.pop():
            return False

    return True
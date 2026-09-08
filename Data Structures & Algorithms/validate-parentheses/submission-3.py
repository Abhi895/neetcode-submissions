class Solution:
    def isValid(self, s: str) -> bool:
        open = []
        parentheses = {'{': '}', '(':')', '[':']'}
        for char in s:
            if char == "(" or char == "{" or char == "[":
                open.append(char)
            else:
                if open == []:
                    return False
                elif char != parentheses[open.pop()]:
                    return False
        if open == []:
            return True
        else:
            return False
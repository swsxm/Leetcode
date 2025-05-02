class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        comp = {")": "(", "]": "[", "}": "{"}
        for paren in s:
            if paren in comp:
                if not stack or stack.pop() != comp[paren]:
                    return False
            else:
                stack.append(paren)
        return not stack

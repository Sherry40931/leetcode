# O(n)
class Solution:
    def isValid(self, s: str) -> bool:
        match = {'(': ')', '{': '}', '[': ']'}
        stack = []
        for c in s:
            if c in match:
                stack.append(c)
            elif len(stack) == 0 or match[stack.pop()] != c:
                return False
        return stack == []


print(Solution().isValid('()'))
print(Solution().isValid('()[]{}'))
print(Solution().isValid('(]'))
print(Solution().isValid('('))
print(Solution().isValid(')'))
print(Solution().isValid('({[()]))'))
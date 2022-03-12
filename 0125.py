class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = [v.lower() for v in s if v.isalnum()]
        return s == s[::-1]


class Solution2:
    # use less memory
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(filter(str.isalnum, s)).lower()
        return s == s[::-1]


class Solution3:
    def isPalindrome(self, s: str) -> bool:
        N = len(s)
        i, j = 0, N - 1
        while i < j:
            while i < j and not s[i].isalnum():
                i += 1
            while j > i and not s[j].isalnum():
                j -= 1
            if s[i].lower() != s[j].lower():
                return False
            i, j = i + 1, j - 1
        return True


print(Solution3().isPalindrome('.,'))
print(Solution3().isPalindrome("A man, a plan, a canal: Panama"))
print(Solution3().isPalindrome("race a car"))
print(Solution3().isPalindrome(' '))
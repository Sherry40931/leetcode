# https://leetcode.com/problems/decode-the-message/
# 2325. Decode the Message
class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        subs = {' ': ' '}
        alpha = 'a'
        for c in key:
            if c in subs:
                continue
            subs[c] = alpha
            alpha = chr(ord(alpha) + 1)
            if alpha > 'z':
                break

        return ''.join([subs[c] for c in message])


print(Solution().decodeMessage('the quick brown fox jumps over the lazy dog',
                               'vkbs bs t suepuv'))
print(Solution().decodeMessage('eljuxhpwnyrdgtqkviszcfmabo',
                               'zwx hnfx lqantp mnoeius ycgk vcnjrdb'))
class Solution:
    def reverseBits(self, n: int) -> int:
        bit = bin(n)[2:].zfill(32)
        return int(bit[::-1], 2)


class Solution2:
    def reverseBits(self, n: int) -> int:
        ans = ''.join([str((n >> i) & 1) for i in range(32)])
        return int(ans, 2)


class Solution3:
    def reverseBits(self, n: int) -> int:
        if n == 0:
            return 0
        ans = 0
        for i in range(32):
            ans <<= 1
            ans += n & 1
            n >>= 1
        return ans


print(Solution2().reverseBits(int('00000010100101000001111010011100', 2)))
print(Solution2().reverseBits(int('11111111111111111111111111111101', 2)))
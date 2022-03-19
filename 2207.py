# 6021. Maximize Number of Subsequences in a String
# https://leetcode.com/contest/biweekly-contest-74/problems/maximize-number-of-subsequences-in-a-string/

from pdb import set_trace as bp


class Solution:
    def maximumSubsequenceCount(self, text: str, pattern: str) -> int:
        cnt1 = cnt2 = ans = 0
        for c in text:
            if c == pattern[1]:
                cnt2 += 1
                ans += cnt1  # 每遇到 pattern[1], 表示之前已累積的 pattern[0] 都可以算
            if c == pattern[0]:  # pattern[0] might == pattern[1], don't use if else
                cnt1 += 1
        # max(cnt1, cnt2) 是為了計算加 pattern[0] 在第一個位置 or 加 pattern[1] 在最後的位置
        # 上述是 optimal 的做法
        return ans + max(cnt1, cnt2)


# accaac, 5
# start = [1, 2]
# end = [2, 1]
# 1*2 + (1+2)*1 = 5
# a[a]ccaac
# start = [2, 2]
# end = [2, 1]
# 2*2 + (2+2)*1 = 8


print(Solution().maximumSubsequenceCount('abdcdbc', 'ac'))
print(Solution().maximumSubsequenceCount('aabb', 'ab'))
print(Solution().maximumSubsequenceCount('accadfgdfgrabbc', 'ac'))
print(Solution().maximumSubsequenceCount('fwymvreuftzgrcrxczjacqovduqaiig', 'yy'))
print(Solution().maximumSubsequenceCount('jdxm', 'pe'))
print(Solution().maximumSubsequenceCount('vnedkpkkyxelxqptfwuzcjhqmwagvrglkeivowvbjdoyydnjrqrqejoyptzoklaxcjxbrrfmpdxckfjzahparhpanwqfjrpbslsyiwbldnpjqishlsuagevjmiyktgofvnyncizswldwnngnkifmaxbmospdeslxirofgqouaapfgltgqxdhurxljcepdpndqqgfwkfiqrwuwxfamciyweehktaegynfumwnhrgrhcluenpnoieqdivznrjljcotysnlylyswvdlkgsvrotavnkifwmnvgagjykxgwaimavqsxuitknmbxppgzfwtjdvegapcplreokicxcsbdrsyfpustpxxssnouifkypwqrywprjlyddrggkcglbgcrbihgpxxosmejchmzkydhquevpschkpyulqxgduqkqgwnsowxrmgqbmltrltzqmmpjilpfxocflpkwithsjlljxdygfvstvwqsyxlkknmgpppupgjvfgmxnwmvrfuwcrsadomyddazlonjyjdeswwznkaeaasyvurpgyvjsiltiykwquesfjmuswjlrphsdthmuqkrhynmqnfqdlwnwesdmiiqvcpingbcgcsvqmsmskesrajqwmgtdoktreqssutpudfykriqhblntfabspbeddpdkownehqszbmddizdgtqmobirwbopmoqzwydnpqnvkwadajbecmajilzkfwjnpfyamudpppuxhlcngkign',
    'rr'))
print(Solution().maximumSubsequenceCount('rrrr', 'rr'))

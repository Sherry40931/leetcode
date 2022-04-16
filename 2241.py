# 6062. Design an ATM Machine
# https://leetcode.com/contest/biweekly-contest-76/problems/design-an-atm-machine/
from typing import List


class ATM:

    def __init__(self):
        self.bank = [20, 50, 100, 200, 500]
        self.count = [0, 0, 0, 0, 0]
        self.N = len(self.bank)

    def deposit(self, banknotesCount: List[int]) -> None:
        for i, n in enumerate(banknotesCount):
            self.count[i] += n

    def withdraw(self, amount: int) -> List[int]:
        take = [0] * self.N
        for i in range(self.N - 1, -1, -1):
            take[i] = min(amount // self.bank[i], self.count[i])
            amount -= self.bank[i] * take[i]

        if amount == 0:
            self.count = [a - b for a, b in zip(self.count, take)]

        return take if amount == 0 else [-1]


# Your ATM object will be instantiated and called as such:
obj = ATM()
obj.deposit([0, 0, 1, 2, 1])
print(obj.withdraw(600))
obj.deposit([0, 1, 0, 1, 1])
print(obj.withdraw(600))
print(obj.withdraw(550))
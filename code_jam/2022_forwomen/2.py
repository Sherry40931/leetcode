from pdb import set_trace as bp
import heapq


class Delivery(object):
    def __init__(self, start: int, elapsed: int, num: int):
        self.start = start
        self.end = start + elapsed
        self.num = num

    def __lt__(self, other):  # for heapq
        return self.end < other.end


def main():
    ans = k = 0
    cur_deliveries = []

    for order in orders:

        # add delivery
        while k < D and order >= deliveries[k].start:
            cur_deliveries.append(deliveries[k])
            k += 1
        heapq.heapify(cur_deliveries)

        # pop delivery
        while len(cur_deliveries) > 0 and cur_deliveries[0].end <= order:
            heapq.heappop(cur_deliveries)

        # use the delivery which expires soon
        rem = U
        while len(cur_deliveries) > 0 and rem > 0:
            d = heapq.heappop(cur_deliveries)
            use = min(rem, d.num)
            rem -= use
            d.num -= use
            if d.num > 0:
                heapq.heappush(cur_deliveries, d)

        if rem > 0:
            break
        ans += 1

        # print('==', [d.num for d in cur_deliveries])

    return ans


if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        D, N, U = [int(v) for v in input().split()]
        # U = leaves needed
        deliveries = []
        for _ in range(D):
            s, n, e = [int(v) for v in input().split()]
            delivery = Delivery(s, e, n)
            deliveries.append(delivery)

        orders = [int(v) for v in input().split()]  # time of order

        ans = main()
        print(f'Case #{i+1}: {ans}')
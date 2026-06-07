from typing import List

class BIT:

    def __init__(self, n: int):
        self.n = n
        self.bit = [0] * (n + 2)

    def add(self, idx: int, delta: int) -> None:
        while idx <= self.n:
            self.bit[idx] += delta
            idx += idx & -idx

    def sum(self, idx: int) -> int:
        s = 0
        while idx > 0:
            s += self.bit[idx]
            idx -= idx & -idx
        return s


    def find_kth(self, k: int) -> int:
        idx = 0
        bit_mask = 1 << (self.n.bit_length())
        while bit_mask:
            nxt = idx + bit_mask
            if nxt <= self.n and self.bit[nxt] < k:
                idx = nxt
                k -= self.bit[nxt]
            bit_mask >>= 1
        return idx + 1


class SegTree:
    def __init__(self, n: int):
        self.n = n
        self.tree = [0] * (4 * n)

    def _update(self, node: int, l: int, r: int, idx: int, val: int) -> None:
        if l == r:
            self.tree[node] = val
            return
        mid = (l + r) // 2
        if idx <= mid:
            self._update(node * 2, l, mid, idx, val)
        else:
            self._update(node * 2 + 1, mid + 1, r, idx, val)
        self.tree[node] = max(self.tree[node * 2], self.tree[node * 2 + 1])

    def update(self, idx: int, val: int) -> None:
        self._update(1, 1, self.n, idx, val)

    def _query(self, node: int, l: int, r: int, ql: int, qr: int) -> int:
        if ql > r or qr < l:
            return 0
        if ql <= l and r <= qr:
            return self.tree[node]
        mid = (l + r) // 2
        return max(self._query(node * 2, l, mid, ql, qr),
                   self._query(node * 2 + 1, mid + 1, r, ql, qr))

    def query(self, ql: int, qr: int) -> int:
        return self._query(1, 1, self.n, ql, qr)


class Solution:
    def getResults(self, queries: List[List[int]]) -> List[bool]:
        MAX_X = 50000
        bit = BIT(MAX_X)
        seg = SegTree(MAX_X)
        results = []

        for q in queries:
            if q[0] == 1:          
                x = q[1]
                cnt = bit.sum(x - 1)
                pre = bit.find_kth(cnt) if cnt > 0 else 0
                total = bit.sum(MAX_X)
                left = bit.sum(x)
                nxt = None
                if total > left:
                    nxt = bit.find_kth(left + 1)
                if nxt is not None:
                    seg.update(nxt, 0)
                seg.update(x, x - pre)
                if nxt is not None:
                    seg.update(nxt, nxt - x)

                bit.add(x, 1)

            else:              
                _, x, sz = q
                cnt = bit.sum(x)
                last = bit.find_kth(cnt) if cnt > 0 else 0
                candidate = x - last
                best = seg.query(1, x)
                results.append(max(best, candidate) >= sz)

        return results
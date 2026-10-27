# Template repository:
# https://github.com/cinnabar7/competitive-programming-templates
#
# References and Licenses
#
# UnionFind:
# Based on https://note.nkmk.me/python-union-find/
# Original source: https://github.com/nkmk/python-snippets
# License: MIT
# License text: THIRD_PARTY_LICENSES/nkmk-LICENSE.txt
#
# COMinit, COM, modlog:
# Adapted from the C++ implementations in:
# https://qiita.com/drken/items/3b4fdf0a78e7a138cd9a
#
# The following MIT license notice applies to the UnionFind implementation.
#
# MIT License
#
# Copyright (c) 2017 
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from collections import defaultdict
import sys
from math import gcd, isqrt
from bisect import bisect_left
sys.setrecursionlimit(10**6)

class UnionFind:
    def __init__(self, n: int) -> None:
        self.n = n
        self.parents = [-1] * n

    def find(self, x: int) -> int:
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x: int, y: int) -> bool:
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return False

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

        return True

    def size(self, x: int) -> int:
        return -self.parents[self.find(x)]

    def same(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)

    def members(self, x: int) -> list[int]:
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self) -> list[int]:
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self) -> int:
        return len(self.roots())

    def all_group_members(self) -> defaultdict[int, list[int]]:
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members

    def __str__(self) -> str:
        return '\n'.join(f'{r}: {m}' for r, m in self.all_group_members().items())



MOD = 998244353
MAX = 510000


# 二項係数の前処理
def COMinit(max_n: int, mod: int = MOD) -> tuple[list[int], list[int]]:
    fac = [1] * (max_n + 1)
    finv = [1] * (max_n + 1)

    for i in range(1, max_n + 1):
        fac[i] = fac[i - 1] * i % mod

    finv[max_n] = pow(fac[max_n], -1, mod)

    for i in range(max_n, 0, -1):
        finv[i - 1] = finv[i] * i % mod

    return fac, finv


# 二項係数 nCk mod mod
def COM(n: int, k: int, fac: list[int], finv: list[int], mod: int = MOD) -> int:
    if n < 0 or k < 0 or n < k:
        return 0

    return fac[n] * finv[k] % mod * finv[n - k] % mod


# a^x ≡ b (mod m) となる最小の正の整数xを求める
# gcd(a, m) = 1, m >= 2 を仮定
def modlog(a: int, b: int, m: int) -> int:
    a %= m
    b %= m

    if gcd(a, m) != 1:
        raise ValueError("gcd(a, m) must be 1")

    sqrtM = isqrt(m - 1) + 1

    apow = {}
    remainder = a

    for r in range(1, sqrtM):
        if remainder not in apow:
            apow[remainder] = r
        remainder = remainder * a % m

    A = pow(a, -sqrtM, m)
    remainder = b

    for q in range(sqrtM):
        if remainder == 1 and q > 0:
            return q * sqrtM
        elif remainder in apow:
            return q * sqrtM + apow[remainder]

        remainder = remainder * A % m

    return -1


def binary_search(A: list[int], target: int) -> int:
    index = bisect_left(A, target)
    if index < len(A) and A[index] == target:
        return index
    return -1

def main() -> None:
    input = sys.stdin.buffer.readline
if __name__ == "__main__":
    main()
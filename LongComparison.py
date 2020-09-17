from LongNumber import LongNumber


class LongComparison:
    def __init__(self, a, b, m):
        gcd = LongNumber.GCD_n(a, b, m)
        self.a = (a % m) // gcd
        self.b = (b % m) // gcd
        self.m = m // gcd

    def get_P_i(self):
        a, m = self.a, self.m
        P = []
        q, old_q = LongNumber('1'), LongNumber('0')
        P.append(old_q)
        P.append(q)
        count = LongNumber('0')
        while m > LongNumber('1'):
            old_q = q
            q = m // a
            P.append(q*P[-1] + P[-2])
            count += LongNumber('1')
            m %= a
            a, m = m, a
        
        
        return P[-2], count

    def solve(self):
        P_n, n = self.get_P_i()
        n -= LongNumber('1')
        return (LongNumber(-1)**n * P_n * self.b) % self.m, self.m
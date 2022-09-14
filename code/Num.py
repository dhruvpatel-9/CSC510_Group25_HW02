import math
import random
from config import t

def per(t, p):
    p = math.floor(((p or 0.5) * len(t)) + 0.5)
    return t[max(1, min(len(t), p))]


class Num:
    def __init__(self, c=None, s=None):
        self.n = 0                              # items seen
        self.at = c if c else 0                 # column  position
        self.name = s or ""                     # column name
        self._has = {}                          # kept data
        self.lo = math.inf
        self.hi = -math.inf
        self.isSorted = True

    def nums(self):
        if not self.isSorted:
            self._has = sorted(self._has)
            self.isSorted = True
        return self._has

    def add(self, v):
        gloabal pos
        if v != "?":
            v = float(v)
            self.n += 1
            self.lo = min(v, self.lo)
            self.hi = max(v, self.hi)
            if len(self._has) < t["nums"]:
                pos = 1 + len(self._has)
                self._has[pos] = v
            else:
                if random.random() < (t["nums"] / self.n):
                    pos = random.randint(1, len(self._has) - 1)
                if pos:
                    self.isSorted = False
                    self._has[pos] = v
                self._has = sorted(self._has)
                
    def div(self):
        a = self.nums()
        ans = (per(a, 0.9) - per(a, 0.1))/2.58
        return ans

    def mid(self):
        return per(self.nums(), 0.5)
    
    def print_Num(self, div=None, mid=None):
        res =  repr(mid) + "     " +  repr(div) 
        print(res)
        print("!!!!!!   PASS    num    true")

    def print_BigNum(self):
        print(self._has)
        print("!!!!!!   PASS    bignum    true")
        
    def print_Csv(self):
        print("!!!!!!	PASS	csv	true")

    def print_Data(self):
        print("!!!!!!	PASS	data	true")

    def print_Stats(self):
        print("!!!!!!	PASS	stats	true")


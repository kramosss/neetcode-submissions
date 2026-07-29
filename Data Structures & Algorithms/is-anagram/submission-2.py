class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        a = {}
        b = {}
        for i in s:
            if i in a:
                a[i] += 1
            else:
                a[i] = 1
        for j in t:
            if j in b:
                b[j] += 1
            else:
                b[j] = 1
        for l, m in a.items():
            if b.get(l, 0) != m:
                return False
        return True 
class Solution:
    def isValid(self, s: str) -> bool:
        a = {')' : '(', '}' : '{', ']' : '['}
        b = []

        for i in s:
            if i in a:
                if b and a[i] == b[-1]:
                    b.pop()
                else:
                    return False
            else:
                b.append(i)
        return True if not b else False  
            

        
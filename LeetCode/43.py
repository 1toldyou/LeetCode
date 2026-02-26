class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        def str2num(s: str) -> int:
            num = 0
            for c in s:
                num *= 10
                num += int(c)
            return num
        return str(str2num(num1) * str2num(num2))
        

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        OPS = ["+", "-", "*", "/"]
        n = len(tokens)
        if n == 1:
            return int(tokens[0])

        a = -1
        b = -1
        window = []
        while b+1 < n:
            b += 1
            if tokens[b] in OPS:
                window = [tokens[b-2], tokens[b-1]]
                a = b-2
                break

        while window and a >= 0:
            # print(window, tokens[b], a, b)
            res = 0
            match tokens[b]:
                case "+":
                    res = int(window[-2]) + int(window[-1])
                case "-":
                    res = int(window[-2]) - int(window[-1])
                case "*":
                    res = int(window[-2]) * int(window[-1])
                case "/":
                    res = int(window[-2]) / int(window[-1])
                    if res > 0:
                        res = math.floor(res)
                    else:
                        res = math.ceil(res)
            window = window[:-2] + [res]
            while b+1 < n:
                b += 1
                if tokens[b] in OPS:
                    break
                else:
                    window.append(tokens[b])
            if len(window) == 1:
                a -= 1
                window = [tokens[a], *window]
        
        # print(window)
        return window[1]

        
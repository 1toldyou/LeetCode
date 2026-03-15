class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letterLogs = []
        digitLogs = []
        for log in logs:
            if ord(log[-1]) >= ord("0") and ord(log[-1]) <= ord("9"):
                digitLogs.append(log)
            else:
                split = log.split(" ", 1)
                letterLogs.append((split[1], split[0]))
        letterLogs.sort()

        ans = []
        for parts in letterLogs:
            ans.append(parts[1]+" "+parts[0])
        ans += digitLogs
        return ans
        
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        possible = [False] * (n+1)
        possible[0] = True
        wordLens = list(set([len(word) for word in wordDict]))
        wordDict = set(wordDict)

        for i in range(1, n+1):
            for wordLen in wordLens:
                if i+1 < wordLen:
                    continue
                window = s[i-wordLen:i]
                if window in wordDict:
                    if possible[i-wordLen] == True:
                        possible[i] = True
                        break

        return possible[-1]
                
        
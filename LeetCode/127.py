class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        words = set(wordList)
        adj: Dict[str, List[str]] = {}

        for word in wordList:
            adj[word] = set()
        adj[beginWord] = set()
        
        wordList.append(beginWord)
        for word in wordList:
            for i in range(len(word)):
                for j in range(26):
                    newWord = word[:i] + chr(ord("a")+j) + word[i+1:]
                    if newWord in words:
                        adj[word].add(newWord)
        wordList.pop()

        visited = {}
        visited[beginWord] = True
        curr = [beginWord]
        dist = 0
        while curr:
            dist += 1
            nextLayer = []
            for word in curr:
                if word == endWord:
                    return dist
                for nextWord in adj[word]:
                    if visited.get(nextWord) is None:
                        visited[nextWord] = True
                        nextLayer.append(nextWord)
            curr = nextLayer

        return 0
        
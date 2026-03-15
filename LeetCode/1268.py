class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        A = ord("a")
        trie = [None] * 27

        def add(node: dict, word: str):
            if word == "":
                node[0] = True
                return
            idx = ord(word[0]) - A + 1
            if node[idx] is None:
                node[idx] = [None] * 27

            add(node[idx], word[1:])
            
        for product in products:
            add(trie, product)

        ans = [[] for i in range(len(searchWord))]
        ansIdx = 0
        seen = ""
        def search(node: dict, path: str):
            if len(ans[ansIdx]) >= 3:
                return

            if node[0] == True:
                ans[ansIdx].append(path)

            for i in range(1, 27):
                if node[i] is None:
                    continue
                search(node[i], path+chr(A+i-1))

        ptr = trie
        for i, c in enumerate(searchWord):
            idx = ord(c) - A + 1
            if ptr[idx] is None:
                break
            ansIdx = i
            seen += c
            ptr = ptr[idx]
            search(ptr, seen)

        return ans

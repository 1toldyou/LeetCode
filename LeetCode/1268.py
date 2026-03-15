class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        trie = [None] * 27

        def add(node: dict, word: str):
            if word == "":
                node[0] = True
                return
            idx = ord(word[0]) - ord("a") + 1
            if node[idx] is None:
                node[idx] = [None] * 27

            add(node[idx], word[1:])
            
        for product in products:
            add(trie, product)
        # print(trie)

        ans = []
        level = []
        seen = ""
        def search(node: dict, path: str):
            # print("search()", path)
            nonlocal level
            if len(level) >= 3:
                return

            if node[0] == True:
                level.append(path)

            for i in range(1, 27):
                if node[i] is None:
                    continue
                search(node[i], path+chr(ord("a")+i-1))

        ptr = trie
        for c in searchWord:
            idx = ord(c) - ord("a") + 1
            if ptr[idx] is None:
                break
            seen += c
            ptr = ptr[idx]
            search(ptr, seen)
            ans.append(level)
            level = []
        if len(ans) < len(searchWord):
            ans += [[] for i in range(len(searchWord)-len(ans))]
        return ans


        
        
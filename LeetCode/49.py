class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        m = {}
        for s in strs:
            y = s
            x = "".join(sorted(s))
            if not m.get(x):
                m[x] = []
            m[x].append(y)
        
        # print(m)

        res = []
        for k, v in m.items():
            res.append(v)
        return res
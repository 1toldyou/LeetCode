class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n = len(hand)

        if n % groupSize != 0:
            return False

        freqs = Counter(hand)
        hand.sort()

        for num in hand:
            if freqs[num] == 0:
                continue
            for i in range(0, groupSize):
                if not freqs.get(num+i):
                    return False
                freqs[num+i] -= 1
        return True
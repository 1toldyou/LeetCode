class Twitter:

    def __init__(self):
        self.following: Dict[int, List[int]] = {}
        self.posts: Dict[int, List[int]] = {}
        self.seq = 1
        self.seqToID: List[int] = [-1]

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.seqToID.append(tweetId)
        if not userId in self.posts:
            self.posts[userId] = []
        self.posts[userId].append(-self.seq)
        self.seq += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        if not userId in self.following:
            self.following[userId] = [userId]
        following = {uid:1 for uid in self.following[userId]}
        pq = []
        for uid, idx in following.items():
            if not uid in self.posts:
                continue 
            if len(self.posts[uid]) >= following[uid]:
                heapq.heappush(pq, (self.posts[uid][-following[uid]], uid))
                following[uid] += 1
        ans = []
        for i in range(10):
            if not pq:
                break
            post, uid = heapq.heappop(pq)
            ans.append(post)
            if len(self.posts[uid]) >= following[uid]:
                heapq.heappush(pq, (self.posts[uid][-following[uid]], uid))
                following[uid] += 1
        return [self.seqToID[-seqID] for seqID in ans]

    def follow(self, followerId: int, followeeId: int) -> None:
        if not followerId in self.following:
            self.following[followerId] = [followerId]
        self.following[followerId].append(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if not followerId in self.following:
            return
        self.following[followerId].remove(followeeId)       


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
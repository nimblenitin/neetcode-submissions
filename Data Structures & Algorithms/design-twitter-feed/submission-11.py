class Twitter:

    def __init__(self):
        self.count = 0
        self.tweetMap = defaultdict(list)
        self.followMap = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.count, tweetId])
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        maxH = []
        self.followMap[userId].add(userId)
        for followeeId in self.followMap[userId]:
            if followeeId in self.tweetMap:
                index = len(self.tweetMap[followeeId]) - 1
                curCount, tID = self.tweetMap[followeeId][index]
                heapq.heappush(maxH, [curCount, followeeId, tID, index - 1])
        while len(res) < 10 and maxH:
            cou, fId, twId, nxt = heapq.heappop(maxH)
            res.append(twId)
            if nxt >= 0:
                curCou, tweeID = self.tweetMap[fId][nxt]
                heapq.heappush(maxH, [curCou, fId, tweeID, nxt - 1])
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)

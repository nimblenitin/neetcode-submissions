class Twitter:

    def __init__(self):
        self.count = 0
        self.followMap = defaultdict(set)
        self.tweetMap = defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.count, tweetId])
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        maxH = []
        self.followMap[userId].add(userId)
        for followeeId in self.followMap[userId]:
            if followeeId in self.tweetMap:
                idx = len(self.tweetMap[followeeId]) - 1
                curCou, tID = self.tweetMap[followeeId][idx]
                maxH.append([curCou, tID, idx - 1, followeeId])
        heapq.heapify(maxH)
        res = []
        while maxH and len(res) < 10:
            cou, twId, prevIdx, fId = heapq.heappop(maxH)
            res.append(twId)
            if prevIdx >= 0:
                curC, tweeID = self.tweetMap[fId][prevIdx]
                heapq.heappush(maxH, [curC, tweeID, prevIdx - 1, fId])
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)


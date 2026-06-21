class Twitter:

    def __init__(self):
        self.count = 0
        self.followerMap = defaultdict(set)
        self.tweetMap = defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.count, tweetId])
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        maxH = []
        self.followerMap[userId].add(userId)
        for followee in self.followerMap[userId]:
            if followee in self.tweetMap:
                idx = len(self.tweetMap[followee]) - 1
                curC, curId = self.tweetMap[followee][idx]
                maxH.append([curC, curId, idx - 1, followee])
                heapq.heapify(maxH)
        res = []
        while len(res) < 10 and maxH:
            curC, curId, idx, followee = heapq.heappop(maxH)    
            res.append(curId)
            if idx >= 0:
                nxtC, nxtId = self.tweetMap[followee][idx]
                heapq.heappush(maxH, [nxtC, nxtId, idx - 1, followee])
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followerMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followerMap[followerId]:
            self.followerMap[followerId].remove(followeeId)

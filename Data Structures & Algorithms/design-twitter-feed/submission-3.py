class Twitter:

    def __init__(self):
        self.followMap = defaultdict(set)
        self.tweetMap = defaultdict(list)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.time, tweetId])
        self.time -= 1
    def getNewsFeed(self, userId: int) -> List[int]:
        minHeap = []
        res = []
        self.followMap[userId].add(userId)
        for followeeId in self.followMap[userId]:
            if self.tweetMap[followeeId]:
                lastIndex = len(self.tweetMap[followeeId]) -1
                time, tweetId = self.tweetMap[followeeId][lastIndex]  
                heapq.heappush(minHeap, [time, tweetId, followeeId, lastIndex - 1])

        while minHeap and len(res) < 10:
            time, tweetId, followeeId, oldIndex = heapq.heappop(minHeap)
            res.append(tweetId)
            if oldIndex >= 0:
                time, tweetId = self.tweetMap[followeeId][oldIndex] 
                heapq.heappush(minHeap, [time, tweetId, followeeId, oldIndex - 1])
        return res 



    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)
    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
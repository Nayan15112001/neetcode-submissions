import heapq
class Twitter:

    def __init__(self):
        self.stk = []
        self.hmap = {}

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.stk.append([userId,tweetId])

    def getNewsFeed(self, userId: int) -> List[int]:
        l = []
        for item in reversed(self.stk):
            if (userId in self.hmap and item[0] in self.hmap[userId]) or item[0] == userId:
                l.append(item[1])
                if len(l) == 10:
                    break
        return l


    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.hmap:
            self.hmap[followerId] = []
        if followeeId not in self.hmap[followerId]:
            self.hmap[followerId].append(followeeId)


    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.hmap and followeeId in self.hmap[followerId]:
            self.hmap[followerId].remove(followeeId)

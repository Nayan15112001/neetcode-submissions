import heapq
class Twitter:

    def __init__(self):
        self.posts = {}
        self.followers = {}
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.posts:
            self.posts[userId] = []
        self.posts[userId].append((self.time,tweetId))
        self.time+=1


    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        l = []
        users = set()
        if userId in self.followers:
            users = self.followers[userId]
        users.add(userId)

        for user in users:
            if user in self.posts:
                for items in self.posts[user]:
                    heapq.heappush(heap,(-items[0],items[1]))

        for i in range(len(heap)):
            time,tweetid = heapq.heappop(heap)
            l.append(tweetid)
            if len(l)==10:
                break
        
        return l


    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.followers:
            self.followers[followerId] = set()
        if followeeId not in self.followers[followerId]:
            self.followers[followerId].add(followeeId)


    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.followers and followeeId in self.followers[followerId]:
            self.followers[followerId].discard(followeeId)

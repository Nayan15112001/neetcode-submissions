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
        user_to_tweet_count = {}

        if userId in self.followers:
            users = self.followers[userId]
        users.add(userId)

        # for user in users:
        #     if user not in user_to_tweet_count:
        #         user_to_tweet_count[user] = 0
        #     if user in self.posts:
        #         user_to_tweet_count[user] = len(self.posts[user])-1

        for user in users:
            if user in self.posts:
                idx = len(self.posts[user])-1
                time,tweetid = -self.posts[user][-1][0],self.posts[user][-1][1]
                heapq.heappush(heap,(time,tweetid,user,idx))
        
        while heap:
            time,tweetid,user,idx = heapq.heappop(heap)
            idx-=1
            if idx>=0:
                heapq.heappush(heap,(-self.posts[user][idx][0],self.posts[user][idx][1],user,idx))
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

class Twitter:

    def __init__(self):
        self.tweets = []
        self.follows = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets.insert(0, (userId, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        page = []
        for user, tweet in self.tweets:
            if user == userId or user in self.follows[userId]:
                page.append(tweet)
            if len(page) >= 10:
                break
        return page

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].discard(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
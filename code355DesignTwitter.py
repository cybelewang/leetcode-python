"""
Design a simplified version of Twitter where users can post tweets, follow/unfollow another user and is able to see the 10 most recent tweets in the user's news feed. Your design should support the following methods:

postTweet(userId, tweetId): Compose a new tweet.
getNewsFeed(userId): Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
follow(followerId, followeeId): Follower follows a followee.
unfollow(followerId, followeeId): Follower unfollows a followee.
Example:

Twitter twitter = new Twitter();

// User 1 posts a new tweet (id = 5).
twitter.postTweet(1, 5);

// User 1's news feed should return a list with 1 tweet id -> [5].
twitter.getNewsFeed(1);

// User 1 follows user 2.
twitter.follow(1, 2);

// User 2 posts a new tweet (id = 6).
twitter.postTweet(2, 6);

// User 1's news feed should return a list with 2 tweet ids -> [6, 5].
// Tweet id 6 should precede tweet id 5 because it is posted after tweet id 5.
twitter.getNewsFeed(1);

// User 1 unfollows user 2.
twitter.unfollow(1, 2);

// User 1's news feed should return a list with 1 tweet id -> [5],
// since user 1 is no longer following user 2.
twitter.getNewsFeed(1);
"""
from heapq import heappop, heappush
class Twitter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = {}  # key: user id, value: (set of followees, list of (-time stamp, post))
        self.timestamp = 0  # a simple increasing counter to record the sequence of the tweet

    def postTweet(self, userId, tweetId):
        """
        Compose a new tweet.
        :type userId: int
        :type tweetId: int
        :rtype: void
        """
        if userId not in self.data:
            self.data[userId] = (set(), [])

        self.data[userId][1].append([-self.timestamp, tweetId]) # use negative timestamp value so the latest tweet always on top in heapq
        self.timestamp += 1

    def getNewsFeed(self, userId):
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        :type userId: int
        :rtype: List[int]
        """
        nf = [] # the result
        if userId not in self.data:
            return nf

        heap = []
        users = self.data[userId][0]    # follow-up users
        users.add(userId)   # add user herself
        last_index = {} # MAP to quickly find the last index of the user's tweet to be push into heapq
        # push each user's latest tweet into minHeap
        for user in users:
            if user not in self.data:
                continue
            posts = self.data[user][1]  # [-time stamp, tweet id]
            last_index[user] = len(posts) - 1
            if len(posts) > 0:
                heappush(heap, posts[-1] + [user]) # [-time stamp, tweet id, user id], -time stamp will serve as the key when comparing with other entries

        # pop out latest tweet from minHeap, and push that user's latest tweet, if she has
        for _ in range(10):
            if len(heap) == 0:
                break
            latest = heappop(heap)
            nf.append(latest[1])
            user = latest[2]
            # push the pop out user's latest tweet
            posts = self.data[user][1]
            last_index[user] -= 1
            if last_index[user] > -1:
                heappush(heap, posts[last_index[user]] + [user])

        return nf

    def follow(self, followerId, followeeId):
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        # followerId may not be in map yet
        if followerId not in self.data:
            self.data[followerId] = (set(), [])
        self.data[followerId][0].add(followeeId)

    def unfollow(self, followerId, followeeId):
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        if followerId in self.data:
            if followeeId in self.data[followerId][0]:
                self.data[followerId][0].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
obj = Twitter()
obj.postTweet(2,5)
obj.postTweet(1,3)
obj.postTweet(1,101)
obj.postTweet(2,13)
obj.postTweet(2,10)
obj.postTweet(1,2)
obj.postTweet(2,94)
obj.postTweet(2,505)
obj.postTweet(1,333)
obj.postTweet(1,22)
print(obj.getNewsFeed(2))
obj.follow(2, 1)
print(obj.getNewsFeed(2))
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)

"""
Input:
["Twitter","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","getNewsFeed","follow","getNewsFeed"]
[[],[2,5],[1,3],[1,101],[2,13],[2,10],[1,2],[2,94],[2,505],[1,333],[1,22],[2],[2,1],[2]]
Output:
[null,null,null,null,null,null,null,null,null,null,null,[505,94,10,13,5],null,[505,94,22,333,10,13,5,2,101,3]]
Expected:
[null,null,null,null,null,null,null,null,null,null,null,[505,94,10,13,5],null,[22,333,505,94,2,10,13,101,3,5]]
"""
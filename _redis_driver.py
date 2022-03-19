# dbsize -> amount of posts stored in cache

import redis
rc = redis.Redis(host="127.0.0.1", port=6379, decode_responses=True)

def getWebsitePosts() -> int:
    rc = redis.Redis(host="127.0.0.1", port=6379, decode_responses=True)
    return rc.dbsize()
    # i.e print('there are {0} posts in this website'.format(r.dbsize()))


def addLikeToPost(post: str, user: str) -> None:
    rc = redis.Redis(host="127.0.0.1", port=6379, decode_responses=True)
    rc.rpush(post, user)


def getPostLikes(post: str) -> int:
    rc = redis.Redis(host="127.0.0.1", port=6379, decode_responses=True)
    return rc.llen(post)


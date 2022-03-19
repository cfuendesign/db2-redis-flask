# https://redis.io/commands#hash
# https://redis.io/commands#list
# https://redis.readthedocs.io/en/v4.1.4/commands.html
# https://dev.to/search?q=Paurakh%20Sharma%20Humagain%20flask
# https://duckduckgo.com/?q=nvim+open+tab&t=min&ia=web&iax=qa <- Remap Nvim keybs

# commands notebook -> https://github.com/databases2-unbosque/redis-tutorial/blob/master/notebooks/redis-tutorial.ipynb
# flask app -> https://github.com/databases2-unbosque/redis-tutorial/blob/master/app.py

import _redis_driver as driver
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("posts/")
def getWebsitePosts() -> str:
    return "This website has {0} posts".format(driver.getWebsitePosts())


@app.route("addLike/?post=<post>,user=<user>")
def addLikeToPost(post, user) -> str:
    return "Updated. Post has {0} likes now".format(driver.addLikeToPost(post, user))


@app.route("posts/<post>/likes")
def getPostLikes(post) -> str:
    return "Post {0} has {1} likes".format(driver.getPostLikes(post), post)


if __name__ == "__main__":
    app.run()


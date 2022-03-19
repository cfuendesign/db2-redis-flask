# db2-redis-flask

WIP: A Webservice working on top of Flask and Redis.py

# features

**Byte decodification**

The ```redis.REDIS.__init__``` has the ```decode_responses``` option set to ```True```, allowing the redis driver to return decoded data from the server

**CRUD**

Currently just retrieves the 'owner' key from redis (Which, in my machine's redis storage, returns 'cfuen')

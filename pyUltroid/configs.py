# Ultroid - UserBot
# Copyright (C) 2021-2023 TeamUltroid
#
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://github.com/TeamUltroid/pyUltroid/blob/main/LICENSE>.

import sys

from decouple import config

try:
    from dotenv import load_dotenv

    load_dotenv()
except ImportError:
    pass


class Var:
    # mandatory
    API_ID = (
        int(sys.argv[1]) if len(sys.argv) > 1 else config("API_ID", default=16267784, cast=int)
    )
    API_HASH = (
        sys.argv[2]
        if len(sys.argv) > 2
        else config("API_HASH", default="b29707434744713a3dad070bda43d856")
    )
    SESSION = sys.argv[3] if len(sys.argv) > 3 else config("SESSION", default=1BVtsOMQBu2-xXRWaEJKAeVZu6u1i46dQoPAGzKvrr4pZ0D8x3WWzvthKzm2CrTD5ntXqopnHh5VQ4e1BN9ajteb62z0y8OcWT97v6z2v1Cyl0rvD-OkO9BSE28FMG8fkuxFsycNSfg0wosdXQ-gBWeRN5HtB9ao-nC-IBQP6Sdj0hS8Mhb7ma1nGodNFCpyIQ-DU017-1qbXt5cvzzD73VTuJEc1Kya95N7WVgbOxghh9DXT_H8qoQZkvuRhF1WVb7t8PHVbcARPYlQ_5Gc2dUqwzuu6bW_o8evBHNSuvXLrBVTrBQyp2ZR0ivQj8JIj6DlQ0Km9X9DIxuaH-6F1NTxPQHMkhfU=)
    REDIS_URI = (
        sys.argv[4]
        if len(sys.argv) > 4
        else (config("REDIS_URI", default=None) or config("REDIS_URL", default=redis-14108.c13.us-east-1-3.ec2.cloud.redislabs.com:14108))
    )
    REDIS_PASSWORD = (
        sys.argv[5] if len(sys.argv) > 5 else config("REDIS_PASSWORD", default=iD7sjrQ2xNtbmfxGcfnq5WkRWWspyUTe
)
    )
    # extras
    BOT_TOKEN = config("BOT_TOKEN", default=None)
    LOG_CHANNEL = config("LOG_CHANNEL", default=0, cast=int)
    HEROKU_APP_NAME = config("HEROKU_APP_NAME", default=None)
    HEROKU_API = config("HEROKU_API", default=None)
    VC_SESSION = config("VC_SESSION", default=None)
    ADDONS = config("ADDONS", default=False, cast=bool)
    VCBOT = config("VCBOT", default=False, cast=bool)
    # for railway
    REDISPASSWORD = config("REDISPASSWORD", default=None)
    REDISHOST = config("REDISHOST", default=None)
    REDISPORT = config("REDISPORT", default=None)
    REDISUSER = config("REDISUSER", default=None)
    # for sql
    DATABASE_URL = config("DATABASE_URL", default=None)
    # for MONGODB users
    MONGO_URI = config("MONGO_URI", default=None)

from environs import Env
import os
import time

env = Env()
env.read_env()


os.environ['TZ'] = 'Asia/Tashkent'


BOT_TOKEN = env.str("BOT_TOKEN")
ADMINS = env.list("ADMINS")
IP = env.str("ip")
DATABASE_URL = env.str('DATABASE_URL')
# DATABASE_URL = 'sqlite:////home/islombek/namozvaqtlari/database.db'
# DATABASE_URL = 'postgresql://postgres:2012@localhost:5432/namozvaqtlari'
# SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:2012@postgres:5432/namozvaqtlari'



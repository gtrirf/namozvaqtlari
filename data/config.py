from environs import Env

env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN")
ADMINS = env.list("ADMINS")
IP = env.str("ip")
DATABASE_URL = 'sqlite:///C:/temp/namozvaqtlaribot/database.db'
# DATABASE_URL = 'postgresql://postgres:2012@localhost:5432/namozvaqtlari'
# SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:2012@postgres:5432/namozvaqtlari'



import os

class Config(object):
    BOT_TOKEN = os.environ.get("7706666288:AAGRPPgROZBjWTLfXuPfgCTZG5hsRBK-NTw")
    API_ID = int(os.environ.get("28116598"))
    API_HASH = os.environ.get("8e148ca61f021189f6f72f8d5723d9ab")
    AUTH_USER = os.environ.get('AUTH_USERS', '6631510369').split(',')
    AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
    HOST = "https://drm-api-six.vercel.app"
    CREDIT = " 𝙎𝘼𝙄𝙉𝙄 𝘽𝙊𝙏𝙎"

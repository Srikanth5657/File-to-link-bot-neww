import os
from os import getenv, environ
from dotenv import load_dotenv



load_dotenv()

class Var(object):
    MULTI_CLIENT = False
    API_ID = int(getenv('API_ID', 26181458))
    API_HASH = str(getenv('API_HASH', "09c734fa0c97721650b5dc0cdbd679d7"))
    BOT_TOKEN = str(getenv('BOT_TOKEN', "6670480122:AAGuyxOSpvonK6eq3CfkKeNMsUdF1KEwZgc"))
    name = str(getenv('name', 'filetolinkbot'))
    SLEEP_THRESHOLD = int(getenv('SLEEP_THRESHOLD', '60'))
    WORKERS = int(getenv('WORKERS', '4'))
    BIN_CHANNEL = int(getenv('BIN_CHANNEL', -1001943293981))
    PORT = int(getenv('PORT', 8080))
    BIND_ADRESS = str(getenv('WEB_SERVER_BIND_ADDRESS', '0.0.0.0'))
    PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes
    OWNER_ID = set(int(x) for x in str(os.environ.get("OWNER_ID", 6077206903)).split() if x.isdigit()) 
    NO_PORT = bool(getenv('NO_PORT', False))
    APP_NAME = None
    OWNER_USERNAME = str(getenv('OWNER_USERNAME', "Banoth_Srikanth"))
    if 'DYNO' in environ:
        ON_HEROKU = True
        APP_NAME = str(getenv('APP_NAME', "cm-stream"))
    
    else:
        ON_HEROKU = False
    FQDN = str(getenv('FQDN', BIND_ADRESS)) if not ON_HEROKU or getenv('FQDN') else APP_NAME+'.herokuapp.com'
    HAS_SSL=bool(getenv('HAS_SSL',False))
    if HAS_SSL:
       # URL = "https://{}/".format(FQDN)
       URL = FQDN
    else:
        #URL = "https://{}/".format(FQDN)
        URL = FQDN 
    DATABASE_URL = str(getenv('DATABASE_URL', "mongodb+srv://rndjsongs:rndjsongs@cluster0.id7dpmm.mongodb.net/?retryWrites=true&w=majority"))
    UPDATES_CHANNEL = str(getenv('UPDATES_CHANNEL', "CinemasMawa"))
    BANNED_CHANNELS = list(set(int(x) for x in str(getenv("BANNED_CHANNELS", "-1001362659779")).split())) 

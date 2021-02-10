#Imports
from twython import Twython
import requests
import configparser

#API Credentils
config = configparser.ConfigParser()
config.read('config.txt')
section = 'TWITTER'

APP_KEY = config.get(section,'APP_KEY')
APP_SECRET = config.get(section,'APP_SECRET')

OAUTH_TOKEN = "dO6bqAAAAAABMm0ZAAABd4ro398"
OAUTH_TOKEN_SECRET = "4uKDBIoAmpkWpnbFckyswfnCWWII9qNf"

AUTH_CODE = '0657467'

twitter = Twython(APP_KEY, APP_SECRET)
twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

final_step = twitter.get_authorized_tokens(AUTH_CODE)
OAUTH_TOKEN = final_step['oauth_token']
OAUTH_TOKEN_SECRET = final_step['oauth_token_secret']

print('Token: %s' % OAUTH_TOKEN)
print('Secret: %s' % OAUTH_TOKEN_SECRET)
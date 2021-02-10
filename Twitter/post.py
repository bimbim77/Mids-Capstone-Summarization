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

OAUTH_TOKEN = config.get(section,'OAUTH_TOKEN')
OAUTH_TOKEN_SECRET = config.get(section, 'OAUTH_TOKEN_SECRET')

#Post to Twitter
twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

article_link = 'https://www.nytimes.com/2021/02/09/us/politics/trump-impeachment-trial-senate.html'
summary = 'Senate agrees to proceed with impeachment trial'
tweet_input = summary + ' ' + article_link

twitter.update_status(status=tweet_input)
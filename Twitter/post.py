#Imports
from twython import Twython
import authentication as a
import configparser

#Tweet inputs
article_link = 'https://www.nytimes.com/2021/02/09/us/politics/trump-impeachment-trial-senate.html'
summary = '6 Republicans vote with Democrats to advance trial.'
tweet_input = summary + ' ' + article_link

#Access Credentials
config = configparser.ConfigParser()
config.read('config.txt')
section = 'TWITTER'

APP_KEY = config.get(section,'APP_KEY')
APP_SECRET = config.get(section,'APP_SECRET')
OAUTH_TOKEN = config.get(section, 'OAUTH_TOKEN')
OAUTH_TOKEN_SECRET = config.get(section,'OAUTH_TOKEN_SECRET')

#Post to Twitter
try:
	twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
	try:
		twitter.update_status(status=tweet_input)
		print("Tweet Successful")
	except:
		print("Tweet not Successful!")

except:
	print("You need to authenticate first!")
	#Authentication
	OAUTH_TOKEN, OAUTH_TOKEN_SECRET, APP_KEY, APP_SECRET = a.auth()

	twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
	try:
		twitter.update_status(status=tweet_input)
		print("Tweet Successful")
	except:
		print("Tweet not Successful!")
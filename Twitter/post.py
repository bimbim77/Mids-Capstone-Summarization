#Imports
from twython import Twython
import authentication as a
import configparser

#Tweet inputs
article_link = 'vox.com'
summary = 'Another test.'
tweet_input = summary + ' ' + article_link

#Access Basic Credentials
config = configparser.ConfigParser()
config.read('config.txt')
section = 'TWITTER'
APP_KEY = config.get(section,'APP_KEY')
APP_SECRET = config.get(section,'APP_SECRET')

def parse_token(tokens):
	OAUTH_TOKEN = tokens.split('___')[0]
	OAUTH_TOKEN_SECRET = tokens.split('___')[1]
	return OAUTH_TOKEN, OAUTH_TOKEN_SECRET

def post_tweet(APP_KEY,APP_SECRET,tweet_input):
	#Get Username
	username = input("Please enter your Twitter handle: ")

	#Get Tokens
	try:
		tokens = config.get(section,username)
		OAUTH_TOKEN, OAUTH_TOKEN_SECRET = parse_token(tokens)
	except:
		print("You need to authenticate first!")
		print("Please log out of any Twitter accounts that are not your desired handle.")
		passcode = input("Please enter Y when ready to proceed: ")
		if passcode == 'Y':
			OAUTH_TOKEN, OAUTH_TOKEN_SECRET= a.auth(username)

	#Post to Twitter
	try:
		twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
		twitter.update_status(status=tweet_input)
		print("Tweet successful!")
	except:
		print("Tweet not Successful! :(")

post_tweet(APP_KEY,APP_SECRET,tweet_input)
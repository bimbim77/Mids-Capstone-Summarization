#Imports
from twython import Twython
import requests
import configparser
import webbrowser
import time

#API Credentils
def get_app_tokens():
	config = configparser.ConfigParser()
	config.read('config.txt')
	section = 'TWITTER'

	APP_KEY = config.get(section,'APP_KEY')
	APP_SECRET = config.get(section,'APP_SECRET')
	return APP_KEY,APP_SECRET

def get_auth_tokens(APP_KEY,APP_SECRET):
	twitter = Twython(APP_KEY, APP_SECRET)
	auth = twitter.get_authentication_tokens()

	#Store OAuth Tokens
	OAUTH_TOKEN = auth['oauth_token']
	OAUTH_TOKEN_SECRET = auth['oauth_token_secret']
	OAUTH_VERIFIER_URL = auth['auth_url']

	#Open Authentication URL
	print("The Authorization URL will now open in 5 seconds. After authorizing access, please input the PIN that appears on the screen.")
	time.sleep(5)
	webbrowser.open(OAUTH_VERIFIER_URL)

	OAUTH_VERIFIER = input("Enter the PIN value: ") 

	return OAUTH_TOKEN, OAUTH_TOKEN_SECRET, OAUTH_VERIFIER

def get_access_codes(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET,OAUTH_VERIFIER):
	twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
	final_step = twitter.get_authorized_tokens(OAUTH_VERIFIER)

	OAUTH_TOKEN_FINAL = final_step['oauth_token']
	OAUTH_TOKEN_SECRET_FINAL = final_step['oauth_token_secret']

	return OAUTH_TOKEN_FINAL, OAUTH_TOKEN_SECRET_FINAL, APP_KEY, APP_SECRET

def auth():
	TW_APP_KEY, TW_APP_SECRET = get_app_tokens()
	TW_OAUTH_TOKEN, TW_OAUTH_TOKEN_SECRET, TW_OAUTH_VERIFIER = get_auth_tokens(TW_APP_KEY,TW_APP_SECRET)
	TW_OAUTH_TOKEN_FINAL, TW_OAUTH_TOKEN_SECRET_FINAL, TW_APP_KEY, TW_APP_SECRET = get_access_codes(TW_APP_KEY,TW_APP_SECRET,TW_OAUTH_TOKEN, TW_OAUTH_TOKEN_SECRET, TW_OAUTH_VERIFIER)

	#Update Credentials to Config file
	config = configparser.ConfigParser()
	config.read('config.txt')
	twitter_section = config["TWITTER"]

	#Update the password
	twitter_section["OAUTH_TOKEN"] = TW_OAUTH_TOKEN_FINAL
	twitter_section['OAUTH_TOKEN_SECRET'] = TW_OAUTH_TOKEN_SECRET_FINAL

	#Write changes back to file
	with open('config.txt', 'w') as conf:
		config.write(conf)

	return TW_OAUTH_TOKEN_FINAL, TW_OAUTH_TOKEN_SECRET_FINAL, TW_APP_KEY, TW_APP_SECRET






#Imports
from twython import Twython
import requests

#API Credentils
APP_KEY = "cAELLleclnVvv3x7PqB5tJxrk"
APP_SECRET = "9X8XzWeXbccs9K8JIdfssq60WsIpJfJrZSxzPlhhDSf7XP49y7"

#Call Twython Package
twitter = Twython(APP_KEY, APP_SECRET)
auth = twitter.get_authentication_tokens()

#Store OAuth Tokens
OAUTH_TOKEN = auth['oauth_token']
OAUTH_TOKEN_SECRET = auth['oauth_token_secret']
oauth_verifier_url = auth['auth_url']
oauth_verifier = requests.get(oauth_verifier_url)

#Print Output
print("Verifier URL is:" + oauth_verifier_url)
print("OAUTH_TOKEN is:" + OAUTH_TOKEN)
print("OAUTH TOKEN SECRET is:" + OAUTH_TOKEN_SECRET)
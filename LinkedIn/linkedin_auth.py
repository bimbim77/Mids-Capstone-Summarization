#Imports
from linkedin_v2 import linkedin
import configparser
import time
import webbrowser
import requests as r

def get_app_tokens():
	config = configparser.ConfigParser()
	config.read('config.txt')
	section = 'LINKEDIN'

	API_KEY = config.get(section,'API_KEY')
	API_SECRET = config.get(section,'API_SECRET')
	RETURN_URL = config.get(section,'RETURN_URL')
	return API_KEY,API_SECRET,RETURN_URL

def get_profile_id(token):
	headers = {'Content-Type': 'application/json',
           	   'X-Restli-Protocol-Version': '2.0.0',
           	   'Authorization': 'Bearer ' + token}

	url = 'https://api.linkedin.com/v2/me'
	response = r.get(url,headers=headers).json()
	profile_id = response['id']
	return profile_id

def auth():
	#Get Credentials
	API_KEY,API_SECRET,RETURN_URL = get_app_tokens()

	#Generate Authentication URL
	auth_url = 'https://www.linkedin.com/oauth/v2/authorization?response_type=code&client_id=%s&scope=w_member_social%%20r_liteprofile&state=123456&redirect_uri=%s' % (API_KEY,RETURN_URL)
	print("The Authorization URL will now open in 5 seconds. After authorizing access, please input the URL you are redirected to.")
	time.sleep(1)
	webbrowser.open(auth_url)

	#Get Auth Code
	auth_code = input("Enter the URL: ")
	auth_code = auth_code.split('?code=')[1].split('&')[0]

	#Get Access Code
	access_token = r.post(
    'https://www.linkedin.com/oauth/v2/accessToken',
    params = {
        'grant_type': 'authorization_code',
        'code': auth_code,
        'redirect_uri': RETURN_URL,
        'client_id': API_KEY,
        'client_secret': API_SECRET,
    },).json()['access_token']

	#Get Profile ID
	profile_id = get_profile_id(access_token)

    #Update Credentials to Config file
	config = configparser.ConfigParser()
	config.read('config.txt')
	li_section = config["LINKEDIN"]

	#Update the password and profile_id
	li_section["ACCESS_TOKEN"] = access_token
	li_section['PROFILE_ID'] = profile_id

	#Write changes back to file
	with open('config.txt', 'w') as conf:
		config.write(conf)

auth()
import requests
#import linkedin_auth as a
import configparser

#Access Credentials
config = configparser.ConfigParser()
config.read('config.txt')
section = 'LINKEDIN'

TOKEN = config.get(section,'access_token')
PROFILE_ID = config.get(section,'profile_id')

#API Call Inputs
url = "https://api.linkedin.com/v2/ugcPosts"
headers = {'Content-Type': 'application/json',
           'X-Restli-Protocol-Version': '2.0.0',
           'Authorization': 'Bearer ' + TOKEN}

#Post Inputs
article_link = 'https://www.nytimes.com/2021/02/09/us/politics/trump-impeachment-trial-senate.html'
summary = 'testing again'


post_data = {
    "author": "urn:li:person:"+PROFILE_ID,
    "lifecycleState": "PUBLISHED",
    "specificContent": {
        "com.linkedin.ugc.ShareContent": {
            "shareCommentary": {
                "text": summary
            },
            "shareMediaCategory": "ARTICLE",
            "media": [
                {
                    "status": "READY",
                    "originalUrl": article_link
                    }
            ]
        }
    },
    "visibility": {
        "com.linkedin.ugc.MemberNetworkVisibility": "CONNECTIONS"
    }
}

response = requests.post(url, headers=headers, json=post_data)

print(response.json())
import base64

import requests
import json
from requests_oauthlib import OAuth1

#Define your keys from the developer portal
client_key = 'f4mEYU64JLUin9Knqz8xRmju2'
client_secret = 'KjfDwM89tdO3bmXlOSHa57ZisZUm1oMX7aBtw35hd0xaCNffBQ'
access_token='1160813328123301888-UaqUGi7eu5g3ZZmkuWmvH4j4MTFhTV' #(Access token)
access_token_secret='Z31zFieg1jISWaNGYSqYWkEh8Q3G5eryq0Jzq0F5W7Uar' #(Access token secret)


auth = OAuth1(client_key, client_secret, access_token,access_token_secret)


#Reformat the keys and encode them


# we start in unicode and then transform to bytes
key_secret = '{}:{}'.format(client_key, client_secret).encode('ascii')


# Transform from bytes to bytes that can be printed
b64_encoded_key = base64.b64encode(key_secret)


#Transform from bytes back into Unicode
b64_encoded_key = b64_encoded_key.decode('ascii')


base_url = 'https://api.twitter.com/'
auth_url = '{}oauth2/token'.format(base_url)
#authentication_url='{}oauth/authenticate'.format(base_url)


auth_headers = {
    'Authorization': 'Basic {}'.format(b64_encoded_key),
    'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'
}
#parameters
auth_data = {                                            
    'grant_type': 'client_credentials'
}

auth_resp = requests.post(auth_url, headers=auth_headers, data=auth_data)
#print(auth_headers)
print('authentication status ',auth_resp.status_code)

#authenticate:-
r=requests.get('https://api.twitter.com/1.1/account/verify_credentials.json',auth=auth)
print('credentials status ',r.status_code)
#print(r.text)

data=json.loads(r.text)
print('name '+data['name'])
print('\n')
print('twitter name @'+data['screen_name'])
print('\n')
print('id is ',data['id'])
print('\n')
print('id string '+data['id_str'])
print('\n')
print('total followers ',data['followers_count'])
print('\n')
print('total followings ',data['friends_count'])
print('\n')




following_list=requests.get('https://api.twitter.com/1.1/friends/list.json',auth=auth)
print('following list status ',following_list.status_code)
followingdata=json.loads(following_list.text)
#for ids in followingdata:
#	print(followingdata['user_id'])
#timeline status
#timeline=requests.get('https://api.twitter.com/1.1/statuses/home_timeline.json',auth=auth)
#print('timeline status ',timeline.status_code)
#data1=json.loads(timeline.text)
#print(data1)


retweet=requests.get('https://api.twitter.com/1.1/statuses/retweet/:id.json',auth=auth)
print('retweet status ',retweet.status_code)

rate_limit=requests.get('https://api.twitter.com/1.1/application/rate_limit_status.json',auth=auth)
print('rate limit left',rate_limit)
print(rate_limit.text)

statusid=requests.get('https://api.twitter.com/1.1/statuses/show.json',auth=auth)
print('status id ',statusid.status_code)
print(statusid)

#print()







# twitter  
#api =twitter.api(consumer_key='f4mEYU64JLUin9Knqz8xRmju2',
#                    consumer_secret='KjfDwM89tdO3bmXlOSHa57ZisZUm1oMX7aBtw35hd0xaCNffBQ',
#                    access_token_key='1160813328123301888-UaqUGi7eu5g3ZZmkuWmvH4j4MTFhTV',
#                    access_token_secret='Z31zFieg1jISWaNGYSqYWkEh8Q3G5eryq0Jzq0F5W7Uar')
#print (api.VerifyCredentials())

import twitter
"""
Change ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY and CONSUMER_SECRET
to your own. 
"""
ACCESS_TOKEN = '1160813328123301888-UaqUGi7eu5g3ZZmkuWmvH4j4MTFhTV'
ACCESS_SECRET = 'Z31zFieg1jISWaNGYSqYWkEh8Q3G5eryq0Jzq0F5W7Uar'
CONSUMER_KEY = 'f4mEYU64JLUin9Knqz8xRmju2'
CONSUMER_SECRET = 'KjfDwM89tdO3bmXlOSHa57ZisZUm1oMX7aBtw35hd0xaCNffBQ'
t = twitter.Api(consumer_key=CONSUMER_KEY,
                consumer_secret=CONSUMER_SECRET,
                access_token_key=ACCESS_TOKEN,
                access_token_secret=ACCESS_SECRET)
#status = t.VerifyCredentials()
#print(status)
#followers=t.GetFollowers(screen_name='rishabhrocks07')
#for d in followers:
#    print (d.id)

#statuses=t.GetUserTimeline(1031509537,count=50)
#print([s.text for s in statuses])

status=t.GetStatus(status_id='2476107409')
print(status)
#x=t.PostUpdates(status='hello world yo')
#print(x.Text)
#rt=t.PostRetweet(status_id=1031509537, trim_user=False)
#print(rt)
#print(len(d.name))
    #print (d.name)
#print(followers)
#results = t.GetSearch(raw_query="q=from%3AGalarnykMichael&src=typd")
#print(results)
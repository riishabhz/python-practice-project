import tweepy
import unicodedata

auth = tweepy.OAuthHandler("f4mEYU64JLUin9Knqz8xRmju2","KjfDwM89tdO3bmXlOSHa57ZisZUm1oMX7aBtw35hd0xaCNffBQ")
auth.set_access_token("1160813328123301888-UaqUGi7eu5g3ZZmkuWmvH4j4MTFhTV","Z31zFieg1jISWaNGYSqYWkEh8Q3G5eryq0Jzq0F5W7Uar")

api = tweepy.API(auth)

#public_tweets = api.home_timeline(count=50)  #timeline tweets
#for tweet in public_tweets:
#    print(tweet.text)

#status=api.statuses_lookup()
#print(status)    

#update=api.update_status(status='yoyo') #to update status
#print(update)

#followers=api.followers() #my followers
#print(followers)

#rt=api.retweeters(id=86548309) 
#for retweet in rt:
#	print(rt)l

#friend=api.friends(id=86548309) #following names
#for friends in friend:
#	print(friend.id)

#ids=api.followers_ids(id=86548309) #followers id
#print(ids)

#ids2=api.friends_ids(id=86548309) #following list
#print(ids2)

fav=api.create_favorite(id=86548309)
print(fav)


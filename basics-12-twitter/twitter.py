from requests_oauthlib import OAuth1Session
import sys
import json

class TWITTER_CREDITIONALS:
    KEY = 'wjRsWCMI3lU3ypwYjQbeIfKef'
    SECRET = '3xB5nyISIdk8MOp4kutpRe4wnAdn2NgTGBEcrGWEV6HMDbPhth'
    TOKEN = '1495931731-exp5kBvqUTp7lZJLFtZ9NmtKd7QwUIBKyRZB2QN'
    TOKEN_SECRET = 'ysLFG2vK5Pp6NUIs4CnV6rL7XWzxFJtNfQjfxCA8p1GXo'

api_keys = TWITTER_CREDITIONALS()
twitter = OAuth1Session(api_keys.KEY,
                        client_secret=api_keys.SECRET,
                        resource_owner_key=api_keys.TOKEN,
                        resource_owner_secret=api_keys.TOKEN_SECRET)
try:
    hashtag = ", ".join(sys.argv[1:])
except Exception as e:
    hashtag = "#cek_python"
r = twitter.post('https://stream.twitter.com/1.1/statuses/filter.json', data={ 'track': hashtag }, stream=True )

print "\n\t START TWEETING WITH HASHTAG '#cek_python'\n"
for line in r.iter_lines():
    if line:
        j = json.loads(line.decode('utf-8'))
        print('\n')
        print(j['user']['name'], "(@%s) : " % j['user']['screen_name'],j['text'])
        # print("\t",j['text'])



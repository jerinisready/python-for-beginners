import facebook, datetime

token = "114182619219745|WqzVxshsPoMEqAC9tDmo2v1JSgo"
fb_id = "bbcnewsenglish"   # Group Id if English Litteratry
since = datetime.datetime.now() - datetime.timedelta(days=2)
d = since.date()
graph = facebook.GraphAPI(token)
data_set = graph.request(str(fb_id) + '/posts/?fields=description,attachments,message,created_time,shares,link,from,'
                                  'type,image,comments.summary(true)&limit=9&since=' + str(d))

data_set = data_set['data']
for data in data_set:
    print "\n"
    print "\n"
    print "USER    : ", data["from"]["name"]
    print "SHARES  : ", data["shares"]["count"]
    print "Likes   : ", len(data["likes"]["data"])
    print "Message : ", data["message"]
    print ""
    try:
        input("Continue...")
    except:
        pass

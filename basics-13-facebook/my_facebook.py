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

SAMPLE_FACEBOOK_API_DATA = """
{
    "from":{
        "name":"BBC News English",
        "id":"228306784290373"
    },
    "description":"The US leader's visit to the demilitarised zone between the two Koreas is dropped due to bad weather.",
    "shares":{
        "count":4
    },
    "link":"http://www.bbc.com/news/world-asia-41910167",
    "comments":{
        "paging":{
            "cursors":{
                "after":"MQZDZD",
                "before":"MgZDZD"
            }
        },
        "data":[
            {
                "created_time":"2017-11-08T04:28:25+0000",
                "message":"Trump can't see even to the testicle of Kim",
                "from":{
                    "name":"Ehsanullah Yousofzai",
                    "id":"299945480520136"
                },
                "id":"376922246095492_376922806095436"
            },
            {
                "created_time":"2017-11-08T04:31:30+0000",
                "message":"",
                "from":{
                    "name":"ThawZin Htoo",
                    "id":"173694486545951"
                },
                "id":"376922246095492_376923426095374"
            }
        ],
        "summary":{
            "total_count":2,
            "can_comment":false,
            "order":"ranked"
        }
    },
    "created_time":"2017-11-08T04:24:19+0000",
    "message":"Donald Trump warns North Korea: 'Do not try us'\n\nUS President Donald Trump has issued a stark warning to North Korea's leader Kim Jong-un in an address to South Korea's parliament.",
    "type":"link",
    "id":"228306784290373_376922246095492",
    "likes":{
        "paging":{
            "cursors":{
                "after":"MzQ2MDQxMjM5MjAyMDAx",
                "before":"MTk2NjM0MTc4MDMwMjI4OAZDZD"
            },
            "next":"https://graph.facebook.com/v2.9/228306784290373_376922246095492/likes?access_token=114182619219745%7CWqzVxshsPoMEqAC9tDmo2v1JSgo&limit=25&after=MzQ2MDQxMjM5MjAyMDAx"
        },
        "data":[
            {
                "id":"1966341780302288",
                "name":"Tufail Ahmed Abro"
            },
            {
                "id":"522996618054985",
                "name":"Abdullfatax Hasan Awaare"
            },
            {
                "id":"803553503186837",
                "name":"Minh Tr\u1ea7n"
            },
            {
                "id":"144602482934009",
                "name":"Nyein Chan"
            },
            {
                "id":"287832481723393",
                "name":"\u09b0\u09bf\u0995\u09cd\u09a4\u09a4\u09be\u09b0 \u09a8\u09c0\u09b2\u09be\u099a\u09b2"
            },
            {
                "id":"105610060213598",
                "name":"Binod Binod Mandal"
            },
            {
                "id":"131119680986108",
                "name":"Kwaku Nyarko"
            },
            {
                "id":"380850262351597",
                "name":"Adigo Amsaya"
            },
            {
                "id":"126261278144303",
                "name":"Mike Pariso"
            },
            {
                "id":"125198144917107",
                "name":"\u101c\u1019\u1004\u1039\u1038 \u1001\u103a\u1005\u1039\u101e\u1030"
            },
            {
                "id":"721331904723946",
                "name":"Al Mamun"
            },
            {
                "id":"150239949056389",
                "name":"Wllat Kurdish"
            },
            {
                "id":"2128498864046799",
                "name":"Mamun Prodhan"
            },
            {
                "id":"696163537246698",
                "name":"S M Zahid Hasan"
            },
            {
                "id":"1974584839476236",
                "name":"Seak Pheng Lim"
            },
            {
                "id":"368685513585675",
                "name":"Nguy\u1ec5n Thu Thu\u1ef7"
            },
            {
                "id":"159623051306556",
                "name":"Fejzullah Llumnica"
            },
            {
                "id":"111869702919610",
                "name":"Sarjubala Kst Sarjubala"
            },
            {
                "id":"129341727835040",
                "name":"Lulu Paul"
            },
            {
                "id":"131764504253822",
                "name":"Wule Yoni"
            },
            {
                "id":"2079997335554578",
                "name":"Abdi M. Kenea"
            },
            {
                "id":"1583020335092658",
                "name":"Khalid Sameth"
            },
            {
                "id":"159094538164890",
                "name":"Chuman Kc"
            },
            {
                "id":"1994557667499717",
                "name":"Amantle Joy Mmolai"
            },
            {
                "id":"346041239202001",
                "name":"Aks Aks"
            }
        ]
    }
}

"""

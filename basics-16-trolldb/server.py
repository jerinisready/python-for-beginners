#!/usr/bin/env python
import socket
import re

def head():
    return """HTTP/1.0 200 OK
Content-Type: text/html


"""



def define_title(slug):
    slug = slug.replace(".", " ")
    slug = slug.replace(slug[0], slug[0].upper())
    replace_handle = re.findall(r'([._\-A-Z]{1})', slug)
    for i in replace_handle:
        if i in "._\-":
            slug = slug.replace(i, " ")
        else:
            slug = slug.replace(i, " %s" % i)
    return slug

define_title("InternationalChaluUnion")
define_title("troll.ktu.official")

def render(data, slug):
    try:

        base = open('base.html', 'r')
        body_holder  = base.read()
        base.close()

        base = open('comment.html', 'r')
        comment_holder = base.read()
        base.close()

        tmp = open('template.html', 'r')
        template_holder  = tmp.read()
        tmp.close()

        rendered_template_out = ""
        rendered_base_out = ""
        print("Point 1")
        for post in data:

            get_comments = post["comments"]["data"]
            src = "#"
            message = post["description"]
            try:
                medias = post["attachments"]["data"]
                for media in medias:
                    try:
                        src = media['image']['src']
                        break
                    except:
                        pass
            except:
                src = "#"

            rendered_comment_out = ""
            for comment_data in get_comments:
                comments = comment_holder
                comments = comments.replace("{{COMMENT-TEXT}}", comment_data["message"])
                comments = comments.replace("{{COMMENTER-NAME}}", comment_data["from"]["name"])
                comments = comments.replace("{{COMMENTED-TIME}}", comment_data["created_time"])
                rendered_comment_out += comments



            template = template_holder
            template = template.replace("{{POST - SENDER}}", post["from"]["name"])
            template = template.replace("{{POST-IMAGE}}", src)
            print( "A")
            template = template.replace("{{POST-COMMENT}}", post["description"])
            print( "b")
            # template = template.replace("{{SHARE-COUNT}}", post["shares"]["count"])
            print( "c")
            # template = template.replace("{{COMMENTS-COUNT}}", post["comments"]["summary"]["total_count"])
            print( "D")
            template = template.replace("{{COMMENTS}}", rendered_comment_out)
            print( "E")
            rendered_template_out += template
            print("Point 4")

        body_holder =body_holder.replace("{{TEMPLATE}}", rendered_template_out)
        body_holder = body_holder.replace("{{FACEBOOK-POST-TITLE}}", define_title(slug))
        rendered_base_out = body_holder

        return rendered_base_out

    except Exception:
        return "Template Rendering Error! "



def fb_json(fb_id):
    import facebook, datetime

    token = "114182619219745|WqzVxshsPoMEqAC9tDmo2v1JSgo"
    fb_id = "bbcnewsenglish"  # Group Id if English Litteratry
    since = datetime.datetime.now() - datetime.timedelta(days=2)
    d = since.date()
    graph = facebook.GraphAPI(token)
    data_set = graph.request(str(fb_id) + '/posts/?fields=description,message,created_time,shares,link,from,'
                                          'type,attachments,comments.summary(true)&limit=9&since=' + str(d))

    return data_set['data']
    # for data in data_set:
    #     print "\n"
    #     print "\n"
    #     print "USER    : ", data["from"]["name"]
    #     print "SHARES  : ", data["shares"]["count"]
    #     print "Likes   : ", len(data["likes"]["data"])
    #     print "Message : ", data["message"]
    #     print ""
    #     try:
    #         input("Continue...")
    #     except:
    #         pass


# ##############################################################

if __name__ == '__main__':
    # Standard socket stuff:
    host = 'localhost' # do we need socket.gethostname() ?
    port = 8085
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((host, port))
    sock.listen(1) # don't queue up any requests

    # Loop forever, listening for requests:
    while True:
        csock, caddr = sock.accept()
        print "Connection from: " + `caddr`
        req = csock.recv(1024) # get the request, 1kB max
        print req
        # Look in the first line of the request for a move command
        # A move command should be e.g. 'http://server/move?a=90'
        match = re.match('GET /\?id=([\w\.\d\-]+)\sHTTP/1', req)
        if match:
            id_from_url = match.group(1)
            data= fb_json(fb_id=id_from_url)
            csock.sendall(head()+render(data,id_from_url))
            csock.close()
        else:

            base = open('base.html', 'r')
            body_holder = base.read()
            base.close()
            body_holder = body_holder.replace("{{FACEBOOK-POST-TITLE}}"," Something More Is There!!! ")
            body_holder = body_holder.replace("{{TEMPLATE}}"," Select a Link")
            csock.sendall(head()+ body_holder)
            csock.close()
            
            
            ##################################

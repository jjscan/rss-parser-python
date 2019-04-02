import feedparser

urls={"http://www.dongguk.edu/rssList.jsp?boardId=3646&id=kr_010802000000&site_id=kr",
      "http://www.dongguk.edu/rssList.jsp?boardId=3638&id=kr_010801000000&site_id=kr",
      "http://www.dongguk.edu/rssList.jsp?boardId=3654&id=kr_010803000000&site_id=kr",
      "http://www.dongguk.edu/rssList.jsp?boardId=3662&id=kr_010804000000&site_id=kr",
      "http://www.dongguk.edu/rssList.jsp?boardId=9457435&id=kr_010807000000&site_id=kr",
      "http://www.dongguk.edu/rssList.jsp?boardId=9457435&id=kr_010807000000&site_id=kr"
      }

def crawl_rss(url) :
    d = feedparser.parse(url)
    print( type(d) )
    print( d.feed["title"] )
    for e in d.entries :
        print( "title = " + e.title)
        print( "link = " + e.link)
        print( " description = " + e.description)
        print( "pubDate =" + str(e.published))

def main() :
    for url in urls:
        crawl_rss(url)

if __name__=="__main__":
    main()

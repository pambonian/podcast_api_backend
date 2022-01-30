### Scraper Function Example

def get_posts_details(rss=None):
    
    """
    Take link of rss feed as argument
    """
    if rss is not None:
        
          # import the library only when url for feed is passed
        import feedparser
          
        # parsing blog feed
        blog_feed = blog_feed = feedparser.parse(rss)
          
        # getting lists of blog entries via .entries
        posts = blog_feed.entries
          
        # dictionary for holding posts details
        posts_details = {
            'site_title': blog_feed.feed.site_title, 
            'itunes_episode': blog_feed.feed.itunes_episode, 
            'itunes_title': blog_feed.feed.itunes_title, 
            'itunes_author': blog_feed.feed.itunes_author, 
            'itunes_duration': blog_feed.feed.itunes_duration, 
            'itunes_explicit': blog_feed.feed.itunes_explicit, 
            'itunes_summary': blog_feed.feed.itunes_summary, 
            'cover_art': blog_feed.feed.cover_art, 
            'audio_link': blog_feed.feed.audio_link,

            
            
            # "Blog title" : blog_feed.feed.title,
            # "Blog link" : blog_feed.feed.link

            

        }
          
        post_list = []
          
        # iterating over individual posts
        for post in posts:
            temp = dict()
              
            # if any post doesn't have information then throw error.
            try:
                temp["title"] = post.title
                temp["link"] = post.link
                temp["author"] = post.author
                temp["time_published"] = post.published
                temp["tags"] = [tag.term for tag in post.tags]
                temp["authors"] = [author.name for author in post.authors]
                temp["summary"] = post.summary
            except:
                pass
              
            post_list.append(temp)
          
        # storing lists of posts in the dictionary
        posts_details["posts"] = post_list 
          
        return posts_details # returning the details which is dictionary
    else:
        return None
  
if __name__ == "__main__":
  import json
  
  feed_url = "https://feeds.simplecast.com/T8TzwY_T"
  
  data = get_posts_details(rss = feed_url) # return blogs data as a dictionary
    
  # if data:
  #   # printing as a json string with indentation level = 2
  #   print(json.dumps(data, indent=2)) 
  # else:
  #   print("None")

data = data

print(json.dumps(data, indent=2)) 
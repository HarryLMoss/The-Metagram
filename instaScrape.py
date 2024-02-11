# Author: Harry Moss
# Date: 11 February, 2024

import json
import httpx
from urllib.parse import quote
import datetime
import time

def getPublishDate(timestamp):
    publish_date = datetime.datetime.fromtimestamp(timestamp)
    return str(publish_date)

def parse_post(post):
    isReel = post["is_video"]
    if not isReel:
        return None
    publishDate = getPublishDate(post["taken_at_timestamp"])
    likesCount = post["edge_media_preview_like"]["count"]
    commentsCount = post["edge_media_to_comment"]["count"]
    videoUrl = post["video_url"] if isReel else None
    videoViewCount = post["video_view_count"] if isReel else None
    shortCode = post["shortcode"]
    caption = ""
    if "edge_media_to_caption" in post and post["edge_media_to_caption"]["edges"]:
        caption = post["edge_media_to_caption"]["edges"][0]["node"]["text"]

    result = {
        "publishDate": publishDate,
        "likesCount": likesCount,
        "commentsCount": commentsCount,
        "videoUrl": videoUrl,
        "videoViewCount": videoViewCount,
        "shortCode": shortCode,
        "caption": caption 
    }
    return result

    

def scrape_user_posts(user_id: str, session: httpx.Client, page_size=12):
    base_url = "https://www.instagram.com/graphql/query/?query_hash=e769aa130647d2354c40ea6a439bfc08&variables="
    variables = {
        "id": user_id,
        "first": page_size,
        "after": None,
    }
    _page_number = 1

    while True:
        reelsList = []
        resp = session.get(base_url + quote(json.dumps(variables)))
        data = resp.json()

        posts = data["data"]["user"]["edge_owner_to_timeline_media"]

        for post in posts["edges"]:
            reelVideoData = parse_post(post["node"])  
            print(reelVideoData)

            if reelVideoData:
                yield reelVideoData
                reelsList.append(reelVideoData)
        
        print('Fetched total reelsList = ', len(reelsList))
        page_info = posts["page_info"]
        if _page_number == 1:
            print(f"scraping total {posts['count']} posts of {user_id}")
        else:
            print(f"scraping page {_page_number}")
        if not page_info["has_next_page"]:
            break
        if variables["after"] == page_info["end_cursor"]:
            break
        variables["after"] = page_info["end_cursor"]
        print('end_cursor : ', variables["after"])
        _page_number += 1

    print(f"Total {len(reelsList)} reels scraped")
    time.sleep(0.2)

# Example run:
if __name__ == "__main__":
    with httpx.Client(timeout=httpx.Timeout(20.0)) as session:
        with open('reels.json', 'w') as outfile:
            outfile.write('[')
            first_item = True
            for reel in scrape_user_posts("10320868", session, page_size=200):
                if not first_item:
                    outfile.write(",\n")
                else:
                    first_item = False
                json.dump(reel, outfile, indent=4)
            outfile.write('\n]')




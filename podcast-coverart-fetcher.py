from pyPodcastParser.Podcast import Podcast
import requests
import urllib

# fetching and parsing the feed
url = 'https://podcast.funkenstrahlen.de/feed/mp3'
response = requests.get(url)
podcast = Podcast(response.content)
print(podcast.itune_image)

# downloading the coverart
coverart_url = podcast.itune_image
coverart = urllib.URLopener()
coverart.retrieve(coverart_url, 'coverart.png')
